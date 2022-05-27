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
-   **tokenization** : using *nltk.tokenize.word_tokenize* that uses the NLTK's reccomended tokenizer to split a sentence in tokens. Internally it uses a series of regular expressions to split the tokens by white spaces and punctuations.
-   **removing punctuations** : using Python list comprehensions to remove all the tokens that contain punctuations. For this I'm using the Python built-in function `isalnum()` that returns true if a string contains only alphanumeric characters, I added a condition to not remove the occurrences of *'covid-19'*.
    ```python
    [token for token in tokens_list if (token.isalnum() or token == "covid-19")]
    ```

-   **lemmatization** : using WordNet corpus lemmatizer WordNetLemmatizer to lemmatize the tokens got in the previous step. I choose to lemmatize instead of stemming because stemming is not so efficient due to the fact that tends to stem to unwanted words.
-   **removing stopwords** : stop words are commonly used words that occure frenquently and usually don't provide additional information. For doing this I used the NLTK corpus *stopwords* that contains a list of stopwords in 11 languages. 
    
    This is the list for english *(Taken from: [https://www.nltk.org/book/ch02.html](https://www.nltk.org/book/ch02.html))*:
    ```python
    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    ```
    and I used this list comprehions command to check if a token is included in the list to remove it:
    ```python
    [token for token in tokens_list if not token in stop_words]
    ```



## Step 3 : Classification
To classify the news articles I used the normalized data produced in the previous step to implement a Naive Bayes classifier from scratch.

A Naive Bayes classifier is a supervised learning algorithm which is based on Bayes Theorem. It's a probabilistic classifier because choses the class of an input based of a probability of its features.

Bayes Theorem formula: ![Bayes Theorem formula](https://miro.medium.com/max/1020/1*tjcmj9cDQ-rHXAtxCu5bRQ.png)

Where:

- P(A|B) is Posterior probability
- P(B|A) is Likelihood probability
- P(A) is Prior Probability:
- P(B) is Marginal Probability

### Getting the training sets
To use the formula for the text classification problem we need to calculate the probabilities that each word has in covid and non covid articles. To do so two training sets are needed for the training, the TRUE training set and the FALSE one, that rappresent respectively the set of articles that are covid related and the one that is not.

To get the training set I wrote a script `getTrainingSets.py` where i divide the normalized articles data in the TRUE and FALSE set. 

In the FALSE set I used the articles written before 2020 because covid was still undected and for the TRUE set I used the articles that contain in the title or in the description the keywords *covid-19* or *coronavirus*.

The training sets have been saved respectively in `./data/training_covid` and `./data/training_NOT_covid`

### Getting the words probabilities
Having the FALSE and TRUE training sets I can loop on them to calculate the frequencies of the words occurencies and from them calculate the probability for each word using `frequency.py`

I'm using a Python default_dict data structure to ease the process of creating the dictionary to save the words frequencies and probabilities.

I chose to treat in the same way the words found in the title and the ones found in the description. 

Having the words frequency I calculate the probability of each word for the both sets (diving the frequency of the word by the sum of all the occurences): 

```python
for word in tqdm(isCovidFreq):
    isCovidProb[word] = isCovidFreq[word] / isCovidWordsLength
```

in this way I get the most commond words in covid news and non covid saved in `./data/prob_covid.json` and `./data/prob_NOT_covid.json`.

The most 20 common words for covid news:
```json
"coronavirus": 0.043835909923861924,
"covid-19": 0.015808012474694544,
"news": 0.010715819839904057,
"ha": 0.009922155787593942,
"new": 0.008365884681941676,
"pandemic": 0.008240723643182362,
"case": 0.006377259274490732,
"time": 0.005009907138240168,
"say": 0.004845602728821659,
"trump": 0.004683742003155996,
"people": 0.004504464476924605,
"lockdown": 0.004464077049082143,
"health": 0.004126004509529567,
"outbreak": 0.0041117867131493825,
"wa": 0.0039550355080578475,
"death": 0.0037163542513254984,
"said": 0.003695160848596286,
"world": 0.0035532938990902566,
"state": 0.0033374499777935793,
"online": 0.003325098267188294,
```

The most 20 common words for NON covid news:
```json
"news": 0.010683131939110142,
"ha": 0.008041611622448533,
"wa": 0.006844409412116912,
"new": 0.006049156914812433,
"time": 0.005171104253908384,
"online": 0.005122369938670393,
"trump": 0.004485226975135559,
"daily": 0.003886308735628415,
"say": 0.0037605308472398883,
"year": 0.0036743987658769293,
"mail": 0.0034204825461542467,
"star": 0.0031140344278150615,
"one": 0.002730815712720413,
"said": 0.0027005474477373444,
"world": 0.002651965678131895,
"video": 0.0026342061550171606,
"president": 0.0026308260649487596,
"first": 0.002223248220952618,
"day": 0.002182060900166639,
"woman": 0.002161523440796165,
```

### Classification




## Step 4 : Classification Accuracy Verification

## Step 5 : Analysis

# Conclusions