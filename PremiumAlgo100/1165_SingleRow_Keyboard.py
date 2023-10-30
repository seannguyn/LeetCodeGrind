class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dictionary = {character: index for index, character in enumerate(keyboard)}
        
        previous_position = 0
        total_time = 0
        for character in word:
            total_time += abs(keyboard_dictionary[character] - previous_position)
            previous_position = keyboard_dictionary[character]
        return total_time

if __name__ == "__main__":
    solution = Solution()
    solution.calculateTime()
