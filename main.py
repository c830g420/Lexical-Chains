
from ReadArticle import ReadArticle
from ProcessingText import ProcessingText
import re


def main() :

	dir = input('Please enter the directory of the article :\n\t')
	
	ra = ReadArticle(dir)
	wordlist = ra.tagging()
	
	pt = ProcessingText(wordlist)
	pt.processing()
	
	chains = pt.getChains()
	result = open('%s_chains' % re.sub(r'[.]', '-', dir), 'w', encoding = 'utf8')
	for i in range(len(chains)) :
		ch = 'Chain %d:\t%s' % (i, ', '.join(chains[i]))
		result.write('%s\n\n' % ch)
		print(ch[:100])
	result.close()




if __name__ == '__main__' :
	main()