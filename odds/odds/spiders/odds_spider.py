from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector, HtmlXPathSelector
from odds.items import OddsItem
import re

class OddsSpider(Spider):
	name = "ti_odds"
	allowed_domains = ["tennisinsight.com"]
	start_urls = [
		"http://www.tennisinsight.com/player_activity.php?player_id=1&min_activity=50&activity=1"
	]

	def fix_urls(self, urls):
		for i in range(len(urls)):
			urls[i] = urls[i][:-2]
			urls[i] = urls[i][22:]
			if urls[i][0]=='m':
				urls[i] = 'http://www.tennisinsight.com/'+urls[i]
		return urls

	def get_index_of_first_odds(self, odds_dates):
		for i in range(len(odds_dates)):
			if odds_dates[i][0]=='$':
				return i

	def remove_all_whitespace(self, odds_dates):
		new_list = []
		for i in range(len(odds_dates)):
			if odds_dates[i]!='':
				new_list.append(odds_dates[i])
		return new_list

	def get_next_odds_position(self, oddsdates, position):
		for i in range(position+1, len(oddsdates)):
			if oddsdates[i][0]=='$':
				return i

	def parse(self, response):
		sel = Selector(response)
		opponents = sel.xpath('//td[@class="matchStyle"]').xpath("a/text()").extract()
		odds = sel.xpath('//td[@class="matchStyle"]').re(r'\$\d+\.\d+')
		#for urls: get all the links that contains javascript:makePopup in the link
		urls = sel.xpath('//a[contains(@href, "javascript:makePopup")]/@href').extract()
		#gets dates
		dates = sel.xpath('//td[@class="tournamentStyle"]').re(r'[a-zA-Z]{3}\s[0-9]{1,2}.\d{4}')
		#very hacky way of doing this, but last resort
		odds_and_dates = sel.xpath('//td[@class="tournamentStyle" or @class="matchStyle"]').re(r'(\$\d+\.[0-9]{3})|([a-zA-Z]{3}\s[0-9]{1,2}.\d{4})')
		odds_and_dates_cleaned = self.remove_all_whitespace(odds_and_dates)
		index_of_first_odds = self.get_index_of_first_odds(odds_and_dates_cleaned)
		new_urls = self.fix_urls(urls)
		items = []
		date_index = index_of_first_odds-1
		current_date = odds_and_dates_cleaned[date_index]
		for i in range(50):
			item = OddsItem()
			item["opponent"] = opponents[i*3]
			item["odds"] = odds[i]
			#next_odds_position = self.get_next_odds_position(odds_and_dates_cleaned,date_index)
			if (odds_and_dates_cleaned[date_index][0]!='$'):
				current_date = odds_and_dates_cleaned[date_index]
				date_index+=1
			#if (odds_and_dates_cleaned[next_odds_position-1][0]!='$'):
			#	current_date = odds_and_dates_cleaned[next_odds_position-1]
			item["date"] = current_date
			#if odds_and_dates_cleaned[date_index][0]!='$':
			#	current_date = odds_and_dates_cleaned[date_index]
			date_index+=1
			item["matchStatsUrl"] = new_urls[i]
			items.append(item)
		return items


# points to all the odds
# sel.xpath('//td[@class="matchStyle"]').re(r'\$\d+\.\d+')