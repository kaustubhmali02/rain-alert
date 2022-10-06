import requests
from twilio.rest import Client
import os


my_lat = 19.198240
my_long = 72.949013

api_key = os.environ['OPEN_WEATHER_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


parameters = {
    "appid": api_key,
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily,alerts"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=parameters)
response.raise_for_status()
data_12hrs = response.json()["hourly"][:12]
# weather_data_ids = []
for data in range(12):
    weather_data_id = int(data_12hrs[data]["weather"][0]["id"])
    if weather_data_id > 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Its going to rain today. Please carry an umbrella.',
            from_='+14798471632',
            to='+918779785606'
        )
        print(message)
        break
