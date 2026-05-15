#include <iostream>
#include <vector>
#include <climits>

using namespace std;


void merge(vector<int> &v, int l, int m, int r){
    int n1 = m - l + 1;
    int n2 = r - m;
    vector<int> L(n1 + 1);
    vector<int> R(n2 + 1);
    for(int i = 0; i < n1; i++){
        L[i] = v[l + i];
    }
    for(int i = 0; i < n2; i++){
        R[i] = v[m + i + 1];
    }
    L[n1] = INT_MAX;
    R[n2] = INT_MAX;
    int i = 0;
    int j = 0;
    for(int k = l; k <= r; k++){
        if(L[i] <= R[j]){
            v[k] = L[i];
            i++;
        }else{
            v[k] = R[j];
            j++;
        }
    }

}

void mergeSort(vector<int> &v, int l, int r){
    if(l < r){
        int m = (l + r) / 2;
        mergeSort(v, l, m);
        mergeSort(v, m + 1, r);
        merge(v, l, m, r);
    }

}

int main(){
    vector<int> v = {1, 3, 5, 7, 9, 2, 4, 6, 8, 10};
    mergeSort(v, 0, v.size() - 1);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}