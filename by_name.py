import snscrape.modules.twitter as sntwitter
import pandas
import traceback


# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
try:
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper('cat since:2022-01-01 until:2022-05-31').get_items()):
        if i > 50:
            break
        tweets_list2.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username])
except Exception as e:
    print(f'this is the exception => {e}')

# Creating a dataframe from the tweets list above
tweets_df2 = pandas.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df2)