#include "lab3.h"
#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    int max = *arr;
    for (int i = 1; i < size; i++) {
        if (*(arr + i) > max) {
            max = *(arr + i);
        }
    }
    return max;
}

void reverseArray(int* arr, int size) {
    int* left = arr;
    int* right = arr + size - 1;
    while (left < right) {
        swapValues(left, right);
        left++;
        right--;
    }
}

int* createArray(int size) {
    return new int[size];
}

void deleteArray(int* arr) {
    delete[] arr;
}

int main() {
    cout << "Creating dynamic array..." << endl;
    int size;
    cout << "Enter array size: ";
    cin >> size;
    int* myArray = createArray(size);

    cout << "enter values: ";
    for (int i = 0; i < size; i++) {
        cin >> myArray[i];
    }

    cout << "Array elements:" << endl;
    printArray(myArray, size);
    cout << "Maximum Element: " << findMax(myArray, size) << endl;

    cout << "----------------------------------" << endl;

    int a = 5, b = 8;
    cout << "Swapping 2 numbers" << endl;
    cout << "Before swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    swapValues(&a, &b);
    cout << "After swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "----------------------------------" << endl;

    cout << "Reversing array..." << endl;
    reverseArray(myArray, size);
    cout << "Array after reverseArray:" << endl;
    printArray(myArray, size);

    cout << "----------------------------------" << endl;

    cout << "Deleting array..." << endl;
    deleteArray(myArray);
    myArray = nullptr;
    cout << "Memory released successfully." << endl;

    return 0;
}