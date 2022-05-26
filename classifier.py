import json
import os
from collections import defaultdict
from fileActions import read_file_to_json, write_json_to_file
from tqdm import tqdm
import math

PROB_COVID_PATH = './data/prob_covid.json'
PROB_NOT_COVID_PATH = './data/prob_NOT_covid.json'
NORMALIZED_DATA_PATH = './data/normalized_data/'
OUTLETS = sorted(os.listdir(NORMALIZED_DATA_PATH))

probCovid = read_file_to_json(PROB_COVID_PATH)
probNotCovid = read_file_to_json(PROB_NOT_COVID_PATH)

classificationResults = {}

lowestCovidProb = probCovid[list(probCovid)[-1]]
lowestNotCovidProb = probNotCovid[list(probNotCovid)[-1]]

"""totalCount2020 = len([n for n in data if n['year'][:4] == '2020'])
covidCount2020 = len([n for n in data if n['year'][:4] == '2020' and n['is_covid_source'] == True])
notCovidCount2020 = len([n for n in data if n['year'][:4] == '2020' and n['is_covid_source'] == False])
priorProbCovid2020 = covidCount2020 / totalCount2020
priorProbNotCovid2020 = notCovidCount2020 / totalCount2020"""

# TODO FIX
priorProbCovid2020 = 0.25
priorProbNotCovid2020 = 0.75

print("priorProbCovid2020 ", priorProbCovid2020)
print("priorProbNotCovid2020 ", priorProbNotCovid2020)

for outlet in tqdm(OUTLETS):
	outlet_file = read_file_to_json(NORMALIZED_DATA_PATH + outlet)
	for news in outlet_file:
		isCovidScore = 0
		notCovidScore = 0
		for word in news['title_tokens']:
			probCovidTmp = lowestCovidProb if not word in probCovid else probCovid[word]
			probNotCovidTmp = lowestNotCovidProb if not word in probNotCovid else probNotCovid[word]

			isCovidScore += math.log(probCovidTmp)
			notCovidScore += math.log(probNotCovidTmp)
		for word in news['description_tokens']:
			probCovidTmp = lowestCovidProb if not word in probCovid else probCovid[word]
			probNotCovidTmp = lowestNotCovidProb if not word in probNotCovid else probNotCovid[word]

			isCovidScore += math.log(probCovidTmp)
			notCovidScore += math.log(probNotCovidTmp)

		priorProbCovid = 0
		priorProbNotCovid = 0
		if news['date'][:4] == '2019':
			priorProbCovid = math.log(0.0000000000000001)
			priorProbNotCovid = math.log(0.99999999999999)
		else:
			priorProbCovid = math.log(priorProbCovid2020)
			priorProbNotCovid = math.log(priorProbNotCovid2020)
		isCovidScore += priorProbCovid
		notCovidScore += priorProbNotCovid

		if isCovidScore > notCovidScore:
			news['class'] = 'IS COVID'
		else:
			news['class'] = 'NOT COVID'
		news['is_covid_score'] = isCovidScore
		news['not_covid_score'] = notCovidScore

	write_json_to_file(outlet_file, "classification_results/" + outlet)

