/**
 * A (mostly) exact solution to question 1. This is not how you should do any of this because, as
 * always, Manish has decided to teach a C++ while writing all his example code in C. For a C++
 * solution, see the other question 1 file (question-1-vectors.cpp).
 *
 * All the functions have been renamed to remove all the BS about "salespeople" and "revenue", since
 * this question is really just:
 * - Fill an array with values
 * - Find the maximum value in an array
 * - Find the average value in an array
 * - Find the index of a value in an array
 */

#include <iostream>
#include <sstream> // for printing arrays
#include <random>

// feel free to ignore this, it's purely for populating the lists
std::random_device dev;
std::mt19937 rng(dev());
int randInt(const int low, const int high) {
    std::uniform_int_distribution<int> dist(low, high);
    return dist(rng);
}

// using namespace std; // NEVER DO THIS. Seriously, don't.

// We pass the size of the array as another parameter because arrays are just pointers and there's
// no (simple) way to just find the size inside the function. Also, it's best practice to use const
// for any parameter that won't be changed in the function
std::string formatArray(const int arr[], const size_t arrSize) {
    // ostringstreams ("output stringstreams") behave like cout, but instead of printing what you
    // give them, they store it and let you get everything later as a formatted string. If you're
    // converting more than one or two values into a string, you should be using this.
    std::ostringstream stream{};

    stream << "[";
    for (size_t i{0}; i < arrSize; ++i) {
        stream << arr[i];
        if (i < arrSize - 1) {
            stream << ", ";
        }
    }
    stream << "]";

    return stream.str();
}

// Replaces pop_salesperson_id_arr and pop_revenues_arr. We don't use & to pass a reference to the
// array because arrays are just pointers, so a reference to them doesn't work.
void populateArray(int arr[], const size_t arrSize, const int minValue, const int maxValue) {
    for (size_t i{0}; i < arrSize; ++i) {
        arr[i] = randInt(minValue, maxValue);
    }
}

// replaces cal_average_revenues_generated
double arrayAverage(const int arr[], const size_t arrSize) {
    double sum{0};
    for (size_t i{0}; i < arrSize; ++i) {
        sum += arr[i];
    }
    return sum / arrSize;
}

// replaces find_max_revenues
int maxValue(const int arr[], const size_t arrSize) {
    int max = arr[0];
    for (int i{0}; i < arrSize; ++i) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// Replaces search_for_salesperson. Returns the index of the value, or -1 if the value wasn't found.
// We use int instead of size_t here because size_t is unsigned and can't be negative.
int findInArray(const int arr[], const size_t arrSize, const int value) {
    for (int i{0}; i < arrSize; ++i) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}

// constants should always be in ALL_CAPS
const int ARRAY_SIZE{10};
const int MIN_VALUE{1}; // minimum possible value
const int MAX_VALUE{10}; // maximum possible value

int main() {
    int numbers[ARRAY_SIZE];
    populateArray(numbers, ARRAY_SIZE, MIN_VALUE, MAX_VALUE);

    std::cout << "Numbers: " << formatArray(numbers, ARRAY_SIZE) << "\n"
              << "Average: " << arrayAverage(numbers, ARRAY_SIZE) << "\n"
              << "Maximum value: " << maxValue(numbers, ARRAY_SIZE) << "\n";

    // (try to) find every possible number
    std::cout << "Finding values...\n";
    for (int n{1}; n <= 10; ++n) {
        std::cout << n << ": ";

        int index = findInArray(numbers, ARRAY_SIZE, n);
        if (index == -1) {
            std::cout << "Not found\n";
        }
        else {
            std::cout << index << "\n";
        }
    }

    return 0;
}
