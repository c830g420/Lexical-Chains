
from collections import Counter, defaultdict
import numpy as np
from nltk.corpus import wordnet as wn

class LChain :

	def __init__(self, startword) :

		self.ctr = Counter()
		# self.idx = defaultdict(lambda : -1)
		self.thre = 0.3
		# self.mnsim = 0

		self.ctr[startword] += 1
		self.chain = list()
		self.chain.append(startword)
		self.ssets = Counter()
		self.ssets.update(wn.synsets(startword))
		self.frq = ssets.most_common(1)[0][1]



	def toAdd(self, word) :

		wsyn = wn.synsets(word)
		sims = np.ones(len(wsyn))


		for i in range(len(wsyn)) :
			if (self.ssets[wsyn[i]] > 0) :
				return True
			if (self.frq > 1) :
				syn = self.ssets.most_common()
				for s in syn :
					if (s[1] > 1) :
						sim = wn.path_simi






	def add(self, word) :

		self.ctr[word] += 1
		i = self.idx[word]
		if (i > 0 and i > )




