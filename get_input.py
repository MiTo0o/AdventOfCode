import os
import requests
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from pytz import timezone
from argparse import ArgumentParser
import time
from pathlib import Path

ADVENT_SESSION_COOKIE = os.getenv('ADVENT_SESSION_COOKIE')

parser = ArgumentParser(description="get the next day's input at midnight, pass arguments to manually fetch for a specific year/day")

parser.add_argument('--year', '-y', type=int, required=False, help='The year to fetch the puzzle for.')
parser.add_argument('--day', '-d', type=int, required=False, help='The day to fetch the puzzle for.')


def get_input(year: int, day: int) -> None:
    input_url = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(input_url, cookies={'session': ADVENT_SESSION_COOKIE})
    status_code = response.status_code
    if status_code == 404:
        print(f'FAILED TO FETCH INPUT FOR YEAR: {year}, DAY: {day}')
        return None
    else:
        return response.text


args = parser.parse_args()


if args.year and args.day:
    input_text = get_input(args.year, args.day)
    with open(Path(__file__).parent / f'{args.year}' / f'day-{str(args.day).zfill(2)}' / 'input.txt', 'w') as f:
        f.write(input_text)
else:
    est = timezone('EST')

    today = datetime.now(est)

    while today.day == datetime.now(est).day:
        print("EST time: ", datetime.now(est))

    now = datetime.now(est)
    input_text = get_input(now.year, now.day)

    if input_text:
        with open(Path(__file__).parent / f'{now.year}' / f'day-{str(now.day).zfill(2)}' / 'input.txt', 'w') as f:
            f.write(input_text)
    else:
        time.sleep(2)
        now = datetime.now(est)
        input_text = get_input(now.year, now.day)
        with open(Path(__file__).parent / f'{now.year}' / f'day-{str(now.day).zfill(2)}' / 'input.txt', 'w') as f:
            f.write(input_text)
    
    