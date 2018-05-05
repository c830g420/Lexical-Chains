##
#
# 5-4-2018
#
# by Chen
#
##

from collections import Counter, defaultdict
import numpy as np
from nltk.corpus import wordnet as wn

class LChain :

	"""
	This is a class for a lexical chain
	"""

	def __init__(self, startword, th = 0.2) :


		# This is a counter for the words of this lexical chain
		self.ctr = Counter()

		# self.idx = defaultdict(lambda : -1)

		# the threshold of the lowest simmilarity to be in this chain
		self.thre = th
		# self.mnsim = 0

		# initiate this chain with a startword (the first word to be in this chain)
		self.ctr[startword] += 1

		# a list to record the words from this chain 
		# in the order of the word appearing in the file
		self.chain = list()
		self.chain.append(startword)

		# a counter of to record the synonym (meaning) set of this chain
		self.ssets = Counter()

		ss = wn.synsets(startword)

		self.ssets.update(ss)
		
		# self.sfrq = ssets.most_common(1)[0][1]
		# self.asets = Counter()
		# self.hypersets = Counter()
		# self.hyposets = Counter()

		# for s in ss :
		# 	self.asets.update(s.lemmas()[0].antonyms())
		# 	self.hypersets.

		# self.hypersets = Counter()

		# for s 

	def isValid(self) :
		
		"""
		This function is to test this lexical chain is valid chain.
		A valid lexical chain means the synonym set is not empty, whhich means this chain has meaning.

		return: 
			size of the synonym set
				(0, if this chain is not valid)
		"""
		return len(self.ssets)


	def getSet(self) :
		"""
		NOT A getter for the synonym set of this chain

		This function is to get the 'most popular' synsets of this chain.

		return:
			the 'most popular' synsets
				if some of the synset counted more than once in this chain,
					return all the synset counted more than once
				else,
					return all the synset

		"""

		mc = self.ssets.most_common()

		if (mc[0][1] > 1) :
			for i in range(len(mc)) :
				if (mc[i][1] < 2) :
					return mc[:i]
			return mc
		else :
			return mc


	def toAdd(self, word) :

		"""
		This function is to test if a word belongs to this set.
		This function uses the most popular synset of this chain.

		param:
			the word to test

		return:
			simmilatity of the word to this chain
				sim, if the word can fit this chain
				0, if the word does not fit this chain

		"""

		wsyn = wn.synsets(word)
		# sims = np.ones(len(wsyn))
		syn = self.getSet()

		masim = 0

		for i in range(len(wsyn)) :

			# if the word has overlap synset with this chain, it belongs to this
			if (self.ssets[wsyn[i]] > 0) :
				return 1
			
			# find the highest simmilarity between the word and synset of this chain
			for s, f in syn :
				sim = s.path_similarity(wsyn[i])
				if (sim and sim > masim) :
					masim = sim

		if (masim > self.thre) :
			return masim
		else :
			return 0


	def toAdd_alter(self, word) :

		"""
		This function is to test if a word belongs to this set (alternative method)

		param:
			the word to test

		return:
			True, if the word can fit this chain
			False, if the word does not fit this chain

		"""
		
		wsyn = wn.synsets(word)

		for i in range(len(wsyn)) :
			if (self.ssets[wsyn[i]] > 0) :
				return True
			
			for s, f in self.ssets.items() :
				sim = s.path_similarity(wsyn[i])
				if (sim and sim > 0.1) :
					return True

		return False




	def add(self, word) :

		"""
		This function is to add the word to this chain.
		The synset is updated with the new word.

		param:
			the word to add

		"""

		self.ctr[word] += 1
		self.ssets.update(wn.synsets(word))
		self.chain.append(word)


	def add_alter(self, word) :

		"""
		This function is to add the word to this chain.
		The synset is NOT updated with the new word.

		param:
			the word to add

		"""

		self.ctr[word] += 1
		# self.ssets.update(wn.synsets(word))
		self.chain.append(word)


	def getLen(self) :

		"""
		This function is get the number of words from this chain.
		If a word appears more than once, count multiple times.

		return:
			the number of words

		"""

		return len(self.chain)


	def getWordChain(self) :

		"""
		A getter for the original lexical chain (self.chain) of this chain
		"""

		return self.chain

	def getChain(self) :

		"""
		A getter for the computed lexical chain (self.chain) of this chain

		return:
			the computed lexical chain
			for example, [girl(2), woman(1), women(3), person(1), she(4)]
		"""


		re = list()
		tm = set()

		for w in self.chain :
			if (w not in tm) :
				re.append('%s(%d)' % (w, self.ctr[w]))
				tm.add(w)

		return re



