/**
 * A (mostly) exact solution to question 2. This is not how you should do any of this because, as
 * always, Manish has decided to teach a C++ while writing all his example code in C. For a C++
 * solution, see the other question 2 file (question-2-vectors.cpp).
 *
 * Most of these functions have been renamed to actually make sense.
 */

#include <iostream>
#include <random>
#include <sstream> // for populating arrays

// using namespace std; // NEVER DO THIS. Seriously, don't.

// rand() is what manish uses, but it's not actually random and is biased toward lower numbers
std::random_device dev;
std::mt19937 rng(dev());
int randInt(const int low, const int high) {
    std::uniform_int_distribution<int> dist(low, high);
    return dist(rng);
}

// Replaces print_random_values_arr, and returns a string instead of printing the values directly.
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

// replaces get_user_guess
int getGuess() {
    int guess;
    std::cout << "Enter your guess:\n";
    std::cin.clear(); // clear out any thing left from previous guesses
    std::cin >> guess;

    // fail() returns true if the input wasn't an integer
    while (std::cin.fail()) {
        // prevent cin from continuously reading itself
        std::cin.clear();
        std::cin.ignore(10000, '\n');

        std::cout << "You must enter a number!\nEnter your guess:\n";
        std::cin >> guess;
    }

    return guess;
}

// Manish just did this in main, but it should be its own function. We don't use & to pass a
// reference to the array because arrays are just pointers, so a reference to them doesn't work.
void populateArray(int arr[], const size_t arrSize, const int minValue, const int maxValue) {
    for (size_t i{0}; i < arrSize; ++i) {
        arr[i] = randInt(minValue, maxValue);
    }
}

// replaces search_array
bool valueInArray(const int arr[], const size_t arrSize, const int value) {
    for (size_t i{0}; i < arrSize; ++i) {
        if (arr[i] == value) {
            return true;
        }
    }
    return false;
}

// This should really be two separate functions. Also, this is a void function because I cannot
// find a reason why this should return a boolean (I think Manish wants it to return whether it
// was successful, but you can't really fail this).
void getMinMaxValue(const int arr[], const size_t arrSize, int &minResult, int &maxResult) {
    int min{arr[0]}, max{arr[0]};
    for (size_t i{1}; i < arrSize; ++i) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    minResult = min;
    maxResult = max;
}

// constants should always be in ALL_CAPS
const int ARRAY_SIZE{10};
const int MIN_VALUE{1}; // minimum possible value
const int MAX_VALUE{10}; // maximum possible value
const int NUM_ALLOWED_GUESSES{5};

int main() {
    int numbers[ARRAY_SIZE];
    populateArray(numbers, ARRAY_SIZE, MIN_VALUE, MAX_VALUE);
    int minValue, maxValue;
    getMinMaxValue(numbers, ARRAY_SIZE, minValue, maxValue);

    std::cout << "Generated numbers\n"
              << "Minimum value: " << minValue << "\n"
              << "Maximum value: " << maxValue << "\n";

    for (int i = 0; i < NUM_ALLOWED_GUESSES; ++i) {
        std::cout << "Guesses remaining: " << NUM_ALLOWED_GUESSES - i << "\n";
        int guess = getGuess();
        if (valueInArray(numbers, ARRAY_SIZE, guess)) {
            std::cout << "That number is in the list!\n";
        }
        else {
            std::cout << "That number is not in the list :(\n";
        }
    }

    return 0;
}
