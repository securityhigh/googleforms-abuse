import requests
import random
import os


agents = [
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.2 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
			"Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996",
			"Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.154 (Edition Campaign 34)",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 OPR/70.0.3728.71",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
			"Mozilla/5.0 (Windows NT 6.3; rv:79.0) Gecko/20100101 Firefox/79.0"
		 ]


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


def divider(text, splitter):
	result = ["", ""]
	line = 0

	for char in text:
		if char == splitter and line == 0:
			line = 1
			continue

		result[line] += char

	return result


def config_read(config_file):
	with open(config_file) as config:
		lines = config.readlines()

		for line in lines:
			sline = divider(line, ":")

			if len(sline) != 2:
				continue;

			s0 = sline[0].strip()
			s1 = sline[1].strip()[1:-1]

			if s0 == "url":
				url = s1 + "/responseForm"

			else:
				data[s0] = s1

		print("Config read!")


def main():
	config_read("config.ini")

	count = int(input("Count > "))
	i = 0

	while count > i:
		rnd1 = random.randint(100000000, 999999999)
		rnd2 = random.randint(1000000000, 9999999999)
		rnd3 = random.randint(0, len(agents) - 1)

		seed = str(rnd1) + str(rnd2)
		draftResponse = f"[null,null,\"{seed}\"]\r\n"

		data["fbzx"] = seed
		data["draftResponse"] = draftResponse
		headers["User-Agent"] = agents[rnd3]

		response = requests.post(url, headers=headers, data=data)
		i += 1

		if response.status_code == 200:
			print("Successfully,", i)

		else:
			print("Response error", response.status_code, ",", i)

	print("Done!")


if __name__ == "__main__":
	try:
		os.system("clear")
		main()

	except requests.exceptions.ConnectionError:
		print("Connection error!")

	except KeyboardInterrupt:
		print("\nProgram was stopped by user!")