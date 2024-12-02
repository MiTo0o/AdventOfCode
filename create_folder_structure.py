from pathlib import Path
import os
from datetime import datetime
from pytz import timezone
import shutil
from argparse import ArgumentParser

est = timezone('EST')
now = datetime.now(est)

parser = ArgumentParser()
parser.add_argument('--year', '-y', type=int, required=False, default=now.year, help='The year to create the folder structure for defauts to current year.')

args = parser.parse_args()

year = args.year
for i in range(25):
    day = str(i + 1)
    
    # creates dir for each day if doesn't exist
    os.makedirs(Path(__file__).parent / f'{year}' / f'day-{day.zfill(2)}', exist_ok=True)
    
    # create empty exmaple input txt file, do nothing if exists
    try:
        open(Path(__file__).parent / f'{year}' / f'day-{day.zfill(2)}' / 'example.txt', 'x')
    except:
        pass
    
    # create empty input txt file, do nothing if exists
    try:
        open(Path(__file__).parent / f'{year}' / f'day-{day.zfill(2)}' / 'input.txt', 'x')
    except:
        pass
    
    part1_dst = Path(__file__).parent / f'{year}' / f'day-{day.zfill(2)}' / 'part1.py'
    part2_dst = Path(__file__).parent / f'{year}' / f'day-{day.zfill(2)}' / 'part2.py'

    try:
        open(part1_dst, 'x')
    except:
        pass
    
    try:
        open(part2_dst, 'x')
    except:
        pass

    # starter_src = Path(__file__).parent / 'starter.py'
    
    # if not os.path.exists(part1_dst):
    #     shutil.copyfile(starter_src, part1_dst)
    
    # if not os.path.exists(part2_dst):
    #     shutil.copyfile(starter_src, part2_dst)