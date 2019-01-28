#15956 숏코딩 by cubelover
import sys

sys.setrecursionlimit(10**8)

p = dict()
q = dict()
o = set()

def f(x):
	if x not in p:
		p[x] = x
		return
	if p[x] == x:
		return
	t = p[x]
	f(t)
	p[x] = p[t]

a = []

for x in input().split('&&'):
	if x.find('!=') != -1:
		u, v = x.split('!=')
		f(u)
		f(v)
		a.append((u, v))
		continue
	u, v = x.split('==')
	f(u)
	f(v)
	p[p[u]] = p[v]

for u in p:
	f(u)
	t = p[u]
	if t not in q or len(u) < len(q[t]):
		q[t] = u
	try:
		tu = int(u)
		if t in o:
			print('0!=0')
			sys.exit()
		o.add(t)
	except Exception:
		pass

r = set()

for u in p:
	t = q[p[u]]
	if u != t:
		r.add('%s==%s' % (u, t))

for u, v in a:
	f(u)
	f(v)
	u = p[u]
	v = p[v]
	if u in o and v in o:
		continue
	u = q[u]
	v = q[v]
	if u == v:
		print('0!=0')
		exit()
	if u > v:
		u, v = v, u
	r.add('%s!=%s' % (u, v))

if not r:
	print('0==0')
	exit()
print('&&'.join(r))

##02 by jh05013
def isnum(s):
    return all((c in '-0123456789') for c in s)

def die():
    print("1==0"); exit()

# == and &&
adj = {}
diff = []
for cond in input().split("&&"):
    if "==" in cond:
        a, b = cond.split("==")
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    else: diff.append(cond.split("!="))

# make groups
group = []
groupnum = {}
stack = []
for w in adj:
    if w in groupnum: continue
    stack.append(w)
    groupnum[w] = len(group); group.append({w})
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if u in groupnum: continue
            groupnum[u] = len(group)-1; group[-1].add(u)
            stack.append(u)
for a, b in diff:
    if a not in groupnum: groupnum[a] = len(group); group.append({a})
    if b not in groupnum: groupnum[b] = len(group); group.append({b})

# get value and shortest word of each group
value = []
sword = []
for G in group:
    value.append(None)
    sword.append(min(G, key=len))
    for w in G:
        if not isnum(w): continue
        if value[-1] != None: die()
        value[-1] = int(w)

# generate shortcode
shortcode = set()
for i in range(len(group)):
    for w in group[i]:
        if w != sword[i]: shortcode.add(w+"=="+sword[i])
for a, b in diff:
    ai = groupnum[a]
    bi = groupnum[b]
    if ai > bi: ai,bi = bi,ai
    if ai == bi: die()
    if None != value[ai] != value[bi] != None: continue
    shortcode.add(sword[ai]+"!="+sword[bi])
if not shortcode: print("1==1")
else: print("&&".join(shortcode))


#03 by randoms
S=list(input().split("&&"))

def is_number(s):
    for i in s:
        if i not in '-0123456789':
            return False
    return True

eqval={}
for s in S:
    if '==' in s:
        a,b=s.split("==")
        if a in eqval:
            eqval[a].add('=='+b)
        else:
            eqval[a]=set(['=='+b])
        if b in eqval:
            eqval[b].add('=='+a)
        else:
            eqval[b]=set(['=='+a])
    else:
        a,b=s.split("!=")
        if a in eqval:
            eqval[a].add('!='+b)
        else:
            eqval[a]=set(['!='+b])
        if b in eqval:
            eqval[b].add('!='+a)
        else:
            eqval[b]=set(['!='+a])

checklist=set()
minsentence={}
numbering={}
contradiction=False

for i in eqval:
    if i in checklist:continue
    checklist.add(i)
    st=[i]
    eqlist=set([i])
    while st:
        j=st.pop()
        for k in eqval[j]:
            if k[2:] in checklist:continue
            if k[:2]=='==':
                eqlist.add(k[2:])
                st.append(k[2:])
                checklist.add(k[2:])
    eqlist=sorted(eqlist,key=lambda x:len(x))
    c=0
    num=None
    for j in eqlist:
        if is_number(j):
            c+=1
            num=j
        minsentence[j]=eqlist[0]
    if c>1:
        contradiction=True
    if c==1:
        for j in eqlist:
            numbering[j]=num

