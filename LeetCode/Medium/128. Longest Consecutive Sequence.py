class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        consec = 0
        for num in nums:
            # Check if is start (no left neighbor, meaning no intermediate num)
            if num - 1 not in myset:
                # keep track of sequence
                next = 0
                # Now we will find if there's any sequence that follows the start
                while num + next in myset:
                    ''' Basically keep the sequence
                    The number is 1 and next is 2
                    The number is 1 and next is 3
                    The number is 1 and next is 4
                    '''
                    next += 1
                    #print(f'The number is {num} and next is {next}')
                # Update the most consec value
                consec = max(consec,next)
        
        return consec

                