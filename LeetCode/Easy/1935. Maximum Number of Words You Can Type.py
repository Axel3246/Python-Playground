class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Create lists
        lsttxt = text.split(" ")
        lstbkn = list(brokenLetters)
        c = 0
        # Check every word
        for word in lsttxt:
            # Flag
            count = 0
            # Check every letter
            for char in lstbkn:
                # Dodge duplicates
                if count == 0:
                    # Sum of words we can't use
                    if char in word:
                        c += 1
                        count = 1
        # Return true number of words len - c
        return len(lsttxt)-c
