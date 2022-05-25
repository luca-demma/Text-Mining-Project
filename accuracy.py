from fileActions import read_file_to_json
from tqdm import tqdm

CLASSIFIED_DATA_PATH = './data/classification_results.json'

classified_data = read_file_to_json(CLASSIFIED_DATA_PATH)

tp = 0
tn = 0
fp = 0
fn = 0

for news in tqdm(classified_data):
	if news['is_covid_source'] == True and news['class'] == 'IS COVID':
		tp += 1
	elif news['is_covid_source'] == False and news['class'] == 'NOT COVID':
		tn += 1
	elif news['is_covid_source'] == False and news['class'] == 'IS COVID':
		fp += 1
	elif news['is_covid_source'] == True and news['class'] == 'NOT COVID':
		fn += 1
	else:
		print("Error in getting news type; news['is_covid_source']: ", news['is_covid_source'], "; news['class']: ", news['class'])

print("Results: \nTP: ", tp, "\nTN: ", tn, "\nFP: ", fp, "\nFN: ", fn)

precision = tp / (tp + fp)
recall = tp / (tp + fn)
accuracy = (tn + tp) / (tn + tp + fn + fp)

print("Precision: ", precision, "\nRecall: ", recall, "\nAccuracy: ", accuracy)
