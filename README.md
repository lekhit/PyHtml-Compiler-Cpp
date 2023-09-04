# HTML Compiler

![License](https://img.shields.io/badge/license-MIT-blue)

**HTML Compiler** is a powerful tool that allows you to convert HTML files written in a Python-like syntax into runnable HTML, eliminating the need for closing tags in HTML documents. It is built in C++ and also supports embedded Python code, making it a versatile solution for web developers and content creators.

## Features

- Convert Python-like HTML syntax to actual runnable HTML.
- Seamless integration with Python code in input files.
- Automatic pre-processing of Python code for inclusion in the output HTML.
- Code blocks are determined based on indentation, simplifying your workflow.
- Implemented from scratch with a focus on efficiency and accuracy.

## How It Works

HTML Compiler functions as a compiler for your HTML files. You can write HTML code using a Python-like syntax, and the compiler will generate the corresponding HTML output. Here's a brief overview of the process:

1. **Input File**: Create an input file with your Python-like HTML code, including any embedded Python scripts.

2. **Compilation**: Run the HTML Compiler, and it will process your input file, recognizing the Python code and generating HTML output.

3. **Output HTML**: The compiler produces a fully functional HTML file with the desired structure, including the Python code pre-processed and integrated into the HTML as needed.

4. **Run and Deploy**: You can now run and deploy the generated HTML file just like any other HTML document.

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/html-compiler.git
   cd html-compiler
