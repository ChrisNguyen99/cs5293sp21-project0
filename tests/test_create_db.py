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
def test_create():
    main.createdb()
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    temp = []
    for row in cur.execute(''' SELECT name FROM sqlite_master WHERE name='incidents' '''):
        temp.append(row)
    assert len(temp) == 1
