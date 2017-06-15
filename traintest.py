import nltk
import numpy as np
import scipy as sp
from sklearn.utils import shuffle
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
import pickle
import feature_extract
import topic
import csv

print 'Pickling out'
# pos_data=np.load('posproc.npy')
# neg_data=np.load('negproc.npy')
# print 'Number of  sarcastic tweets :', len(pos_data)
# print 'Number of  non-sarcastic tweets :', len(neg_data)

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

print 'Training topics'

topic_mod = topic.topic(nbtopic=200,alpha='symmetric')
topic_mod.fit(np.concatenate((pos_data,neg_data)))

print 'Feature eng'
# label set
cls_set = ['Non-Sarcastic','Sarcastic']
featuresets = [] 

index=0
for tweet in pos_data:
	if (np.mod(index,10000)==0):
		print "Positive tweet processed: ",index
	featuresets.append((feature_extract.dialogue_act_features(tweet,topic_mod),cls_set[1]))
	index+=1
 
index=0
for tweet in neg_data:
	if (np.mod(index,10000)==0):
		print "Negative tweet processed: ",index
	featuresets.append((feature_extract.dialogue_act_features(tweet,topic_mod),cls_set[0]))
	index+=1
		
featuresets=np.array(featuresets)
targets=(featuresets[0::,1]=='Sarcastic').astype(int)

print 'Dictionnary vectorizer'
vec = DictVectorizer()
featurevec = vec.fit_transform(featuresets[0::,0])

#Saving the dictionnary vectorizer
file_Name = "vecdict.p"
fileObject = open(file_Name,'wb') 
pickle.dump(vec, fileObject)
fileObject.close()

# print 'Feature splitting'
#Shuffling
# order=shuffle(range(len(featuresets)))
# targets=targets[order]
# featurevec=featurevec[order,0::]

#Spliting
size = int(len(featuresets) * .3) # 30% is used for the test set

trainvec = featurevec[:,0::]
train_targets = targets
# testvec = featurevec[:size,0::]
# test_targets = targets[:size]

print 'Training'

#Artificial weights
pos_p=(train_targets==1)
neg_p=(train_targets==0)
ratio = np.sum(neg_p.astype(float))/np.sum(pos_p.astype(float))
new_trainvec=trainvec
new_train_targets=train_targets
for j in range(int(ratio-1.0)):
	new_trainvec=sp.sparse.vstack([new_trainvec,trainvec[pos_p,0::]])
	new_train_targets=np.concatenate((new_train_targets,train_targets[pos_p]))    

classifier = LinearSVC(C=0.1,penalty='l2',dual=True)
classifier.fit(new_trainvec,new_train_targets)

#Saving the classifier
file_Name = "classif.p"
fileObject = open(file_Name,'wb') 
pickle.dump(classifier, fileObject)
fileObject.close()

# print 'Validating'

# output = classifier.predict(testvec)
# print classification_report(test_targets, output, target_names=cls_set)

#BASIC TEST
basic_test = []
file_test = open('test_MLWARE1.csv','r')
file_test_read = csv.reader(file_test)
i = 0
for each_tweet in file_test_read:
	if i != 0:
		basic_test.append(each_tweet[1])
	else:
		i = 1

# basic_test=["This is just a long sentence, to make sure that it's not how long the sentence is that matters the most",\
# 			'I just love when you make me feel like shit','Life is odd','Just got back to the US !', \
# 			"Isn'it great when your girlfriend dumps you ?", "I love my job !", 'I love my son !']
feature_basictest=[]
for tweet in basic_test: 
	feature_basictest.append(feature_extract.dialogue_act_features(tweet,topic_mod))
feature_basictest=np.array(feature_basictest) 
feature_basictestvec = vec.transform(feature_basictest)
print classifier.predict(feature_basictestvec)
file_test_open = open('test.csv','w')
file_test_write = csv.writer(file_test_open)
for each_output in classifier.predict(feature_basictestvec):
	file_test_write.writerow(each_output)
# print basic_test
# print classifier.predict(feature_basictestvec)
# print classifier.decision_function(feature_basictestvec)

