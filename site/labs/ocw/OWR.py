# coding: utf-8

# # Representation

# In[1]:

import pandas as pd
import numpy as np

# ### OCR Factor $\psi_o$
# 
# These factors capture the predictions of a character-based OCR system, and hence exist between every image variable and its corresponding character variable. The number of these factors of word w is $len(w)$. The value of factor between an image variable and the character variable at position i is dependent on $img(i)$ and $char(i)$
# 
# $$\psi_o (img(i)=id,char(i)=a) = prob$$

# In[2]:

ocr_table_factor = pd.read_table("dataset/ocr.dat", names=["id", "character", "p"], index_col=["id", "character"])
ocr_table_factor


# In[3]:

def flat(X):
    return [item for sublist in X for item in sublist]


def ocr_factor(X):
    """ocr factor
    
    :type X: list of list
    :param list X: list of assignments for each sentence
    :return the probability of factor
    """
    X = flat(X)
    return np.exp(np.sum(np.log([ocr_table_factor.ix[item["img"], item["char"]]["p"] for item in X])))


# ### Transition Factors $\psi_t$
# 
# Since we also want to represent the co-occurence frequencies of the characters in our model, we add these factors between all consecutive character variables. The number of these factors of word $w$ is $len(w)-1$. The value of factor between two character variables at positions $i$ and $i+1$ is dependent on $char(i)$ and $char(i+1)$, and is high if $char(i+1)$ is frequently preceded by $char(i)$ in english words
# 
# $$\psi_t(char(i)=a, char(i+1)=b) = prob$$

# In[4]:

transition_table_factor = pd.read_table("dataset/trans.dat", names=["current", "next", "p"],
                                        index_col=["current", "next"])
transition_table_factor


# In[5]:

def trans_factor(X):
    """trans factor
    
    :type X: list of list
    :param list X: list of assignments for each sentence
    
    :return the probability of factor
    """
    p = [trans_factor_sentence(s) for s in X]
    return np.exp(np.sum(np.log(p)))


def trans_factor_sentence(X):
    """trans factor
    
    :type X: list of list
    :param list X: list of assignments for each sentence
    
    :return the probability of factor
    """
    return np.exp(
        np.sum(np.log([transition_table_factor.ix[X[i]["char"], X[i + 1]["char"]]["p"] for i in range(0, len(X) - 1)])))


# ### Skip Factors $\psi_s$
# 
# We would like to capture in our model is that similar images in a word always represent the same character. Thus our model score should be higher if it predicts the same characters for similar images. These factors exist between every pair of image variables that have the same id, i.e. this factor exist between all $i$,$j$, $i \ne j$ such that $img(i)==img(j)$. The value of this factor depends on $char(i)$ and $char(j)$, and is $5.0$ if $char(i)==char(j)$, and $1.0$ otherwise.

# In[6]:

import itertools


def skip_factor(X):
    """trans factor
    
    :type X: list of dictionary
    :param list X: list of assignment 
    
    :return the probability of factor
    """
    X = flat(X)
    result = 1
    pairs = itertools.combinations(X, 2)
    for i, j in pairs:
        if i['img'] == j['img'] and i["char"] == j["char"]:
            result = result * 5
    return result


# In[7]:

class Model:
    def __init__(self, factors=None):
        self.factors = factors

    def score(self, X):
        p = [factor(X) for factor in self.factors]
        return np.exp(np.sum(np.log(p)))

    @staticmethod
    def make_assignment(list_char, word_image):
        return [[{"char": a[0], "img": a[1]} for a in zip(list_char, word_image)]]

    def predict(self, word_image):
        chars = "etaoinshrd"
        assignments = list(itertools.product(chars, repeat=len(word_image)))
        assignments = [self.make_assignment(list_char, word_image) for list_char in assignments]
        scores = [(assignment, self.score(assignment)) for assignment in assignments]
        best = max(scores, key=lambda score: score[1])
        return best


# In[8]:

model_1 = Model(factors=[ocr_factor])
model_2 = Model(factors=[ocr_factor, trans_factor])
model_3 = Model(factors=[ocr_factor, trans_factor, skip_factor])

# X = [[int(t) for t in s.split()] for s in open("dataset/data_small.dat", "r").readlines()]
# Y = [model_1.predict(x) for x in X]
# Y = ["".join([item['char'] for item in y[0][0]]) for y in Y]
# open("dataset/output_small_model_1.dat", "w").write("\n".join(Y))

X = [[int(t) for t in s.split()] for s in open("dataset/data_small.dat", "r").readlines()]
Y = [model_2.predict(x) for x in X]
Y = ["".join([item['char'] for item in y[0][0]]) for y in Y]
open("dataset/output_small_model_2.dat", "w").write("\n".join(Y))
print 0