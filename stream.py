#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
with open('SECRETS.txt') as s:
    lines = s.read().splitlines()
    access_token = lines[0]
    access_token_secret = lines[1]
    consumer_key = lines[2]
    consumer_secret = lines[3]
    s.close()

filename = 'btc_log_raw.txt'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):    
    
    def on_data(self, data):
        try:
            with open(filename,'a') as f:
                f.write(data)
                f.close()
            print(data)
        except IOError as e:
            print(e)
        return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Bitcoin, btc, cryptocurrency'])