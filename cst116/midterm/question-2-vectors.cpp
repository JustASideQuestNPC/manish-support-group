/**
 * A revision of question 2 that does everything the C++ way.
 *
 * All of the functions have been renamed to actually make sense, and a few of them have been
 * added/removed (also to actually make sense).
 */

#include <iostream>
#include <vector> // vectors are arrays, but you don't have to manage your memory
#include <algorithm> // for finding values in a vector
#include <sstream> // for printing vectors
#include <random>

// using namespace std; // NEVER DO THIS. Seriously, don't.

// rand() is what manish uses, but it's not actually random and is biased toward lower numbers
std::random_device dev;
std::mt19937 rng(dev());
int randInt(const int low, const int high) {
    std::uniform_int_distribution<int> dist(low, high);
    return dist(rng);
}

// Replaces print_random_values_arr, and returns a string instead of printing the values directly.
// When using strings, vectors, or anything else that's more complicated than just a number as a
// parameter, use a reference so the entire thing doesn't get copied every time. If the function
// never changes that thing, it's best practice to make it a const reference.
std::string formatVector(const std::vector<int> &vec) {
    // ostringstreams ("output stringstreams") behave like cout, but instead of printing what you
    // give them, they store it and let you get everything later as a formatted string. If you're
    // converting more than one or two values into a string, you should be using this.
    std::ostringstream stream{};

    stream << "[";
    // size_t is the actual type used for vector indexes. It's basically just a special type of int.
    for (size_t i{0}; i < vec.size(); ++i) {
        stream << vec[i];

        if (i < vec.size() - 1) {
            stream << ", ";
        }
    }
    stream << "]";

    return stream.str();
}

// manish just did this in main, but it should be its own function
std::vector<int> randomVector(const int size, const int minValue, const int maxValue) {
    // vectors are "templated" which means they can hold any type, so we use <int> to specify that
    // we want this one to hold integers
    std::vector<int> vec;

    for (int i{0}; i < size; ++i) {
        // push_back adds a value to the end of a vector (if this were a raw array like in the
        // original question, we'd have to do it manually)
        vec.push_back(randInt(minValue, maxValue));
    }

    return vec;
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

// replaces search_array
bool valueInVector(const std::vector<int> &vec, const int value) {
    // "auto" tells the compiler to figure out what the type of a variable is based on what's being
    // assigned to it. If you use it a ton it'll make things confusing, but it's nice for things
    // with insanely long typenames. If you're curious, pos is a
    // "std::_Vector_const_iterator<std::_Vector_val<std::_Simple_types<int>>>"
    auto pos = std::find(vec.begin(), vec.end(), value);
    return pos != vec.end();
}

// Replaces half of find_max_min_arr_values. I've split it into two functions so that nobody has
// to deal with reference parameters.
int minValue(const std::vector<int> &vec) {
    // technically i should check for an empty vector, but in this case i know that the vector will
    // always have at least 1 item in it
    int min = vec[0];
    for (size_t i{1}; i < vec.size(); ++i) {
        if (vec[i] < min) {
            min = vec[i];
        }
    }
    return min;
}

// replaces the other half of find_max_min_arr_values
int maxValue(const std::vector<int> &vec) {
    // technically i should check for an empty vector, but in this case i know that the vector will
    // always have at least 1 item in it
    int max = vec[0];
    for (size_t i{1}; i < vec.size(); ++i) {
        if (vec[i] > max) {
            max = vec[i];
        }
    }
    return max;
}

// constants should always be in ALL_CAPS
const int VECTOR_SIZE{10};
const int MIN_VALUE{1}; // minimum possible value
const int MAX_VALUE{10}; // maximum possible value
const int NUM_ALLOWED_GUESSES{5};

int main() {
    std::vector<int> numbers = randomVector(VECTOR_SIZE, MIN_VALUE, MAX_VALUE);
    std::cout << "Generated numbers\n"
              << "Minimum value: " << minValue(numbers) << "\n"
              << "Maximum value: " << maxValue(numbers) << "\n";

    for (int i = 0; i < NUM_ALLOWED_GUESSES; ++i) {
        std::cout << "Guesses remaining: " << NUM_ALLOWED_GUESSES - i << "\n";
        int guess = getGuess();
        if (valueInVector(numbers, guess)) {
            std::cout << "That number is in the list!\n";
        }
        else {
            std::cout << "That number is not in the list :(\n";
        }
    }

    return 0;
}
