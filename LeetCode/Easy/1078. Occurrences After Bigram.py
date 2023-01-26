class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # List of words of the text
        tlst = text.split(" ")
        #print(tlst)
        # Ans arr
        res = []
        # For every word in the arr length - 2 
        for i in range(0, len(tlst)-2):
            # if we find a match, append third word to ans array and move i three places further
            if(tlst[i] == first and tlst[i+1] == second):
                res.append(tlst[i+2])
                i += 3
        
        return res
        
        