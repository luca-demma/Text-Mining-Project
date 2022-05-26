import json
import os
from collections import defaultdict
from fileActions import read_file_to_json, write_json_to_file
from tqdm import tqdm

COVID_TRUE_PATH = './data/training_covid/'
COVID_FALSE_PATH = './data/training_NOT_covid/'
OUTLETS_TRUE = sorted(os.listdir(COVID_TRUE_PATH))
OUTLETS_FALSE = sorted(os.listdir(COVID_FALSE_PATH))


def def_value(): return 0


isCovidFreq = defaultdict(def_value)
notCovidFreq = defaultdict(def_value)

print("STEP 1/4")
for outlet in tqdm(OUTLETS_TRUE):
	outlet_file = read_file_to_json(COVID_TRUE_PATH + outlet)
	for news in outlet_file:
		for word in news['title_tokens']:
			isCovidFreq[word] += 1
		for word in news['description_tokens']:
			isCovidFreq[word] += 1

print("STEP 2/4")
for outlet in tqdm(OUTLETS_FALSE):
	outlet_file = read_file_to_json(COVID_FALSE_PATH + outlet)
	for news in outlet_file:
		for word in news['title_tokens']:
			notCovidFreq[word] += 1
		for word in news['description_tokens']:
			notCovidFreq[word] += 1

# ordering dicts
isCovidFreq = {key: value for key, value in sorted(isCovidFreq.items(), key=lambda item: item[1], reverse=True)}
notCovidFreq = {key: value for key, value in sorted(notCovidFreq.items(), key=lambda item: item[1], reverse=True)}

# writing on file
write_json_to_file(isCovidFreq, "frequency_covid.json")
write_json_to_file(notCovidFreq, "frequency_NOT_covid.json")

# probabilities
isCovidProb = {}
notCovidProb = {}

"""isCovidWordsLength = len(isCovidFreq)
notCovidWordsLength = len(notCovidFreq)"""
isCovidWordsLength = sum(isCovidFreq.values())
notCovidWordsLength = sum(notCovidFreq.values())

print("STEP 3/4")
for word in tqdm(isCovidFreq):
	isCovidProb[word] = isCovidFreq[word] / isCovidWordsLength

print("STEP 4/4")
for word in tqdm(notCovidFreq):
	notCovidProb[word] = notCovidFreq[word] / notCovidWordsLength

# ordering dicts
isCovidProb = {key: value for key, value in sorted(isCovidProb.items(), key=lambda item: item[1], reverse=True)}
notCovidProb = {key: value for key, value in sorted(notCovidProb.items(), key=lambda item: item[1], reverse=True)}

# writing on file
write_json_to_file(isCovidProb, "prob_covid.json")
write_json_to_file(notCovidProb, "prob_NOT_covid.json")
