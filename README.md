# cs5293sp21-project0
project 0 of Text Analytics  
Christopher Nguyen  
getting list of natures from incident pdf on norman pd site with count of each incident  
python3 on linux 
pipenv, PyPDF2, sqlite3, re, urllib, argparse, tempfile should be installed 
  
Instructions:  
get code using git clone into desired directory git@github.com:ChrisNguyen99/cs5293sp21-project0.git  
ls into project0  
run using: pipenv run python project0/main.py --incidents <url>  
replace <url> with pdf file site so for example: pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf  
  
Functions:  
fetchincidents(url): uses urllib request to open website passed in and store in a temporary file  
extractincidents(incident_data): uses temp file to read pdf data and extract text using PyPDF2 file reader, each page is read and rows are split and stroed in an array that's returned  
createdb(): create a new table based on pdf headers from sqlite3 after connecting, new table each run  
populatedb(db, incidents): takes array extracted and removes headers from top of page 1 and removes date/time from bottom of file, regex matches headers and inserts into table  
status(): as per request list of natures is selected from table and is printed along with number of occurences by alphabet  
  
Bugs/Assumptions:  
a valid url is provided(one used above works)  
pdf is from march 2021  
at least one nature is provided  
gps coordinates are not read into location  
the number of entries in the table is less than the total records in the pdf, regex didn't catch everything  
because of this array lengths per header were different, had to compromise and insert number of rows based on smallest array  
tested on single pdf as provided above  

Testing:  
pipenv install pytest installs pytest  
pipenv run pytest runs tests in the directory which should pass all 5 tests:  
test_download.py: verifies a temp file was created and isn't empty  
test_extract.py: verifies text was extracted from pages and rows were added to a returned array  
test_create_db.py: verifies a table was added to hold incident records  
test_populate_db.py: tests rows were inserted into created table and each column isn't empty  
test_status.py: tests list of natures was outputed and isn't empty  

Sources:  
official documentation getting to know libraries:  
https://docs.python.org/3.8/library/importlib.html  
https://docs.python.org/3.8/library/sqlite3.html  
https://docs.python.org/3/library/urllib.request.html  
https://pythonhosted.org/PyPDF2/PdfFileReader.html  
https://pythonhosted.org/PyPDF2/PageObject.html#PyPDF2.pdf.PageObject  
https://docs.python.org/3/library/re.html  

https://stackoverflow.com/questions/17015980/python-how-to-print-sqlite-table: clarifying how to use sqlite3 and cursors  
https://stackoverflow.com/questions/12700558/print-without-space-in-python-3: printing without extra spaces after fetching table records  
https://stackoverflow.com/questions/11452299/import-parent-directory-for-brief-tests: fixing import errors on tests  
https://pythonexamples.org/python-sqlite3-check-if-table-exists/: how to check if a table exists  
