import argparse
import urllib
import project0

def fetchincidents(url):
    url = ("https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf")
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()

def createdb():
    CREATE TABLE incidents (
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT
    );
    
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
