
from LChain import LChain



class ProcessingText :

	def __init__(self, wlist) :

		self.wordList = wlist
		self.chains = list()



	def processing(self) :

		for w, t in self.wordList :
			if t == 'NN' :
				# print(w)
				found = False

				for c in self.chains :
					if (c.toAdd(w)) :
					# if (c.toAdd_alter(w)) :
						c.add(w)
						# c.add_alter(w)
						found = True
						break

				if (not found) :
					# print(len(self.chains))
					tmc = LChain(w)
					if (tmc.isValid()) :
						self.chains.append(tmc)


	def getChains(self) :

		return [c.getChain() for c in self.chains]




