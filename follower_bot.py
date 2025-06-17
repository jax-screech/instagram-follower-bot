from instagrapi import Client
import random
import time

USERNAME = "followingaccount1"
PASSWORD = "random123"

client = Client()

try:
    client.login(USERNAME, PASSWORD)
except Exception as e:
    print(f"Login failed: {e}")
    exit()

hashtags = ["fitness", "coding", "art"]
chosen_hashtag = random.choice(hashtags)
print(f"Using hashtag: #{chosen_hashtag}")

posts = client.hashtag_medias_recent(chosen_hashtag, amount=5)
my_id = client.user_id
current_followings = client.user_following(my_id)

for post in posts:
    user = post.user
    user_id = user.pk
    username = user.username

    try:
        if user.is_private:
            print(f"Skipped (private): {username}")
            continue

        if user_id not in current_followings:
            client.user_follow(user_id)
            print(f"Followed: {username}")
            time.sleep(random.randint(5, 10))
        else:
            print(f"Already following: {username}")
    except Exception as e:
        print(f"Failed to follow {username}: {e}")
