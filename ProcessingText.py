
from LChain import LChain



class ProcessingText :

	def __init__(self, wlist, th = 0.2) :

		self.wordList = wlist
		self.chains = list()
		self.thre = th



	def processing(self) :

		for w, t in self.wordList :
			if t == 'NN' :
				# print(w)
				# found = False

				masim = self.thre
				ci = -1

				for i in range(len(self.chains)) :
					sim = self.chains[i].toAdd(w)
					if (sim > masim) :
						# found = True
						masim = sim
					# if (c.toAdd_alter(w)) :
						ci = i
				
						# c.add_alter(w)
						
						# break

				# if (not found) :
				if (ci < 0):
					# print(len(self.chains))
					tmc = LChain(w, self.thre)
					if (tmc.isValid()) :
						self.chains.append(tmc)
				else :
					self.chains[ci].add(w)



	def getChains(self) :

		return self.chains


	def getChainsString(self) :

		return [c.getChain() for c in self.chains]




