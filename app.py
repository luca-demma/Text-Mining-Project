import json
import contractions
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download("punkt")

print('READING DATA FROM FILE ...')
STRUCTURED_DATA_PATH = './data/structured_resource.json'
file = open(STRUCTURED_DATA_PATH)
data = json.load(file)
print('READING DATA FROM FILE COMPLETED !')


def to_lower_case(news):
	news['title_processed'] = news['title'].lower()
	news['description_processed'] = news['description'].lower()


def fix_contractions(news):
	news['title_processed'] = contractions.fix(news['title_processed'], slang=False)
	news['description_processed'] = contractions.fix(news['description_processed'], slang=False)


def tokenize(news):
	news['title_tokens'] = word_tokenize(news['title_processed'])
	news['description_tokens'] = word_tokenize(news['description_processed'])


def remove_punctuations(news):
	news['title_tokens'] = [token for token in news['title_tokens'] if token.isalnum()]
	news['description_tokens'] = [token for token in news['description_tokens'] if token.isalnum()]


def lemmatize(news):
	news['title_tokens'] = [lemmatizer.lemmatize(tokens) for tokens in news['title_tokens']]
	print(news['title'])
	print(news['title_tokens'])
	print('/////////////////////////////////////')



print('STARTING PROCESSING ...')


for news in data:
	to_lower_case(news)
	fix_contractions(news)
	tokenize(news)
	remove_punctuations(news)
	lemmatize(news)
