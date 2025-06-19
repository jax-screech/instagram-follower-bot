from instagrapi import Client
import random
import time
import csv
from datetime import datetime

USERNAME = "projecttest696"
PASSWORD = "account@123"

client = Client()

try:
    client.login(USERNAME, PASSWORD)
except Exception as e:
    print(f"Login failed: {e}")
    exit()

hashtags = ["fitness", "coding", "art"]
chosen_hashtag = random.choice(hashtags)
print(f"Using hashtag: #{chosen_hashtag}")

try:
    posts = client.hashtag_medias_recent(chosen_hashtag, amount=5)
except Exception as e:
    print(f"Error fetching posts: {e}")
    posts = []

my_id = client.user_id
current_followings = client.user_following(my_id)

# Prepare CSV file
filename = "followers.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Username", "User ID", "Is Private", "Action Taken", "Timestamp"])

    for post in posts:
        user = post.user
        user_id = user.pk
        username = user.username
        is_private = user.is_private
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            if is_private:
                print(f"Skipped (private): {username}")
                writer.writerow([username, user_id, is_private, "Skipped (Private)", timestamp])
                continue

            if user_id not in current_followings:
                client.user_follow(user_id)
                print(f"Followed: {username}")
                current_followings[user_id] = user
                writer.writerow([username, user_id, is_private, "Followed", timestamp])
                time.sleep(random.randint(30, 90))  # safer delay
            else:
                print(f"Already following: {username}")
                writer.writerow([username, user_id, is_private, "Already Following", timestamp])

        except Exception as e:
            print(f"Failed to follow {username}: {e}")
            writer.writerow([username, user_id, is_private, f"Failed: {e}", timestamp])
