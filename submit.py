from bs4 import BeautifulSoup
from termcolor import colored, cprint
import shutil
import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = 'https://adventofcode.com/2022/day/7'
cookie = os.getenv('ADVENT_SESSION_COOKIE')
# xd = requests.get(url, cookies={'session':cookie})

res = requests.post(
    'https://adventofcode.com/2018/day/1/answer',
    headers={"User-Agent": 'this is already you know xdd'},
    cookies={"session": cookie},
    data={"level": 1, "answer": str('470')},
)

soup = BeautifulSoup(res.text, 'html.parser')

def string_center_terminal(s: str) -> str:
    columns = shutil.get_terminal_size().columns
    return s.center(columns)

if soup.find("article").find("p").find_all('span', {'class': 'day-success'}):
    print()
    print()
    cprint(string_center_terminal('CORRECT'), "green")
    print()
    print()
else:
    print()
    print()
    cprint(string_center_terminal('WRONG'), "red")
    print()
    print()