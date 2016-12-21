import time
from datetime import datetime as dt

hosts_path='./hosts'
website_list = ['www.facebook.com','facebook.com', 'mail.yahoo.com']
REDIRECT_IP = '127.0.0.1'

def is_working_hours():
    # return True
    now = dt.now()
    return dt(now.year,now.month, now.day, 8) < dt.now() and dt.now() < dt(now.year,now.month,now.day, 16)

def update_hosts_for_working():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(REDIRECT_IP + " " + website + "\n")

def update_hosts_for_offhours():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            # use of the 'any' keyword
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

while True:
    if is_working_hours():
        update_hosts_for_working()
    else:
        update_hosts_for_offhours()
    time.sleep(5)
