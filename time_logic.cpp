//
// Created by Ege Engin on 27.02.2026.
//

#include "time_logic.h"
#include <iostream>
int main() {
    int total_seconds;
    std::cout << "Enter a total number of seconds:\n";
    std::cin >> total_seconds;
    int hours = total_seconds / 3600;
    int remaining_seconds = total_seconds % 3600;

    int minutes = remaining_seconds / 60;
    int seconds = remaining_seconds % 60;

    std::cout << total_seconds << " seconds is " << hours << " hours, "
              << minutes << " minutes, and " << seconds << " seconds.\n";

    return 0;
}
