import time
import requests
from PlatinAuth import PlatinAuth
class ServerRaid():

	data = None
	auth = None
	invite = None
	channelid = None
	message = None
	amount = None

	def grabData(self):
		invite = input("Input your server invite to the target.\n")
		channelid = int(input("Input the target channel id.\n"))
		message = input("Input the message you want sent.\n")
		amount = int(input("Input the amount of messages you want sent.\n"))
		self.invite = invite
		self.channelid = channelid
		self.message = message
		self.amount = amount

	def createInfo(self, username, password, plan):
		data = {
			"MyTokenList": "", 
			"Invite": self.invite,
			"ID": self.channelid,
			"message": self.message,
			"Amount": self.amount
		}
		self.data = data
		auth = {
		"cookie":"Username=%s; Password=%s; Plan=%s;" % (username, password, plan),
		}
		self.auth = auth
	def startSR(self):
		c = 1
		while True:
			if c == 1:
				SR = requests.post("https://platinbots.xyz/panel/Raid.php", data=self.data, headers=self.auth)
				if SR.status_code == 302:
					status = True
				else:
					status = False
				if status == True:
					print("Bot army is a success!")
				else:
					print("Bot army was a failure.")
				c = 2
			else:
				time.sleep(20)
				SR = requests.post("https://platinbots.xyz/panel/Raid.php", data=self.data, headers=self.auth)
				if SR.status_code == 302:
					status = True
				else:
					status = False
				if status == True:
					print("Bot army is a success!")
				else:
					print("Bot army was a failure.")
				

