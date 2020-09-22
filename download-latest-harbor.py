#!/usr/bin/env python3
import os, json, requests

release_data_url = "https://api.github.com/repos/SkyrimTogether/issues-launcher/releases/latest"
release_data = requests.get(url=release_data_url)
assets_data_url = release_data.json()['assets_url']
assets_data = requests.get(url=assets_data_url)
assets = assets_data.json()

if(os.path.isfile('_harbor.exe')):
    os.remove('_harbor.exe')
    print("Removed old download")

if(assets):
    for asset in assets:
        if(str(asset['name']).endswith('.exe')):
            harbor_download_url = str(asset['browser_download_url'])
            print("Downloading: " + harbor_download_url)
            harbor_data = requests.get(harbor_download_url, allow_redirects=True)
            open('_harbor.exe', 'wb').write(harbor_data.content)
            print("Done!")
            break

    if(os.path.isfile('_harbor.exe')):
        exit(0)
exit(1)