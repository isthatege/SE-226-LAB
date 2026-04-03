//
// Created by Ege Engin on 3.04.2026.
//

#include "question4.h"
#include <iostream>

using namespace std;

double geometricSeries(int n, double r) {
    if (n == 0) {
        return 1;
    }
    
    double term = 1;
    for (int i = 0; i < n; i++) {
        term *= r;
    }
    
    return geometricSeries(n - 1, r) + term;
}

int main() {
    int n;
    double r;

    cout << "Enter the highest power (n for Gn): ";
    cin >> n;

    cout << "Enter the common ratio (r): ";
    cin >> r;

    cout << "Geometric Series Sum = " << geometricSeries(n, r) << endl;

    return 0;
}

