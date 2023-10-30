from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        # Convert the list into a dictionary
        similarPairs_dict = {}
        for key, value in similarPairs:
            if key in similarPairs_dict:
                similarPairs_dict[key].append(value)
            else:
                similarPairs_dict[key] = [value]

        for i in range(0, len(sentence1)):
            sentence1_word = sentence1[i]
            sentence2_word = sentence2[i]
            if not (sentence1_word == sentence2_word \
                or sentence1_word in similarPairs_dict and sentence2_word in similarPairs_dict[sentence1_word] \
                or sentence2_word in similarPairs_dict and sentence1_word in similarPairs_dict[sentence2_word]):
                return False
        
        return True
    
if __name__ == "__main__":
    solution = Solution()
    solution.areSentencesSimilar(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]])