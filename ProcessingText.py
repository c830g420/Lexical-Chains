
##
#
# 5-4-2018
#
# by Chen
#
##

from LChain import LChain


class ProcessingText :

	def __init__(self, wlist, th = 0.2) :

		# the list of words from the file
		self.wordList = wlist

		# the chains generated from the file
		self.chains = list()

		# the threshold for this file
		self.thre = th



	def processing(self) :
		
		"""
		This function is to analyze the words from the file

		"""

		for w, t in self.wordList :

			# take only the noun words into consideration
			if t == 'NN' :
				# print(w)
				# found = False

				masim = self.thre
				ci = -1

				# find the most suitable chain for the word (highest simmilarity)
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
					# if no suitable chains found, start a new chain
					# print(len(self.chains))
					tmc = LChain(w, self.thre)
					if (tmc.isValid()) :
						# some words cannot start a valid lexical chain
						self.chains.append(tmc)
				else :
					self.chains[ci].add(w)



	def getChains(self) :

		return self.chains


	def getChainsString(self) :

		"""
		return:
			a list of list of words with appearance 
			for example [[girl(2), woman(1), women(3), person(1), she(4)],
						[hat(2), skirt(1), pants(2), clothes(1), shirt(2)]]
		"""

		return [c.getChain() for c in self.chains]




