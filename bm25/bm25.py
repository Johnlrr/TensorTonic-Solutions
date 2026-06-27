import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    N = len(docs)
    avgdl = np.sum([len(doc) for doc in docs])/N

    df = []
    for t in query_tokens:
        count = 0
        for doc in docs:
            if t in doc: count += 1
        df.append(count)
    df = np.array(df)

    idf = np.log((N - df + 0.5)/(df + 0.5) + 1)

    dl = [len(doc) for doc in docs]
    scores = np.zeros(N)

    for i, t in enumerate(query_tokens):
        tf_t = np.array([doc.count(t) for doc in docs])
        denom = tf_t + k1*(1- b + b*(dl/avgdl))
        num = tf_t*(k1 + 1)
        term_score = idf[i]*num/denom
        scores +=  (term_score)
    return scores