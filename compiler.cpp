#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <cstdlib> 

///
using namespace std;
# define LEN(ITEM) ((int)ITEM.size())
#define TERMENATOR ':'
set<string> BLOCK_ELEMENTS={"address","article","aside","blockquote","body","br","caption","div","dl","fieldset","footer","form","h1","h2","h3","h4","h5","h6","header","hr","main","nav","ol","p","pre","section","table","tbody","td","th","thead","ul"};
int getLeftCount(string s){
  int c=0;
for(auto i:s){if(i!=' ') break; if(i==' ') c++;}
return c;
}
int CheckTAG(string s){
  int n=(int)s.size()-1;int i=n;

 {
    // removing all the trailing spaces
    while(i>=0 ){if(s[i]==' ') i--;else break;  }
    if(s[i]==TERMENATOR) return i;
  }
  return -1;
}
string getTAG(string s){
  int n=LEN(s);string tag="";
int i=0;
    // remove l spaces
    while (i<n && s[i]==' ')
      {i++;}
    while(i<n) {
      if(s[i]==' '||s[i]==TERMENATOR) break;
      tag+=s[i];i++;}

  return tag;
}
string getCompleteStartTag(string s){
  int n=LEN(s);
  int terminator=CheckTAG(s);
  int start=0;
  string ans="";
 string tag="";
    // remove l spaces
    while (start<n && s[start]==' ')
      {start++;}
  for(int i=start;i<(terminator);i++){
    ans+=s[i];
  }
return ans;
}
string addPadding(string input,bool end=false){
  string toadd="<";
  if(end) toadd="</";
  
return toadd+input+">";
}
string sanitizeLine(string input){
  string ans="";
  for(auto i:input){
    // if(i=='"') ans+=;
    // if(i=='\'') ans+="\";
    ans+=i;
  }
  return ans;
}

string GetPyIndentaion(string s,int min_indent){
  string ans="";
  for(int i=0;i<LEN(s);i++){
    while(i<min_indent) i++;
    ans+=s[i];
  }
  return ans;
}
int runPY(){

  int returnValue = std::system("python3 pyrun.py");

    // Check the return value to determine if the execution was successful
    if (returnValue == 0) {
        // Python script executed successfully
        // You can add further logic here
    } else {
        // An error occurred during execution
        // You can handle the error or log it
    }
  return returnValue;
}

void processString(list<string>::iterator itr, list<pair<string,int>> &lt,list<pair<string,int>>::iterator &it){
  string s=(*itr);
 int  count=getLeftCount(s);

        //means we are deaing with tag
        auto startTag=addPadding( getCompleteStartTag(s));
        auto endTag=addPadding(getTAG(s),true);
        if(lt.begin()!=it){
          if((*it).second<count){
            // meaning we are inserting inside the outer parent
            // nothing special here
          }
          else if((*it).second==count){
            // dealing with sibling
            //finding parent
          while((*it).second==count){advance(it,1);}

          }
          else{
            // dealing with new parent
            //get the upper parrent
            // count<(*it).second
            while((*it).second>=count){advance(it,1);}
          }
        }
        else{
          // no special condition is applied
          // handling the first insertion
        }
        // doing the nessacery insertion
        lt.insert(it,{startTag,count});
        lt.insert(it,{endTag,count});
        advance(it,-1);

      
}

void makePYrunFILE(vector<string> v,int pyindent){
   ofstream myfile;
myfile.open("pyrun.py",ios::out|ios::trunc);
myfile<<"\nimport sys\noriginal_stdout = sys.stdout\noutput_file = open('pyout.txt', 'w')\nsys.stdout = output_file\n";
for(auto i:v) {myfile<<GetPyIndentaion(i,pyindent)<<endl;}
myfile<<"\nsys.stdout = original_stdout\noutput_file.close()";
myfile.close();
}
string processIndentaionPython(string s,int pycount){
  string ans="";
  for(int i=0;i<=pycount;i++){
    ans+=" ";
  }
  ans+=s;
  return ans;
}

void processPythonFILE(list<string>::iterator &it,list<string> &input, int pycount){
ifstream inputfile("pyout.txt");
int cnt=0;
  string s;
  while(getline(inputfile,s)){
    string ans=(processIndentaionPython(s,pycount));
    input.insert(it,ans);
    cnt++;
  }
  advance(it,cnt*-1);
  inputfile.close();
}


string processPythonString(list<string>::iterator &it,list<string> &input){
  string s=(*it);
  int count=getLeftCount(s);
vector<string> pyLines;
      string py=getTAG(s);
      int pyCount=count;
      int pyindent=INT_MAX;


       
        //cout<<py;
        // getline(cin,py);
        ++it;
        py=(*it);
        do{
        count=getLeftCount(py);
        pyindent=min(count,pyindent);
        pyLines.push_back(py);
       ++it;
       py=(*it);
        count=getLeftCount(py);
        }while((count>pyCount));
        s=py;// giving the last line for further processing;
        makePYrunFILE(pyLines,pyindent);
      if(runPY()==0){
        // successful execution of python file
        processPythonFILE(it,input,pyCount);

      }
      
    return s;
    }



int main(int n , char** args){


    // Check if Python was initialized successfully
   
    // Finalize the Python interpreter when done
    
  auto file=freopen("html.html", "r", stdin);
  auto out_file=freopen("output.html", "w", stdout);
  string s;int count=0;
  list<pair<string,int>> lt;
  auto it=lt.begin();
  int preTagIndentaion=0;
  list<string> input;
  while(getline(cin,s)){
    input.push_back(s);
  }

for(auto itr=input.begin();itr!=input.end();itr++){
  string s=(*itr);
    if(LEN(s)==0) continue;
    // getting indentaion count
    //s=sanitizeLine(s);
    //printf("%s %d\n",s.c_str(),count);
    if(CheckTAG(s)!=-1){
      string Tag=getTAG(s);
      if(Tag=="python"){
  processPythonString(itr,input);}
  else if(Tag=="global"){

  }
  processString(itr, lt,it);}
  else{
        // simple line is recieved and we will add it as it is
        lt.insert(it,{s,count});
      }
    // detect and seprate python
    
      
      
    //$
  }
  for(auto [i,j]:lt) cout<<i<<endl;

  return 0;
}