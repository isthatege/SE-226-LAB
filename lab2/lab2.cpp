#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int digitSum(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

void task1() {
    int n;
    cout << "Please enter a positive integer greater than 9: ";
    while (true) {
        cin >> n;
        if (n > 9) break;
        cout << "Invalid input. Please enter a positive integer greater than 9: ";
    }

    int steps = 0;
    cout << n;

    while (n >= 10) {
        n = digitSum(n);
        steps++;
        cout << " -> " << n;
    }

    cout << endl;
    cout << "Final value: " << n << endl;
    cout << "Total steps: " << steps << endl;
}

void task2() {
    int n;
    cout << "Please enter a number between 10 and 100: ";
    while (true) {
        cin >> n;
        if (n >= 10 && n <= 100) break;
        cout << "Invalid input. Please enter a number between 10 and 100: ";
    }

    int fizzCount = 0, buzzCount = 0, fizzBuzzCount = 0;

    for (int i = 1; i <= n; ++i) {
        if (i % 7 == 0) {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzBuzzCount++;
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        } else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        } else {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count : " << fizzCount << endl;
    cout << "Buzz count : " << buzzCount << endl;
    cout << "FizzBuzz count: " << fizzBuzzCount << endl;
}

void task3() {
    int n;
    cout << "Please enter a number between 3 and 9: ";
    while (true) {
        cin >> n;
        if (n >= 3 && n <= 9) break;
        cout << "Invalid input. Please enter a number between 3 and 9: ";
    }

    for (int i = 1; i <= 2 * n - 1; ++i) {
        int k = n - abs(n - i);
        for (int j = 1; j <= k; ++j) {
            cout << j;
        }
        cout << endl;
    }
}

int main() {
    cout << "--- Task 1 ---" << endl;
    task1();
    cout << "\n--- Task 2 ---" << endl;
    task2();
    cout << "\n--- Task 3 ---" << endl;
    task3();
    return 0;
}
