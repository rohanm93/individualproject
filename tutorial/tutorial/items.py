# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MatchStatsItem(Item):
        matchId = Field()
	tournament = Field()
	t_round = Field()
	winner = Field()
        duration = Field()
	player1 = Field()
        player2 = Field()
	p1Aces = Field()
        p1DoubleFaults = Field()
        p1FirstServePercentage = Field()
        p1FirstServePointsWonPercentage = Field()
        p1SecondServePointsWon = Field()
        p1FirstReturnPointsWon = Field()
        p1SecondReturnPointsWon = Field()
        p1BreakPointsWon = Field()
        p1Winners = Field()
        p1UnforcedErrors = Field()
        p1NetApproaches = Field()
        p1PointsWonAtNet = Field()
	p1AverageFirstServeSpeed = Field()
        p1AverageSecondServeSpeed = Field()
        p2Aces = Field()
        p2DoubleFaults = Field()
        p2FirstServePercentage = Field()
        p2FirstServePointsWonPercentage = Field()
        p2SecondServePointsWon = Field()
        p2FirstReturnPointsWon = Field()
        p2SecondReturnPointsWon = Field()
        p2BreakPointsWon = Field()
        p2Winners = Field()
        p2UnforcedErrors = Field()
        p2NetApproaches = Field()
        p2PointsWonAtNet = Field()
        p2AverageFirstServeSpeed = Field()
        p2AverageSecondServeSpeed = Field()
