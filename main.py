
from ReadArticle import ReadArticle
from ProcessingText import ProcessingText
import re


def main() :

	# ask for the directory of the file
	dirt = input('Please enter the directory of the article :\n\t')
	fnm = re.sub(r'[.]', '-', dirt)
	
	# read file and tag the words
	ra = ReadArticle(dirt)
	wordlist = ra.tagging()
	
	# process the words and get the chains
	pt = ProcessingText(wordlist, 0.4)
	pt.processing()
	
	# write the chains to a file
	chains = pt.getChainsString()
	chsfl = open('%s_chains' % fnm, 'w', encoding = 'utf8')
	for i in range(len(chains)) :
		ch = 'Chain %d:\t%s' % (i, ', '.join(chains[i]))
		chsfl.write('%s\n\n' % ch)
		# print(ch[:100])
	chsfl.close()

	# get three longest chains, and write into a file
	chs = sorted(pt.getChains(), key = lambda x : -x.getLen())[:3] 
	sumfl = open('%s_summary' % fnm, 'w', encoding = 'utf8')
	for c in chs :
		sc = ' '.join(c.getWordChain())
		sumfl.write('%s\n\n' % sc)
		print(sc)
	sumfl.close()





if __name__ == '__main__' :
	main()