/**
 * A revision of question 1 that does everything the C++ way.
 *
 * All the functions have been renamed to remove all the BS about "salespeople" and "revenue", since
 * this question is really just:
 * - Fill an array with values
 * - Find the maximum value in an array
 * - Find the average value in an array
 * - Find the index of a value in an array
 */

#include <iostream>
#include <vector> // vectors are arrays, but you don't have to manage your memory
#include <algorithm> // for finding values in a vector
#include <sstream> // for printing vectors
#include <random>

// feel free to ignore this, it's purely for populating the lists
std::random_device dev;
std::mt19937 rng(dev());
int randInt(const int low, const int high) {
    std::uniform_int_distribution<int> dist(low, high);
    return dist(rng);
}

// using namespace std; // NEVER DO THIS. Seriously, don't.

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

// Replaces pop_salesperson_id_arr and pop_revenues_arr. This returns a vector of integers since
// setting it through a reference is entirely unnecessary here.
std::vector<int> randomVector(const int size, const int minValue, const int maxValue) {
    // vectors are "templated" which means they can hold any type, so we use <int> to specify that
    // we want this one to hold integers
    std::vector<int> vec; // {} initializes the vector but leaves it empty

    for (int i{0}; i < size; ++i) {
        // push_back adds a value to the end of a vector (if this were a raw array like in the
        // original question, we'd have to do it manually)
        vec.push_back(randInt(minValue, maxValue));
    }

    return vec;
}

// replaces cal_average_revenues_generated
double vectorAverage(const std::vector<int> &vec) {
    double sum{0}; // you could also use "sum = 0", but brackets are usually considered "better"

    // "int n : vec" creates a "range-based for loop". It's effectively the same as using
    // "size_t i{0}; i < vec.size(); ++i" and then setting n to vec[i].
    for (int n : vec) {
        sum += n;
    }

    return sum / vec.size();
}

// replaces find_max_revenues
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

// Replaces search_for_salesperson. Returns the index of the value, or -1 if the value wasn't found.
// We use int instead of size_t here because size_t is unsigned and can't be negative.
int findInVector(const std::vector<int> &vec, const int value) {
    // "auto" tells the compiler to figure out what the type of a variable is based on what's being
    // assigned to it. If you use it a ton it'll make things confusing, but it's nice for things
    // with insanely long typenames. If you're curious, pos is a
    // "std::_Vector_const_iterator<std::_Vector_val<std::_Simple_types<int>>>"
    auto pos = std::find(vec.begin(), vec.end(), value);
    // check if the value is in the array
    if (pos == vec.end()) {
        return -1;
    }

    return std::distance(vec.begin(), pos); // weird pointer arithmetic
}

// constants should always be in ALL_CAPS
const int VECTOR_SIZE{10};
const int MIN_VALUE{1}; // minimum possible value
const int MAX_VALUE{10}; // maximum possible value

int main() {
    // create a vec of 5 random numbers that are all between 1 and 10
    std::vector<int> numbers = randomVector(VECTOR_SIZE, MIN_VALUE, MAX_VALUE);

    // this is why i prefer functions that return strings over functions that directly print things
    std::cout << "Numbers: " << formatVector(numbers) << "\n"
              << "Average: " << vectorAverage(numbers) << "\n"
              << "Maximum value: " << maxValue(numbers) << "\n";

    // (try to) find every possible number
    std::cout << "Finding values...\n";
    for (int n{1}; n <= 10; ++n) {
        std::cout << n << ": ";

        int index = findInVector(numbers, n);
        if (index == -1) {
            std::cout << "Not found\n";
        }
        else {
            std::cout << index << "\n";
        }
    }

    return 0;
}
