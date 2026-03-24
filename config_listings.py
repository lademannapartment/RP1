import datetime as dt

# --- ВАШИ КОНСТАНТЫ ---
# URL Вашей Google Таблицы
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1t8jZFnJ5PxW9ry8SPN8WAGhbsgICn5F9BZCR9d4vB5U/edit"

# Названия листов
SHEET_NAME_GDANSK = "RankPokGdansk"
SHEET_NAME_SOPOT = "RankSopot"
SHEET_NAME_GDYNIA = "RankPokGdynia"  # <<< НОВАЯ КОНСТАНТА
# Общие параметры поиска
STAY_NIGHTS = 1
TIMEOUT_SEC = 60
DAYS_FORWARD = 60
MAX_RANK = 400
CREDENTIALS_FILE = "silken-glyph-443313-i4-cdf14b36288a.json"

# --- ЛИСТИНГИ ГДАНЬСКА (GDANSK) ---
MMRENT_COUNT_COLUMN_GDANSK = 3
# СВЯЗКА: Название листинга -> Индекс столбца (начиная с I=9)
LISTING_COLUMNS_GDANSK = {
    "Cactus Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 9,
    "Pineapple Room": 10,
    "Jager Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 11,
    "Cosy Room - Peaceful Retreat, 2 Minutes to Gdańsk Old Town": 12,
    "Lovely Room - Peaceful Retreat, 2 Minutes to Gdańsk Old Town": 13,
    "Spacious Room - Peaceful Retreat, 2 Minutes to Gdańsk Old Town": 14,
    "Bay Room -15 Minutes to Gdańsk Old Town & Seaside": 15,
    "Mirror Room -15 Minutes to Gdańsk Old Town & Seaside": 16,
    "Beacon Room -15 Minutes to Gdańsk Old Town & Seaside": 17,
    "Pink lady Room - 15 Minutes to Gdańsk Old Town & Sea": 18,
    "Dotted Room": 19,
    "Butterfly Room - 15 Minutes to Gdańsk Old Town & Sea": 20,
    "Monroe Room - 15 Minutes to Gdańsk Old Town & Sea": 21,
    "Superfly room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 22,
    "Sensational room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 23,
    "Vintage room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 24,
    "Leaf Room - 20 Minutes to Gdańsk Old Town & Seaside": 25,
    "Nest Room - 20 Minutes to Gdańsk Old Town & Seaside": 26,
    "Square Room - 20 Minutes to Gdańsk Old Town & Seaside": 27,
    "Twig Room - 20 Minutes to Gdańsk Old Town & Seaside": 28,
    "Alpha Room 10 min to Old Town Gdansk": 29,
    "Beta Room 10 min to Old Town Gdansk": 30,
    "Gamma Room 10 min to Old Town Gdansk": 31,
    "Downtown Room at Old Town Gdansk": 32,
    "Plaza Room at Old Town Gdansk": 33,
    "Danzig Room at Old Town Gdansk": 34,
    "Dali Room -10 Minutes to Gdańsk Old Town & Sea": 35,
    "Munch Room -10 Minutes to Gdańsk Old Town & Sea": 36,
    "Picasso Room -10 Minutes to Gdańsk Old Town & Sea": 37,
    "Beksiński Room -10 Minutes to Gdańsk Old Town & Sea": 38,
    "René Room -10 Minutes to Gdańsk Old Town & Sea": 39,
    "Van Gogh Room - 10 Minutes to Gdańsk Old Town & Sea": 40,
    "Creative Room - 10 Minutes to Gdańsk Old Town & Seaside": 41,
    "World Room - 10 Minutes to Gdańsk Old Town & Seaside": 42,
    "Lama Room - 10 Minutes to Gdańsk Old Town & Seaside": 43,
    "Colourful Room - 10 Minutes to Gdańsk Old Town & Seaside": 44,
    "Dolce Vita Room - 10 Minutes to Gdańsk Old Town & Seaside": 45,
    "Shrek Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 47,
    "Scooby Doo Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 49,
    "Pink Panther Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 50,
    "Spongebob Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 51,
    "Core Room - Charming Place, 5 Minutes to Gdańsk Old Town": 52,
    "Hub Room - Charming Place, 5 Minutes to Gdańsk Old Town": 53,
    "Direct Room - Charming Place, 5 Minutes to Gdańsk Old Town": 54,
    "Pane Room - Charming Place, 5 Minutes to Gdańsk Old Town": 55,
    "Lambert Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 56,
    "August Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 57,
    "Batory Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 58,
    "Sobieski Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 59,
    "Waza Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 60,
    "Walezy Room - Peaceful Retreat, 10 Minutes to Gdańsk Old Town & Seaside": 61,
    "Shark Room - 3 km to Baltic Sea": 62,
    "Piggy Room - 3 km to Baltic Sea": 63,
    "Turtle Room - 3 km to Baltic Sea": 64,
    "Tiny Room - 10 Minutes to Gdańsk Old Town": 65,
    "Astro Room - 10 Minutes to Gdańsk Old Town": 66,
    "Future Room - 10 Minutes to Gdańsk Old Town": 67,
    "Hope Room - 10 Minutes to Gdańsk Old Town": 68,
    "Brand Room - 10 Minutes to Gdańsk Old Town": 69,
    "Umbrella Room - 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 70,
    "Duo Room - 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 71,
    "Teddy Bear Room - 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 72,
    "Circus Room - 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 73,
    "Bonjour Room - 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 74,
    "Ocean Room - 1 km to Baltic Sea & 15 Minutes to Gdańsk Old Town": 75,
    "Sandcastle Room - 1 km to Baltic Sea & 15 Minutes to Gdańsk Old Town": 76,
    "Coral Room - 1 km to Baltic Sea & 15 Minutes to Gdańsk Old Town": 77,
    "Jungle Room Old Town Gdansk": 78,
    "Rose Room Old Town Gdansk": 79,
    "Paris Room Old Town Gdansk": 80,
    "Giraffe Room 5 min to Old Town Gdańsk": 81,
    "Zebra Room 5 min to Old Town Gdańsk": 82,
    "Monkey Room 5 min to Old Town Gdańsk": 83,
    "Snake Room 5 min to Old Town Gdańsk": 84,
    "Stitch Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 85,
    "Lion King Room 10 Min to Old Town Gdańsk,PKP & Shopping Mall": 86,
    "Ruby Room at Old Town Gdańsk": 87,
    "Silver Room at Old Town Gdańsk": 88,
    "Bronze Room at Old Town Gdańsk": 89,
    "Mercury Room - 15 min to Old Town Gdansk": 90,
    "Hostel Room - 15 min to Old Town Gdansk": 91,
    "Earth Room - 15 min to Old Town Gdansk": 92,
    "Mars Room - 15 min to Old Town Gdansk": 93,
    "Jupiter Room - 15 min to Old Town Gdansk": 94,
    "Saturn Room - 15 min to Old Town Gdansk": 95,
    "Uranus Room - 15 min to Old Town Gdansk": 96,
    "Neptune Room - 15 min to Old Town Gdansk": 97,
    "Pluto Room - 15 min to Old Town Gdansk": 98,
    "Milkyway Room - 15 min to Old Town Gdansk": 99,
    "Sunlight Room - 15 min to Old Town Gdansk": 100,
}

# --- ЛИСТИНГИ СОПОТА (SOPOT) ---
LISTING_COLUMNS_SOPOT = {
    "Deer Room - 5 Minutes to Sopot Molo & Seaside": 6,   # F
    "Elk Room - 5 Minutes to Sopot Molo & Seaside": 7,    # G
    "Balance Room - 5 Minutes to Sopot Molo & Seaside": 8,# H
    "Funky Room - 5 Minutes to Sopot Molo & Seaside": 9,  # I
    "Array Room - 5 Minutes to Sopot Molo & Seaside": 10, # J
    "Surf Room - 5 Minutes to Sopot Molo & Seaside": 11,  # K
}

LISTING_COLUMNS_GDYNIA = {
    "Blue Room 2 minutes to City Center Gdynia & Seaside": 6,
    "Green Room 2 minutes to City Center Gdynia & Seaside": 7,
    "Orange Room 2 minutes to City Center Gdynia & Seaside": 8,
}
