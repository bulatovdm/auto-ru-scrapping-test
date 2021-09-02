import datetime
from pprint import pprint
from itertools import cycle
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from logger import get_logger
from sleep import scrapping_sleep
from string_to_number import string_to_number
from proxies import AUTO_RU_SCRAPPER_PROXIES
from common_config import AUTO_RU_SCRAPPING_HEADERS, LOGFILE_PATH, AUTO_RU_REGIONS_ALIASES, SEARCH_PARAMS, START_YEAR, TIMEOUT_TIME

logger = get_logger(__name__, LOGFILE_PATH)


def main(region="Санкт-Петербург"):
    """Scrapping offers from a listing.

    Args:
        region (str, optional): The region to parse data. Defaults to "Санкт-Петербург".
    """
    start_time = datetime.datetime.now()
    options = prepare_scrapping_options(region)

    with Pool(processes=len(AUTO_RU_SCRAPPER_PROXIES)) as pool:
        pool.map(parse_base_page_data, options)

    logger.info(
        f'Время выполнения скрипта: {datetime.datetime.now() - start_time}')


def parse_base_page_data(options):
    """Parsing the list of pagination URLs and the base page's source code.

    Args:
        options (dict): The options dictionary.
    """

    headers = options['headers']
    region = options['region']
    year = options['year']
    proxy = options['proxy']

    region_alias = AUTO_RU_REGIONS_ALIASES[region]

    logger.info(f'Параметры: год – {year}, регион - {region}')
    url = f'https://auto.ru/{region_alias}/cars/{year}-year/used/?{"&".join(SEARCH_PARAMS)}'
    logger.info(
        f'Получаем исходный код для базовой страницы c url {url}...')

    try:
        response = requests.get(url, headers=headers,
                                proxies=proxy, timeout=TIMEOUT_TIME)
        response.encoding = 'urf-8'

        source_code = response.text
        soup = BeautifulSoup(source_code, 'html.parser')
        offers_elements = soup.find_all(class_='ListingItem')

        for offer_element in offers_elements:
            offer_data = {}

            try:
                url_element = offer_element.find(
                    'a', class_='ListingItemTitle__link')
            except:
                logger.warning('Отсутствует ссылка для предложения.')
                continue

            try:
                href = url_element.get('href')
            except:
                logger.warning('Отсутствует аттрибут href для предложения.')
                continue

            href = href.split('?')[0]
            offer_data['url'] = href
            title = url_element.get_text()
            offer_data['title'] = title

            price_element = offer_element.find(class_='ListingItem__price')

            if price_element is not None:
                price = price_element.get_text()
                price = string_to_number(price)
                offer_data['price'] = price

            release_year_element = offer_element.find(
                class_='ListingItem__year')

            if release_year_element is not None:
                release_year = release_year_element.get_text()
                release_year = string_to_number(release_year)
                offer_data['release_year'] = release_year

            run_element = offer_element.find(class_='ListingItem__kmAge')

            if run_element is not None:
                run = run_element.get_text()
                run = string_to_number(run)
                offer_data['run'] = run

            logger.info(
                f'Данные предложений на странице: {pprint(offer_data)}')

    except Exception as e:
        logger.warning(
            f'Возникла ошибка при парсинге страницы с url  {url}. Прокси: {proxy}. Текси ошибки: {e}')


def prepare_scrapping_options(region):
    """Preparing parsing options
    Args:
        region (str): The region to parse data.

    Returns:
        list: The list of options including `year` and `proxy` keys.
    """

    current_year = datetime.datetime.now().year
    year = START_YEAR
    proxy_cycle = cycle(AUTO_RU_SCRAPPER_PROXIES)
    proxy = next(proxy_cycle)

    options = []

    while year <= current_year:
        options.append({
            'year': year,
            'proxy': {
                'http': f'http://{proxy}'
            },
            'region': region,
            'headers': AUTO_RU_SCRAPPING_HEADERS
        })

        year += 1
        proxy = next(proxy_cycle)
    return options


if __name__ == '__main__':
    main()
