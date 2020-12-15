// https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int binary_search(vector<int>& array, int low, int high, int key){
    // the array is actually a vector
    while (high-low > 1){
        int middle = low + (high-low) / 2;
        if (array[middle] >= key)
            high = middle;
        else
            low = middle;
    }
    return high;
}

int lis(vector<int>& array){
    if (array.size() == 0)
        return 0;
    // stores the current best sequence
    vector<int> best(array.size(), 0);
    int length = 1;
    best[0] = array[0];
    for (size_t i=1; i<array.size(); i++){
        // if smaller than current smallest best value, new smallest value
        if (array[i] < best[0])
            best[0] = array[i];
        // else extends the current best sequence e.g. (1) to (1, 5)
        else if (array[i] > best[length-1])
            best[length++] = array[i]; // length+=1
        // else update all sequences e.g. replace (1,5) to (1,2)
        else
            best[binary_search(best, -1, length-1, array[i])] = array[i];
    }
    return length;
}

int main(){
    int placeholder;
    cin >> placeholder;

    int ree;
    vector<int> a;
    while (cin >> ree){
        a.push_back(ree);
    }

    printf("%d\n", lis(a));
    return 0;
}