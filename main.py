from instabot import Bot, utils

# Prompt the user for Instagram username and password
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Initialize the InstagramBot
bot = Bot()
bot.login(username=username, password=password)

# Open a text file to save the list of non-followers
f = utils.file("config/non-followers.txt")

# Calculate the list of non-followers
non_followers = set(bot.following) - set(bot.followers) - bot.friends_file.set
non_followers = list(non_followers)
non_followers_names = []

# Iterate through non-followers, retrieve their usernames, and print them
for user in non_followers:
    name = bot.get_username_from_user_id(user)
    non_followers_names.append(name)
    print(name)
    bot.small_delay()

# Save the list of non-follower usernames to the text file
f.save_list(non_followers_names)

# Logout from your Instagram account
bot.logout()
