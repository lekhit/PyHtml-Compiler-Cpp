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
    known=["if","for","while","print","def","return","$e","$eh"]
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


def blockendindex(startindex ,lines):
    total= len(lines)
    index=startindex
    initalspaces=countspaces(lines[startindex])
    for i in range(startindex+1,total):
        if countspaces(lines[i])>initalspaces:
            index+=1
    return index
            
def eh(startindex,lt):
    
  i=startindex
  e=[]
  re=[]
  e.append(lt[startindex].replace("$eh","def"))
  for j in range(i+1,len(lt)):    
    line=lt[j]
    if (line.strip()).endswith("/h"):
      break
    if notknown(line):
      e.append(f"print('{line}')")
  re=[e,j]
  return re
    

"""line="html:"
lt=[line,"    div:","    this ant athath"]
lt=finder(line,lt)
print(lt)
"""

myfile=open("html.txt")
#myfile=open(input("enter file name in .txt format to convert:"))
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
        

for i in range(0,len(lt)):
    line=lt[i]
    line=line.replace("\n","")

    if notknown(line):
        spaces=countspaces(line)
        index=lt.index(line)
        line=line.replace('"','\"')
        line=line.replace("'","\'")
        line=line.replace("\n","")
        lt[index]=f'print(\'{line}\')'
    else:
        
        if line.rstrip().startswith("$e") :
            re=eh(i,lt)
            for k in range(i,re[1]):
                for line in re[0]:
                    lt[k]=line
            
            
        if line.rstrip().endswith(":"):
            spaces=countspaces(line)
            
            
            endindex=blockendindex(i,lt)
            for j in range(i,endindex):
                line=lt[j]
                lt[j]=line[spaces:]
            i=endindex
        

    
def delist(lt):
	e=[]
	for item in lt:
		if type(item) is list:
			for i in item:
				e.append(i)
			delist(e)
		else:
			e.append(item)
	return e
                 
                 
                 
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




