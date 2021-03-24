import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "XXXXXXXXX"
TOKEN = "XXXXXXXXX"
GRAPH_ID = "XXXXXXXXX"
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "WalkingGraph",
    "unit": "Km",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today_time = datetime.now()
# print((today_time.strftime("%Y%m%d"))

pixel_data = {
    "date": today_time.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_time.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)