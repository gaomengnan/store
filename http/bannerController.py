from models import Options
class bannerController():


	def getBanner(self):
		options = Options.Options.query.filter(Options.Options.option_name=='banner').first()
		return options.option_value
