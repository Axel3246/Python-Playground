class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Convert string to list
        newlst = list(s)
        # Get indexes from arr and iterate
        for i in spaces:
            # add trailing space
            newlst[i] =  " " + newlst[i]
            #print(newlst[i])
        # return as string
        return "".join(newlst)
            