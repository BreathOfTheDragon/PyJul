import requests
import os
import json
import pandas as pd

with open('./pollinators.txt') as f:
    pollinators = f.read().splitlines()

print(pollinators)

for common_name in pollinators:

    download_folder = common_name.replace(" ", "_")
    with open(f'{download_folder}/{common_name}.json', 'r') as f:

        data = json.load(f)
        observations_list_of_dicts = data.get("results", [])

        i = 1
        for little_dict in observations_list_of_dicts:

            # print(little_dict["photos"][0]["url"].replace("square", "large"))
            # print(little_dict["id"])

            # some data type testing, nothing to see here
            # {
            # print(len(little_dict))
            # print(type(little_dict))
            # print(type(little_dict["taxon"]))
            # print(little_dict["taxon"].keys())
            # print(little_dict["taxon"]["default_photo"]["medium_url"])
            # print(little_dict["taxon"].keys())
            # for (key, value) in little_dict.items():
            #     print(key)
            #     print(value)
            #     print("************")
            # }
            try:
                url = little_dict['photos'][0]['url'].replace("square", "large")
                idd = little_dict['id']

                response = requests.get(url)

                if not os.path.exists(download_folder):
                    os.makedirs(download_folder)

                if response.status_code == 200:
                    with open(os.path.join(download_folder, f"{i}_{idd}.jpg"), 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded {i}th image of {common_name} with id {idd}")
                else:
                    print(f"Failed to download {i}th image of {common_name} with id {idd}")
                i += 1
            except:
                pass
