import nltk
from nltk import word_tokenize
from nltk import pos_tag
import json
from tqdm import tqdm
import time
from fileActions import read_file_to_json, write_json_to_file
from nltk.tag import StanfordNERTagger
import os

# change with os JAVA_PATH
JAVA_PATH = "/var/run/host/usr/lib/jvm/java-11-openjdk-amd64/bin/java"
os.environ['JAVAHOME'] = JAVA_PATH

st = StanfordNERTagger('/home/luca/UNI/Text Mining/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/home/luca/UNI/Text Mining/stanford-ner-2020-11-17/stanford-ner.jar',
					   encoding='utf-8')

STRUCTURED_DATA_PATH = './data/structured_resource.json'

data = read_file_to_json(STRUCTURED_DATA_PATH)

for news in tqdm(data):
	# Descriptions
	description_tokens_raw = word_tokenize(news['description'])
	ner_tagged = st.tag(description_tokens_raw)
	print(news['description'])
	print(ner_tagged)
	print("/////////////////////////////")

write_json_to_file(data, "ner.json")
