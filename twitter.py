
import tweepy #https://github.com/tweepy/tweepy
import csv
import re


#Twitter API credentials, you have to create one yourself
consumer_key = ######
consumer_secret = #####
access_key = #####
access_secret = ###########



#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# We are importing our tweets to csv file
csvFile = open('sample.csv', 'w')

#Use csv writer
csvWriter = csv.writer(csvFile)

# api search allows you search for tweets from individual user
for tweet in tweepy.Cursor(api.search,
                           q = "from:Waltonchain -filter:retweets AND -filter:replies",   #this filter out retweets and replies
                           lang='en').items(): 
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
