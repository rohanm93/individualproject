# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = {'tutorial.pipelines.TutorialPipeline' : 100}
CONCURRENT_REQUESTS = 1

FEED_EXPORTERS = {
    'csv': 'tutorial.feedexport.CSVkwItemExporter'
}

# By specifying the fields to export, the CSV export honors the order
# rather than using a random order.
EXPORT_FIELDS = [
    'matchId',
    'tournament',
    'player1',
    'player2',
    'winner',
    't_round',
    'duration',
    'p1Aces',
    'p1DoubleFaults',
    'p1FirstServePercentage',
    'p1FirstServePointsWonPercentage',
    'p1SecondServePointsWon',
    'p1FirstReturnPointsWon',
    'p1SecondReturnPointsWon',
    'p1BreakPointsWon',
    'p1Winners',
    'p1UnforcedErrors',
    'p1NetApproaches',
    'p1PointsWonAtNet',
    'p1AverageFirstServeSpeed',
    'p1AverageSecondServeSpeed',
    'p2Aces',
    'p2DoubleFaults',
    'p2FirstServePercentage',
    'p2FirstServePointsWonPercentage',
    'p2SecondServePointsWon',
    'p2FirstReturnPointsWon',
    'p2SecondReturnPointsWon',
    'p2BreakPointsWon',
    'p2Winners',
    'p2UnforcedErrors',
    'p2NetApproaches',
    'p2PointsWonAtNet',
    'p2AverageFirstServeSpeed',
    'p2AverageSecondServeSpeed',
    'urlVisited'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
