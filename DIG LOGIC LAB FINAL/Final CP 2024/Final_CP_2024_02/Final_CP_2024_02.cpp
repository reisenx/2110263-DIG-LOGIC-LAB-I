#include<bits/stdc++.h>
using namespace std;

vector<int> wireSpliter(int &R)
{
    vector<int> binary(4,0);
    if(R >= 8) { binary[3] = 1; R -= 8; }
    if(R >= 4) { binary[2] = 1; R -= 4; }
    if(R >= 2) { binary[1] = 1; R -= 2; }
    if(R >= 1) { binary[0] = 1; R -= 1; }
    return binary;
}

int powerR(vector<int> &R, int &X)
{
    int product = 1;
    if(R[0] == 1) product *= X;
    else product = product;

    int X2 = X * X;
    if(R[1] == 1) product *= X2;
    else product = product;

    int X4 = X2 * X2;
    if(R[2] == 1) product *= X4;
    else product = product;

    int X8 = X4 * X4;
    if(R[3] == 1) product *= X8;
    else product = product;

    return product;
}

int main()
{
    // Input
    int A, R;
    cout << "Input A (0-65535): "; cin >> A;
    cout << "Input R (1-15): "; cin >> R;

    // Use wire spliter
    vector<int> bin = wireSpliter(R);

    // Calculate floor square root
    int X = 2, product = 1, nroot;
    bool isRoot1 = (R == 1);
    bool busy = (product <= A);
    if(isRoot1) busy = false;

    if(isRoot1) nroot = A;
    else
    {
        while(busy)
        {
            X++;
            product = powerR(bin, X);
            busy = (product <= A);
        }
        nroot = X - 1;
    }

    // Output
    cout << "Result: " << nroot;
    return 0;
}