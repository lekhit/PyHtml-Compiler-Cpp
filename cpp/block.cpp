#include <bits/stdc++.h>
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
  int n=(int)s.size()-1;
  for(int i=n;i>=0;i--){
    // removing all the trailing spaces
    while(i>=0 && s[i]==' '){i--;}
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
string getTag_content(string s){
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
  if(end) toadd="<\\";
  
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



int main(){
  auto file=freopen("html.text", "r", stdin);
  auto out_file=freopen("output.txt", "w", stdout);
  vector<vector<string>> ans;
  string s;int count=0;
vector<pair<string,int>> st;
  vector<string> enders;
  while(getline(cin,s)){
    count=getLeftCount(s);
    s=sanitizeLine(s);
    //printf("%s %d\n",s.c_str(),count);
    if(CheckTAG(s)!=-1){
      string tag=getTAG(s);
        if(LEN(st)>0){
          auto [curr,cnt]=st.back();
          if(count<cnt){ // this will create a block
          vector<string> block;
          block.push_back(enders.back());enders.pop_back();
            while(count<=cnt){
              if(count==cnt)
              block.push_back(curr);
              st.pop_back();
             auto item=st.back();
             curr=item.first;cnt=item.second;
            }  
            reverse(block.begin(),block.end());
            ans.push_back(block);
          }
        }
        {
          st.push_back({addPadding(getTag_content(s)),count});
          enders.push_back(addPadding(tag,true));
        }
        }
    else{
      if(LEN(s)>0)
       { st.push_back({s,count});}
    }   
    //$
  }
  for(auto i:ans){
  for(auto j:i) cout<<j<<endl;
  cout<<endl;
}
for(auto i:enders) cout<<i<<" ";cout<<endl;
for(auto [i,j]:st)  cout<<i<<" ";
  return 0;
}