import pytest
import argparse
import urllib
import argparse
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import tempfile
import re
from urllib import request
import sqlite3
from project0 import main

url =  "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"
incident_data = main.fetchincidents(url)
incidents  = main.extractincidents(incident_data)
db = main.createdb()

def test_populate():
    main.populatedb(db, incidents)
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    time = []
    num = []
    loc = []
    nat = []
    ori = []
    for row in cur.execute('SELECT incident_time FROM incidents'):
        time.append(row)
    assert len(time) > 1

    for row in cur.execute('SELECT incident_number FROM incidents'):
        num.append(row)
    assert len(num) > 1

    for row in cur.execute('SELECT incident_location FROM incidents'):
        loc.append(row)
    assert len(loc) > 1

    for row in cur.execute('SELECT nature FROM incidents'):
        nat.append(row)
    assert len(nat) > 1

    for row in cur.execute('SELECT incident_ori FROM incidents'):
        ori.append(row)
    assert len(ori) > 1    
