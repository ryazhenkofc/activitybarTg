import time
import subprocess
import re
import json
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# Define the path to the configuration file
CONFIG_FILE = "config.json"

# Define your API ID, API Hash, and phone number
api_id = "API_ID"
api_hash = "API_Hash"
phone_number = "PHONE_NUMBER"

# Create the client and connect
client = TelegramClient("client_name", api_id, api_hash)


async def update_bio(new_bio):
    await client.start(phone=phone_number)

    await client(UpdateProfileRequest(about=new_bio))
    print("Bio updated successfully.")


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def get_active_window_title_linux(config):
    """
    Retrieves the title of the active window in a Linux environment.

    Args:
        config (dict): A dictionary containing configuration settings.

    Returns:
        str: The formatted string representing the active window title, or None if the window should be ignored.
    """
    root = subprocess.Popen(
        ["xprop", "-root", "_NET_ACTIVE_WINDOW"], stdout=subprocess.PIPE
    )
    stdout, _ = root.communicate()

    m = re.search(b"^_NET_ACTIVE_WINDOW.* ([\w]+)$", stdout)
    if m is not None:
        window_id = m.group(1)
        window = subprocess.Popen(
            ["xprop", "-id", window_id, "WM_NAME", "WM_CLASS"], stdout=subprocess.PIPE
        )
        stdout, _ = window.communicate()
    else:
        return None

    match_name = re.search(b'WM_NAME\(\w+\) = "(.*)"', stdout)
    match_class = re.search(b'WM_CLASS\(\w+\) = "(.*)", "(.*)"', stdout)

    if match_name is not None and match_class is not None:
        class_name = match_class.group(2).decode("utf-8")
        class_name = class_name.capitalize()
        if class_name in config.get("ignore_list", []):
            return None
        symbol = config.get(class_name, "")
        if not symbol:
            config[class_name] = ""
            save_config(config)
        return f"{symbol} {class_name} ~ {match_name.group(1).decode('utf-8')}"

    return None


def main():
    config = load_config()
    current_title = get_active_window_title_linux(config)
    while True:
        new_title = get_active_window_title_linux(config)
        if new_title != current_title:
            print(new_title)
            current_title = new_title
            with client:
                client.loop.run_until_complete(update_bio(current_title))
        time.sleep(10)


if __name__ == "__main__":
    main()
