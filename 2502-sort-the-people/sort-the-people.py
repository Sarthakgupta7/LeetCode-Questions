class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        k=[]
        ssr=sorted(zip(heights, names), reverse=True)
        for (x,y) in ssr:
            k.append(y)
        return k