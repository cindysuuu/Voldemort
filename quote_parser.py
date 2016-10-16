import json
from textblob import TextBlob

with open('quote-revised.txt', 'r') as f:
	content = f.readlines()
f.close()

data = {'content':[]}

for c in content:
	if c.strip() == "":
		continue
	tokens = c.split('\t')

	quote = tokens[0].strip()
	author = tokens[1].strip()
	topic = tokens[2].strip()
	tags = tokens[3].strip().split(',')
	sent = TextBlob(unicode(quote, encoding='utf-8', errors='replace')).sentiment.polarity

	dct = {'quote': quote, 'author': author, 'topic': topic, 'tags': tags, 'sentiment': sent}
	
	data['content'].append(dct)

with open('quote.json', 'w') as f:
	f.write(json.dumps(data, ensure_ascii=False))
f.close()