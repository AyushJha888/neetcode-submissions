class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        # for i in strs:
        #     print(i)
        for index, str_i in enumerate(strs):
            len_words=len(str_i)
            s=s+str(len_words) +"#"+ str_i
        return s


    def decode(self, s: str) -> List[str]:

        dlist=[]
        i=0

        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            length =int(s[i:j])
            start=j+1
            end=start+length
            
            dlist.append(s[start:end])
            i=end
        
        return dlist
