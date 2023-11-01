### Need to be run within the machamp folder

#usr/bin/env python3

import io, os, argparse, sys

mapping = {'twitter': 'cardiffnlp-twitter-roberta-base'}

#child = sys.argv[1]

for child in ['Abe_Kuczaj', 'Adam_Brown', 'Emma_Weist', 'Laura_Braunwald', 'Lily_Providence', 'Naima_Providence', 'Roman_Weist', 'Sarah_Brown', 'Thomas_Thomas', 'Violet_Providence']:
	if child + '_indomain_parents' not in os.listdir('../predict/machamp/'):
		os.system('mkdir ../predict/machamp/' + child + '_indomain_parents/')
	for file in os.listdir('../processed_data/' + child + '/'):
		if file.endswith('.child'):
			for seed in [1, 2, 3]:
				if file + '.machamp.twitter.' + str(seed) + '.indomain' not in os.listdir('../predict/machamp/' + child + '_indomain_parents/') or os.stat('../predict/machamp/' + child + '_indomain_parents/' + file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain').st_size == 0:
					print(file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain')
				#	try:
					os.system("python3 predict.py logs/parents.machamp." + str(seed) + '.cardiffnlp-twitter-roberta-base/*/model.tar.gz ../processed_data/' + child + '/' + file + ' ../predict/machamp/' + child + '_indomain_parents/' + file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain --device 0 --batch_size 16')
				#	except:
				#		print(file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)
