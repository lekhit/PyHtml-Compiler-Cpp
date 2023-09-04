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
    known=["if","for","while","print"]
    for v in known:
            if (line.lstrip()).startswith(v):
                return False
    return True

def finder(line,lt):
    n=countspaces(line)
    rlist=[]
    s=line.lstrip()
    j=0
    s="/<"+s[:s.find(" ")]+">"
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
    rlist=[]
    s=line.lstrip()
    j=0
    d={}
    s=spacestring(n+4)+"</"+s[:s.find(" ")]+">"
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

def nameindex(s):
    if s.find(' ')>0:
        return s.find(' ')
    else: return s.find(':')


"""line="html:"
lt=[line,"    div:","    this ant athath"]
lt=finder(line,lt)
print(lt)
"""
myfile=open("html.txt")
lt=myfile.readlines()
lt=blanklineremover(lt)

ltr=lt

for line in lt:
    n=countspaces(line)
    s=line.lstrip()
    
    if line.rstrip().endswith(":"):
        
        if notknown(line):
            s=spacestring(n)+"</"+s[:nameindex(s)]+">"
            s1=spacestring(n)+"<"+s[:nameindex(s)]+">"
            index=lt.index(line)
            lt[lt.index(line)]=spacestring(n)+"<"+line.replace(":",">").lstrip()
            inserted=False        
            
            for i in range(index+1,len(lt)):
                if countspaces(lt[i])<n+4:
                    lt[index]=spacestring(n)+"<"+line.replace(":",">").lstrip()
                    lt.insert(i,s)
                    inserted=True
                    break
            if not inserted:
                lt.insert(len(lt),s)


for line in lt:
    if notknown(line):
        spaces=countspaces(line)
        line=line.replace('"','\"')
        line=line.replace("'","\'")
        lt[lt.index(line)]=f'print("""{line}""")'
    else:
        lt[lt.index(line)]=line[spaces+4:]
        
        
for line in lt:
    print(line)
    
runfile = open("runfile.py","w")

        
for line in lt:
    runfile.write(line+"")
runfile.close()

f = open("test.py","w")

f.write("e=[]\n")
        
for line in lt:
    line1=line
    f.write(line+"\n")
    if "print" in line1:
        line1=line1.replace("print",'e.append')
        f.write(line1+"\n")
    



f.write('\nhtmlfile=open("htmlfinal.html","w")')
f.write('\nfor line in e:\n')
f.write('    htmlfile.write(line)\n')
f.write('htmlfile.close()')


f.close()
exec(open("./test.py").read())
import os
os.system('open htmlfinal.html')

            
