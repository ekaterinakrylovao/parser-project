import logging
import pandas as pd

# Настройка логирования
logging.basicConfig(filename='parser.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def log_error(message):
    """Логирование ошибок."""
    logging.error(message)


def save_to_csv(data, filename):
    """Сохранение данных в CSV."""
    if not data:
        print("Нет данных для сохранения.")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Данные сохранены в {filename}")
