from instagrapi import Client
import random as r
import time
import schedule

USERNAME = "_almightyyy._"
PASSWORD = "jerryperry2116"

tags = ["fooball", "opium", "coding", "lifestyle", "coding" "gaming"]

comments = ["Cute!", "Nice!", "Great work!", "Good job!"]

def search_tags():
    client = Client()
    client.login(USERNAME, PASSWORD)

    num_interaction_posts = r.randint(1, 20)

    time.sleep(r.randint(2000, 7000)/1000)

    tag_choice = r.choice(tags)
    hashtag_posts = client.hashtag_medias_recent(tag_choice)

    print(f"searched for the tag {tag_choice}")
    print(f"interacting with {num_interaction_posts} post ...")

    chosen_posts_ids = {}

    