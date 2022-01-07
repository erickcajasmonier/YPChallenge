# YPChallenge

## Task #1: Exploratory Testing Challenge
Please find the exploratory testing challenge markdown file [here](/Exploratory_Charters.md)

## Task #2: RESTful API Automation Testing
Python version:
- Python 3.9

In case you are using a Macbook and have two versions of python (python 2 and python 3), please execute the following command to have python 3 as the default python version runner: `ln -s -f /usr/local/bin/python3.# /usr/local/bin/python`, replease # with the python version number.
Then reopen the terminal and execute `python --version` to check the correct latest default version.

You must install the pip packages in order to run the automation testing, please execute `pip install -r requirements.txt` in your terminal.

Python Packages used for this AUT project:
- pytest v6.2.5
- requests v2.27.1
- Faker v11.3.0
- python-dotenv v0.19.2

There is a **.env.template** file, this file must be name changed to **.env** file.

To run all tests you need to go to the main project folder for example: `cd /Users/CodeChallenge/YPChallenge` and execute the command `pytest` or `pytest -s` using the terminal.