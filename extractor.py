import json
import os
from fileActions import write_json_to_file
from tqdm import tqdm

RESOURCE_PATH = '/home/luca/UNI/Text Mining/processed/release/'
NEWSPAPERS = sorted(os.listdir(RESOURCE_PATH))

resourceStructured = []

for newspaper in tqdm(NEWSPAPERS):
	currentNewspaperPath = RESOURCE_PATH + newspaper + '/per_day/'
	tqdm.write("Extracting: " + newspaper)
	for day in sorted(os.listdir(currentNewspaperPath)):
		dayFile = open(currentNewspaperPath + day)
		dayData = json.load(dayFile)
		for singleNewsId in dayData:
			resourceStructured.append({
				'newspaper': newspaper,
				'date': day,
				'year': day[:4],
				'title': dayData[singleNewsId]['title'],
				'description': dayData[singleNewsId]['description'],
				'is_covid_source': dayData[singleNewsId]['is_covid']
			})

write_json_to_file(resourceStructured, "structured_resource.json")
