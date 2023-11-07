import json # 오브젝트를 딕셔너리로
import requests
import time # 시간과 관련된 기능제공
import urllib

TOKEN = "6516167516:AAHM9UaOf3gqs5MPlFQNoXqaYI1SPOSj5mY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url): # 문자열 제공
    response = requests.get(url)
    content = response.content.decode("utf8") # 유니코드
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates" # https://api.telegram.org/bot6516167516:AAHM9UaOf3gqs5MPlFQNoXqaYI1SPOSj5mY/getUpdates
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main(): # 두번째 호출
    last_update_id = None # 값이 없어 참인지 구분이 안됨
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0: # ID 값이 존재하면 값이 0<1 True
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__': # 첫번째 호출
    main()