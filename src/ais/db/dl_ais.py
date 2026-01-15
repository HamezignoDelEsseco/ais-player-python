import os
import tqdm
import requests
import datetime as dt
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2024/AIS_{}.zip"
OUTPUT_DIR = "C:/AIS_RAW/"

START = dt.date(2024, 1, 1)
END = dt.date(2024, 12, 31)


MAX_WORKERS = 3

def date_range(start: dt.date, end: dt.date) -> List[str]:
    days = (end - start).days
    return [str(start + dt.timedelta(days=i)).replace('-', '_') for i in range(0, days)]



def download_one(date_str: str) -> str:
    url = BASE_URL.format(date_str)
    save_path = os.path.join(OUTPUT_DIR, f'{date_str}.zip')

    try:
        with requests.get(url, stream=True) as r:
            if r.status_code == 404:
                return f'File {date_str} failed'

            r.raise_for_status()

            total_size = int(r.headers.get('content-length', 0))
            block_size = 8192

            with open(save_path, 'wb') as f, tqdm.tqdm(
                    total=total_size,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                    leave=False,
            ) as bar:
                for chunk in r.iter_content(chunk_size=block_size):
                    if chunk:
                        size = f.write(chunk)
                        bar.update(size)

        return f'Downloaded {date_str}'

    except Exception as e:
        return f'Error when processing file {date_str}: {str(e)}'

def download_all():
    all_dates = date_range(START, END)
    print(f'Downloading all dates (total of {len(all_dates)}, from {all_dates[0]} to {all_dates[-1]})')
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_date = {executor.submit(download_one, d): d for d in all_dates}
        for future in as_completed(future_to_date):
            result = future.result()
            print(result)


# download_all()