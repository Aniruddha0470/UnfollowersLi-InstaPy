# UnfollowersLi-InstaPy
Python Script that generates list of people that don't follow you back 😤

# Instagram Non-Followers Finder

## Overview

This Python script utilizes the `instabot` library to identify and save a list of Instagram users who are not following back the specified account. It provides a convenient way to manage your Instagram followers by helping you identify non-reciprocal followers.

## Usage

1. **User Input**: The script prompts the user for their Instagram username and password. It requires these credentials to access the Instagram account.

2. **Instagram Bot Initialization**: An instance of the `InstagramBot` class is initialized from the `instabot` library, enabling interaction with Instagram's API.

3. **Login**: The script logs in to the specified Instagram account using the provided username and password.

4. **File Setup**: It opens a text file named "non-followers.txt" in which the list of non-followers will be saved.

5. **Non-Follower Calculation**: The script calculates the list of non-followers by comparing the accounts the bot is following with the accounts following the bot and accounts listed in the bot's friends file. The result is a list of users who are not following back.

6. **Iterating and Displaying**: It iterates through the list of non-followers, retrieves their usernames using the `bot.get_username_from_user_id` method, and prints them to the console. A small delay is introduced between requests to prevent rate limiting.

7. **Saving Results**: The list of non-follower usernames is saved to the "non-followers.txt" text file for future reference.

8. **Logout**: The script concludes by logging out from the Instagram account.

## Security Considerations

- This script ensures user security by prompting for Instagram credentials rather than hardcoding them or using command-line arguments.
- It is important to exercise caution when handling passwords in code and to use this script in a trusted environment.
- Be aware that automated actions on Instagram may be subject to Instagram's terms of service; users should review and comply with those terms.

---

*Note: Please be responsible when using this script and consider the potential consequences of automating actions on Instagram, which may include account suspension or restrictions.*

