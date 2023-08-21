import requests
import time
from colorama import init, Fore, Style

init()

username = ""
address_eth = ""

def send_get_request():
    url = f'https://api.tss.traitsniper.com/tweet/get-code?address={address_eth}&username={username}'

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "api.tss.traitsniper.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "TE": "trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/116.0"
    }

    try:
        response = requests.get(url, headers=headers)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        if response.status_code != 304:
            response_data = response.json()

            if response_data.get('data') is not None:
                log_message = f"{Fore.GREEN}Success:{Style.RESET_ALL} {response_data}"
            else:
                log_message = f"{Fore.RED}Error:{Style.RESET_ALL} No data available"
        else:
            log_message = f"{Fore.YELLOW}Request cached, nothing changed! {Style.RESET_ALL}"
    except Exception as e:
        log_message = f"{Fore.RED}Error while making the request:{Style.RESET_ALL} {e} \n Server response: {response.status_code}, {response.content}"

    with open("logs.txt", "a") as log_file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"[{timestamp}] {log_message}\n")

    print(timestamp, log_message)

def main():
    while True:
        send_get_request()
        time.sleep(30)

if __name__ == "__main__":
    main()

