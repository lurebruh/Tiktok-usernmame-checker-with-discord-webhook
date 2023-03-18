import requests
import random

print("\033[94mWelcome to Lure TikTok Gen v3!\033[0m\n")

# Get user input
username_length = int(input("Enter the length of the username (between 3 and 5): "))
num_usernames = int(input("Enter the number of usernames you want to check: "))

# Ask if user wants to use webhook
use_webhook = input("Do you want to use a Discord webhook? (y/n): ")

if use_webhook.lower() == "y":
    webhook_url = input("Enter the Discord webhook URL: ")
else:
    webhook_url = None

# Generate usernames and check availability
for i in range(num_usernames):
    # Generate a random username
    username = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=username_length))

    # Send a request to TikTok API to check if the username is available
    response = requests.get(f"https://www.tiktok.com/@{username}", allow_redirects=False)

    # Determine if the username is available, banned, or unavailable
    if response.status_code == 404:
        if "This account has been banned" in response.content.decode():
            status_text = "\033[91m🔴 banned\033[0m"
        else:
            status_text = "\033[92m✅ available\033[0m"
        if webhook_url:
            payload = {
                "username": "Lure TikTok Gen v3",
                "content": f"`Username: {username} | Status: {status_text}`"
            }
            requests.post(webhook_url, json=payload)
    else:
        status_text = "\033[91m🔴 unavailable\033[0m"
        if webhook_url:
            payload = {
                "username": "Lure TikTok Gen v3",
                "content": f"`Username: {username} | Status: {status_text}`"
            }
            requests.post(webhook_url, json=payload)

    # Print the username and status
    print(f"Username: {username} | Status: {status_text}")

print("\nThank you for using Lure TikTok Gen v3!")
