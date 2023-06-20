class Solution:
    def reverseBits(self, n: int) -> int:

        oribin='{0:032b}'.format(n)
        print(oribin)
        reversebin=oribin[::-1]
        return int(reversebin,2)
        

        
        