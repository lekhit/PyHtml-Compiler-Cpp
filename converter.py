def countspaces(s):
    n=len(s)
    s=s.lstrip()
    n1=len(s)
    return (n-n1)
def spacestring(num):
    s=""
    for i in range(num):
        s+=" "
    return s
        

def blanklineremover(lt):
    for i in range(len(lt)):
        if lt[i]=='':
            lt.pop(i)
    return (lt)

def notknown(line):
    known=["if","for","while"]
    for v in known:
            if (line.lstrip()).startswith(v):
                return False
    return True

def finder(line,lt):
    n=countspaces(line)
    rlist=[]
    s=line.lstrip()
    j=0
    s="</"+s[:s.find(" ")]+">"
    if line.rstrip().endswith(":"):
        
        if notknown(line):
            
            index=lt.index(line)
            for i in range(index+1,len(lt)):
                if countspaces(line)>n+4:
                    print(lt)
                else:
                    j=i
            lt.insert(j+1,spacestring(n+4)+s)
                
    return lt
def finder1(line,lt):
    n=countspaces(line)
    
    if line.rstrip().endswith(":"):
        
        if notknown(line):
            
            index=lt.index(line)
            for i in range(index+1,len(lt)):
                if countspaces(lt[i])<n+4:
                    d={i:s}
                    print(d)
                    return d
    d={len(lt):s}
    return d
                
                


"""line="html:"
lt=[line,"    div:","    this ant athath"]
lt=finder(line,lt)
print(lt)
"""
myfile=open("html.text")
lt=myfile.readlines()
lt=blanklineremover(lt)
d={}
for line in lt:
    d.update(finder1(line,lt))
for j1 in d:
    lt.insert(j1,d.get(j1))
print("final")
for line in lt:
    print(line)
            
            
            
