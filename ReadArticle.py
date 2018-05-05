
##
#
# 5-4-2018
#
# by Chen
#
##

import re
import nltk

class ReadArticle :

	def __init__(self, directory) :

		self.dir = directory
		file = open(directory, 'r', encoding = 'utf8')
		self.raw = file.read()


	def tokenize(self) :
		
		"""
		This function is to tokenize all the words from the file.
		All the non word character (r'\W+') is removed.

		return:
			a list of words
		"""

		raw1 = re.sub(r'\W+', ' ', self.raw.lower())
		return raw1.split()


	def tagging(self) :

		"""
		Tag the words from the file, using nltk function pos_tag()
		"""

		wlist = self.tokenize()
		return nltk.pos_tag(wlist)