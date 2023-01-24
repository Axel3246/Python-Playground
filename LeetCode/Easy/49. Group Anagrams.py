class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # MAPPING EACH STRING, USING DEFAULT DICT TO AVOID EMPTY KEYS
        hashmapp = defaultdict(list)
        # TRAVERSING THE ARRAY
        for s in strs:
            # LOWERCASE ENGLISH LETTERS ONLY -> 26 ZEROES a ... z
            contador = [0] * 26
            for c in s:
                # NOW WE MAP HOW MANY TIMES THE LETTER REPEATS USING ORD
                contador[ord(c) - ord ("a")] += 1
            # NOW WE STORE THE NEW STRING IN ITS CORRESPONDING KEY (WE CAN USE      TUPLE OR STRING)
            hashmapp[tuple(contador)].append(s)  
        # WE LASTLY THEN RETURN THE VALUES OF THE HASHMAP
        return hashmapp.values()       
