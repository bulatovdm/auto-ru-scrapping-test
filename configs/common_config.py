import os

ROOT_PATH = os.path.dirname(os.path.abspath(
    os.path.join(os.path.dirname(__file__))))
LOGFILE_PATH = ROOT_PATH + '/scrapper.log'
AUTO_RU_REGIONS_ALIASES = {
    'Санкт-Петербург': 'sankt-peterburg'
}
START_YEAR = 2021
SEARCH_PARAMS = [
    'sort=cr_date-desc',
    'top_days=1'
]
TIMEOUT_TIME = 10
AUTO_RU_SCRAPPING_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Cookie': 'suid=71698f0d73df343552fe4189c2db2be4.0824d35ebeef942bc1f5ddb9b33fb4f0; yandexuid=1715021361619998515; my=YwA%3D; counter_ga_all7=2; _ym_uid=16205849251010990045; _ga=GA1.2.901636436.1621862388; _csrf_token=dff3af998bc2878d22871148dba1bee4009e3b1d77d80d98; from=direct; gdpr=0; panorama_press_and_spin_closed=true; panorama_interior_press_and_spin_closed=true; autoruuid=g6114545b2tf38ut4700ct69jbog3fel.a974a2fae00fdf93bc0c063382c50d90; yuidlt=1; autoru_sid=a%3Ag6114545b2tf38ut4700ct69jbog3fel.a974a2fae00fdf93bc0c063382c50d90%7C1629866869131.604800.1X08GcsfsqZioHyjUNlvCA.H5ybycZ3mQxkQD2eeJPC2dbr54J07LrAGzE6NeQEZZ0; crookie=QS/CLdrPh33luWAbp3bJMvRQl21ASKUi/kkcR/Xt5qZxmTBtrsFy5zZxMGkK5Koh96LSLmWm+3XzP2EGh25xZqYDCPY=; cmtchd=MTYyOTg2Njg2OTg3NA==; _gid=GA1.2.1789929771.1629866870; _ym_isad=2; bltsr=1; X-Vertis-DC=vla; autoru-visits-count=25; autoru-visits-session-unexpired=1; _gat_fixprocent=1; from_lifetime=1629895254222; _ym_d=1629895256; gradius=50',
    'Host': 'auto.ru',
    'origin': 'https://auto.ru',
    'Referer': 'https://auto.ru/sankt-peterburg/cars/used',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
