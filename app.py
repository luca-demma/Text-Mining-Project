import json
import os

RESOURCE_PATH = '/home/luca/UNI/Text Mining/processed/release/'
NEWSPAPERS = sorted(os.listdir(RESOURCE_PATH))

resourceStructured = []

for newspaper in NEWSPAPERS:
	currentNewspaperPath = RESOURCE_PATH + newspaper + '/per_day/'
	print("Extracting: " + newspaper)
	for day in sorted(os.listdir(currentNewspaperPath)):
		dayFile = open(currentNewspaperPath + day)
		dayData = json.load(dayFile)
		for singleNewsId in dayData:
			resourceStructured.append({
				'newspaper': newspaper,
				'date': day,
				'year': day[:4],
				'title': dayData[singleNewsId]['title'],
				'description': dayData[singleNewsId]['description']
			})

outFile = open('./data/structured_resource.json', 'w')
json.dump(resourceStructured, outFile, indent=4)
outFile.close()

"""
structuredDataJsonString = json.dumps(resourceStructured, indent=4)

with open('./data/structured_resource.json', 'w') as outfile:
	outfile.write(structuredDataJsonString)
"""