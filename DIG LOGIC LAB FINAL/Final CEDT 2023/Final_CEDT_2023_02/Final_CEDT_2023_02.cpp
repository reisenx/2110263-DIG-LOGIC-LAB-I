#include<bits/stdc++.h>
using namespace std;

int main()
{
    // Input
    int A;
    cout << "Input A (0-65535): "; cin >> A;

    // Calculate floor nth root (Binary Search)
    int clock = 0;
    int low = 1, high = A;
    bool busy = low <= high;
    while(busy)
    {
        // Calculate compare value
        int mid = (low + high)/2;
        int product = mid * mid;
        bool LShift = product <= A;
        bool HShift = product > A;
        // Output each clock process
        cout << "----- Clock " << clock << " -----\n";
        cout << "Consider [low, mid, high]: [" << low << ", " << mid << ", " << high << "]\n";
        cout << "Value [current, A]: [" << product << ", " << A << "]\n";
        if(LShift)
        {
            cout << "Process: shift low from " << low;
            low = mid + 1;
            cout << " to " << low << "\n";
        }
        if(HShift)
        {
            cout << "Process: shift high from " << high;
            high = mid - 1;
            cout << " to " << high << "\n";
        }

        // Update value
        busy = (low <= high);
        clock++;
    }

    // Output results
    cout << "\n----- END -----\n";
    cout << "Result = " << high << "\n";
    cout << "Uses " << clock << " clock\n";
    cout << "--------------------";
    return 0;
}