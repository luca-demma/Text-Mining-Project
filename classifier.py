import json
from collections import defaultdict

PROB_COVID_PATH = './data/prob_covid.json'
PROB_NOT_COVID_PATH = './data/prob_NOT_covid.json'
NORMALIZED_DATA_PATH = './data/normalized_data.json'

print('READING DATA FROM FILE ...')
file = open(PROB_COVID_PATH)
probCovid = json.load(file)
file = open(PROB_NOT_COVID_PATH)
probNotCovid = json.load(file)
file = open(NORMALIZED_DATA_PATH)
data = json.load(file)
print('READING DATA FROM FILE COMPLETED !')

classificationResults = {}

lowestCovidProb = probCovid[list(probCovid)[-1]]
lowestNotCovidProb = probNotCovid[list(probNotCovid)[-1]]

for news in data:
	isCovidScore = 1
	notCovidScore = 1
	for word in news['title_tokens']:
		probCovidTmp = lowestCovidProb if not word in probCovid else probCovid[word]
		probNotCovidTmp = lowestNotCovidProb if not word in probNotCovid else probNotCovid[word]

		isCovidScore *= probCovidTmp
		notCovidScore *= probNotCovidTmp
	if isCovidScore > notCovidScore:
		news['class'] = 'IS COVID'
	else:
		news['class'] = 'NOT COVID'


# writing on file
outFile = open('./data/classification_results.json', 'w')
json.dump(data, outFile, indent=4)
outFile.close()
