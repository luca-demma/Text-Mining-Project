import json
import contractions
import nltk
import os
from fileActions import read_file_to_json, write_json_to_file
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from fileActions import write_json_to_file
from tqdm import tqdm
import multiprocessing
from pqdm.processes import pqdm
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
nltk.download("punkt")

STRUCTURED_DATA_PATH = './data/structured_resource/'
OUTLETS = sorted(os.listdir(STRUCTURED_DATA_PATH))

NUM_CORES = multiprocessing.cpu_count()


def to_lower_case(string):
	return string.lower()


def fix_contractions(string_processed):
	return contractions.fix(string_processed, slang=False)


def tokenize(string_processed):
	return word_tokenize(string_processed)


def remove_punctuations(tokens_list):
	return [token for token in tokens_list if (token.isalnum() or token == "covid-19")]


def lemmatize(tokens_list):
	return [lemmatizer.lemmatize(tokens) for tokens in tokens_list]


def remove_stopwords(tokens_list):
	return [token for token in tokens_list if not token in stop_words]


print('STARTING PROCESSING ...')


def normalize(outlet):
	outlet_file = read_file_to_json(STRUCTURED_DATA_PATH + outlet)
	for news in outlet_file:
		# news['description']
		title_processed = to_lower_case(news['title'])
		description_processed = to_lower_case(news['description'])

		# fix_contractions
		title_processed = fix_contractions(title_processed)
		description_processed = fix_contractions(description_processed)

		# tokenize
		title_tokens = tokenize(title_processed)
		description_tokens = tokenize(description_processed)

		# remove_punctuations
		title_tokens = remove_punctuations(title_tokens)
		description_tokens = remove_punctuations(description_tokens)

		# lemmatize
		title_tokens = lemmatize(title_tokens)
		description_tokens = lemmatize(description_tokens)

		# remove_stopwords
		title_tokens = remove_stopwords(title_tokens)
		description_tokens = remove_stopwords(description_tokens)

		news['title_processed'] = title_processed
		news['description_processed'] = description_processed

		news['title_tokens'] = title_tokens
		news['description_tokens'] = description_tokens

	write_json_to_file(outlet_file, "normalized_data/" + outlet)


pqdm(OUTLETS, normalize, n_jobs=NUM_CORES)
