from con2 import countspaces

def blockmaker(lt):
    indexes={}
    for line in lt:
        n=countspaces(line)
        if line.strip().endswith(":"):
            index=lt.index(line)
            startindex=index
            for i in range(index+1,len(lt)):
                if countspaces(lt[i])>=n+4:
                    index+=1
                if countspaces(lt[i])<n+4:

                    break
            endindex=index
    if startindex==endindex:
        code=[]
    else:
        code=lt[startindex+1:endindex]
        block={lt[startindex]:code}
        indexes={"start":startindex,"end":endindex}
    return indexes


myfile=open("html.txt")
lt=myfile.readlines()
blocks={}
blocks.update(blockmaker(lt))
print(blocks)
    
