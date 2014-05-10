from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector, HtmlXPathSelector
from tutorial.items import MatchStatsItem
import re

class TISpider(CrawlSpider):
	name = "getdata"
	allowed_domains = ["tennisinsight.com", "atpworldtour.com"]
#	start_urls = [
#		"http://www.tennisinsight.com/match_stats_popup.php?matchID=183704701"
#	]
	start_urls = [
		"http://www.tennisinsight.com/player_activity.php?player_id=1",
		"http://www.tennisinsight.com/player_activity.php?player_id=1&min_activity=50&activity=1"
	]

	def getPopupLink(value):
		m = re.search("javascript:makePopup\('(.+?)'\)", value)
		if m:
			return m.group(1)

	def getPopupLinkATP(value):
		m = re.search("javascript:makePopup\('(.+?)'\)", value)
		if m:
			return m.group(1)
			#group(1) is the www.atp..etc link


	rules = (
			Rule(SgmlLinkExtractor(allow=r"match_stats_popup.php\?matchID=\d+",
				restrict_xpaths='//td[@class="matchStyle"]',
				tags='a', attrs='href', process_value=getPopupLink), callback='parse_match', follow=True),
			Rule(SgmlLinkExtractor(allow=r"http\:\/\/www\.atpworldtour\.com\/Share\/Match\-Facts\-Pop\-Up\.aspx\?t=\d+&y=\d+&r=\d+&p=....",	
				restrict_xpaths='//td[@class="matchStyle"]', canonicalize=False,
				tags='a', attrs='href', process_value=getPopupLinkATP), callback='parse_match_atp', follow=True),
			)

	def parse_match_atp(self,response):
		sel = Selector(response)
		listOfStats = []
		stats = sel.xpath("//table//td//text()").extract()
		tennisStats = MatchStatsItem()
		for i in range(0, len(stats)):
			stats[i] = stats[i].replace(u'\xa0', u' ')
			if stats[i]=="Tournament":
				tennisStats['tournament'] = stats[i+1]
			if stats[i]=="Round":
				tennisStats['t_round'] = stats[i+1]
			if stats[i]=="Winner":
				tennisStats['winner'] = stats[i+1]
			if stats[i]=="Time":
				duration = stats[i+1].replace(u'\xa0', u' ')
				tennisStats['duration'] = duration
			if stats[i]=="Players":
				tennisStats['player1'] = stats[i+1]
				tennisStats['player2'] = stats[i+2]
			if stats[i]=="Aces":
				tennisStats['p1Aces'] = stats[i+1]
				tennisStats['p2Aces'] = stats[i+2]
			if stats[i]=="Double Faults":
				tennisStats['p1DoubleFaults'] = stats[i+1]
				tennisStats['p2DoubleFaults'] = stats[i+2]
			if stats[i]=="1st Serve":
				tennisStats['p1FirstServePercentage'] = stats[i+1]
				tennisStats['p2FirstServePercentage'] = stats[i+2]
			if stats[i]=="1st Serve Points Won":
				tennisStats['p1FirstServePointsWonPercentage'] = stats[i+1]
				tennisStats['p2FirstServePointsWonPercentage'] = stats[i+2]
			if stats[i]=="2nd Serve Points Won":
				tennisStats['p1SecondServePointsWon'] = stats[i+1]
				tennisStats['p2SecondServePointsWon'] = stats[i+2]
			if stats[i]=="1st Serve Return Points Won":
				tennisStats['p1FirstReturnPointsWon'] = stats[i+1]
				tennisStats['p2FirstReturnPointsWon'] = stats[i+2]
			if stats[i]=="2nd Serve Return Points Won":
				tennisStats['p1SecondReturnPointsWon'] = stats[i+1]
				tennisStats['p1SecondReturnPointsWon'] = stats[i+2]
			if stats[i]=="Break Points Converted":
				tennisStats['p1BreakPointsWon'] = stats[i+1]
				tennisStats['p2BreakPointsWon'] = stats[i+2]
			tennisStats['urlVisited'] = response.url
			# not checked below this line
			if stats[i]=="Winners":
				tennisStats['p1Winners'] = stats[i+1]
				tennisStats['p2Winners'] = stats[i+2]
			if stats[i]=="Unforced Errors":
				tennisStats['p1UnforcedErrors'] = stats[i+1]
				tennisStats['p2UnforcedErrors'] = stats[i+2]
			if stats[i]=="Net Approaches":
				tennisStats['p1NetApproaches'] = stats[i+1]
				tennisStats['p2NetApproaches'] = stats[i+2]
			if stats[i]=="Points Won at Net":
				tennisStats['p1PointsWonAtNet'] = stats[i+1]
				tennisStats['p2PointsWonAtNet'] = stats[i+2]
			if stats[i]=="Average 1st Serve":
				tennisStats['p1AverageFirstServeSpeed'] = stats[i+1]
				tennisStats['p2AverageFirstServeSpeed'] = stats[i+2]
			if stats[i]=="Average 2nd Serve":
				tennisStats['p1AverageSecondServeSpeed'] = stats[i+1]
				tennisStats['p2AverageSecondServeSpeed'] = stats[i+2]
		listOfStats.append(tennisStats)
		return listOfStats

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
			#if stats[i]=="Duration":
			#	tennisStats['duration'] = stats[i+2]
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
			# if stats[i]=="1st Serve Points Won":
			# 	tennisStats['p1FirstServePointsWonPercentage'] = stats[i+2]
			# 	tennisStats['p2FirstServePointsWonPercentage'] = stats[i+4]
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

