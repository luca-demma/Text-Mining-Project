import json

NORMALIZED_DATA_PATH = './data/normalized_data.json'

print('READING DATA FROM FILE ...')
file = open(NORMALIZED_DATA_PATH)
data = json.load(file)
print('READING DATA FROM FILE COMPLETED !')

isCovidTraining = []
isNotCovidTraining = []


def is_covid(news):
	if 'covid-19' in news['title_tokens'] or 'covid-19' in news['description_tokens'] or 'coronavirus' in news['title_tokens'] or 'coronavirus' in news['description_tokens']:
		return True
	else:
		return False


def is_not_covid(news):
	if int(news['year']) <= 2019:
		return True
	else:
		return False


for news in data:
	if is_covid(news):
		isCovidTraining.append(news)
	elif is_not_covid(news):
		isNotCovidTraining.append(news)

print('covid news count:' + str(len(isCovidTraining)))
print('NOT covid news count:' + str(len(isNotCovidTraining)))


outFile = open('./data/training_covid.json', 'w')
json.dump(isCovidTraining, outFile, indent=4)
outFile.close()

outFile = open('./data/training_NOT_covid.json', 'w')
json.dump(isNotCovidTraining, outFile, indent=4)
outFile.close()