totallist=set()
for i in eqval:
    if minsentence[i]==i:
        continue
    totallist.add(minsentence[i]+'=='+i)

for i in eqval:
    for j in eqval[i]:
        if j[:2]=='!=':
            ii,jj=minsentence[i],minsentence[j[2:]]
            temp=sorted([ii,jj])
            if ii==jj: contradiction=True
            if ii in numbering and jj in numbering:continue
            totallist.add('!='.join(temp))

if contradiction:print("0==1")
elif not totallist:print("0==0")
else:print('&&'.join(totallist))

'''c++14 by green55
#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> pii;

const int MAX = 1000000;
int parent[MAX];
int find(int a){
	if(parent[a]<0) return a;
	return parent[a] = find(parent[a]);
}
void merge(int a, int b){
	a = find(a), b = find(b);
	if(a==b) return;
	if(parent[a] < parent[b]) swap(a,b);
	parent[b] += parent[a];
	parent[a] = b;
}

string input;
vector<string> group[MAX];
bool hasNumber[MAX];

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	memset(parent, -1, sizeof(parent));

	cin >> input;
	input += "&&";

	map<string, int> str2int;
	vector<string> int2str;

	vector<pii> same;
	vector<pii> diff;

	string tmpS[2];
	bool usingSpos = 0;
	bool isDiff;

	for(int i=0; i<input.size(); ++i){

		if(input[i] != '=' && input[i] != '&' && input[i] != '!')
			tmpS[usingSpos].push_back(input[i]);

		else if(usingSpos == 0){
			isDiff = (input[i] == '!');
			usingSpos = 1;
			++i;
		}

		else{
			int a, b;

			if(str2int.count(tmpS[0]))
				a = str2int[tmpS[0]];
			else{
				str2int[tmpS[0]] = int2str.size();
				a = int2str.size();
				int2str.push_back(tmpS[0]);
			}
			if(str2int.count(tmpS[1]))
				b = str2int[tmpS[1]];
			else{
				str2int[tmpS[1]] = int2str.size();
				b = int2str.size();
				int2str.push_back(tmpS[1]);
			}

			if(isDiff == 0)
				same.push_back({a,b});
			else
				diff.push_back({a,b});

			tmpS[0] = tmpS[1] = "";
			usingSpos = 0;
			++i;
		}
	}
    
	string ansS;

	for(auto P : same)
		merge(P.first, P.second);
	
	for(int i=0; i<int2str.size(); ++i)
		group[find(i)].push_back(int2str[i]);

	for(int i=0; i<int2str.size(); ++i){

		int cntNumber = 0;
		for(auto &ss : group[i])
			cntNumber += (isdigit(ss[0]) || (ss[0]=='-'));
		if(cntNumber >= 2){
			cout << "0==1";
			return 0;
		}
		if(cntNumber == 1) hasNumber[i] = true;

		if(group[i].size() < 2) continue;

		int minLen = group[i][0].size(), minIdx = 0;
		for(int j=1; j<group[i].size(); ++j){
			if(group[i][j].size() < minLen){
				minLen = group[i][j].size();
				minIdx = j;
			}
		}
		string tmptmp = group[i][minIdx];
		for(int j=0; j<group[i].size(); ++j){
			if(j==minIdx) continue;
			ansS += group[i][j] + "==" + tmptmp + "&&";
		}

		swap(group[i][0], group[i][minIdx]);
	}

	set<pii> diffZip;
	for(auto &P : diff){

		int a = find(P.first), b = find(P.second);
		if(a==b){ 
			cout << "a!=a";
			return 0;
		}

		if(hasNumber[a] && hasNumber[b]) continue;
		diffZip.insert({min(a,b), max(a,b)});
	}

	for(auto &P : diffZip){
		int a = P.first, b = P.second;
		ansS += group[P.first][0] + "!=" + group[P.second][0] + "&&";
	}

	if(ansS.empty()){
		cout << "1==1";
		return 0;
	}
    
	ansS.pop_back(); ansS.pop_back(); 
	cout << ansS;
}
'''
