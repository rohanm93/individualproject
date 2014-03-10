from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector, HtmlXPathSelector
from tutorial.items import MatchStatsItem

class TISpider(CrawlSpider):
	name = "tennisinsightwawrinka"
	allowed_domains = ["tennisinsight.com"]
#	start_urls = [
#		"http://www.tennisinsight.com/match_stats_popup.php?matchID=183704701"
#	]
	start_urls = [
		"http://www.tennisinsight.com/player_activity.php?player_id=1"
	]
	rules = (
		Rule(SgmlLinkExtractor(allow='/match_stats_popup.php?matchID=\d+'),'parse', follow=True),
	)


	def parse_match(self,response):
		sel = Selector(response)
		listOfStats = []
		stats = sel.xpath("//table//td//text()").extract()
		tennisStats = MatchStatsItem()
		#change into for loop. loop through entire array, and if for eg we find the word "1st serve percentage", take the array position+2 for p1 serve percentage
		tennisStats['matchId'] = 183704701
		tennisStats['tournament'] = stats[8]
		tennisStats['t_round'] = stats[14]
		tennisStats['winner']  = stats[20]
		tennisStats['duration'] = stats[26]
		tennisStats['player1'] = stats[34]
		tennisStats['player2'] = stats[36]
		tennisStats['p1Aces'] = stats[50]
		tennisStats['p2Aces'] = stats[52]
		tennisStats['p1DoubleFaults'] = stats[58]
		tennisStats['p2DoubleFaults'] = stats[60]
		tennisStats['p1FirstServePercentage'] = stats[66]
		tennisStats['p2FirstServePercentage'] = stats[68]
		tennisStats['p1FirstServePointsWonPercentage'] = stats[74]
		tennisStats['p2FirstServePointsWonPercentage'] = stats[76]
		tennisStats['p1SecondServePointsWon'] = stats[82]
		tennisStats['p2SecondServePointsWon'] = stats[84]
		tennisStats['p1FirstReturnPointsWon'] = stats[110]
		tennisStats['p2FirstReturnPointsWon'] = stats[112]
		tennisStats['p1SecondReturnPointsWon'] = stats[118]
		tennisStats['p2SecondReturnPointsWon'] = stats[120]
		tennisStats['p1BreakPointsWon'] = stats[126]
		tennisStats['p2BreakPointsWon'] = stats[128]
		if stats[168]=="Detailed Statistics":
			print "detailed statistics are available"
			tennisStats['p1Winners'] = stats[174]
			tennisStats['p2Winners'] = stats[176]
			tennisStats['p1UnforcedErrors'] = stats[182]
	                tennisStats['p2UnforcedErrors'] = stats[184]
			tennisStats['p1NetApproaches'] = stats[190]
			tennisStats['p2NetApproaches'] = stats[192]
			tennisStats['p1PointsWonAtNet'] = stats[198]
			tennisStats['p2PointsWonAtNet'] = stats[200]
			tennisStats['p1AverageFirstServeSpeed'] = stats[214]
			tennisStats['p2AverageFirstServeSpeed'] = stats[216]
	                tennisStats['p1AverageSecondServeSpeed'] = stats[222]
        	        tennisStats['p2AverageSecondServeSpeed'] = stats[224]
		listOfStats.append(tennisStats)
		return listOfStats
#		print stats[214], "testp1avgfirstservespeed"
'''
		items = hxs.select('//table/td')
		tennisStats['matchId'] = 183704701

		for item in items:
			tennisStats['player1'] = item.
			tennisStats['player2'] = 
			tennisStats['p1Aces']  =
			tennisStats['p1DoubleFaults']
#		sel = Selector(response)
#		stats = sel.xpath
#rules = [Rule(SgmlLinkExtractor(allow=['/match_stats_popup.php?matchID=\d+'
'''

