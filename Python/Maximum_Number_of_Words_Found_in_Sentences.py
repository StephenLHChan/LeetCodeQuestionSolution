# 2114. Maximum Number of Words Found in Sentences

def mostWordsFound(self, sentences: List[str]) -> int:
    wordCountList = []
    for sentence in sentences:
        wordCountList.append(sentence.count(' ') + 1)
    return max(wordCountList)
