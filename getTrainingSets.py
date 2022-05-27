import json
import os
from tqdm import tqdm
from fileActions import read_file_to_json, write_json_to_file
import multiprocessing
from pqdm.processes import pqdm

NUM_CORES = multiprocessing.cpu_count()

NORMALIZED_DATA_PATH = './data/normalized_data/'
OUTLETS = sorted(os.listdir(NORMALIZED_DATA_PATH))


def is_covid(news):
	if 'covid-19' in news['title_tokens'] or 'covid-19' in news['description_tokens'] or 'coronavirus' in news['title_tokens'] or 'coronavirus' in news['description_tokens']:
		return True
	else:
		return False


def is_not_covid(news):
	if int(news['date'][:4]) <= 2019:
		return True
	else:
		return False


def get_training_sets(outlet):
	isCovidTraining = []
	isNotCovidTraining = []
	outlet_file = read_file_to_json(NORMALIZED_DATA_PATH + outlet)
	for news in outlet_file:
		if is_covid(news):
			isCovidTraining.append(news)
		elif is_not_covid(news):
			isNotCovidTraining.append(news)
	write_json_to_file(isCovidTraining, "training_covid/" + outlet)
	write_json_to_file(isNotCovidTraining, "training_NOT_covid/" + outlet)


# multiprocessing
pqdm(OUTLETS, get_training_sets, n_jobs=NUM_CORES)
