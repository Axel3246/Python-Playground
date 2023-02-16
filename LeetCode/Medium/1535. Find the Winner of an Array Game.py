'''
Given an integer array arr of distinct integers and an integer k.
Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

'''

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Track Winstreak
        winStrk = 0
        # First num
        winner = arr[0]
        for i in range(1, len(arr),1):
            # If winstreak is k, return winner
            if (winStrk == k):
                return winner
            # If winner is greater than next element, add to winstreak
            if winner > arr[i]:
                winStrk += 1
            # If winner is less than next element, update winner and set winstreak to 1
            elif winner < arr[i]:
                winner = arr[i]
                winStrk = 1
                
            # Since we dont update the array, when winner == winner no variables will be updated,
            # thus maintaining the problem constraints.

        # If K is greater than the arr length, just return the winner
        return winner
            


