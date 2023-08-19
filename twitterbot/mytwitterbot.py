# mytwitterbot.py
# IAE 101, Fall 2022
# Project 04 - Building a Twitterbot
# Name: Sung Mo Yang
# netid: 112801117
# Student ID: sungyang

import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "mjNYvvXzlpOBARv4rE5j6BS6I"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "cRZaIAgMIHZtt7mYBpoaTUPyUjByaVegWKwOKRYBPpsK4mTGs0"


# THIS IS MILDLY IMPORTANT
# boolean value for manually controlling BONG feature and retweeting/replying feature
# set this to True to only run BONG feature
# set this to False to run BONG feature and retweeting/replying feature
ONLY_TIMER = True

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    print("Exercise 1")
    timeline = simple_twit.get_home_timeline(api=api, count=10)
    for i in range(len(timeline)):
        print("\tTweet: "+str(i+1))
        print("\t\tTweet ID: ", timeline[i]._json["id"])
        print("\t\tAuthor's Name: ", timeline[i]._json["user"]["name"])
        print("\t\tAuthor's Screen Name: ", timeline[i]._json["user"]["screen_name"])
        print("\t\tTweet Creation Date: ", timeline[i]._json["created_at"])
        print("\t\tTweet Full Text: ", timeline[i]._json["full_text"])
        print()
    return timeline

# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    print("Exercise 2")
    timeline = simple_twit.get_user_timeline(api=api, user="stonybrooku", count=10)
    for i in range(len(timeline)):
        print("\tTweet: "+str(i+1))
        print("\t\tTweet ID: ", timeline[i]._json["id"])
        print("\t\tAuthor's Name: ", timeline[i]._json["user"]["name"])
        print("\t\tAuthor's Screen Name: ", timeline[i]._json["user"]["screen_name"])
        print("\t\tTweet Creation Date: ", timeline[i]._json["created_at"])
        print("\t\tTweet Full Text: ", timeline[i]._json["full_text"])
        print()
    return timeline


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    print("Exercise 3")
    # generate a random number between 1 and 100
    rand_num = random.randint(1, 100)
    tweet = simple_twit.send_tweet(api=api, text="Exercise 3 Tweet: "+str(rand_num))
    return tweet


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    print("Exercise 4")
    tweet = simple_twit.send_media_tweet(api=api, text="Exercise 4 Tweet", filename="wolfie.jpg")
    return tweet

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
    # infinite loop. at every hour, send a tweet with text with "BONG" for each hour

    # at every minute, check for a new mention. Reply to that mention with a picutre of a wolf
    previousMention = False
    possibleTexts = [
        "Who's a seawolf?",
        "I'm a seawolf!",
        "Go! Fight! Win!"
    ]

    previousSBUTweet = False

    if (ONLY_TIMER):
        print("running BONGS only")

    while True:
        # check if current time is a new hour like 1:00, 2:00, 3:00, etc.
        if time.strftime("%M") == "00" and time.strftime("%S") == "00":
            # get today's date in the format of MM/DD/YYYY
            bongText = time.strftime("%m/%d/%Y")
            # add to text whether or not it is AM or PM
            if int(time.strftime("%H")) < 12:
                bongText += " (AM)"
            else:
                bongText += " (PM)"
            bongText += ": "
            for i in range(int(time.strftime("%H"))):
                bongText += "BONG "
            simple_twit.send_tweet(api=api, text=bongText)
            if (ONLY_TIMER):
                time.sleep(5)
                continue
        if (ONLY_TIMER):
            continue
        #get last tweet from @stonybrooku. if it is new, retweet it
        # im boldly assuming that the @account has already tweeted.
        # this means timeline will always equal at least 1
        timeline = simple_twit.get_user_timeline(api=api, user="stonybrooku", count=1)
        currentSBUTweet = timeline[0]._json["id"]
        
        if previousSBUTweet == False:
            #first retrieval of loop
            previousSBUTweet = timeline[0]._json["id"]
            simple_twit.retweet(api=api, id=previousSBUTweet)
            currentSBUTweet = previousSBUTweet

        elif previousSBUTweet != currentSBUTweet:
            simple_twit.retweet(api=api, id=timeline[0]._json["id"])
            previousSBUTweet = timeline[0]._json["id"]


        print("looking for mentions")
        currentMention = simple_twit.get_mentions(api=api, count=1)
        if len(currentMention) <= 0:
            print("no mentions")
        else:
            mentionTweetId = currentMention[0]._json["id"]
            replyText = "@" + currentMention[0]._json["user"]["screen_name"] + " " + random.choice(possibleTexts)
            if previousMention == False:
                print("First mention of loop!")
                print("sending reply to first mention of loop")
                simple_twit.send_reply_media_tweet(api=api, 
                                                text=replyText, 
                                                tweet_id=mentionTweetId,
                                                filename="wolfie.jpg")
                previousMention = currentMention
            else:
                print("check for new mention")
                if previousMention[0]._json["id"] != currentMention[0]._json["id"]:
                    print("Found New Mention!")
                    print("sending reply")
                    simple_twit.send_reply_media_tweet(api=api, 
                                                    text=replyText, 
                                                    tweet_id=mentionTweetId,
                                                    filename="wolfie.jpg")
                    previousMention = currentMention
                else:
                    print("No new mention")
        continue

                

if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    # exercise1(api)
    # exercise2(api)
    # exercise3(api)
    # exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
