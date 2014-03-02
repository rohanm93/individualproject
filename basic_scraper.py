from scrapy.item import Item, Field

name = 'federerstats'
start_url = ['http://www.tennisinsight.com/player_activity.php?player_id=1']
rules = [Rule(SgmlLinkExtractor(allow=['/match_stats_popup.php?matchID=\d+'


MatchIdItem(Item):
	matchId = Field()
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
	p1AverageFirstServeSpeed = Field())
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
        p2AverageFirstServeSpeed = Field())
        p2AverageSecondServeSpeed = Field()

