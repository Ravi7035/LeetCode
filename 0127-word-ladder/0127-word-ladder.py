class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set=set(wordList)

        if endWord not in word_set:
            return 0

        q=deque([(beginWord,1)])

        while q:
            word,steps=q.popleft()

            if word==endWord:
                return steps

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    new_word=word[:i]+ch+word[i+1:]

                    if new_word in word_set:
                        q.append((new_word,steps+1))
                        word_set.remove(new_word)

        return 0

        

                    
        