import nltk
from nltk import word_tokenize
from nltk import pos_tag
import json

STRUCTURED_DATA_PATH = './data/structured_resource.json'

print('READING DATA FROM FILE ...')
file = open(STRUCTURED_DATA_PATH)
data = json.load(file)
print('READING DATA FROM FILE COMPLETED !')


def ner_tree_to_list(tree):
	ner_list = []
	for chunk in tree:
		if hasattr(chunk, 'label'):
			ner_list.append({
				"entity": "".join(c[0] for c in chunk), # used join to convert to string
				"label": chunk.label()
			})
	return ner_list


for news in data:
	news['title_tokens_raw'] = word_tokenize(news['title'])
	news['title_pos_tagged'] = pos_tag(news['title_tokens_raw'])
	ner_tree_title = nltk.ne_chunk(news['title_pos_tagged'])
	news['title_ner'] = ner_tree_to_list(ner_tree_title)

	news['description_tokens_raw'] = word_tokenize(news['description'])
	news['description_pos_tagged'] = pos_tag(news['description_tokens_raw'])
	ner_tree_description = nltk.ne_chunk(news['description_pos_tagged'])
	news['description_ner'] = ner_tree_to_list(ner_tree_description)


outFile = open('./data/ner.json', 'w')
json.dump(data, outFile, indent=4)
outFile.close()



