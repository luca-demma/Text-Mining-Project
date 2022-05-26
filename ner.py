import nltk
from nltk import word_tokenize
from nltk import pos_tag
import json
from tqdm import tqdm
import time
from fileActions import read_file_to_json, write_json_to_file
from collections import defaultdict

CLASSIFIED_DATA_PATH = './data/classification_results.json'

data = read_file_to_json(CLASSIFIED_DATA_PATH)
data = [n for n in data if n['class'] == "IS COVID"]


def def_value(): return 0


total_ner = defaultdict(def_value)


def ner_tree_to_list(tree):
	ner_list = []
	for chunk in tree:
		if hasattr(chunk, 'label'):
			entity = "".join(c[0] for c in chunk)  # used join to convert to string
			label = chunk.label()

			ner_list.append({
				"entity": entity,  # used join to convert to string
				"label": label
			})

			total_ner[str(entity + " / " + label)] += 1


	return ner_list


for news in tqdm(data):
	# Titles
	title_tokens_raw = word_tokenize(news['title'])
	title_pos_tagged = pos_tag(title_tokens_raw)
	ner_tree_title = nltk.ne_chunk(title_pos_tagged)
	title_ner = ner_tree_to_list(ner_tree_title)

	news['title_tokens_raw'] = title_tokens_raw
	news['title_pos_tagged'] = title_pos_tagged
	news['title_ner'] = title_ner

	# Descriptions
	description_tokens_raw = word_tokenize(news['description'])
	description_pos_tagged = pos_tag(description_tokens_raw)
	ner_tree_description = nltk.ne_chunk(description_pos_tagged)
	description_ner = ner_tree_to_list(ner_tree_description)

	news['description_tokens_raw'] = description_tokens_raw
	news['description_pos_tagged'] = description_pos_tagged
	news['description_ner'] = description_ner


total_ner = {key: value for key, value in sorted(total_ner.items(), key=lambda item: item[1], reverse=True)}

# write_json_to_file(data, "ner_structured_data.json")

write_json_to_file(total_ner, "ner_total.json")
