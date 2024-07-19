import requests
import logging
from requests.adapters import HTTPAdapter, Retry
import time
import json
import os

cookies = {
    'abgroup': '10',
    'aboptin': '1',
    'preferredPlatform': 'desktop',
    '_ga': 'GA1.1.1551574057.1713978854',
    'XSRF-TOKEN': '3d29f144-9992-4589-b768-829ac740c5ed',
    'WSID01': 'OTA1MmE3ZGYtZjRhOC00ODYzLTg2ZmQtZTZhODI3NjQ5NzBi',
    '_ga_Z9WBZVFLPZ': 'GS1.1.1721242365.8.1.1721243013.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    # 'cookie': 'abgroup=10; aboptin=1; preferredPlatform=desktop; _ga=GA1.1.1551574057.1713978854; XSRF-TOKEN=3d29f144-9992-4589-b768-829ac740c5ed; WSID01=OTA1MmE3ZGYtZjRhOC00ODYzLTg2ZmQtZTZhODI3NjQ5NzBi; _ga_Z9WBZVFLPZ=GS1.1.1721242365.8.1.1721243013.0.0.0',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://patriots.win/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-platform': 'Scored-Desktop',
    'x-xsrf-token': '3d29f144-9992-4589-b768-829ac740c5ed',
}

params = {
    'community': 'thedonald',
}



logging.basicConfig(level=logging.DEBUG)

s = requests.Session()
retries = Retry(total=5, backoff_factor=1)
s.mount('https://patriots.win/', HTTPAdapter(max_retries=retries))

try:
    response = s.get(
        'https://patriots.win/api/v2/post/hotv2.json',
        headers=headers,
        cookies=cookies,
        params=params
    )
    if response.status_code == 200:
        data = response.json()
        #create a 15-character timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        with open(f"{timestamp}.json", 'w') as file:
            json.dump(data, file)
    else:
        logging.error(f"Request failed with status code {response.status_code}")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")