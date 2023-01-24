class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Check for 3 consecutive odds
        for i in range(0, len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True

        return False