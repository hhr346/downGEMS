'''
Get the Level2 data of GEMS
'''

import datetime
import os
import subprocess


APISITE="https://nesc.nier.go.kr:38032/api/"
#route
SATELLITE="GK2"
LEVEL="L2"
DATATYPE="UVI"

#parameter
APIKEY="api-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create each day's directory
filepath_pre = 'your_filepath'
begin = datetime.date(2023, 8, 1)
end = datetime.date(2023, 12, 31)
d = begin

while d<=end:
    filepath = filepath_pre + d.strftime("%Y%m/%d/")
    os.makedirs(filepath, exist_ok=True)
    os.chdir(filepath)
    for suffix in ['0045', '0145', '0245', '0345', '0445', '0545']:
        DDATE = d.strftime("%Y%m%d"+suffix)
        URL = APISITE + SATELLITE + "/" + LEVEL + "/" + DATATYPE + "/data/getFileItem.do?date=" + DDATE + "&key=" + APIKEY
        CURL = ["curl", "-OJ", "-#", URL]
        subprocess.run(CURL, check=True)
    d += datetime.timedelta(days=1)

