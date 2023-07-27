# import snscrape.modules.twitter as sntwitter

from datetime import timedelta
from prefect import task, flow
from prefect.tasks import task_input_hash
# Creating list to append tweet data to


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract(start_date:str, end_date:str, search_term:str):
    """
    Scrape Twitter for tweets containing a search term between a start and end date.
    """
    # Creating list to append tweet data to
    # attributes_container = []
    # # Using TwitterSearchScraper to scrape data and append tweets to list
    # for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_term} since:{start_date} until:{end_date}').get_items()):
    #     if i>150:
    #         break
    #     attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    # # Creating a dataframe to load the list
    # tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    return "tweets_df"


@flow
def scrape(start_date:str, end_date:str, search_term:str):
    """
    Scrape Twitter for tweets containing a search term between a start and end date.
    """
    tweets_df = extract(start_date, end_date, search_term)
    return tweets_df
    