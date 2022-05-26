from fileActions import read_file_to_json, write_json_to_file
from tqdm import tqdm
import os

CLASSIFIED_DATA_PATH = './data/classification_results/'
OUTLETS = sorted(os.listdir(CLASSIFIED_DATA_PATH))

tp = 0
tn = 0
fp = 0
fn = 0

for outlet in tqdm(OUTLETS):
	outlet_file = read_file_to_json(CLASSIFIED_DATA_PATH + outlet)
	for news in outlet_file:
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


precision = tp / (tp + fp)
recall = tp / (tp + fn)
accuracy = (tn + tp) / (tn + tp + fn + fp)


results = {
	'accuracy_results': {
		'raw': {
			'TP': tp,
			'TN': tn,
			'FP': fp,
			'FN': fn
		},
		'precision': precision,
		'recall': recall,
		'accuracy': accuracy
	}
}

print(results)

write_json_to_file(results, "accuracy_results.json")

