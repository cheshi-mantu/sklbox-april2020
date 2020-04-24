# for processing the requests to web sites
import requests
#to be able to make pause
import time
# creating the list of URLs we'll try to get using requests
lstURList = ["https://ya.ru",
             "https://www.multitran.com",
             "https://www.netnetweb.com/truefalse",
             "https://canihazip.com/s",
             "https://google.com"]
#checking if the number of URLs is enough accordignly to the homework requirements
print (f"The length of the list is {len(lstURList)}")
# integer to store the number of attempts
intNumberOfAttempts = 100
# int number of seconds to wait before next attempt
intNumberOfSecondsToWait  = 0
# log file name to store the output
fileOutputFileName = "request_results.txt"
#list to store the string with site address number of attempt and the result
listResultsStorage = []
#we'll open file for writing
fileOpenMode = "w"
# string to build line to store
strTempString = ""
strCRLF = "\n"
# here we go
for siteAddress in lstURList:
    print(f"Now requesting {siteAddress}")
    for i in range(0,intNumberOfAttempts):
        strTempString = "Site " + siteAddress + " attempt " +  str(i+1) + " returned status " + str(requests.get(siteAddress).status_code)
        listResultsStorage.append(strTempString)
        print (strTempString)
        time.sleep(intNumberOfSecondsToWait)
fileOutput = open(fileOutputFileName, fileOpenMode)
#writing file output
for item in listResultsStorage:
    fileOutput.write(item+strCRLF)
fileOutput.close()
print (f"Results are saved to file {fileOutputFileName}")