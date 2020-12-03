---
title: 'Project documentation template'
disqus: hackmd
---

TFIDF-Python
===


[![hackmd-github-sync-badge](https://hackmd.io/60hpuUHTSeK-S_vbSrmqoA/badge)](https://hackmd.io/60hpuUHTSeK-S_vbSrmqoA)



## 分詞

首先我們來做分詞，其中比較值得注意的地方是我們設法剔除了其中的標點符號
```gherkin=
def get_tokens(text):
	lowers = text.lower()
	#remove the punctuation using the character deletion step of translate
	remove_punctuation_map = dict((ord(char),None)for char in string.punctuation)
	no_punctuation = lowers.translate(remove_punctuation_map)
	tokens = nltk.word_tokenize(no_punctuation)
	return tokens

tokens = get_tokens(text1)
count = Counter(tokens)
print (count.most_common(10))
```

**Result :**
```gherkin=
[('the', 6), ('python', 5), ('a', 5), ('and', 4), ('in', 3), ('films', 3), ('madefortv', 2), ('by', 2), ('film', 2), ('of', 2)]
```

## 剔除與文章無關的字
顯然，像 the, a, and 這些詞儘管出現的次數很多，但是它們與文件所表述的主題是無關的，所以我們還要去除“詞袋”中的“停詞”（stop words），程式碼如下：

```gherkin=
def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens :
		stemmed.append(stemmer.stem(item))
	return stemmed

tokens = get_tokens(text1)
filtered = [w for w in tokens if not w in stopwords.words()]
count = Counter(filtered)
print(count.most_common(10))
```

**Result:** 缺乏實際意義的 the, a, and 等詞已經被過濾掉了
```gherkin=
[('python', 5), ('films', 3), ('madefortv', 2), ('film', 2), ('california', 2), ('2000', 1), ('horror', 1), ('movie', 1), ('directed', 1), ('richard', 1)]
```

## 詞幹提取(stem)或詞形還原
但這個結果還是不太理想，像 films, film, filmed 其實都可以看出是 film，而不應該把每個詞型都分別進行統計。這時就需要要用到我們在前面文章中曾經介紹過的 Stemming 方法。程式碼如下：

1. 詞形還原（lemmatization），是把一個任何形式的語言詞彙還原為一般形式（能表達完整語義）
> ex. 如將“drove”處理為“drive”，將“driving”處理為“drive”。
2. 詞幹提取（stemming）是抽取詞的詞幹或詞根形式（不一定能夠表達完整語義）
> ex. 如將“cats”處理為“cat”，將“effective”處理為“effect”
```gherkin=
#詞幹提取
tokens = get_tokens(text1)
filtered = [w for w in tokens if not w in stopwords.words('english')]
stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)
print(count)
print(count.most_common(10))
```
**Result:**
```gherkin=
[('film', 6), ('python', 5), ('madefortv', 2), ('includ', 2), ('california', 2), ('2000', 1), ('horror', 1), ('movi', 1), ('direct', 1), ('richard', 1
```
###### tags: `Templates` `Documentation`
