import requests
import json
import sys
from datetime import datetime

# Firebase Database configuration file
CONFIG_FILE = "config.json"

# 1. Send a chat message
def send_chat_message(sender, receiver, message):
    # INPUT : Sender, Receiver, Message Body
    # RETURN : Status code of the Firebase REST API call [response.status_code]
    # EXPECTED RETURN : 200
    try:
        with open(CONFIG_FILE) as file:
            config = json.load(file)
        url = f"{config['dburl']}{config['node']}.json"
        timestamp = int(datetime.now().timestamp())

        chat_message = {
            "sender": sender,
            "receiver": receiver,
            "body": message,
            "timestamp": timestamp
        }

        response = requests.post(url, json=chat_message)
        response.raise_for_status()
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"


# 2. Retrieve the most recent message for a person
def get_recent_message(person):
    # INPUT : Person (as sender or receiver)
    # RETURN : JSON object with details of the most recent message or None if no message exists
    # EXPECTED RETURN : {"sender": "john", "receiver": "david", "body": "hello", "timestamp": 1674539458} or None
    try:
        with open(CONFIG_FILE) as file:
            config = json.load(file)
        url = f"{config['dburl']}{config['node']}.json"

        response = requests.get(url)
        response.raise_for_status()
        messages = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    if messages:
        sorted_messages = sorted(messages.values(), key=lambda x: x["timestamp"], reverse=True)
        for msg in sorted_messages:
            if msg["sender"] == person or msg["receiver"] == person:
                return json.dumps({
                    "sender": msg["sender"],
                    "receiver": msg["receiver"],
                    "body": msg["body"],
                    "timestamp": msg["timestamp"]
                }, separators=(',', ':'))
    return json.dumps(None, separators=(',', ':'))


# 3. Retrieve the last k messages between two people
def get_last_k_messages(person1, person2, k):
    try:
        with open(CONFIG_FILE) as file:
            config = json.load(file)
    except FileNotFoundError:
        return json.dumps([])

    url = f"{config['dburl']}{config['node']}.json"

    response = requests.get(url)
    response.raise_for_status()
    messages = response.json()

    chat_list = [
        msg for msg in messages.values()
        if (msg["sender"] == person1 and msg["receiver"] == person2) or
           (msg["sender"] == person2 and msg["receiver"] == person1)
    ]

    chat_list.sort(key=lambda x: x["timestamp"])

    last_k_messages = chat_list[-k:]

    return json.dumps(
        [{"sender": m["sender"],
          "receiver": m["receiver"],
          "body": m["body"],
          "timestamp": m["timestamp"]} for m in
         last_k_messages],
        separators=(",", ":")
    )


# Main execution logic
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Sihang_Wang_hw1.py [operation] [arguments]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "send_message":
        sender = sys.argv[2]
        receiver = sys.argv[3]
        message = sys.argv[4]
        result = send_chat_message(sender, receiver, message)
        print(result)
    
    elif command == "get_recent":
        person = sys.argv[2]
        result = get_recent_message(person)
        print(result)
    
    elif command == "get_last_k":
        person1 = sys.argv[2]
        person2 = sys.argv[3]
        k = int(sys.argv[4])
        result = get_last_k_messages(person1, person2, k)
        print(result)
    
    else:
        print("Invalid command. Use 'send_message', 'get_recent', or 'get_last_k'.")
