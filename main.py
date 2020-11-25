from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import requests
import random
import json
import os

url = ""
data = {
		 "fvv": "1",
		 "draftResponse": "",
		 "pageHistory": "0",
		 "fbzx": ""
       }
headers = {
			"User-Agent": "",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
		  }


def user_agent():
	software_names = [SoftwareName.CHROME.value]
	operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

	user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
	return user_agent_rotator.get_random_user_agent()


def main():
	with open("config.json") as file:
		jsons = json.loads(file.read())

		for j in jsons:
			if j == "url":
				url = jsons[j] + "/formResponse"
			else:
				data[j] = jsons[j]

	count = int(input("count: "))
	i = 0

	while count > i:
		rnd1 = random.randint(100000000, 999999999)
		rnd2 = random.randint(1000000000, 9999999999)

		seed = str(rnd1) + str(rnd2)

		data["fbzx"] = str(rnd1) + str(rnd2)
		data["draftResponse"] = f"[null,null,\"{seed}\"]\r\n"
		headers["User-Agent"] = user_agent()

		response = requests.post(url, headers=headers, data=data)
		i += 1

		if response.status_code == 200:
			print("success,", i)

		else:
			print("response error", response.status_code, i)

	print("..done")


if __name__ == "__main__":
	try:
		os.system("clear")
		main()

	except requests.exceptions.ConnectionError:
		print("connection error")

	except KeyboardInterrupt:
		print("\nprogram was stopped by user")