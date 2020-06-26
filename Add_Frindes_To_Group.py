

logo = """

 _______ _     ____ _______                  _             _             
|__   __| |   |___ \__   __|                (_)           | |            
   | |  | |__   __) | | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
   | |  | '_ \ |__ <  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
   | |  | | | |___) | | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
   |_|  |_| |_|____/  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| 
					
		    TH3 TERMINATOR SCRIPT TOOL :")
		   Coded by Bido. => Abdallah Ahmed
		   https://www.facebook.com/bido.32
"""


print(logo)

import requests, json
import time

access = input("Enter Your Access Token >> ")
group_id = input("Enter Your Group ID >> ")
timer = input("Enter Seconds To Wait >> ")
print("\nOk Please Wait...")

url = 'https://graph.facebook.com/me/friends?fields=id&limit=5000&access_token='+access+'&method=get'
res = requests.get(url)
for item in res.json()['data']:
	link = 'https://graph.facebook.com/'+group_id+'/members?method=post&member='+item['id']+'&access_token='+access+''
	time.sleep(int(timer))
	xres = requests.get(link)
	print (xres.json())