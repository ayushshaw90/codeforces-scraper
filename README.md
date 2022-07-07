# scraper
In this project, one can monitor the number of questions solved by one's friends in codeforces.
The output is in the form of an questions_solved.xlsx file

## Installation instructions
Prerequisites: python3 and pip3 are needed.

### Install dependencies:
pip install -r requirements.txt

## Setting the credentials
in the api_info.py file, enter your codeforces api key and secret in appropriate places.

## Types of scans:
## Comprehensive scan
If one wants to get latest data about all his friends of codeforces, he can choose comprehensive scan
The only shortcoming of this process is, it requests data about all users. As a result, it takes longer time.

## Quick scan
If one wants to update the xlsx sheet with data of newly added friend whose data is not available in the xlsx sheet, he can use this scan.
The only shortcoming of this scan is, it does not update the data of users whose data is already present in the xlsx sheet.

