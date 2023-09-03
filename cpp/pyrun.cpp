#include <Python.h>
#include <iostream>

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Check if Python was initialized successfully
    if (Py_IsInitialized()) {
        // Python code to execute as a string
        const char* pythonCode = "print('Hello from Python!')";

        // Execute the Python code
        int result = PyRun_SimpleString(pythonCode);

        // Check the result
        if (result != 0) {
            PyErr_Print();
        }
    } else {
        std::cerr << "Failed to initialize Python." << std::endl;
        return 1;
    }

    // Finalize the Python interpreter when done
    Py_Finalize();
    return 0;
}
