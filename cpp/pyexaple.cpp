#include <cstdlib>  // For system() function

int main() {
    // Execute a Python file (replace "your_script.py" with your actual Python file)
    int returnValue = std::system("python3 pyrun.py");

    // Check the return value to determine if the execution was successful
    if (returnValue == 0) {
        // Python script executed successfully
        // You can add further logic here
    } else {
        // An error occurred during execution
        // You can handle the error or log it
    }

    return 0;
}
