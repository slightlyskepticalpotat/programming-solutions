// checking if ManchurioX's solution works

#include <bits/stdc++.h>

using namespace std;

int main() {

    int a, b, n; cin >> a >> b >> n;
    a = a + 1;
    
    string result = "";
    bool overflow = false;

    int cc = 0;
    int rows = 1;

    regex e(" ");
    regex_token_iterator<string::iterator> end;

    string t; getline(cin, t);

    for (int i=0; i<n; i++) {
        string s; getline(cin, s);
        if (overflow) continue;
        regex_token_iterator<string::iterator> words(s.begin(), s.end(), e, -1);
        while (words != end) {
            string current = *words++;
            if (cc + current.size() + 1 <= a) {
                cc += current.size() + 1;
                result += current + " ";
            }
            else if (rows == b) {
                result = "Terminal Overflow ";
                overflow = true;
            }
            else {
                cc = current.size() + 1;
                rows++;
                result = result.substr(0, result.size()-1) + "\n" + current + " ";
            }
        }
        result += '\n';
        cc = 0;
    }

    cout << result.substr(0, result.size()-1) << endl;

}