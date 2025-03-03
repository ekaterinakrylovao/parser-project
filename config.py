# Список ИНН для парсинга
INNS = ['2310031475', '7717127211']

# Выходной файл
OUTPUT_FILE = 'data/organizations.csv'

# User-Agent для запросов
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive"
}

# Прокси (если нужно)
PROXIES = None
# PROXIES = {
#     'http': 'http://',
#     'https': 'https://'
# }
