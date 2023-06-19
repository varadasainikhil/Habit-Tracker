import os
import requests
from dotenv import load_dotenv
from datetime import *

load_dotenv()
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_GRAPH_ID = os.getenv("GRAPH_ID")
TODAYS_DATE = date.today()
if TODAYS_DATE.month < 10:
    date = f"{TODAYS_DATE.year}0{TODAYS_DATE.month}{TODAYS_DATE.day}"
else:
    date = f"{TODAYS_DATE.year}{TODAYS_DATE.month}{TODAYS_DATE.day}"
print(date)
pixela_endpoint_account_creation = "https://pixe.la/v1/users"
pixela_endpoint_graph_creation = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/"
pixela_endpoint_pixel_creation = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
pixela_endpoint_pixel_updation = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date}"

print(PIXELA_TOKEN)
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
pixel_configuration = {
     "date": date,
     "quantity": "120",
}
pixel_updation = {
     "date": date,
     "quantity": "520",
}
response = requests.put(url=pixela_endpoint_pixel_updation, json=pixel_updation, headers=headers)
print(response.text)
