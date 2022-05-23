import json
from tqdm import tqdm
from fileActions import read_file_to_json, write_json_to_file

NORMALIZED_DATA_PATH = './data/normalized_data.json'

data = read_file_to_json(NORMALIZED_DATA_PATH)

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


print("STARTING PROCESSING ...")

for news in tqdm(data):
	if is_covid(news):
		isCovidTraining.append(news)
	elif is_not_covid(news):
		isNotCovidTraining.append(news)

print('covid news count:' + str(len(isCovidTraining)))
print('NOT covid news count:' + str(len(isNotCovidTraining)))

write_json_to_file(isCovidTraining, "training_covid.json")
write_json_to_file(isNotCovidTraining, "training_NOT_covid.json")
