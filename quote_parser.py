import json
from textblob import TextBlob

with open('quote-revised.txt', 'r') as f:
	content = f.readlines()
f.close()

data = {'content':{}}

lst_tags = []
dct_tags = {}

for c in content:
	if c.strip() == "":
		continue
	tokens = c.split('\t')

	quote = tokens[0].strip()
	author = tokens[1].strip()
	topic = tokens[2].strip()
	tags = tokens[3].strip().split(',')
	tags.append(topic)

	sent = TextBlob(unicode(quote, encoding='utf-8', errors='replace')).sentiment.polarity

	dct = {'quote': quote, 'author': author, 'tags': tags, 'sentiment': sent}
	#data['content'].append(dct)

	for t in tags:
		if t.strip() == "":
			continue
		if t not in data['content']:
			data['content'][t] = []
		if t not in dct_tags:
			dct_tags[t] = []
		if quote not in dct_tags[t]:
			dct_tags[t].append(quote)
			data['content'][t].append(dct)

	for t in tags:
		if t not in lst_tags:
			lst_tags.append(t)

data['list_tags'] = lst_tags

with open('quote.json', 'w') as f:
	f.write(json.dumps(data, ensure_ascii=False))
f.close()