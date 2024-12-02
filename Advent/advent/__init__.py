import os
from pathlib import Path
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import shutil
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Advent:
    def __init__(self, year: int, day: int, example: bool, file: str) -> None:
        self.year = year
        self.day = day
        # self.ADVENT_SESSION_COOKIE = os.getenv('ADVENT_SESSION_COOKIE')
        if example:
            self.data = open(Path(file).parent / 'example.txt', 'r', encoding='utf-8').read()
        else:
            self.data = open(Path(file).parent / 'input.txt', 'r', encoding='utf-8').read()
        
    # def print_cookie(self):
    #     print(self.ADVENT_SESSION_COOKIE, self.year, self.day)
        
    def raw(self):
        return self.data
    
    def paragraph(self):
        return [i.splitlines() for i in self.data.split('\n\n')]

    def lines(self):
        return self.data.splitlines()

    def string_center_terminal(self, s: str) -> str:
        columns = shutil.get_terminal_size().columns
        return s.center(columns)

    def submit(self):
        pass

    def __floordiv__(self, answer):
        c = colored(answer, 'green')
        bruh = f'The answer is: *^* {c} *^*'
        submit_notice = self.string_center_terminal(f'{bruh}')
        print(submit_notice)

    # def 