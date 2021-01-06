# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.


# ANS


# Trick is that anagrams have same char count so
# for two anagrams, anagrams1 and anagram 2
# sorted(anagram1) = sorted(anagram2)

# Leverage above fact and throw a dict at it and Voila!

class Solution:
    def groupAnagrams(strs):

        results = []
        sortedToVals = {}

        for word in strs:
            # remember keys need to be of hashable type
            # In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable
            # list not hashable
            sortedWord = ''.join(sorted(word))

            if sortedWord not in sortedToVals:
                sortedToVals[sortedWord] = [word]
            else:
                sortedToVals[sortedWord].append(word)

        for value in sortedToVals.values():
            results.append(value)

        return results

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



















