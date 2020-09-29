from sys import argv
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'}
try:
    os.mkdir(argv[1])
except FileExistsError:
    pass
pages_stack = list()
created_files = []
while True:
    input_url = input()
    if input_url.count('.'):  # My naive approach to detect proper URLS from saved files ._.
        if not input_url.startswith('https://'):
            input_url = 'https://' + input_url
        web_request = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(web_request.text)
        all_tags = soup.find_all()
        input_url = input_url.strip('https://')[:-4]
        with open(f'./{argv[1]}/' + input_url, 'w', encoding='utf-8') as writer:
            created_files.append(input_url)
            for tag in all_tags:
                if tag.name == 'a':
                    print(Fore.BLUE + tag.text)
                    writer.write(Fore.BLUE + tag.text)
                else:
                    print(Fore.WHITE + tag.text)
                    writer.write(Fore.WHITE + tag.text)
        with open(f'./{argv[1]}/' + input_url, 'r', encoding='utf-8') as reader:
            pages_stack.append(reader.read())
    elif input_url == 'exit':
        break
    elif input_url == 'back':
        try:
            print(pages_stack[:-1].pop())
        except IndexError:
            pass
    else:
        if input_url not in created_files:
            print('Error: Incorrect URL')
        else:
            with open(f'./{argv[1]}/' + input_url, encoding='utf-8') as reader:
                print(reader.read())
