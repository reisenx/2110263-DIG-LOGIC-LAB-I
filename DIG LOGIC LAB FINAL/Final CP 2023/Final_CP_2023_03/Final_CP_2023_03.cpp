#include<bits/stdc++.h>
using namespace std;

int A, first, second;
bool input, reset;

int main()
{
    int clock = 1;
    while(true)
    {
        // Input
        cout << "----- Clock " << clock << " -----\n";
        cout << "Input A: "; cin >> A;
        cout << "Input? (0/1): "; cin >> input;
        cout << "Reset? (0/1): "; cin >> reset;

        // Circuit signal
        bool s1 = (A > first);
        bool s2 = !(A > first) && A > second;

        // Manage second
        if(s1) second = first;
        if(s2) second = A;

        // Manage first
        if(s1) first = A;

        if(reset) { first = 0; second = 0; }

        // Output
        cout << "----- Result " << clock << " -----\n";
        cout << "First: " << first << "\n";
        cout << "Second: " << second << "\n";
        cout << "----------------------\n\n";

        clock++;
    }
    return 0;
}