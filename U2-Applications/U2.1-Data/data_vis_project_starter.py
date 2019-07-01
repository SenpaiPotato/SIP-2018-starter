'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
tweetText = [] 
polarities = []
subjectivities = []
tweetstring = ''


for tweet in tweetData:
    tweetstring += tweet["text"]
    tweets = TextBlob(tweet["text"])
    tweetText.append(tweets)
    subjectivities.append(tweets.subjectivity)
    polarities.append(tweets.polarity)
tweetBlob = TextBlob(tweetstring)

word_dict = {}
generic_words = {'and', 'a', 'the', 'or', 'I' }
for word in tweetBlob.words:
    if len(word)<3:
        continue 
    if word.lower() in generic_words:
        continue 
    if not word.isalpha():
        continue 
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]
    print(word_dict)

print(word_dict)

avgPolarity = (sum(polarities)/len(polarities))
avgSubjectivity = sum(subjectivities)/len(subjectivities)
#print(tweetstring)
#print(avgPolarity)
#print(avgSubjectivity)


# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.sentiment)

# plt.hist(polarities, bins=[-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
# plt.xlabel('Values')
# plt.ylabel('Number of Items')
# plt.title('Histogram of Polarities')
# plt.axis([-0.7, 1.5, 0, 50])
# plt.grid(True)
# plt.show()

