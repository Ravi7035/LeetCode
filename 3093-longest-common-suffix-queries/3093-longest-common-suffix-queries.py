class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.best_index = -1

        root = TrieNode()
        def better(i, j):

            if j == -1:
                return i

            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i

            if len(wordsContainer[i]) == len(wordsContainer[j]):

                if i < j:
                    return i

            return j

        for i, word in enumerate(wordsContainer):

            node = root
            node.best_index = better(i, node.best_index)

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                node.best_index = better(i, node.best_index)

        ans = []
        for query in wordsQuery:

            node = root

            for ch in reversed(query):

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.best_index)

        return ans
                
                
            
            
            

        