import nltk

porter = nltk.PorterStemmer()
features = {}
sentence_reg = 'wow i really forgot how much i love the traffic scene'

tokens = nltk.word_tokenize(sentence_reg)
tokens = [porter.stem(t.lower()) for t in tokens] 
bigrams = nltk.bigrams(tokens)
bigrams = [tup[0]+' ' +tup[1] for tup in bigrams]
grams = tokens + bigrams

for t in grams:
	features['contains(%s)' % t] = 1.0
print features