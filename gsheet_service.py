import datetime as dt
import gspread
import os
import sys
import json
import time
import socket
from google.oauth2.service_account import Credentials
from gspread.exceptions import APIError
from config_listings import SPREADSHEET_URL, CREDENTIALS_FILE
from config_listings import MMRENT_COUNT_COLUMN_GDANSK

# Global gspread client
gc = None

# ---------------------------------------------
# Функция для перевода номера колонки в букву
# ---------------------------------------------
def col_to_letter(col: int) -> str:
    result = ""
    while col > 0:
        col, rem = divmod(col - 1, 26)
        result = chr(65 + rem) + result
    return result

# ---------------------------------------------
# Авторизация gspread
# ---------------------------------------------
def authorize_gspread():
    global gc

    if "GOOGLE_CREDS" in os.environ:
        try:
            creds_json = json.loads(os.environ["GOOGLE_CREDS"])
            creds = Credentials.from_service_account_info(
                creds_json,
                scopes=["https://www.googleapis.com/auth/spreadsheets"]
            )
            print("✅ GOOGLE_CREDS загружены из переменной окружения.")
        except json.JSONDecodeError:
            print("❌ Ошибка: переменная GOOGLE_CREDS не является корректным JSON.")
            sys.exit(1)
    else:
        if not os.path.exists(CREDENTIALS_FILE):
            print(f"❌ Критическая ошибка: файл учетных данных '{CREDENTIALS_FILE}' не найден.")
            sys.exit(1)
        creds = Credentials.from_service_account_file(
            CREDENTIALS_FILE,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        print(f"✅ GOOGLE_CREDS загружены из локального файла {CREDENTIALS_FILE}")

    try:
        gc = gspread.authorize(creds)
    except Exception as e:
        print(f"❌ Критическая ошибка авторизации gspread: {e}")
        sys.exit(1)

# ---------------------------------------------
# Инициализация Google Sheet
# ---------------------------------------------
def initialize_gspread(sheet_name: str):
    if gc is None:
        authorize_gspread()
        if gc is None:
            return None
    try:
        sh = gc.open_by_url(SPREADSHEET_URL)
        ws = sh.worksheet(sheet_name)
        return ws
    except Exception as e:
        print(f"❌ Ошибка при работе с Google Sheets (Лист: {sheet_name}): {e}")
        return None

# ---------------------------------------------
# Поиск строки по дате с ретраями
# ---------------------------------------------
def find_row_by_date(ws, target_date: dt.date, retries: int = 3):
    for attempt in range(1, retries + 1):
        try:
            values = ws.col_values(1)
            for idx, cell in enumerate(values, start=1):
                if not cell.strip():
                    continue
                try:
                    try:
                        cell_date = dt.datetime.strptime(cell.strip(), "%d.%m.%Y").date()
                    except ValueError:
                        cell_date = dt.datetime.strptime(cell.strip(), "%Y-%m-%d").date()
                    if cell_date == target_date:
                        return idx
                except ValueError:
                    continue
            return None  # дата реально не найдена
        except (APIError, ConnectionError, socket.error) as e:
            print(f"⚠️ Ошибка соединения при поиске даты {target_date} "
                  f"(попытка {attempt}/{retries}): {e}")
            time.sleep(2)
    raise RuntimeError(f"❌ Не удалось получить данные из Google Sheets для даты {target_date}")

# ---------------------------------------------
# Обновление данных в Google Sheet
# ---------------------------------------------
def update_spreadsheet_data(
        ws: gspread.Worksheet,
        row_index: int,
        ranks_map: dict,
        listings_map: dict,
        city_name: str,
        mmrent_count: int = None,
):
    data_to_run = []

    # НОВЫЙ БЛОК: Создаем нормализованную карту рангов (без лишних пробелов)
    # Это гарантирует, что "Stitch Room" совпадет с "Stitch Room "
    norm_ranks = {str(k).strip(): v for k, v in ranks_map.items() if v is not None}

    # 1. Обрабатываем ВСЕ листинги из карты
    for listing_title, col_idx in listings_map.items():
        clean_title = str(listing_title).strip()
        rank = norm_ranks.get(clean_title)  # Ищем в нормализованной карте

        col_letter = col_to_letter(col_idx)
        value_to_write = rank if rank is not None else ""

        # ЛОГ ДЛЯ ТЕСТА (можно потом убрать)
        if rank:
            print(f"      📝 Подготовка записи: {clean_title} -> {col_letter}{row_index} (Ранг: {rank})")

        data_to_run.append({
            'range': f"{col_letter}{row_index}",
            'values': [[value_to_write]]
        })

    # 2. Подготовка MMRent Count (только для Гданьска)
    if city_name == "Гданьск" and mmrent_count is not None:
        try:
            from config_listings import MMRENT_COUNT_COLUMN_GDANSK
            mmrent_col_letter = col_to_letter(MMRENT_COUNT_COLUMN_GDANSK)
            data_to_run.append({
                'range': f"{mmrent_col_letter}{row_index}",
                'values': [[mmrent_count]]
            })
        except ImportError:
            print("   ⚠️ Не удалось импортировать MMRENT_COUNT_COLUMN_GDANSK")

    # Выполняем пакетное обновление
    if data_to_run:
        try:
            # Используем 'USER_ENTERED', чтобы числа записывались как числа, а не текст
            ws.batch_update(data_to_run, value_input_option='USER_ENTERED')
            print(f"✅ [GSheets] {city_name}: Данные успешно отправлены в таблицу.")
        except Exception as e:
            print(f"❌ Ошибка пакетного обновления {city_name}: {e}")
