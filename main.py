from parser import parse_organization
from utils import save_to_csv
import config
import time


def main():
    inns = config.INNS  # Список ИНН для парсинга
    data = []

    for inn in inns:
        print(f"Парсинг ИНН: {inn}")
        org_data = parse_organization(inn)
        if org_data:
            print(f"Данные получены: {org_data}")
            data.append(org_data)
        else:
            print(f"Данные для ИНН {inn} не найдены.")
        time.sleep(2)  # Задержка 2 секунды между запросами

    save_to_csv(data, config.OUTPUT_FILE)


if __name__ == "__main__":
    main()
