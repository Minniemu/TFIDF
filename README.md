---
title: 'Project documentation template'
disqus: hackmd
---

TFIDF-Python
===


## Table of Contents

[TOC]

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



###### tags: `Templates` `Documentation`
