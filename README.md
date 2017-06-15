# Sarcasam-Detection-for-Tweets
Main purpouse of this is to detect Sarcasam in tweets streaming from Twitter.

First comes data collection and in this case I am lucky enough as the data is already readily available and Now main task was to do good pre-processing
Preprocessing: Actually the normal preprocessing is to remove all the hash-tags and retweets and words with @ and so on but a preliminary examination at the data gave me some insights such as in tweets with #not is more than 99.6% probable that it is a sarcastic tweet and same is the case with some other hash tags like #sarcasam and some other so i thought that one feature for classification can be if there are is a hash_tag which is present in a list which is already there with me than I will have ‘one’ in the as value of feature element otherwise it will be zero. Note : Frequency analysis on hash_tags clearly showed us that out of 51300 sarcastic tweets there are 9885 tweets that have #not and #sarcasm in 4251 tweets and so on..
I remove duplicates and we remove tweets whose length is less than 3 and also tweets which are not in English and removing all the @ and punctuation removing unicode and so on...
Feature Engineering:
First Feature is n-gram mainly unigram and bigram, For this each tweet is tokenized and stemmed.
Sentiment Score by textblob : Explain all the hypothesis used and considered. (First very positive and then negative) . 3 parts and 2 parts
Topics : First we need to learn the topics so that classifier will be learning topics associated with sarcastic tweets and so on..
Python library gensim which implements topic modeling using latentDirchiletallocation. First all tweets are feed to topic modeler and then each tweet can be decomposed as sum of topics which we use as features.
SVM is the classifier used 

I have followed http://www.thesarcasmdetector.com/ for this project and I need to say that this has cleared some basic concepts in text analytics.
