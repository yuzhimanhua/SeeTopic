import argparse

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='scidocs')
parser.add_argument('--num_iter', default=2, type=int)
parser.add_argument('--rho', default=0.1, type=float)
args = parser.parse_args()

dataset = args.dataset
num_iter = args.num_iter
rho = args.rho
topM = 100
epsilon = 1e-8
weights = [0.5, 0.5]

if dataset == 'scidocs':
	models = ['biobert', 'local']
else:
	models = ['bert', 'local']

scores = {}
names = []
for i, model in enumerate(models):
	with open(f'{dataset}/keywords_{model}_{num_iter}.txt') as fin:
		for c, line in enumerate(fin):
			if i == 0:
				scores[c] = {}
			data = line.strip().split(':')[1].split(',')
			names.append(data[0])
			data = data[1:topM]
			for r, word in enumerate(data):
				if word not in scores[c]:
					scores[c][word] = [epsilon for _ in range(len(models))]
				scores[c][word][i] = weights[i] * 1/(r+1)

for c in scores:
	for word in scores[c]:
		total_score = 0
		for x in scores[c][word]:
			total_score += x ** rho
		scores[c][word] = total_score

words_sorted = [None for _ in range(len(scores))]
for c in range(len(scores)):
	scores_sorted = sorted(scores[c].items(), key=lambda item: item[1], reverse=True)
	words_sorted[c] = [k for k, v in scores_sorted]

expanded_words = set()
expanded_list = [[] for _ in range(len(scores))]
pointer = [0 for _ in range(len(scores))]
for _ in range(topM):
	for c in range(len(scores)):
		while pointer[c] < len(words_sorted[c]) and words_sorted[c][pointer[c]] in expanded_words:
			pointer[c] += 1
		if pointer[c] < len(words_sorted[c]):
			w = words_sorted[c][pointer[c]]
			expanded_words.add(w)
			expanded_list[c].append(w)
			pointer[c] += 1

with open(f'{dataset}/keywords_{num_iter}.txt', 'w') as fout:
	for c in range(len(scores)):
		fout.write(str(c)+':'+names[c]+','+','.join(expanded_list[c])+'\n')