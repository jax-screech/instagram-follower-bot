from instagrapi import Client
import random as r
import time
import schedule
#just for the bot to login to the account
USERNAME = "_projecttt_"
PASSWORD = "example@123"
#the type of posts that I want my bot  to interact with
tags = ["football", "music", "coding", "lifestyle", "gaming", "fitness"]
#the comments that I want the bot to make
comments = ["Nice job!", "Great work!", "Good job!", "Very cool!", "Cute", "Awesome work!"]

def search_tags():#define function to enable the bot to search for the posts
    client = Client()#creating instance of a Client object from the api
    client.login(USERNAME, PASSWORD)#enable the Client to login to the account 

    num_interaction_posts = r.randint(1, 5)

    time.sleep(r.randint(2000, 7000)/1000)#delay for avoiding detection by instagram

    tag_choice = r.choice(tags)
    hashtag_posts = client.hashtag_medias_recent(tag_choice)#it will fetch most recent posts for the tag that is randomly selected



    print(f"searched for the tag {tag_choice}")
    print(f"interacting with {num_interaction_posts} post...")

    chosen_posts_ids = []#empty list for containing the ids for the found posts
 #for loop to randomly pick posts from the hashtag posts list
    for i in range(num_interaction_posts):
        insertion_index = r.randint(0, len(hashtag_posts) - 1)#randomly pick an index within the bounds of the hashtag_posts
        while insertion_index in chosen_posts_ids:
            insertion_index = r.randint(0, len(hashtag_posts ) - 1)
            chosen_posts_ids.append(insertion_index)
            #print out the caption text of each post that the script interacted with
            for i in chosen_posts_ids:
                print(f"Interacting with the post '{hashtag_posts[i].caption_text}'")


                like = True
                if r.randint(0, 100) < 10:#the bot has a 10 percent chance of not liking
                    like = False

                comment = True
                if r.randint(0, 100) < 40:#the bot has a 40 percent chance of not commenting
                    comment = False

                follow = True
                if r.randint(0, 100) < 80:#the bot has a 80 percent chance of not following
                    follow = False
                      #variables to store the ids of the post and creator of the post
                    media_id = hashtag_posts[i].pk
                    user_id = hashtag_posts[i].userpk
                        #another rest to simulate the user looking at the post
                    time.sleep(r.randint(4000,8000)/1000)

    if follow:
        time.sleep(r.randint(3000, 9000) / 1000)
        try:
            client.user_follow(user_id)
            print(f"Followed the user {user_id}")
        except Exception as error:
            print("Too many follow requests at once. Slow down following.")

    if like:
        time.sleep(r.randint(3000, 9000) / 1000)
        try:
            client.media_like(media_id)
            print(f"Added a like to the post with ID {media_id}")
        except Exception as error:
            print("Too many likes at once. Slow down liking.")

    if comment:
        time.sleep(r.randint(3000, 9000) / 1000)
        try:
            comment_text = r.choice(comments)
            client.media_comment(media_id, comment_text)
            print(f"Added a comment on the post {media_id}: {comment_text}")
        except Exception as error:
            print("Too many comments at once. Slow down commenting.")

#a time will be randomly selected
time_1 = str(r.randint(10, 10)) + ":" + str(r.randint(10, 39))
time_2 = str(r.randint(13, 13)) + ":" + str(r.randint(10, 39))
#just scedual the bot to perform the funstion two times everyday
schedule.every().day.at(time_1).do(search_tags)
schedule.every().day.at(time_2).do(search_tags)

print(f"The scheduled times are:{time_1} and {time_2} to perform the actions")
#just keeps the script alive and check if the function is due to run and executes it
while True:
    schedule.run_pending()
    time.sleep(1)#just to stay 1 second before checkin again