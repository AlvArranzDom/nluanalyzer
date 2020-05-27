#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Alvaro Arranz"
__copyright__ = "Copyright 2020, Alvaro Arranz"

import re
import time
import json
import spacy
import logging
import unicodedata
import numpy as np
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

XLSX_SUFFIX = ".xlsx"
NLP = spacy.load("es")
STOPWORDS = stopwords.words('spanish')


class NLUAnalyzer:
    logging.basicConfig()
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)

    def __init__(self, input_path):
        """
            In this script we generate several summary, each one of an transcript. With the txt files we get the
            necessary files to identify structures, verbs or nouns.

            :param input_path: CSV File with all the Utterances.
            :type input_path: str
        """
        date = time.strftime("%x").replace("/", "-")

        if XLSX_SUFFIX not in input_path:
            self.utterances_path = input_path + ".xlsx"
            self.results_path = input_path + "_analyzed.xlsx"
        else:
            self.utterances_path = input_path
            self.results_path = input_path.replace(".xlsx", "") + "_" + date + "_analyzed.csv"

    def __execute__(self):
        """ In this function we iterate all the sheets analyzing the information. """

        utterances_df = pd.read_excel(self.utterances_path)
        utterances_df = utterances_df.replace(np.nan, '', regex=True)

        analysis_dict = {}

        for idx, intent in enumerate(utterances_df.head()):
            utters = []
            cleaned_utters = []

            for utter in utterances_df.iloc[:, idx]:
                if utter != "":
                    utters.append(utter)
                    cleaned_utter = self.__clean_sentence(utter)
                    cleaned_utters.append(cleaned_utter)

            analysis_dict[intent] = {
                "utters": {
                    "raw": utters,
                    "clean": cleaned_utters
                },
                "pos_tokens": self.__count_pos_tokens(cleaned_utters),
                "ngrams": self.__count_vectorizer(cleaned_utters)
            }

        with open('self.results_path', 'w') as outfile:
            json.dump(analysis_dict, outfile)

        logging.info(f"Successfully saved intents analyzed file in {self.results_path}")

    @staticmethod
    def __strip_accents(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

    def __clean_sentence(self, sentence):
        # tokenizer = nltk.RegexpTokenizer(r"\w+")
        cleaned_sentence = self.__strip_accents(sentence.lower())
        cleaned_sentence = re.sub('[^a-z]+', ' ', cleaned_sentence)
        cleaned_words = cleaned_sentence.split(" ")
        # cleaned_words = [word for word in cleaned_words if word not in STOPWORDS and word != ""]

        return ' '.join(cleaned_words)

    def __count_vectorizer(self, utters):
        grams_1 = CountVectorizer(ngram_range=(1, 1)).fit(utters, 1).get_feature_names()
        grams_2 = CountVectorizer(ngram_range=(2, 2)).fit(utters, 2).get_feature_names()
        grams_3 = CountVectorizer(ngram_range=(3, 3)).fit(utters, 3).get_feature_names()
        grams_4 = CountVectorizer(ngram_range=(4, 4)).fit(utters, 4).get_feature_names()

        count_grams_1 = []
        count_grams_2 = []
        count_grams_3 = []
        count_grams_4 = []

        for utter in utters:
            count_grams_1 = self.__count_ngrams(utter, grams_1)
            count_grams_2 = self.__count_ngrams(utter, grams_2)
            count_grams_3 = self.__count_ngrams(utter, grams_3)
            count_grams_4 = self.__count_ngrams(utter, grams_4)

        return {
            "size_1": dict(Counter(count_grams_1)),
            "size_2": dict(Counter(count_grams_2)),
            "size_3": dict(Counter(count_grams_3)),
            "size_4": dict(Counter(count_grams_4))
        }

    @staticmethod
    def __count_ngrams(utter, grams):
        count_grams = []

        for gram in grams:
            if gram in utter:
                count_grams.append(gram)

        return count_grams

    @staticmethod
    def __count_pos_tokens(utters):
        verbs_conj = []
        verbs_lemma = []
        nouns = []
        adjectives = []

        for utter in utters:
            doc = NLP(utter)
            for token in doc:
                if str(token.pos_) == "VERB" or str(token.pos_) == "AUX":
                    verbs_conj.append(token.text)
                    verbs_lemma.append(token.lemma_)

                if str(token.pos_) == "NOUN":
                    nouns.append(token.text)

                if str(token.pos_) == "ADJ":
                    adjectives.append(token.text)

        return {
            "nouns": dict(Counter(nouns)),
            "adjectives": dict(Counter(adjectives)),
            "verbs": {
                "conjugations": dict(Counter(verbs_conj)),
                "lemma": dict(Counter(verbs_lemma))
            }
        }
