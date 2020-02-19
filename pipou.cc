#include <bits/stdc++.h>

using namespace std;
using VI = vector<int>;
using VVI = vector<VI>;
using VB = vector<bool>;

tuple<VVI, int, int> parse() {
    char c;
    string s;
    int n, m;
    getline(cin, s);
    stringstream ssfirst(s);
    ssfirst >> n >> c >> m;
    VVI G(m);
    for(int i = 0; i < m; ++i) {
	getline(cin, s);
	stringstream ss(s);
	int x;
	ss >> x;
	G[i].push_back(x);
	while(ss >> c >> x) G[i].push_back(x);
    }
    return make_tuple(G, n, m);
}

inline void switch_li(VB &lights, int &score, int i) {
    if(lights[i]) score --;
    else score++;
    lights[i] = ! lights[i];
}

inline void switch_sw(VVI &G, VB &lights, VB &switches, int &score, int i) {
    for(int j : G[i]) switch_li(lights, score, j);
    switches[i] = ! switches[i];
}

void test(VVI &G, VB &lights, VB &switches, int &best_ans, int &ans, int n, int m, int lst, int k) {
    if(k == 0) {
        if(ans > best_ans) {
	    best_ans = ans;
	    cout << "NEW " <<  ans << endl;
	    for(int i = 0; i < m; ++i) if(switches[i]) cout << i << endl;
	}
	return;
    }
    for(int i = lst; i < m; ++i) {
	switch_sw(G, lights, switches, ans, i);
	test(G, lights, switches, best_ans, ans, n, m, i + 1, k - 1);
	switch_sw(G, lights, switches, ans, i);
    }
}

int main() {
    auto t = parse();
    VVI G = get<0>(t);
    int n = get<1>(t), m = get<2>(t);
    VB lights(n, false), switches(m, false);
    int ans = 0, best_ans = 0;
    //test(G, lights, switches, best_ans, ans, n, m, 0, 4);
    VI partial_solution = {1, 53, 118, 187};
}
