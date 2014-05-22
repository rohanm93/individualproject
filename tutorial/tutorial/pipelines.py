# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TutorialPipeline(object):
	def process_item(self, item, spider):
		splitted = item['p1FirstServePercentage'].split('%')[0]
		item['p1FirstServePercentage'] = splitted
		item['p1FirstServePointsWonPercentage'] = item['p1FirstServePointsWonPercentage'].split('%')[0]
		item['p1SecondServePointsWon'] = item['p1SecondServePointsWon'].split('%')[0]
		item['p1FirstReturnPointsWon'] = item['p1FirstReturnPointsWon'].split('%')[0]
		item['p1SecondReturnPointsWon'] = item['p1SecondServePointsWon'].split('%')[0]
		if '%' in item['p1BreakPointsWon']:
			item['p1BreakPointsWon'] = item['p1BreakPointsWon'].split('%')[0]
		if item.has_key('p1AverageFirstServeSpeed'):
			item['p1AverageFirstServeSpeed'] = item['p1AverageFirstServeSpeed'].split('k')[0]
		if item.has_key('p1AverageSecondServeSpeed'):
			item['p1AverageSecondServeSpeed'] = item['p1AverageSecondServeSpeed'].split('k')[0]
		item['p2FirstServePercentage'] = item['p2FirstServePercentage'].split('%')[0]
		item['p2FirstServePointsWonPercentage'] = item['p2FirstServePointsWonPercentage'].split('%')[0]
		item['p2SecondServePointsWon'] = item['p2SecondServePointsWon'].split('%')[0]
		item['p2FirstReturnPointsWon'] = item['p2FirstReturnPointsWon'].split('%')[0]
		item['p2SecondReturnPointsWon'] = item['p2SecondServePointsWon'].split('%')[0]
		if '%' in item['p2BreakPointsWon']:
			item['p2BreakPointsWon'] = item['p2BreakPointsWon'].split('%')[0]
		if item.has_key('p2AverageFirstServeSpeed'):
			item['p2AverageFirstServeSpeed'] = item['p2AverageFirstServeSpeed'].split('k')[0]
		if item.has_key('p2AverageSecondServeSpeed'):
			item['p2AverageSecondServeSpeed'] = item['p2AverageSecondServeSpeed'].split('k')[0]
		item['duration'] = item['duration'].split(' ')[0]
		item['p1ServePointsWon'] = item['p1ServePointsWon'].split('%')[0]
		item['p2ServePointsWon'] = item['p2ServePointsWon'].split('%')[0]
		item['p1ReturnPointsWon'] = item['p1ReturnPointsWon'].split('%')[0]
		item['p2ReturnPointsWon'] = item['p2ReturnPointsWon'].split('%')[0]
		return item
