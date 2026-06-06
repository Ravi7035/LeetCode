from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)

        level = {beginWord}
        found = False

        while level and not found:

            next_level = set()

            for word in level:
                wordSet.discard(word)

            for word in level:

                for i in range(len(word)):

                    for ch in 'abcdefghijklmnopqrstuvwxyz':

                        new_word = word[:i] + ch + word[i+1:]

                        if new_word in wordSet:

                            parents[new_word].append(word)
                            next_level.add(new_word)

                            if new_word == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        ans = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return ans