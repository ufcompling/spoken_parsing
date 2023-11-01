import io, os

### Read *.conllu file ###

def conll_read_sentence(file_handle):
	sent = []
	for line in file_handle:
		line = line.strip('\n')	
		if line.startswith('#') is False :
			toks = line.split("\t")					
			if len(toks) == 1:
				return sent 
			else:
				if toks[0].isdigit() == True:
					sent.append(toks)
	return None

train = []
for directory in os.listdir('processed_data/'):
	for file in os.listdir('processed_data/' + directory + '/'):
		if file.endswith('parent'):
			with open('processed_data/' + directory + '/' + file) as f:
				sent = conll_read_sentence(f)
				while sent is not None:
					train.append(sent)
					sent = conll_read_sentence(f)
	
with open('processed_data/train_parents.conllu', 'w') as f:
	for sent in train:
		for tok in sent:
			f.write('\t'.join(w for w in tok) + '\n')
		f.write('\n')


					