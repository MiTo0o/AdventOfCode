# HOW TO USE THIS TEMPLATE

# set up

# .env file

`ADVENT_SESSION_COOKIE="YOUR_SESSION_COOKIE"`


`python3 -m venv .venv`

switch to use the venv 
close and reopen terminal to use venv terminal

# activate the venv

## On Windows, run:
 
`.venv\Scripts\activate.bat`
## On Unix or MacOS, run:

`source .venv/bin/activate`

# install packages 

`pip3 install -r requirements.txt`

# install advent packagte

`pip install -e Advent`

# install util package
`pip install -e Util`

# gitignore

# import not resolved
## breaks for custom modules
https://stackoverflow.com/questions/72322120/vscode-import-x-could-not-be-resolved-even-though-listed-under-helpmodules


## UNCOMMENT THINGS FROM GITIGNORE
add .gitignore file 
  - add .venv
  - add base files
  - ignore all original files

# Remove md files
# add readme.md

