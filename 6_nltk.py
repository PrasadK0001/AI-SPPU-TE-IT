import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict


class InformationRetrievalSystem:
    def __init__(self, documents):
        self.documents = documents
        self.index = defaultdict(list)
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.build_index()

    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token.isalnum()]
        tokens = [self.stemmer.stem(token) for token in tokens if token not in self.stop_words]
        return tokens

    def build_index(self):
        for doc_id, doc in enumerate(self.documents):
            for token in self.preprocess(doc):
                self.index[token].append(doc_id)

    def search(self, query):
        query_tokens = self.preprocess(query)
        result = set(self.index[query_tokens[0]])
        for token in query_tokens[1:]:
            result = result.intersection(set(self.index[token]))
        return [self.documents[doc_id] for doc_id in result]

# Example usage
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A brown fox is seen jumping over the sleeping dog.",
    "The dog is sleeping peacefully.",
    "The fox and the dog are friends."
]

ir_system = InformationRetrievalSystem(documents)

query = "brown fox"
results = ir_system.search(query)

print("Documents containing '{}' in the collection:".format(query))
for result in results:
    print("-", result)
