'''
A python script to get the datelist of the data from the NIER API
'''
import subprocess
APISITE="https://nesc.nier.go.kr:38032/api/"

#route
SATELLITE="GK2"
LEVEL="L2"
DATATYPE="UVI"

#parameter
SDATE="202312261004"
EDATE="202312271004"
FORMAT="json"
APIKEY="api-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#selectType
METHOD="getFileDateList" #search : observation Time
# METHOD="getFileList"  #search : Filename

URL = APISITE + SATELLITE + "/" + LEVEL + "/" + DATATYPE + "/data/" + METHOD + ".do?sDate=" + SDATE + "&eDate=" + EDATE + "&format=" + FORMAT + "&key=" + APIKEY
command = ["curl", "-i", URL]
result = subprocess.run(command, check=True)

# command = "curl -i " + URL
# result = subprocess.check_output(command, shell=True)

