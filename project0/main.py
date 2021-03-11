import argparse
import urllib
import project0
import PyPDF2
import tempfile
import re

def fetchincidents(url):
    url = ("https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf")
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()

def extractincidents(data):
    fp = tempfile.TemporaryFile()
    row = []
    arr = []
    #write to temp file
    fp.write(data.read())
    
    #set cursor to beginning
    fp.seek(0)
    
    #read pdf
    pdfReader = PyPDF2.pdf.PdfFileReader(fp) 
    
    #loop through pages and extract to array
    for x in range(pdfReader.getNumPages()):
        # Get first page
        page1 = pdfReader.getPage(0).extractText()
        row = page1.split("\n")
        for y in row
            arr.append(y)
    
    return arr
    
def createdb():
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    
    cur.execute("CREATE TABLE incidents(
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT)")
    con.commit()
    
def populatedb(db, incidents)
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    incidents.pop(0)
    incidents.pop(0)
    incidents.pop(0)
    for row in incidents:
        time = re.search(r"3\w*2021 \w+:\w+\b", row)
        num = re.search(r"2021-\w+\b", row)
        loc = re.search(r"\b[A-Z0-9] \t+ ^[A-Z]$", row)
        nature = re.search(r"\w[A-Z][a-z]* (\s[A-Z][a-z]*)*)) ", row)
        ori = re.search("\w[A-Z]+", row)
        temp = [time,num,loc,nature,ori]
        cur.execute("INSERT INTO incidents VALUES(?,?,?,?,?)", temp)
    con.commit()
    cur.close()
    con.close()
    
def status():
    con = sqlite3.connect('normanpd.db')
    cur - con.cursor()
    
    
def main(url):
    #download data
    incident_data = project0.fetchincidents(url)
    
    #extract data
    incidents = project0.extractincidents(incident_data)
    
    #create new database
    db = project0.createdb()
    
    #insert data
    project0.populatedb(db, incidents)
    
    #print incident counts
    project0.status(db)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parse.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
