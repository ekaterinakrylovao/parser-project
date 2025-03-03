import requests
from bs4 import BeautifulSoup
from utils import log_error
import config


def parse_organization(inn):
    url = f"https://www.rusprofile.ru/search?query={inn}"
    try:
        response = requests.get(url, headers=config.HEADERS, proxies=config.PROXIES)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение данных
        name = soup.find('h1', itemprop='name').text.strip() if soup.find('h1', itemprop='name') else None

        # Полное наименование организации
        full_name_element = soup.find('span', itemprop='legalName')
        full_name = full_name_element.text.strip() if full_name_element else None

        # ОГРН
        ogrn_element = soup.find('span', id='clip_ogrn')
        ogrn = ogrn_element.text.strip() if ogrn_element else None

        # ИНН
        inn_element = soup.find('span', id='clip_inn')
        inn = inn_element.text.strip() if inn_element else None

        # КПП
        kpp_element = soup.find('span', id='clip_kpp')
        kpp = kpp_element.text.strip() if kpp_element else None

        # Дата регистрации
        registration_date_element = soup.find('dd', class_='company-info__text', itemprop='foundingDate')
        registration_date = registration_date_element.text.strip() if registration_date_element else None

        # Юридический адрес
        address_element = soup.find('span', id='clip_address')
        address = address_element.text.strip() if address_element else None

        # Уставный капитал
        capital_element = soup.find('span', class_='copy_target')
        capital = capital_element.text.strip() if capital_element else None

        return {
            'name': name,
            'full_name': full_name,
            'ogrn': ogrn,
            'inn': inn,
            'kpp': kpp,
            'registration_date': registration_date,
            'address': address,
            'capital': capital
        }
    except Exception as e:
        log_error(f"Ошибка при парсинге ИНН {inn}: {e}")
        return None
