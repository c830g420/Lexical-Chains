
import re
import nltk

class ReadArticle :

	def __init__(self, directory) :

		self.dir = directory
		file = open(directory, 'r', encoding = 'utf8')
		self.raw = file.read()


	def tokenize(self) :

		raw1 = re.sub(r'\W+', ' ', self.raw.lower())
		return raw1.split()


	def tagging(self) :

		wlist = self.tokenize()
		return nltk.pos_tag(wlist)