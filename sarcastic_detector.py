import csv
import re



def preprocessing():
	file_open = open('sarcastictweets_marked_with_hashtags.csv','r')
	file_open_read = csv.reader(file_open)
	file_open_clean = open('sarcastic_tweets_clean.csv','w')
	file_open_write = csv.writer(file_open_clean)
	for each_row in file_open_read:
		removing_rt = re.compile(r'(\srt\s|^rt\s)',re.I)
		removing_unicode = re.compile(r'^b[\'\"]')
		removing_words_with_attherate = re.compile(r'@\w+\s?')
		removing_words_with_hashtags = re.compile(r'#\w+\s?')
		removing_http_tags = re.compile(r'http\w+\s?',re.I)
		removing_non_ascii_chraceters = re.compile(r'[^A-Za-z0-9]+')
		unicode_removed = removing_unicode.sub('',each_row[1])
		rt_removed = removing_rt.sub(' ',unicode_removed)
		attherate_removed = removing_words_with_attherate.sub('',rt_removed)
		hash_tag_removed = removing_words_with_hashtags.sub('',attherate_removed)
		http_tag_removed = removing_http_tags.sub(' ',hash_tag_removed)
		clean_tweet = ' '.join([each_word.strip().lower() for each_word in http_tag_removed.split()])
		if len(clean_tweet.split()) > 2:
			file_open_write.writerow([each_row[0],clean_tweet,each_row[2],each_row[3]])
	file_open_clean.close()
	file_open.close()
if __name__ == '__main__':
	preprocessing()


