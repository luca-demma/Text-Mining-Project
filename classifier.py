import json
from collections import defaultdict
from fileActions import read_file_to_json, write_json_to_file
from tqdm import tqdm

PROB_COVID_PATH = './data/prob_covid.json'
PROB_NOT_COVID_PATH = './data/prob_NOT_covid.json'
NORMALIZED_DATA_PATH = './data/normalized_data.json'

probCovid = read_file_to_json(PROB_COVID_PATH)
probNotCovid = read_file_to_json(PROB_NOT_COVID_PATH)
data = read_file_to_json(NORMALIZED_DATA_PATH)

classificationResults = {}

lowestCovidProb = probCovid[list(probCovid)[-1]]
lowestNotCovidProb = probNotCovid[list(probNotCovid)[-1]]

for news in tqdm(data):
	isCovidScore = 1
	notCovidScore = 1
	for word in news['title_tokens']:
		probCovidTmp = lowestCovidProb if not word in probCovid else probCovid[word]
		probNotCovidTmp = lowestNotCovidProb if not word in probNotCovid else probNotCovid[word]

		isCovidScore *= probCovidTmp
		notCovidScore *= probNotCovidTmp
	for word in news['description_tokens']:
		probCovidTmp = lowestCovidProb if not word in probCovid else probCovid[word]
		probNotCovidTmp = lowestNotCovidProb if not word in probNotCovid else probNotCovid[word]

		isCovidScore *= probCovidTmp
		notCovidScore *= probNotCovidTmp
	if isCovidScore > notCovidScore:
		news['class'] = 'IS COVID'
	else:
		news['class'] = 'NOT COVID'
	news['is_covid_score'] = isCovidScore
	news['not_covid_score'] = notCovidScore


write_json_to_file(data, "classification_results.json")

