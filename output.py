import pickle
import csv
import feature_extract
import topic
import numpy as np
import scipy as sp
from sklearn.feature_extraction import DictVectorizer

file_open_sarcastic = open('sarcastic_tweets_clean.csv','r')
file_read_sarcastic = csv.reader(file_open_sarcastic)
sarcastic_tweets = []
for each_tweet in file_read_sarcastic:
	sarcastic_tweets.append(each_tweet[1])
pos_data = np.array(sarcastic_tweets)
file_open_non_sarcastic = open('non_sarcastic_tweets_clean.csv','r')
file_read_non_sarcastic = csv.reader(file_open_non_sarcastic)
non_sarcastic_tweets = []
for each_tweet in file_read_non_sarcastic:
	non_sarcastic_tweets.append(each_tweet[1])
neg_data = np.array(non_sarcastic_tweets)
print 'Before topic Modelling'
topic_mod = topic.topic(nbtopic=200,alpha='symmetric')
topic_mod.fit(np.concatenate((pos_data,neg_data)))
print 'Before Pickling'
pkl_file_1 = open('vecdict.p')
vec = pickle.load(pkl_file_1)
pkl_file = open('classif.p', 'rb')
classifier  = pickle.load(pkl_file)
basic_test = []
file_test = open('test_MLWARE1.csv','r')
file_test_read = csv.reader(file_test)
i = 0

for each_tweet in file_test_read:
	if i != 0:
		basic_test.append(each_tweet[1])
	else:
		i = 1
feature_basictest=[]
for tweet in basic_test: 
	feature_basictest.append(feature_extract.dialogue_act_features(tweet,topic_mod))
feature_basictest=np.array(feature_basictest) 
feature_basictestvec = vec.transform(feature_basictest)
print classifier.predict(feature_basictestvec)

file_test_open = open('test','w')
# file_test_write = csv.writer(file_test_open)
output = list(classifier.predict(feature_basictestvec))
for each_output in output:
	file_test_open.write(str(each_output))
	file_test_open.write('\n')
	# file_test_write.writerow(each_output)


