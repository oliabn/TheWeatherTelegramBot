import requests
import json
import time

import const


def answer_user_bot(msg, chat_id):
    data = {
        "chat_id": chat_id,
        "text": msg
    }
    url = const.URL.format(token=const.TOKEN, method=const.SEND_METH)
    response = requests.post(url, data=data)


def parse_weather_data(data):
    for elem in data["weather"]:
        weather_state = elem["main"]
    temp = round(data["main"]["temp"] - 273.15, 2)
    city = data["name"]
    msg = f"The weather in {city}, Temp: {temp}, State: {weather_state}"
    return msg


def get_weather(location):
    # Sending request and Getting result
    url = const.WEATHER_URL.format(city=location, token=const.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return "City not found"
    data = json.loads(response.content)
    return parse_weather_data(data)


def get_message(data):
    return data["message"]["text"]


def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, "w") as file:
        file.write(str(update["update_id"]))
    const.UPDATE_ID = update["update_id"]
    return True


def main():
    while True:
        # Sending request and Getting result
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text
        data = json.loads(content)
        result = data["result"][::-1]
        needed_part = None

        # Finding the last message and
        # writing this getting result from request as dict. into needed_part
        for elem in result:
            needed_part = elem
            break

        # If the last message hasn't yet been processed -> get the message and save this update as processed
        if const.UPDATE_ID != needed_part["update_id"]:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg, needed_part["message"]["chat"]["id"])
            save_update_id(needed_part)

        time.sleep(1)


if __name__ == "__main__":
    main()

