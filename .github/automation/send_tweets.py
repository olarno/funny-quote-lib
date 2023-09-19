import json
import tweepy
import os

def read_tweet_config():
    try:
        with open('.github/automation/tweet_config.json', 'r', encoding='utf-8') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        print("Le fichier de configuration tweet_config.json n'a pas été trouvé.")
        return None

def get_tweet(config, lang):
    if config and lang in config:
        return config[lang]  

    return None

def send_tweets(tweets):
    consumer_key = os.environ['TWITTER_API_KEY']
    consumer_secret = os.environ['TWITTER_API_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    for tweet in tweets:
        api.update_status(tweet)
        print("Tweet envoyé:", tweet)

def main():
    config_data = read_tweet_config()

    if config_data:
        tweet_fr = get_tweet(config_data, 'tweets-fr')
        tweet_en = get_tweet(config_data, 'tweets-en')

        # Envoi des tweets
        if tweet_fr:
            send_tweets(tweet_fr)
            print("Tweet en français envoyé:", tweet_fr)
        
        if tweet_en:
            send_tweets(tweet_en)
            print("Tweet en anglais envoyé:", tweet_en)

if __name__ == "__main__":
    main()