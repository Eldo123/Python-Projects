import time
from datetime import datetime as dt

host_path="hosts"
redirect= "127.0.0.1"
website_list=["www.9gag.com","9gag.com"]

while(True):
    if(dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,20)):
        with open(host_path,"r+") as f:
            data=f.read()
            for website in website_list:
                if(website in data):
                    pass
                else:
                    f.write(redirect+" "+website+"\n")

    else:
        with open(host_path,"r+") as f:
            data=f.readlines()
            f.seek(0)
            for line in data:
                if(not any(website in line for website in website_list)):
                    f.write(line)
            f.truncate()
