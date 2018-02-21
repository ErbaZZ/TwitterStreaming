#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
with open('SECRETS.txt') as s:
    lines = s.read().splitlines()
    access_token = lines[0]
    access_token_secret = lines[1]
    consumer_key = lines[2]
    consumer_secret = lines[3]
    s.close()

#File to store the stream data
filename = 'diabetes.txt'

#This is a basic listener that appends the stream data to a file
class StdOutListener(StreamListener):    
    
    def on_data(self, data):
        try:
            with open(filename,'ab') as f:
                f.write(data.encode('utf8'))
                f.close()
            print(data[15:45])
        except IOError as e:
            print(e)
        return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    #This handles Twitter authetication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Diabetes', 'Cancer'])