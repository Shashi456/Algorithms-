def BFS(s,adj):
    level={s:0};
    parent={s:none}
    i=1
    frontier=[s]
    while frontier :
        nxt=[]
        for u in frontier :
            for u in adj[u]:
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    nxt.append(v)
            frontier=nxt
            i+=1
