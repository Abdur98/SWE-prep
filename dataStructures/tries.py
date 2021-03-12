# Tries
# all funcs O(k) where k is lenght of input word

class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.is_word = False    # mark the end of a word


class Trie(object):

    def __init__(self):
        # initialize the root node
        self.root = TrieNode()

    def add(self, word):
        # add a new word to the trie
        current = self.root
        for c in word:
            if c not in current.children:
                # create new node if the character is not in children
                current.children[c] = TrieNode()
            current = current.children[c]
        # mark the end of word
        current.is_word = True

    def search(self, word):
        # return True if the word is in the trie
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word

    def search_prefix(self, prefix):
        # return True if the prefix is in the trie
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        # we don't need a completed word for prefix
        return True


# We can efficiently do prefix search (e.g. auto-complete, spell checking) with Trie.
# The main disadvantage of tries is that they need a lot of memory for storing the strings. Hence, if you don’t need to do prefix search, we can use hash set to check the existence of a word.
