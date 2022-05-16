import nltk
from nltk import word_tokenize
from nltk import pos_tag
import json

STRUCTURED_DATA_PATH = './data/structured_resource.json'

print('READING DATA FROM FILE ...')
file = open(STRUCTURED_DATA_PATH)
data = json.load(file)
print('READING DATA FROM FILE COMPLETED !')


for news in data:
	news['title_tokens_raw'] = word_tokenize(news['title'])
	news['title_pos_tagged'] = pos_tag(news['title_tokens_raw'])
	news['title_ner'] = nltk.ne_chunk(news['title_pos_tagged'])

	news['description_tokens_raw'] = word_tokenize(news['description'])
	news['description_pos_tagged'] = pos_tag(news['description_tokens_raw'])
	news['description_ner'] = nltk.ne_chunk(news['description_pos_tagged'])
	print(news['description'])
	print(news['description_ner'])
	print('///////////////////')



