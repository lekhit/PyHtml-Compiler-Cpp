
import json,os


def store(d):
  with open('d.txt','w') as f:
    json.dump(d,f)

def getData():
  di=dict()
  with open('d.txt','r') as f:
    di=json.load(f)
  return di
if not os.path.exists('d.txt'):
  d={}
  store(d)

while(True):
  i=input("what do you want to do? enter new entry (1), delete entry (2), find meaning(3) (of life;), exit(0)\n")
  d=getData()
  
  if i=='0': 
    exit()
    break

  word=input('enter word\n')
  if(i=='1'):
    meaning=input('enter meaning using | in meaning is forbidden\n')
    d[word]=meaning
  if(i=='2'):
    if word in d.keys():
      d.pop(word)
  if( i=='3'):
    if word in d.keys():
      print("meaning is ",d[word])
    else:
      print("word not found")
  #print(d)
  store(d)
  
  
