#include<bits/stdc++.h>
using namespace std;
#define int long long 
#define mod 1000000007

int min_kadane(std::vector<int>&v,std::vector<int>&dp  )
{dp[0]=v[0];
  for(int i=1;i<v.size();i++)
  {
    int take=dp[i-1]+v[i];
    int not_take=v[i];
    dp[i]=min(take,not_take);
  }
  return *min_element(dp.begin(),dp.end());
}

int kadane(std::vector<int>&v,std::vector<int>&dp  )
{dp[0]=v[0];
  for(int i=1;i<v.size();i++)
  {
    int take=dp[i-1]+v[i];
    int not_take=v[i];
    dp[i]=max(take,not_take);
  }
  return *max_element(dp.begin(),dp.end());
}


void solve()
{
int t;
int n;
cin>>n;
std::vector<int>v(n) ;
int total=0;
for(int i=0;i<n;i++){cin>>v[i];
total+=v[i];}
std::vector<int>dp(n,0) ;
std::vector<int>dp2(n,0) ;
int mmin =min_kadane(v,dp);
mmin=total-mmin;
int kad= kadane(v,dp2);
if (kad>0){//cout<<max(kad,mmin)<<"\n";
if(kad > mmin){
cout<<kad;

}
else{
cout<<mmin;
}
}
else{
cout<<kad;
}
}

int32_t main()
{

    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);    

solve();

}