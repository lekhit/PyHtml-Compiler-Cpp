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

int main(){
  auto file=freopen("html.text", "r", stdin);
  auto out_file=freopen("output.txt", "w", stdout);
  string s;int count=0;
  list<pair<string,int>> lt;
  auto it=lt.begin();
  int preTagIndentaion=0;
  while(getline(cin,s)){
    if(LEN(s)==0) continue;
    count=getLeftCount(s);// getting indentaion count
    
    //printf("%s %d\n",s.c_str(),count);
      if(CheckTAG(s)!=-1){
      }
    //$
  }
  for(auto [i,j]:lt) cout<<i<<endl;
  return 0;
}