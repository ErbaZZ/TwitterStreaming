# Twitter Trend Geolocation Visualization From Time Zone Data (Course Project for ITCS414 Information Storage and Retrieval)
This project uses python to retrieve Twitter tweets stream, and extract the timezone data to approximate their geolocation and visualize them on the world map in the form of heatmap.

# Introduction
Twitter, one of the most popular social network platform, generates a massive amount of data everyday. Those data are from the users’ interactions in the form of “tweets” that the users publishes on Twitter. On average, more than 6,000 Tweets are “Tweeted” every second, resulting in over 500 million Tweets per day. The data from these Tweets can be collected and analyzed for deeper insights in various purposes such as finding trending topics, measuring the effectiveness of marketing campaigns, or determining customers’ satisfaction.

# Problem Statement
In the present, Twitter allows the users to search for the Tweets with keywords on the topics that they want to see. The users can also specify the location, so they can see the topics that are popular in each area. or see the topics that are trending around the world. However, even if they know the topics that are popular, they cannot possibly know where in the world each topic is popular in using Twitter native searching tools.

# Goal
This project aims to visualize the popularity of a keyword using geolocation data extracted from tweets, so the locations of where the keyword is popular in the world can be seen easily in the form of heatmap. This information could be useful in planning marketing strategies or other purposes that require location data of the trends.

# Implementation
For this project, we use Python for the implementation since there are various libraries available to assist in the implementation.
*Data Preparation*
For the ease of the visualization, the coordinates for each timezone should be predefined. As Geopy can be used to convert location name to coordinate, it is used once to get the estimate coordinate for each timezone using the timezone names as most are city names. Furthermore, manual coordinate editing is done for the time zones that are not city name, such as, Central Time, Mountain Time, or Pacific Time. After converting, the coordinates are stored together with the time zone name line-by-line in a file.
**Data Retrieval**
To gather the data, Tweepy is used to access the Twitter Stream API with Python. The API allows the Tweet data to be streamed, which can be collected and written to a file in the form of Tweet object that contains all fundamental attributes of a Tweet including the id, time created, content, or time zone that we want to extract. Each Tweet is stored as raw data one line per tweet, so that it can be cleaned and reused in case we need it for other purposes.
**Data Cleaning**
As only a few specific attributes for the geolocation visualization, the raw data is filtered to have only time, user-defined location, timezone, and Tweet content. The timezone is then converted to coordinates predefined for each timezone. The filtered data is then stored into a csv file for the visualization.
**Data Visualization**
Pandas is used to read the csv file and extract the data, then Jupyter Notebook and Gmaps are used for visualizing the coordinate data in the form of heatmap.

# Result
As a result, the system can generate a heatmap from the Tweet data stream which contains the keywords provided in the system. The scale of the color is sorted from transparent to red. Red zone signify the highest Tweet density for that area. Orange, yellow and green have lower Tweet density respectively. This heatmap can help the users to see the locations of where a keyword is popular in, which could be used for targeted advertisements or various other purposes. This system can provide the locations with much higher coverage of the total tweets; however, it cannot pinpoint the location of each tweet as accurate as the systems that use the ‘coordinates’ data.
