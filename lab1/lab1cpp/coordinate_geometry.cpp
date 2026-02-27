//
// Created by Ege Engin on 27.02.2026.
//

#include "../../coordinate_geometry.h"
#include <iostream>
#include <cmath>

int main() {
    double x1, y1, x2, y2;

    std::cout << "Enter x1: ";
    std::cin >> x1;
    std::cout << "Enter y1: ";
    std::cin >> y1;
    std::cout << "Enter x2: ";
    std::cin >> x2;
    std::cout << "Enter y2: ";
    std::cin >> y2;

    double distance = std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));

    std::cout << "Distance: " << distance << "\n";

    return 0;
}