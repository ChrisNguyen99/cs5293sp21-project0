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

def test_extract():
    incidents = main.extractincidents(incident_data)
    assert  len(incidents) > 1
