import tarfile
from itertools import islice
from sklearn.feature_extraction.text import CountVectorizer


def load_chat(num_docs):
    loc = 'ChatGroup.tar'
    with tarfile.open(loc) as tar :
        datafile = tar.extractfile('ChatGroup.tar/ChatGroup.txt')
        return list(islice(datafile, num_docs))
def make_matrix(docs, binary=False):
    vec = CountVectorizer(min_df=10, max_df=0.1, binary=binary)
    mtx = vec.fit_transform(docs)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    return mtx, cols
