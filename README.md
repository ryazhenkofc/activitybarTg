# Automatic Bio Update for Telegram

This Python script automatically updates your Telegram bio to reflect the title of the active window on your Linux system.

## Features:

    Monitors the active window title.
    Uses customizable symbols to represent different applications.
    Ignores specific applications (e.g., Telegram itself).

## Requirements:

    pip install telethon


## Configuration:

    Create a file named config.json in the same directory as the script.
    Add the following structure to the config.json file:

## JSON

    {
    "ignore_list": ["Telegramdesktop", "Discord"],
    "Spotify": "♫",
    "Code": "",
    # ... Add more application names and symbols as needed ...
    }

## Usage:

    Replace the placeholders in the script:
        API_ID: Your Telegram API ID.
        API_Hash: Your Telegram API Hash.
        PHONE_NUMBER: Your Telegram phone number.
    Run the script: python3 main.py

## Note:

    Not recommened to set delay less than 10 seconds.

----------

Author:

ryazhenkofc (GitHub profile: https://github.com/ryazhenkofc)

----------

Additional Resources:

-   Telethon: [https://docs.telethon.dev/en/stable/]
-   Telegram API: [https://core.telegram.org/#telegram-api]


----------