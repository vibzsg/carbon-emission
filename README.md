## Overview

This is a project to analyze and potentially reduce carbon emissions associated with computing tasks. power consumption and CPU utilization for AMD and Intel processors.

### Overall Workflow

1.carbonemission.py - This file implements a Flask-based API that calculates carbon emissions based on CPU power consumption and utilization data and stores the results in a PostgreSQL database.

2. schedule.py - This file simulates CPU power and utilization data and periodically sends it to the Flask API.

3. It sends the data to carbonemission.py's API via a POST request.
   
4. mwc_test_history2.csv (CSV Data Source) - This is a CSV file that contains historical CPU power and utilization data.

5. carbonemission.py calculates carbon emissions and stores them in the database.

6. The PostgreSQL database (mwc) contains the stored power and carbon emission data.



### Data Structure

The backend processes JSON payloads with the following structure:

postman body --->

{
        "c_date" : "2022-09-19 10:59:00" ,
        "amd_power" : "645",
        "amd_cpu_util" : "55"  ,
        "amd_cpu_util_percentage" : "0.55",
        "intel_power"  : "656",
        "intel_cpu_util"  : "50",
        "intel_cpu_util_percentage" : "0.5"
}
