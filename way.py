def path(n,m,way):
    if n==0 and m==0:
        print(way)
        return
    if n:
        way1=way[:]
        way1+="^"
        path(n-1,m,way1)
    if m:
        way2=way[:]
        way2+=">"
        path(n,m-1,way2)
if __name__=="__main__":
    path(3,2,"")
