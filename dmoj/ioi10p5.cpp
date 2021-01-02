#include <bits/stdc++.h>

using namespace std;

vector<int> cards[25];

void play()
{
    for (int i = 1; i <= 50; i++) {
        cards[faceup(i) - 'A'].push_back(i);
    }
    for (int i = 0; i < 25; i++) {
        for (auto j: cards[i]) {
            faceup(j);
        }
    }
}