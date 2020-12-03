import nltk
import math
import string
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords,wordnet
from collections import Counter
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
text1 = "Python is a 2000 made-for-TV horror movie directed by Richard \
Clabaugh. The film features several cult favorite actors, including William \
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy, \
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the \
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean \
Whalen. The film concerns a genetically engineered snake, a python, that \
escapes and unleashes itself on a small town. It includes the classic final\
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles, \
California and Malibu, California. Python was followed by two sequels: Python \
II (2002) and Boa vs. Python (2004), both also made-for-TV films."
text2 = "Python, from the Greek word (πύθων/πύθωνας), is a genus of \
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are \
recognised.[2] A member of this genus, P. reticulatus, is among the longest \
snakes known."
text3 = "The Colt Python is a .357 Magnum caliber revolver formerly \
manufactured by Colt's Manufacturing Company of Hartford, Connecticut. \
It is sometimes referred to as a \"Combat Magnum\".[1] It was first introduced \
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now discontinued \
Colt Python targeted the premium revolver market segment. Some firearm \
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy \
Thompson, Renee Smeets and Martin Dougherty have described the Python as the \
finest production revolver ever made."
def get_tokens(text):
	lowers = text.lower()
	#remove the punctuation using the character deletion step of translate
	remove_punctuation_map = dict((ord(char),None)for char in string.punctuation)
	no_punctuation = lowers.translate(remove_punctuation_map)
	tokens = nltk.word_tokenize(no_punctuation)
	return tokens

def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens :
		stemmed.append(stemmer.stem(item))
	return stemmed

def tf(word, count):
	return count[word] / sum(count.values())
def n_containing(word, count_list):
	return sum(1 for count in count_list if word in count)
def idf(word, count_list):
	return math.log(len(count_list) / (n_containing(word, count_list)))
def tfidf(word, count, count_list):
	return tf(word, count) * idf(word, count_list)
def count_term(text):
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count = Counter(stemmed)
    return count

def main():
    texts = [text1, text2, text3]
    countlist = []
    for text in texts:
        countlist.append(count_term(text))
    for i, count in enumerate(countlist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse=True)
        for word, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

if __name__ == "__main__":
    main()

#https://zhuanlan.zhihu.com/p/26766008	