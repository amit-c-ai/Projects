 #include<bits/stdc++.h>
 using namespace std;
 #pragma GCC push_options
 #pragma GCC optimize ("unroll-loops")
 #define watch(x) cout << (#x) << " is " << (x) << "\n"
 #define watch2(x,y) cout <<(#x)<<" is "<<(x)<<" and "<<(#y)<<" is "<<(y)<<"\n"
 #define pow2(x) ((x)*(x))
 #define max3(a,b,c) max(a,max(b,c))
 #define min3(a,b,c) min(a,min(b,c))
 #define ll long long
 #define ld long double
 #define eb emplace_back
 #define pb push_back
 #define pf push_front
 #define mod 1000000007
 #define clock (clock() * 1000.0 / CLOCKS_PER_SEC)
 #define mp make_pair
 #define ff first
 #define ss second
 #define all(c) (c).begin(),(c).end()
 #define nl "\n"
 typedef vector<int> vi;
 typedef vector<ll> vl;
 typedef vector<vi> vvi;
 typedef vector<vl> vvl;
 typedef pair<int,int> ii;
 typedef pair<ll,ll> pll;
 typedef map<ll,ll> mll;
 typedef map<int,int> mii;
 int main()
 {
     ios_base::sync_with_stdio(false);
     cin.tie(0);
     cout.tie(0);
     ll n,m,k;
     cin >> n >> m >> k;
     ll ar1[n],ar2[m];
     for(int i=0;i<n;i++)
     	cin >> ar1[i];
     for(int i=0;i<m;i++)
     	cin >> ar2[i];
     vl v;
     for(int i=1; i<=sqrt(k); i++) 
     { 
         if (k%i == 0) 
         {  
             if (k/i == i) 
                 v.eb(i); 
   
             else // Otherwise print both 
             {
             	v.eb(i);
             	v.eb(k/i);
             }
         } 
     }
     sort(all(v));
     ll pre1[n+1],pre2[m+1];
     pre1[0] = ar1[0];
     pre1[n] = 0;
     for(int i=1;i<n;i++)
     {
     	if(ar1[i]==1)
     		pre1[i] = 1+pre1[i-1];
     	else
     		pre1[i]=0;
     }
     pre2[0] = ar2[0];
     pre2[m] = 0;
     for(int i=1;i<m;i++)
     {
     	if(ar2[i]==1)
     		pre2[i] = 1+pre2[i-1];
     	else
     		pre2[i]=0;
     }
     ll ar3[n+1];
     memset(ar3,0ll,sizeof(ar3));
     for(int i=1;i<=n;i++)
     {
     	if(pre1[i]==0)
     	{
     		for(int j=1;j<=pre1[i-1];j++)
     			ar3[j] += pre1[i-1]-j+1;
     	}
     }
     ll ar4[m+1];
     memset(ar4,0ll,sizeof(ar4));
     for(int i=1;i<=m;i++)
     {
     	if(pre2[i]==0)
     	{
     		for(int j=1;j<=pre2[i-1];j++)
     			ar4[j] += pre2[i-1]-j+1;
     	}
     }
 	// for(int i=0;i<=n;i++)
 	// 	cout << ar3[i] << " ";
 	// cout << nl;
 	// for(int i=0;i<=m;i++)
 	// 	cout << ar4[i] << " ";
 	// cout << nl;
     ll ans = 0ll;
    // watch2(v[0],v[1]);
     for(int i=0;i<v.size();i++)
     {
     	int temp1 = v[i];
     	int temp2 = k/v[i];
     	if(temp1<=n && temp2<=m)
     	{
     		ans += ar3[temp1]*ar4[temp2];
     	}
     }
     cout << ans << nl;
     return 0;
 }
