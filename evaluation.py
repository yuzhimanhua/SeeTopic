import math
import argparse

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='scidocs')
parser.add_argument('--model', default='seetopic')
parser.add_argument('--topk', default=10, type=int)
args = parser.parse_args()

dataset = args.dataset
model = args.model
topk = args.topk
epsilon = 1

word2cnt = {}
topics = []
with open(f'{dataset}/keywords_{model}.csv') as fin:
	for line in fin:
		words = line.strip().split()[1:topk+1]
		topics.append(words)
		for word in words:
			word2cnt[word] = set()

tot = 0.0
with open(f'{dataset}/{dataset}_test.txt') as fin:
	for idx, line in enumerate(fin):
		tot += 1
		text = set(line.strip().split())
		for word in word2cnt:
			if word in text:
				word2cnt[word].add(idx)

pmi = npmi = lcp = 0
for words in topics:
	for i in range(topk):
		for j in range(i):
			wi = words[i]
			wj = words[j]
			pi = (len(word2cnt[wi]) + epsilon) / tot
			pj = (len(word2cnt[wj]) + epsilon) / tot
			pij = (len(word2cnt[wi].intersection(word2cnt[wj])) + epsilon) / tot
				
			# PMI
			pmi += math.log(pij/(pi*pj))

			# NPMI
			npmi += -1 + math.log(pi*pj)/math.log(pij)

			# LCP
			lcp += math.log(pij/pj)

word_set = set()
num_topics = 0
with open(f'{dataset}/keywords_{model}.csv') as fin:
	for line in fin:
		words = line.strip().split()[1:topk+1]
		num_topics += 1
		for word in words:
			word_set.add(word)

print(model)
print('PMI:', pmi / len(topics) / (topk*(topk-1)/2))
print('NPMI:', npmi / len(topics) / (topk*(topk-1)/2))
print('LCP:', lcp / len(topics) / (topk*(topk-1)/2))
print('Diversity:', len(word_set) / ((topk)*num_topics))
