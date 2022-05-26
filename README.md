# Report for the project-based exam for DM882: Text Mining
## Option 1 : News Articles
### Luca Demma
---
## Introduction
The goal of this project is to implement a Natural Language Processing (NLP) pipeline to classify news articles taken from the front pages of 172 outlets in 11 countries using the semi-structured data source made by this project [http://sciride.org/news.html](http://sciride.org/news.html) , data used is present at this link provided by the teacher [https://news-mine.s3.eu-west-2.amazonaws.com/processed.tar.gz](https://news-mine.s3.eu-west-2.amazonaws.com/processed.tar.gz).

The implementation of the pipeline should provide 3 types of results:

-   **Text classification** starting from natural language text and the formal calculation of its accuracy
-   Based on the text classification execute data analysis to get **insights** from the data to get the proportion of articles on COVID-19, more specifically:

    - How many COVID-19 news have been issued as proportion of all articles in 2020
    - How many COVID-19 news have been issued as proportion of all articles in each month of 2020
    - How many COVID-19 news have been issued as proportion of articles in an outlet (e.g. CNN) in 2020

-   Getting the most commonly mentioned Named Entities in COVID-19 news doing Named Entity Recognition (NER)

For the implementation I used the python programming language because is the most used language for NLP and there are a lot of libraries easily importable as the ones I used:
-   **NLTK** *([https://www.nltk.org/](https://www.nltk.org/))* and its modules:
    -   word_tokenize
    -   WordNetLemmatizer
    -   pos_tag
    -   ne_chunk
    -   stopwords
    -   punkt
-   **contractions**

## Pipeline
![Pipeline](./report_pics/Text%20Mining%20Pipeline.drawio.svg)