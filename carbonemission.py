from flask import Flask
import psycopg2
from flask import Flask, request, jsonify
import traceback
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/populate_values1',methods=['POST'])
def populate_values():
    _json = request.json
    print("Received json is:",_json)    
    try :
        if request.method == 'POST':  

            print("POST requested received ...")
            #Create connection to Postgresql
            con = psycopg2.connect(database="mwc",user='amd', password='amd@1234!',host='localhost', port='5432')

            #Cursor 
            cur = con.cursor()
            print("Connected to database ...")

            c_date = _json["c_date"] 
            amd_power = int(_json["amd_power"])
            #amd_cpu_util = float(_json["amd_cpu_util"])*100    
            amd_cpu_util = float(_json["amd_cpu_util"])
            amd_cpu_util_percentage = float(_json["amd_cpu_util_percentage"] )  
            intel_power  = float(_json["intel_power"])
            #intel_cpu_util  = float(_json["intel_cpu_util"])*100 
            intel_cpu_util  = float(_json["intel_cpu_util"])
            intel_cpu_util_percentage  = float(_json["intel_cpu_util_percentage"])    

            print("Recieved values are:",c_date,amd_power,amd_cpu_util,amd_cpu_util_percentage,intel_power,intel_cpu_util,intel_cpu_util_percentage)
            #formula to Calculate AMD_Carbon_Emission
            amd_carbon_emission = round((amd_power*amd_cpu_util*0.00138*4.91*4),2)

            #formula to Calculate Intel_Carbon_Emission
            intel_carbon_emission = round((intel_power*intel_cpu_util*0.00138*4.91*4),2)

            current_date=datetime.now()
            c_date=current_date.strftime('%Y-%m-%d %H:%M:%S')

            insert_query="""insert into mwc_test("TimeStamp","Power_Consumption","CPU_Utilization","AMD_Carbon_Emission","Intel_Carbon_Emission","Intel_Power_Consumption","Intel_CPU_Utilization") VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            cur.execute(insert_query,(c_date,amd_power , 
                                        amd_cpu_util_percentage, 
                                        amd_carbon_emission,
                                        intel_carbon_emission,
                                        intel_power,
                                        intel_cpu_util_percentage))
            print("Inserted Successfully",insert_query)
            con.commit()
            con.close()
    except :
        print("Error occurred while posting the data ...")
        traceback.print_exc()
        

    return _json



if __name__ == '__main__':
    app.run()