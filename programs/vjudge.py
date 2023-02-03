import requests
import csv
from datetime import datetime
import pandas as pd
vjudge_user_name=['NAHID_HASAN_RAJU']
headers= {
    'Accept': 'application/json',
    'Content-Type': 'apllication/json'
}
for i in range(1):
        url="https://vjudge.net/status/data?draw=1&start=0&length=20&un="+vjudge_user_name[i]+"&OJId=All&probNum=&res=0&language=&onlyFollowee=false&orderBy=run_id&20paging_simple_numbers=1&Mine=6&_=167539930135"
        response=requests.request("GET",url,headers=headers,data={})
        myjson=response.json()
        ourdata=[]
        csvheader=['UserName','OJ','Problem_Name','Result','Language','Submission_Time']
        for x in myjson['data']:
            unixToDatetime =datetime.fromtimestamp((x['time']/1000)) 
            # print(unixToDatetime)
            lisiting=[x['userName'],x['oj'],x['probNum'],x['status'],x['language'],unixToDatetime]
            ourdata.append(lisiting)
        with open('Vjudge.csv','w',encoding='UTF8',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(csvheader)
            writer.writerows(ourdata)






            