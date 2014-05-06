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
		"http://www.tennisinsight.com/player_activity.php?player_id=1"
	]

	def parse(self, response):
		sel = Selector(response)
		opponents = sel.xpath('//td[@class="matchStyle"]').xpath("a/text()").extract()
		odds = sel.xpath('//td[@class="matchStyle"]').re(r'\$\d+\.\d+')
		items = []
		for i in range(50):
			item = OddsItem()
			item["opponent"] = opponents[i*3]
			item["odds"] = odds[i]
			items.append(item)
		return items

# points to all the odds
# sel.xpath('//td[@class="matchStyle"]').re(r'\$\d+\.\d+')


