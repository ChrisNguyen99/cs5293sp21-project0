# cs5293sp21-project0
project 0 of Text Analytics
Christopher Nguyen
getting list of natures from incident pdf on norman pd site with count of each incident
python3 on linux
pipenv, PyPDF2, sqlite3, re, urllib should be installed

Instructions:
get code using git clone into desired directory git@github.com:ChrisNguyen99/cs5293sp21-project0.git
ls into project0
run using: pipenv run python project0/main.py --incidents <url>
replace <url> with pdf file site so for example: pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf

Functions:
fetchincidents(url): uses urllib request to open website passed in and store in a temporary file
extractincidents(incident_data): uses temp file to read pdf data and extract text using PyPDF2 file reader, each page is read and stored in a 

Bugs/Assumptions:
gps coordinates are not read into location
the number of entries in the table is less than the total records in the pdf, regex didn't catch everything


