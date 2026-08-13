import requests
from datetime import datetime


with open("check_log.txt", "a") as log_file:
    

    site = "https://www.mehdisalhi.com"

    try:
        response = requests.get(site)

        response_time = response.elapsed.total_seconds()

        if response.status_code == 200:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : The site {site} is up and running. Response time: {round(response_time, 2)} seconds.\n")
        else:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : The site {site} is down. Status code: {response.status_code}\n")

    except requests.exceptions.RequestException as e:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : The site {site} is down. Error: {e}\n")