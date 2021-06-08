import requests
import json

url = input("WebhookURL: ")
message = input("Message: ")
name = input("UserName: ")

while True:
	data = {
		"content": f"{message}",
		"username": f"{name}"
	}
	requests.post(url, data=data)