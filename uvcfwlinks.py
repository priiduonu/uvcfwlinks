#!/usr/bin/env python3

"""
uvcfwlinks

Fetches UVC camera firmware information from the Ubiquiti firmware API endpoint(s).

- if no camera platform is given, returns the latest f/w info for all platforms
- if camera platform is given, returns all f/w info for the given platform
"""

import requests
import argparse


def fetch_data(url):

    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit(1)


def main():

    parser = argparse.ArgumentParser(description="Fetch firmware information from the Ubiquiti firmware API.")
    parser.add_argument("-p", "--platform", dest="platform", help="return all f/w info for the given platform")

    args = parser.parse_args()
    platform = args.platform

    # set the API endpoint based on the presence of the platform parameter:
    if platform:
        url = f"https://fw-update.ui.com/api/firmware?filter=eq~~product~~uvc&filter=eq~~channel~~release&filter=eq~~platform~~{platform}&sort=version&limit=999"
    else:
        url = "https://fw-update.ui.com/api/firmware-latest?filter=eq~~product~~uvc&filter=eq~~channel~~release&sort=platform"

    data = fetch_data(url)

    firmware_list = data.get("_embedded", {}).get("firmware", [])

    if firmware_list:
        for firmware in firmware_list:
            print(f"platform: {firmware.get('platform')}")
            print(f"version:  {firmware.get('version')}")
            print(f"updated:  {firmware.get('updated')}")
            print(f"link:     {firmware.get('_links', {}).get('data', {}).get('href')}")
            print(f"sha256:   {firmware.get('sha256_checksum')}")
            print("-" * 50)
        print(f"{len(firmware_list)} records found")
    else:
        print("No firmware data found.")


if __name__ == "__main__":
    main()
