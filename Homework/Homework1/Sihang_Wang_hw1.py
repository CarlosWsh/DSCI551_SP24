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
    return

# 2. Retrieve the most recent message for a person
def get_recent_message(person):
    # INPUT : Person (as sender or receiver)
    # RETURN : JSON object with details of the most recent message or None if no message exists
    # EXPECTED RETURN : {"sender": "john", "receiver": "david", "body": "hello", "timestamp": 1674539458} or None
    return     

# 3. Retrieve the last k messages between two people
def get_last_k_messages(person1, person2, k):
    # INPUT : Person1, Person2, Number of messages (k)
    # RETURN : List of JSON objects with the k most recent messages or an Empty list if no messages exist
    # EXPECTED RETURN : [{"sender": "john", "receiver": "david", "body": "nothing much, how about we go out?", "timestamp": 1737676770}, ...] or []
    return

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
