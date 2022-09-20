# import readline
import time
import requests
import time
from datetime import datetime
import random
import csv
import sys
import traceback


SLEEP_VALUE=5

def generator():

    amd_power = random.randint(600,1100)
    amd_cpu_util = random.randint(10,60)
    amd_cpu_util_percentage = amd_cpu_util / 100
    current_date=datetime.now()
    c_date=current_date.strftime('%Y-%m-%d %H:%M:%S')
    intel_power = random.randint(950,1400)
    intel_cpu_util = random.randint(15,90)
    intel_cpu_util_percentage = intel_cpu_util / 100
    print("Generated values are:",c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
    return(c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)



def getDataFromCSV(csvfile):
    
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(csvfile)
    reader_obj.re
        #reopen the file to read from begining
    #for row in reader_obj:
    c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage = row

    print("CSV values are:",c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
    return(csvfile,c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)

def postData(c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage):
    data = {'c_date':c_date,
        'amd_power':amd_power,
        'amd_cpu_util':amd_cpu_util,
        'amd_cpu_util_percentage':amd_cpu_util_percentage,
        'intel_power':intel_power,
        'intel_cpu_util':intel_cpu_util,
        'intel_cpu_util_percentage':intel_cpu_util_percentage
        }

    url = 'http://localhost:5000/populate_values1'
    x = requests.post(url, json=data)
    print("POST Response is:",x.text)
    print('sleep for ',SLEEP_VALUE)
    time.sleep(SLEEP_VALUE)

if __name__ == '__main__':

    if (len(sys.argv)<2) :
        print("Two arguments expected, Usage schedule.py method  For example: schedule.py 0 #For Generator.  schedule.py 1 mwc_test1.csv #For CSV")
        exit(1)

    flag=sys.argv[1]

    if (flag=="0") :
        print("Using Generator method ...")
    elif (flag=="1"):
        print("Using CSV method ...")
    else :
        print("Usage schedule.py method  For example: schedule.py 0 #For Generator.  schedule.py 1 mwc_test1.csv #For CSV")
        exit(1)
    time.sleep(3)

    while True:
        
        if (flag=="0"):  #generator
            c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage=generator()
            postData(c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
        else:
            try :
                csvfilename = r"mwc_test1.csv"
                if (len(sys.argv)>2 and (sys.argv[2]!="") ):
                    csvfilename = sys.argv[2]

                with open(csvfilename) as csvfile:
                    reader_obj = csv.reader(csvfile)
                    head = next(reader_obj)
                    for row in reader_obj:

                        c_date,amd_power,amd_cpu_util_percentage,intel_power,intel_cpu_util_percentage = row

                        amd_cpu_util=float(amd_cpu_util_percentage) * 100
                        intel_cpu_util=float(intel_cpu_util_percentage)*100
                        
                        #c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage = row
                        print("CSV values are:",c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
                        postData(c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
                csvfile.close()
                print("------------------------->Restarting from begining of the file.")
            except :
                print("Error occured while reading/posting data ....") 
                traceback.print_exc()
                exit(1)

                
            

       
#ap.con.close()