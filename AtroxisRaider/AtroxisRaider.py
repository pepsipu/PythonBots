#import stuff
import requests
import time
from CMDS.ServerRaid import ServerRaid
from PlatinAuth import PlatinAuth
#define variables
username = None
password = None
plan = None
#define functions
def readAuth():
	global username
	global password
	global plan
	Auth = open("Auth.txt", "r")
	Authlines = Auth.readlines()
	for line in Authlines:
		line = line.split()
		username = line[0]
		password = line[1]
		plan = line[2]


#intro
print(" █████╗ ████████╗██████╗  ██████╗ ██╗  ██╗██╗███████╗   ███╗   ██╗███████╗████████╗")
print("██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚██╗██╔╝██║██╔════╝   ████╗  ██║██╔════╝╚══██╔══╝")
print("███████║   ██║   ██████╔╝██║   ██║ ╚███╔╝ ██║███████╗   ██╔██╗ ██║█████╗     ██║")   
print("██╔══██║   ██║   ██╔══██╗██║   ██║ ██╔██╗ ██║╚════██║   ██║╚██╗██║██╔══╝     ██║")   
print("██║  ██║   ██║   ██║  ██║╚██████╔╝██╔╝ ██╗██║███████║██╗██║ ╚████║███████╗   ██║")   
print("╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝")
time.sleep(.5) 
print("                             Atroxis Discord Raid Bot                           ")
time.sleep(.5)
print("                                 Sammy Hajhamid                                 ")
time.sleep(.5)
print("                               Uses PlatinBots API                              ")

import os
exists = os.path.isfile('Auth.txt')
if exists:
    readAuth()
else:
    print("You need to login into PlatinBots!")
    PlatinAuth().createLogin()



ServerRaid().grabData()
ServerRaid().createInfo(username, password, plan)
ServerRaid().startSR()