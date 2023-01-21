class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # CREATE A HASHMAP
        hashmapp = defaultdict(int)
        # SORT THE ARRAY
        nums.sort()
        # HELPER ARRAY FOR LATER
        res = []
        # TRAVERSE SORTED ARRAY AND STORE OCURRENCES IN HASHMAP
        for num in nums:
            if num in hashmapp:
                hashmapp[num] += 1
            else:
                hashmapp[num] = 1
        
        # STORE THE HASHMAP AS A LIST OF TUPLES, SO THAT WE CAN THEN SORT BY VALUE
        d = sorted(hashmapp.items(), key=lambda x:x[1])
        d.sort(key=lambda a: a[1])
        d.reverse()
        # GET ALL FIRST VALUES OF THE TUPLES. CONVERT MAP TO LIST FOR EASY ACCESS IN THE TRAVERSAL OF "K"
        first_data = list(map(operator.itemgetter(0), d))
        # GETTING THE K ELEMENTS
        for i in range(0,k):
            res.append(first_data[i])
        
        return res

'''
SOLUTION USING BUCKET SORT TRICK - NEETCODE
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HASHMAP TO STORE REPEATING NUMS
        count = {}
        # BUCKET SORT LIST OF LENGHT OF nums + 1 (No Zero Ocurrences)
        freq = [[] for i in range(len(nums) + 1)]

        # STORE IN HASHMAP OCURRENCES
        for n in nums:
            # COUNT.GET(N,0) = GET THE CURR VALUE OF KEY AND SUM + 1 ELSE PUT 0
            count[n] = 1 + count.get(n, 0)
        # BUCKET SORT TRICK, WHERE THE COUNT IS NOW THE 
        # COUNT.ITEMS WORKS LIKE A TUPLE
        # C = INDEX, N VALUE
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # REVERSE TRAVERSAL OF ARRAY
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # BREAK CONDITION
                if len(res) == k:
                    return res

        # O(n)

