'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

Return the number of different transformations among all words we have.

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Morse code
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # Hash map
        hmap = defaultdict(int)
        # Get word and decode it
        for word in words:
            re = ""
            for c in word:
                re += morse[(ord(c) - ord("a"))]   
            # update hashmap   
            hmap[re] = 1 + hmap.get(re,0)
        # ans will be the len of hashmap (num of keys)
        return(len(hmap))
                