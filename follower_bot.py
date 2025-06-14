from instagrapi import Client
import random as r
import time
import schedule

USERNAME = "_projecttt_"
PASSWORD = "example@123"

tags = ["football", "music", "coding", "lifestyle", "gaming"]

comments = ["Nice job!", "Great work!", "Good job!", "Very cool!", "Cute"]

def search_tags():
    client = Client()
    client.login(USERNAME, PASSWORD)

    num_interaction_posts = r.randint(1, 20)

    time.sleep(r.randint(2000, 7000)/1000)

    tag_choice = r.choice(tags)
    hashtag_posts = client.hashtag_medias_recent(tag_choice)

    print(f"searched for the tag {tag_choice}")
    print(f"interacting with {num_interaction_posts} post...")

    chosen_posts_ids = ()

    for i in range(num_interaction_posts):
        insertion_index = r.randint(0, len(hashtag_posts) - 1)
        while insertion_index in chosen_posts_ids:
            insertion_index = r.randint(0, len(hashtag_posts ) - 1)
            chosen_posts_ids.append(insertion_index)
            for i in chosen_posts_ids:
                print(f"Interacting with the post '{hashtag_posts[i].caption_text}'")


                like = True
                if r.randint(0, 100) < 10:
                    like = False

                comment = True
                if r.randint(0, 100) < 40:
                    comment = False

                follow = True
                if r.randint(0, 100) < 90:
                    follow = False

                    media_id = hashtag_posts[i].pk
                    user_id = hashtag_posts[i].userpk
                            
                    time.sleep(r.randint(4000,8000)/1000)

                    if (follow):
                        time.sleep(r.randint(3000, 9000)/1000)

                        try:
                            client.user_follow(user_id)
                        except Exception as error:
                            print("Too many follow requests.Slow down following")

                            print("Followed the user")
                    if (like):
                        time.sleep(r.randint(3000, 9000)/1000)

                        try:
                            client.user_like(user_id)
                        except Exception as error:
                            print("Too many likes.Slow down liking")

                            print("liked the post")
                    if (comment):
                        time.sleep(r.randint(3000, 9000)/1000)

                        try:
                            client.user_comment(user_id)
                        except Exception as error:
                            print("Too many commented.Slow down commenting")

                            print("commented on the post")

time_1 = str(r.randint(10, 12)) + ":" + str(r.randint(10, 59))
time_2 = str(r.randint(13, 15)) + ":" + str(r.randint(10, 59))

schedule.every().day.at(time_1).do(search_tags)
schedule.every().day.at(time_2).do(search_tags)

print(f"The scheduled times are:{time_1} and {time_2} to perform the actions")

while True:
    schedule.run_pending()
    time.sleep(1)