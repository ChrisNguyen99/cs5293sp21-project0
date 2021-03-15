import argparse
import urllib
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter
import tempfile
import re
from urllib import request
import sqlite3

def fetchincidents(url):
   # url = ("https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf")
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    file = open('temp.txt', 'wb')
    file.write(data)
    file.close()

def extractincidents(data):
    data = open('temp.txt', 'rb')
    fp = tempfile.TemporaryFile()
    row = []
    arr = []
    #write to temp file
    fp.write(data.read())
    
    #set cursor to beginning
    fp.seek(0)
    
    #read pdf
    pdfReader = PdfFileReader(fp) 
    
    #loop through pages and extract to array
    for x in range(pdfReader.getNumPages()):
        # Get page
        page = pdfReader.getPage(x).extractText()
        row = page.split("\n")
        for y in row:
            arr.append(y)
   
    return arr
    
def createdb():
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS incidents")
    cur.execute("CREATE TABLE IF NOT EXISTS  incidents(\
        incident_time TEXT,\
        incident_number TEXT,\
        incident_location TEXT,\
        nature TEXT,\
        incident_ori TEXT)")
    con.commit()
    
def populatedb(db, incidents):
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
        
    time = []
    num = []
    loc = []
    nat = []
    ori = []
    temp = []
    #remove headers
    incidents.remove('NORMAN POLICE DEPARTMENT')
    incidents.remove('Daily Incident Summary (Public)')
    incidents.remove('Date / Time')
    incidents.remove('Incident Number')
    incidents.remove('Location')
    incidents.remove('Nature')
    incidents.remove('Incident ORI')
    for str in incidents:
        match = re.search('^3/', str)
        if match != None:
            time.append(str)
        match = re.search('^2021-', str)
        if match != None:
            num.append(str)
        match = re.search('[A-Z0-9\s ]+ [A-Z0-9\s ]+ [A-Z0-9 ]+', str)
        if match != None:
            loc.append(str)
        match = re.search('[A-Z]+[a-z]+', str)
        if match != None:
            nat.append(str)
        match = re.search('^[A-Z0-9]+$', str)
        if match != None:
            ori.append(str)
    #extra header at end    
    time.pop()

    for x in range(len(loc)):
        temp.append((time[x], num[x], loc[x], nat[x], ori[x]))
    
    cur.executemany("INSERT INTO incidents VALUES (?,?,?,?,?)", temp)
    con.commit()
    cur.close()
    con.close()
    
def status():
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    natures = []
    con.commit()
    for row in cur.execute('SELECT nature, COUNT(nature) FROM incidents GROUP BY nature HAVING COUNT(nature) > 0'):
        natures.append(row)
    for nat in range(len(natures)):
        print(natures[nat][0],'|',natures[nat][1],sep='')
    
def main(url):
    #download data
    incident_data = fetchincidents(url)
    
    #extract data
    incidents = extractincidents(incident_data)
    
    #create new database
    db = createdb()
    
    #insert data
    populatedb(db, incidents)
    
    #print incident counts
    status()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
