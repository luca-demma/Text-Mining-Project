from fileActions import read_file_to_json, write_json_to_file
from tqdm import tqdm
import os

CLASSIFIED_DATA_PATH = './data/classification_results/'
OUTLETS = sorted(os.listdir(CLASSIFIED_DATA_PATH))

total_news_2020 = 0
count_covid_news_2020 = 0

# how many covid-19 news as proportion of all articles in 2020
for outlet in tqdm(OUTLETS):
	outlet_file = read_file_to_json(CLASSIFIED_DATA_PATH + outlet)
	for news in outlet_file:
		if news['date'][:4] == "2020":
			total_news_2020 += 1
			if news['class'] == "IS COVID":
				count_covid_news_2020 += 1


percentage_covid_news_2020 = count_covid_news_2020 * 100 / total_news_2020

results = {
	'total_2020': total_news_2020,
	'covid_2020': count_covid_news_2020,
	'percentage_2020': percentage_covid_news_2020
}
print("2020\n", results)

write_json_to_file(results, "analysis/perc_2020.json")


# how many covid-19 news as proportion of all articles in each month of 2020
months = range(1, 11)  # months in data go from january (01) to october (10)
results = {}
for month in tqdm(months):
	total_month_news = 0
	count_covid_month_news = 0
	for outlet in OUTLETS:
		outlet_file = read_file_to_json(CLASSIFIED_DATA_PATH + outlet)
		for news in outlet_file:
			if news['date'][:4] == "2020" and int(news['date'][4:6]) == month:
				total_month_news += 1
				if news['class'] == "IS COVID":
					count_covid_month_news += 1

	percentage_covid_month_news = count_covid_month_news * 100 / total_month_news

	results[month] = {
		'total': total_month_news,
		'covid': count_covid_month_news,
		'percentage ': percentage_covid_month_news
	}


print("MONTHS\n", results)
write_json_to_file(results, "analysis/perc_months_2020.json")


# how many covid-19 news as proportion of all articles for each outlet
results = {}
for outlet in OUTLETS:
	total_outlet_news = 0
	count_covid_outlet_news = 0

	outlet_file = read_file_to_json(CLASSIFIED_DATA_PATH + outlet)
	for news in outlet_file:
		total_outlet_news += 1
		if news['class'] == 'IS COVID':
			count_covid_outlet_news += 1

		percentage_covid_outlet_news = count_covid_outlet_news * 100 / total_outlet_news

		results[outlet] = {
			'total': total_outlet_news,
			'covid': count_covid_outlet_news,
			'percentage ': percentage_covid_outlet_news
		}

print("OUTLETS\n", results)
write_json_to_file(results, "analysis/perc_outlets.json")
