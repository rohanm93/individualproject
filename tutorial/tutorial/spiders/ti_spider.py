from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector, HtmlXPathSelector
from tutorial.items import MatchStatsItem
import re

class TISpider(CrawlSpider):
	name = "tennisinsightwawrinka"
	allowed_domains = ["tennisinsight.com"]
#	start_urls = [
#		"http://www.tennisinsight.com/match_stats_popup.php?matchID=183704701"
#	]
	start_urls = [
		"http://www.tennisinsight.com/player_activity.php?player_id=1"
	]

	def getPopupLink(value):
		m = re.search("javascript:makePopup\('(.+?)'\)", value)
		if m:
			return m.group(1)

	rules = (
			Rule(SgmlLinkExtractor(allow=r"match_stats_popup.php\?matchID=\d+",
				restrict_xpaths='//td[@class="matchStyle"]',
				tags='a', attrs='href', process_value=getPopupLink), callback='parse_match', follow=True),
			)

	#rules = (
	#	Rule(SgmlLinkExtractor(allow='/match_stats_popup.php?matchID=\d+'),'parse', follow=True),
	#)


	def parse_match(self,response):
		sel = Selector(response)
		listOfStats = []
		stats = sel.xpath("//table//td//text()").extract()
		tennisStats = MatchStatsItem()
		#change into for loop. loop through entire array, and if for eg we find the word "1st serve percentage", take the array position+2 for p1 serve percentage
		for i in range(0, len(stats)):
			if stats[i]=="Tournament":
				tennisStats['tournament'] = stats[i+2]
			if stats[i]=="Round":
				tennisStats['t_round'] = stats[i+2]
			if stats[i]=="Winner":
				tennisStats['winner'] = stats[i+2]
			if stats[i]=="Duration":
				tennisStats['duration'] = stats[i+2]
			if stats[i]=="Duration":
				tennisStats['duration'] = stats[i+2]
			tennisStats['player1'] = stats[34]
			tennisStats['player2'] = stats[36]
			if stats[i]=="Aces":
				tennisStats['p1Aces'] = stats[i+2]
				tennisStats['p2Aces'] = stats[i+4]
			if stats[i]=="Double Faults":
				tennisStats['p1DoubleFaults'] = stats[i+2]
				tennisStats['p2DoubleFaults'] = stats[i+4]
			if stats[i]=="1st Serve Percentage":
				tennisStats['p1FirstServePercentage'] = stats[i+2]
				tennisStats['p2FirstServePercentage'] = stats[i+4]
			if stats[i]=="1st Serve Points Won":
				tennisStats['p1FirstServePointsWonPercentage'] = stats[i+2]
				tennisStats['p2FirstServePointsWonPercentage'] = stats[i+4]
			if stats[i]=="1st Serve Points Won":
				tennisStats['p1FirstServePointsWonPercentage'] = stats[i+2]
				tennisStats['p2FirstServePointsWonPercentage'] = stats[i+4]
			if stats[i]=="2nd Serve Points Won":
				tennisStats['p1SecondServePointsWon'] = stats[i+2]
				tennisStats['p2SecondServePointsWon'] = stats[i+4]
			if stats[i]=="1st Return Points Won":
				tennisStats['p1FirstReturnPointsWon'] = stats[i+2]
				tennisStats['p2FirstReturnPointsWon'] = stats[i+4]
			if stats[i]=="2nd Return Points Won":
				tennisStats['p1SecondReturnPointsWon'] = stats[i+2]
				tennisStats['p1SecondReturnPointsWon'] = stats[i+4]
			if stats[i]=="Break Points Won":
				tennisStats['p1BreakPointsWon'] = stats[i+2]
				tennisStats['p2BreakPointsWon'] = stats[i+4]
			tennisStats['urlVisited'] = response.url
			if stats[i]=="Winners":
				tennisStats['p1Winners'] = stats[i+2]
				tennisStats['p2Winners'] = stats[i+4]
			if stats[i]=="Unforced Errors":
				tennisStats['p1UnforcedErrors'] = stats[i+2]
				tennisStats['p2UnforcedErrors'] = stats[i+4]
			if stats[i]=="Net Approaches":
				tennisStats['p1NetApproaches'] = stats[i+2]
				tennisStats['p2NetApproaches'] = stats[i+4]
			if stats[i]=="Points Won at Net":
				tennisStats['p1PointsWonAtNet'] = stats[i+2]
				tennisStats['p2PointsWonAtNet'] = stats[i+4]
			if stats[i]=="Average 1st Serve":
				tennisStats['p1AverageFirstServeSpeed'] = stats[i+2]
				tennisStats['p2AverageFirstServeSpeed'] = stats[i+4]
			if stats[i]=="Average 2nd Serve":
				tennisStats['p1AverageSecondServeSpeed'] = stats[i+2]
				tennisStats['p2AverageSecondServeSpeed'] = stats[i+4]
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

