# Report for the project-based exam for DM882: Text Mining
## Option 1 : News Articles
### Luca Demma

---

# Introduction
The goal of this project is to implement a Natural Language Processing (NLP) pipeline to classify news articles taken from the front pages of 172 outlets in 11 countries using the semi-structured data source made by this project [http://sciride.org/news.html](http://sciride.org/news.html) , data used is present at this link provided by the teacher [https://news-mine.s3.eu-west-2.amazonaws.com/processed.tar.gz](https://news-mine.s3.eu-west-2.amazonaws.com/processed.tar.gz).

The implementation of the pipeline should provide 3 types of results:

-   **Text classification** starting from natural language text and the formal calculation of its accuracy
-   Based on the text classification execute data analysis to get **insights** from the data to get the proportion of articles on COVID-19, more specifically:

    - How many COVID-19 news have been issued as proportion of all articles in 2020
    - How many COVID-19 news have been issued as proportion of all articles in each month of 2020
    - How many COVID-19 news have been issued as proportion of articles in an outlet (e.g. CNN) in 2020

-   Getting the most commonly mentioned Named Entities in COVID-19 news doing Named Entity Recognition (NER)

For the implementation I used the Python programming language because is the most used language for NLP and there are a lot of libraries easily importable as the ones I used:
-   **NLTK** *([https://www.nltk.org/](https://www.nltk.org/))* and its modules:
    -   *word_tokenize*
    -   *WordNetLemmatizer*
    -   *pos_tag*
    -   *ne_chunk*
    -   *stopwords*
    -   *punkt*
-   **contractions**

Having to deal with huge quantity of data I chose to implement most of the scripts in a multi-process way using the power of the parallelism. This has been possible mainly because the majority of the operations are parallelizable not handling sequetial data. Using this technique permites to speed up the whole process up to 8 times in modern computers with multiple CPUs. To implement multiprocessing I used the Python module *pqdm*.

---

# Pipeline

The following picture describes the pipeline of the processing implemented by the code divided in 6 macro steps:
-   File cleaning
-   Extraction
-   Normalization
-   Classification
-   Classification accuracy
-   Analysis

![Pipeline](./report_pics/Text%20Mining%20Pipeline.drawio.svg)

Each step saves in the its output result in the `data` folder in the json format. For the steps that have as output big quantity of data it has been chosen to split the results in sub-files for each news outlet to avoid problems related to out-of-memory.

## Step 0 : File cleaning
The first step is related to file cleaning and preparation, in this step I started to clean the source data and to make it easily consumable by the Python implentation of the pipeline.

To do so I followed the following actions:

### Removing old articles
Removing of all the articles issued before the 2019, as stated in the project description to handle a reasonable count of news we use only the 2019 and 2020 ones. 

To do so I run a simple bash command that finds all the files name that don't start with `2019` and `2020`:

```bash
find . -type f ! -name '2019*' -and ! -name '2020*' -delete
```

### Unzipping all the files
To speed up and make the processing easier I choose to pre-decompress all the files present in the .gzip format.

To do so I used a simple bash command to decompress all the files found in the folders recursively

```bash
gunzip -rv .
```

### Remove all the non english news outlets
My implementation is based on the handle of just a single language of news, for this reason in this step I'm gonna remove from the news outlets list all the outlets that are not in english language.

To do so I wrote a Python script `english.py` that uses the file provided by the teacher `AvailableOutlets.txt` to delete all the folders that use non english language. After this removal the news outlets became 91.

After this steps the data has been prepared to be consumed by the pipeline in a more convient way.

## Step 1 : Extraction
In this step I aim to clean the data source from all the unnecessary fields and to give a structure that can make it easier the handling.

I had to think how to handle all the data to avoid out-of-memory problems because my first thought has been to save every cleaned news data in a single json file but this idea fastly showed its limitations because of the data size related problems, the python script was often crashing when creating the huge single json file with out-of-memory error.

For this reason I chose to handle the data by steps for every outlet, this required some more reasoning but it made possible the handling of the huge data source.

My goal here was to strip down the input data giving a structure, to do this I use a Python script `extractor.py` where I read all the articles for each outlet and I keep only the following fields in the following json format:

```json
{
    "newspaper": "abcnews.go.com",
    "date": "20190101",
    "title": "Shutdown talks broken between...",
    "description": "As the government shutdown en...",
    "is_covid_source": false  // comes from the source, keyword based
}
```

I save all the article in the format shown previously in an array of objects in `./data/structured_resource/outlet_name` where *outlet_name* is the file name of the json rapresented by the outlet name e.g. *abcnews.go.com*

In this script I used multiprocessing to speed up considerably the execution speed.

## Step 2 : Normalization
This step is crucial to transform natural language in a structured data source that can be handled by a software.

In my pipeline I used the following normalization techniques for titles and descriptions in the following order (implementation in `normalizer.py` file):
-   **to lower case** : transforming the texts to lower case to make easier matching for the same words with different casing
-   **expanding contractions** : expanding the english language contractions (e.g. I'm -> I am). I used the the module [contractions](https://github.com/kootenpv/contractions)
-   **tokenization** : 
-   **removing punctuations** :
-   **lemmatization** :
-   **removing stopwords** :

## Step 3 : Classification

## Step 4 : Classification Accuracy Verification

## Step 5 : Analysis

# Conclusions