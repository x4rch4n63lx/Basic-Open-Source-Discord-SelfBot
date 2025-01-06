# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 12/30/2024 - 11:09PM 
# Script Purpose : Basic Open Source Discord SelfBot coded in Python
# Description    : This script allows users to:
#                  1. Send a message via a webhook.
#                  2. Spam a webhook with a specified message.
#                  3. Delete a webhook.
# 
# Features       : 
#                  - Simple login mechanism for security.
#                  - Sends a notification to a Discord server when the self bot starts.
#                  - Sends a notification upon successful login.
#                  - Clear console screen post-login for a clean interface.
#                  - Easy user interaction with options to input webhook URLs and messages.
#
# Usage Note     : Ensure compliance with Discord's Terms of Service and use responsibly.
# ===================================================================================
import requests
import json
import getpass
import pyfiglet
import os

USER_CREDENTIALS = {
    "username": "root",
    "password": "root"
}

LOGIN_NOTIFICATION_WEBHOOK = 'WEBHOOK-HERE'

def send_start_notification():
    message = {
        'content': 'Self bot has started!'
    }
    payload = json.dumps(message)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LOGIN_NOTIFICATION_WEBHOOK, data=payload, headers=headers)
    return response.status_code

def send_login_notification():
    message = {
        'content': 'A user has successfully logged in.'
    }
    payload = json.dumps(message)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LOGIN_NOTIFICATION_WEBHOOK, data=payload, headers=headers)
    return response.status_code

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        print("Login successful!")
        send_login_notification()
        clear_screen()
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def send_message(webhook_url, message):
    payload = json.dumps({'content': message})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=payload, headers=headers)
    return response.status_code

def spam_webhook(webhook_url, message, count):
    payload = json.dumps({'content': message})
    headers = {'Content-Type': 'application/json'}
    for _ in range(count):
        response = requests.post(webhook_url, data=payload, headers=headers)
        if response.status_code != 204:
            print(f'Failed to send message. Error: {response.status_code}')
    return

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    return response.status_code

def main_menu():
    banner = pyfiglet.figlet_format("Discord Tool")
    print(banner)
    print("Choose an option:")
    print("1. Send a message")
    print("2. Spam a webhook")
    print("3. Delete a webhook")

    option = input("Enter the number of the option you want to choose: ")

    if option == '1':
        webhook_url = input("Enter the webhook URL: ")
        message = input("Enter the message to send: ")
        status_code = send_message(webhook_url, message)
        if status_code == 204:
            print('Message sent successfully!')
        else:
            print('Failed to send message. Error:', status_code)

    elif option == '2':
        webhook_url = input("Enter the webhook URL: ")
        message = input("Enter the message to spam: ")
        count = int(input("Enter the number of times to spam: "))
        spam_webhook(webhook_url, message, count)
        print('Spamming completed!')

    elif option == '3':
        webhook_url = input("Enter the webhook URL: ")
        status_code = delete_webhook(webhook_url)
        if status_code == 204:
            print('Webhook deleted successfully!')
        else:
            print('Failed to delete webhook. Error:', status_code)

    else:
        print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    send_start_notification()
    if login():
        main_menu()
