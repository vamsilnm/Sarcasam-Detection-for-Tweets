import csv
import re
# file_open_train = open('train_MLWARE1.csv','r')
# file_open_read = csv.reader(file_open_train)
file_open_sarcastic = open('sarcastic_tweets.csv','r')
file_open_sarcastic_reader = csv.reader(file_open_sarcastic)
file_open_non_sarcastic = open('non_sarcastic_tweets.csv','r')
file_open_non_sarcastic_reader = csv.reader(file_open_non_sarcastic)

hash_tag_sarcastic = {}
for each_row in file_open_sarcastic_reader:
	hash_tag_lower = []
	tweet_containing_b = each_row[1]
	tweet_without_b = re.sub(r'^b[\'\"]','',tweet_containing_b)
	tweet_clean = re.sub(r'^[\'\"]','',tweet_without_b)
	hash_tag = re.findall(r'#\w+\s?',tweet_clean)

file_open_sarcastic.close()

sarcastic_key_words_list = []
file_open = open('sarcastic_hash_tag','r')
for each_tag in file_open:
	sarcastic_key_words_list.append(each_tag.strip())
file_open.close()

file_open_sarcastic_1 = open('sarcastic_tweets.csv','r')
file_open_sarcastic_reader_1 = csv.reader(file_open_sarcastic_1)

file_open_labelling_sarcastic_tweets = open('sarcastictweets_marked_with_hashtags.csv','w')
file_open_labelling_sarcastic_tweets_writer = csv.writer(file_open_labelling_sarcastic_tweets)
for each_row in file_open_sarcastic_reader_1:
	is_found = 0
	each_tweet_lower = each_row[1].lower()
	for each_key_word in sarcastic_key_words_list:
		if each_tweet_lower.find(each_key_word) != -1:
			file_open_labelling_sarcastic_tweets_writer.writerow([each_row[0],each_row[1],each_row[2],'1'])
			is_found = 1
			break
	if not is_found:
		file_open_labelling_sarcastic_tweets_writer.writerow([each_row[0],each_row[1],each_row[2],'0'])






	
		


