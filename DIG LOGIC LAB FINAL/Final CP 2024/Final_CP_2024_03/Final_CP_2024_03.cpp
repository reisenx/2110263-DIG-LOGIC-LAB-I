#include<bits/stdc++.h>
using namespace std;

int A, first, second, third;
int peak = 0, cnt = 0;
bool input, load, reset, ready;

void shift()
{
    third = second;
    second = first;
    first = A;
}

void calculatePeak()
{
    int half01 = first - second;
    int half02 = second - third;
    if(half01 < 0) half01 *= -1;
    if(half02 < 0) half02 *= -1;
    int sum = half01 + half02;

    if((sum > peak) && ready) peak = sum;
}

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
        cnt++;

        // Circuit signal
        load = (!reset) && input;
        ready = cnt > 2;

        // Shift value and calculate peak
        shift();
        calculatePeak();
        if(reset)
        {
            first = 0;
            second = 0;
            third = 0;
            cnt = 0;
            peak = 0;
        }

        // Output
        cout << "----- Result " << clock << " -----\n";
        cout << "Peak: " << peak << "\n";
        cout << "First: " << first << "\n";
        cout << "Second: " << second << "\n";
        cout << "Third: " << third << "\n";
        cout << "----------------------\n\n";

        clock++;
    }
    return 0;
}