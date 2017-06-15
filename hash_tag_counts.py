import csv
import re


file_open_sarcastic = open('sarcastic_tweets.csv','r')
file_open_sarcastic_reader = csv.reader(file_open_sarcastic)

hash_tag_sarcastic = {}

for each_row in file_open_sarcastic_reader:
	tweet_containing_b = each_row[1]
	tweet_without_b = re.sub(r'^b[\'\"]','',tweet_containing_b)
	tweet_clean = re.sub(r'^[\'\"]','',tweet_without_b)
	hash_tag = re.findall(r'#\w+\s?',tweet_clean)
	hash_tag_lower = []
	if len(hash_tag):
		hash_tag_lower = [each_tweet.lower().strip() for each_tweet in hash_tag]
	for each_tag in hash_tag_lower:
		if hash_tag_sarcastic.get(each_tag):
			hash_tag_sarcastic[each_tag] += 1
		else:
			hash_tag_sarcastic[each_tag] = 1
hash_tag_sarcastic_frequency_sorted = sorted(hash_tag_sarcastic.items(),key = lambda x:x[1],reverse=True)
for each_tag in hash_tag_sarcastic_frequency_sorted:
	print each_tag
	raw_input()