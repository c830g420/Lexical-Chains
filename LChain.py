
from collections import Counter, defaultdict
import numpy as np
from nltk.corpus import wordnet as wn

class LChain :

	def __init__(self, startword, th = 0.2) :

		self.ctr = Counter()
		# self.idx = defaultdict(lambda : -1)
		self.thre = th
		# self.mnsim = 0

		self.ctr[startword] += 1
		self.chain = list()
		self.chain.append(startword)
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
		return len(self.ssets)


	def getSet(self) :

		mc = self.ssets.most_common()

		if (mc[0][1] > 1) :
			for i in range(len(mc)) :
				if (mc[i][1] < 2) :
					return mc[:i]
			return mc
		else :
			return mc


	def toAdd(self, word) :

		wsyn = wn.synsets(word)
		# sims = np.ones(len(wsyn))
		syn = self.getSet()

		masim = 0

		for i in range(len(wsyn)) :
			if (self.ssets[wsyn[i]] > 0) :
				return 1
			
			for s, f in syn :
				sim = s.path_similarity(wsyn[i])
				if (sim and sim > masim) :
					masim = sim

		if (masim > self.thre) :
			return masim
		else :
			return 0


	def toAdd_alter(self, word) :
		
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

		self.ctr[word] += 1
		self.ssets.update(wn.synsets(word))
		self.chain.append(word)


	def add_alter(self, word) :

		self.ctr[word] += 1
		# self.ssets.update(wn.synsets(word))
		self.chain.append(word)


	def getLen(self) :

		return len(self.chain)


	def getWordChain(self) :

		return self.chain

	def getChain(self) :

		re = list()
		tm = set()

		for w in self.chain :
			if (w not in tm) :
				re.append('%s(%d)' % (w, self.ctr[w]))
				tm.add(w)

		return re



