import scrapy

def create_urls(topics):
	basename = 'http://www.brainyquote.com/quotes/topics/topic_'
	url = []
	for t in topics:
		topname = basename + t.lower()
		url.append(topname + '.html')
		for i in range(2, 40):
			pagename = topname + str(i) + '.html'
			url.append(pagename)
	return url

class QuoteSpider(scrapy.Spider):
	name = 'quotespider'
	#start_urls = ['http://www.brainyquote.com/quotes/topics/topic_age.html']

	lst_topic_url = ['Age','Alone','Amazing','Anger','Anniversary','Architecture','Art','Attitude','Beauty','Best','Brainy','Business','Car','Chance','Change','Christmas','Communication','Computers','Cool','Courage','Dad','Dating','Death','Design','Diet','Dreams','Education','Environmental','Equality','Experience','Failure','Faith','Family','Famous','Fear','Finance','Fitness','Food','Forgiveness','Freedom','Friendship','Funny','Future','Gardening','God','Good','Government','Graduation','Great','Happiness','Health','History','Home','Hope','Humor','Imagination','Independence','Inspirational','Intelligence','Jealousy','Knowledge','Leadership','Learning','Legal','Life','Love','Marriage','Medical','Men','Mom','Money','Morning','Motivational','Movies','MovingOn','Music','Nature','Parenting','Patience','Patriotism','Peace','Pet','Poetry','Politics','Positive','Power','Relationship','Religion','Respect','Romantic','Sad','Science','Smile','Society','Space','Sports','Strength','Success','Sympathy','Teacher','Technology','Teen','Thankful','Time','Travel','Trust','Truth','War','Wedding','Wisdom','Women','Work']
	start_urls = create_urls(lst_topic_url)

	def parse(self, response):
		topic = response.css('h1.quoteListH1').xpath('text()').extract()[0].split('Quotes')[0].strip().encode('utf-8').lower()
		with open('quote.txt', 'a') as f:

			for quoteBox in response.css('div.masonryitem'):
				quote = quoteBox.xpath('.//span[@class="bqQuoteLink"]/a/text()').extract()
				author = quoteBox.xpath('.//div[@class="bq-aut"]/a/text()').extract()

				tags = []
				for t in quoteBox.xpath('.//div[@class="body bq_boxyRelatedLeft bqBlackLink"]//a'):
					tags.append(t.xpath('text()').extract()[0])
				tags = ','.join(tags)

				quote = quote[0].encode('utf-8')
				author = author[0].encode('utf-8')
				tags = tags.encode('utf-8').lower()

				f.write(quote + '\t' + author + '\t' + topic + '\t' + tags + '\n')
        