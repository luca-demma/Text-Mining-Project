import json
from collections import defaultdict

COVID_TRUE_PATH = './data/training_covid.json'
COVID_FALSE_PATH = './data/training_NOT_covid.json'

print('READING DATA FROM FILE ...')
file = open(COVID_TRUE_PATH)
isCovid = json.load(file)
file = open(COVID_FALSE_PATH)
notCovid = json.load(file)
print('READING DATA FROM FILE COMPLETED !')


def def_value(): return 0


isCovidFreq = defaultdict(def_value)
notCovidFreq = defaultdict(def_value)

for news in isCovid:
	for word in news['title_tokens']:
		isCovidFreq[word] += 1
	for word in news['description_tokens']:
		isCovidFreq[word] += 1

for news in notCovid:
	for word in news['title_tokens']:
		notCovidFreq[word] += 1
	for word in news['description_tokens']:
		notCovidFreq[word] += 1

# ordering dicts
isCovidFreq = {key: value for key, value in sorted(isCovidFreq.items(), key=lambda item: item[1], reverse=True)}
notCovidFreq = {key: value for key, value in sorted(notCovidFreq.items(), key=lambda item: item[1], reverse=True)}


# writing on file
outFile = open('./data/frequency_covid.json', 'w')
json.dump(isCovidFreq, outFile, indent=4)
outFile.close()

outFile = open('./data/frequency_NOT_covid.json', 'w')
json.dump(notCovidFreq, outFile, indent=4)
outFile.close()


# probabilities

isCovidProb = {}
notCovidProb = {}

isCovidWordsLength = len(isCovidFreq)
notCovidWordsLength = len(notCovidFreq)

for word in isCovidFreq:
	isCovidProb[word] = isCovidFreq[word] / isCovidWordsLength

for word in notCovidFreq:
	notCovidProb[word] = notCovidFreq[word] / notCovidWordsLength

# ordering dicts
isCovidProb = {key: value for key, value in sorted(isCovidProb.items(), key=lambda item: item[1], reverse=True)}
notCovidProb = {key: value for key, value in sorted(notCovidProb.items(), key=lambda item: item[1], reverse=True)}

# writing on file
outFile = open('./data/prob_covid.json', 'w')
json.dump(isCovidProb, outFile, indent=4)
outFile.close()

outFile = open('./data/prob_NOT_covid.json', 'w')
json.dump(notCovidProb, outFile, indent=4)
outFile.close()
