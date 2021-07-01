import requests
import os
from datetime import datetime

GRAPH_ID = "habitgraph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": os.environ.get("USER_TOKEN"),
    "username": os.environ.get("USER_NAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.environ.get('USER_NAME')}/graphs"

headers = {
    "X-USER-TOKEN": os.environ.get("USER_TOKEN")
}
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Hour",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
date_ = datetime(year=2021, month=4, day=23)
pixel_post_parameters = {
    "date": date_.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_post_parameters, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_post_endpoint}/{date_.strftime('%Y%m%d')}"
pixel_update_parameters = {
    "quantity": "7",
}
# response = requests.put(url=update_pixel_endpoint, json=pixel_update_parameters, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixel_post_endpoint}/{date_.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
