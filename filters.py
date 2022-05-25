from fileActions import read_file_to_json
from tqdm import tqdm

CLASSIFIED_DATA_PATH = './data/classification_results.json'

classified_data = read_file_to_json(CLASSIFIED_DATA_PATH)

# how many covid-19 news as proportion of all articles in 2020
news_list_2020 = [n for n in classified_data if n['date'][:4] == "2020"]
total_news_2020 = len(news_list_2020)

covid_news_list_2020 = [n for n in news_list_2020 if n['class'] == "IS COVID"]
count_covid_news_2020 = len(covid_news_list_2020)

percentage_covid_news_2020 = count_covid_news_2020 * 100 / total_news_2020

print("Total news 2020: ", total_news_2020)
print("Covid-19 news count 2020: ", count_covid_news_2020)
print("Percentage of covid news in 2020: ", percentage_covid_news_2020, "%\n")

# how many covid-19 news as proportion of all articles in each month of 2020
months = range(1, 11)  # months in data go from january (01) to october (10)
for month in months:
	month_news = [n for n in news_list_2020 if int(n['date'][4:6]) == month]
	total_month_news = len(month_news)

	covid_month_news_list = [n for n in month_news if n['class'] == "IS COVID"]
	count_covid_month_news = len(covid_month_news_list)

	percentage_covid_month_news = count_covid_month_news * 100 / total_month_news

	print("Total news month: ", month, " : ", total_month_news)
	print("Covid-19 news count month: ", month, " : ", count_covid_month_news)
	print("Percentage of covid news in month: ", month, " : ", percentage_covid_month_news, "%\n")
