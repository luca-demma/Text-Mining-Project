import json
import os
from fileActions import write_json_to_file
from pqdm.processes import pqdm
import multiprocessing

NUM_CORES = multiprocessing.cpu_count()

# where is the source data
RESOURCE_PATH = '/home/luca/UNI/Text Mining/processed/release/'
OUTLETS = sorted(os.listdir(RESOURCE_PATH))


def extract(outlet):
	resourceStructured = []
	currentNewspaperPath = RESOURCE_PATH + outlet + '/per_day/'
	for day in sorted(os.listdir(currentNewspaperPath)):
		dayFile = open(currentNewspaperPath + day)
		dayData = json.load(dayFile)
		for singleNewsId in dayData:
			resourceStructured.append({
				'newspaper': outlet,
				'date': day,
				'title': dayData[singleNewsId]['title'],
				'description': dayData[singleNewsId]['description'],
				'is_covid_source': dayData[singleNewsId]['is_covid']
			})
	write_json_to_file(resourceStructured, "structured_resource/" + outlet)


# multiprocessing
pqdm(OUTLETS, extract, n_jobs=NUM_CORES)
