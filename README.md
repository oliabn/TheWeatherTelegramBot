# The Weather Telegram Bot

## Links and descriptions

### Built-in API request by city name

Info here -> https://openweathermap.org/current#name

Example from openweathermap.org:
```
https://api.openweathermap.org/data/2.5/weather?id={city}&appid={API key}
city={city name}
appid={API key}
units={metric}
```

Example from Python:
```python
import requests
from apiKey import TOKEN

city = "Lodz"
params = {"q": f"{city}", "appid": TOKEN, "units": "metric"}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

json_dict = response.json()
# content = requests.get(url).text
# data_dict = json.loads(content)
```
________________

### Icons
Icons list here -> https://openweathermap.org/weather-conditions


