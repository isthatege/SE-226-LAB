//
// Created by Ege Engin on 27.02.2026.
//

#include "../../myFirstLabScript.h"
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "What is your name?\n";
    std::cin >> name;

    std::cout << "Hello " << name << ".\n";

    std::string student_id;
    std::cout << "What is your Student ID?\n";
    std::cin >> student_id;

    std::cout << "Your ID is " << student_id << ".\n";

    return 0;
}