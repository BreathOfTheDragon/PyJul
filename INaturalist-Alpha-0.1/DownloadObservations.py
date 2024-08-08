import requests
import os
import json
import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

per_page = 200

with open('./pollinators.txt') as f:
    pollinators = f.read().splitlines()

print(pollinators)


def get_observations(common_name, per_page=200, page=1):
    url = "https://api.inaturalist.org/v1/observations"
    params = {
        "q": common_name,  # taxon name : common name
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        download_folder = common_name.replace(" ", "_")
        with open(f'{download_folder}/{common_name}.json', 'w') as f:
            json.dump(data, f)
    else:
        print("get_observations failed")


for common_name in pollinators:
    download_folder = common_name.replace(" ", "_")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    get_observations(common_name=common_name, per_page=per_page)
