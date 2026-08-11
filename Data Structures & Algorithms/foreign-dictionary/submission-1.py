class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList={c: set() for word in words for c in word}

        #compare 2 words at a time
        for i in range(len(words)-1):
            w1, w2= words[i], words[i+1]
            min_len=min(len(w1), len(w2))
            #check for cases abc, ab
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]:
                return ''
            #now check the order
            for i in range(min_len):
                if w1[i]!=w2[i]:
                    adjList[w1[i]].add(w2[i])

                    break 

        visit={} #c: bool False means visited, True means current path
        res=[]

        def dfs(n):
            if n in visit: 
                return visit[n]

            visit[n]=True 

            for nei in adjList[n]:
                if dfs(nei):
                    return True #found loop

            visit[n]=False 
            res.append(n)

        for c in adjList: 
            if dfs(c):
                return ''

        res.reverse()
        return ''.join(res)

        
            
            
            