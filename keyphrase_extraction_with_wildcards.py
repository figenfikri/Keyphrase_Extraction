# The algorithm in Xie et al. (2017) was implemented.
# Reference: Xie, F., Wu, X., & Zhu, X. (2017). Efficient sequential pattern mining with wildcards for keyphrase extraction. Knowledge-Based Systems, 115, 27-39.

import operator
import codecs
import nltk

p = []
d = {}

def spmw(seqDB, n, m , minSup):
	alphabet = set(seqDB)
	for e in alphabet:
		NL = [(i,) for i, x in enumerate(seqDB) if x == e]
		minFre(seqDB, e, minSup, NL, n, m, alphabet)



def minFre(seqDB, pattern, minSup, NL, n, m, alphabet):
	sup = calcSup(seqDB, pattern, NL)
	NL2 = []
	if sup >= minSup:
		#p.append(pattern)
		#d[pattern] = sup
		for e in alphabet:
			nodes = []
			pattern2 = pattern + " " + e
			NL2 = [i for i, x in enumerate(seqDB) if x == e]
			for i in range(len(NL)):
				for j in range(len(NL2)):
					if NL2[j]-NL[i][len(NL[i])-1]-1 >= n and NL2[j]-NL[i][len(NL[i])-1]-1 <= m:
						nodes.append(NL[i]+(NL2[j],))
			sup = calcSup(seqDB, pattern, nodes)
			if sup >= minSup:
				p.append(pattern2)
				d[pattern2] = sup
				print d
				print('\n')
	
			

def calcSup(seqDB, pattern, NL):
	support = []
	seen = set()
	for node in NL:
		flag = 1
		for i in range(len(node)):
			if node[i] in seen:
				flag = 0
				break
		if flag == 1:
			support.append(node)
			for i in range(len(node)):
				seen.add(node[i])
	return len(support)



 
w=[]
	
with codecs.open('preprocessed.txt','r', encoding = 'UTF-8') as f:
	for line in f:
		for word in line.split():
			w.append(word) 

			
print("Number of words:")
print(len(w))
print("\n")
print("Number of different words:")
print(len(set(w)))	
print("\n")	

minGap = input("Please enter minimum gap: ")
maxGap = input("Please enter maximum gap: ")
minSup = input("Please enter minimum support: ")
freq = input("Please enter minimum bigram frequency: ")

print("\n")	

spmw(w, minGap, maxGap, minSup)

print(len(p))
print('\n')
print d
print('\n')

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print sorted_d
print('\n')

phrases = codecs.open('phrases.txt', 'w', encoding = 'UTF-8')
for e in d:
	phrases.write(e)
	phrases.write('\n')

	
pairs = nltk.bigrams(w)
fdist=nltk.FreqDist(pairs)
bigram = filter(lambda x: fdist[x] >= freq, fdist)
bigrams = codecs.open('bigrams.txt', 'w', encoding = 'UTF-8')
for e in bigram:
	bigrams.write(e[0])
	bigrams.write('\t')
	bigrams.write(e[1])
	#bigrams.write('\t')
	#bigrams.write(fdist[e])
	bigrams.write('\n')

print('\n')
print(bigram)

freqDist = nltk.FreqDist(w)
frequentWords = filter(lambda x: freqDist[x] >= freq, freqDist)
freqWords = codecs.open('freqWords.txt', 'w', encoding = 'UTF-8')
for e in frequentWords:
	freqWords.write(e)
	freqWords.write('\n')






