from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import math
from sklearn.preprocessing import normalize
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
vectorizer = TfidfVectorizer(sublinear_tf=False, stop_words=None, token_pattern="(?u)\\b\\w+\\b", smooth_idf=True, norm='l2')
tfidf = vectorizer.fit_transform([text1,text2,text3])
df_tfidf = pd.DataFrame(tfidf.toarray(),columns=vectorizer.get_feature_names(), index=['text1', 'text2', 'text3'])
print("TFIDF")
print(df_tfidf)