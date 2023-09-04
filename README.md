# Cpp Compiler

![License](https://img.shields.io/badge/license-MIT-blue)

 ## Image speaks louder than words
 
   ![Screenshot 2023-09-05 at 1 35 16 AM](https://github.com/lekhit/Cpp-Compiler/assets/82832791/efe0a3a2-9c4c-479d-a16f-ce30dafe3111)



**Cpp Compiler** is a powerful tool that allows you to convert HTML files written in a Python-like syntax into runnable HTML, eliminating the need for closing tags in HTML documents. It is built in C++ and also supports embedded Python code, making it a versatile solution for web developers and content creators.

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
   git clone https://github.com/lekhit/Cpp-Compiler.git
   cd Cpp-Compiler
   ```
2. Compile the code with g++:
   ```bash
   g++ -std="c++2a" compiler.cpp -o compiler.out
   ```
3. Execute the binary ensuring that python3 is present in your system.
   ```bash
   ./compiler.out <input.txt> <output.html>
   ```
## Results
The results are provided as <output.html> it is a direct runnable HTML file. Simply run the file on browser.

## Demo
### Hello world (Basic)
> Input File
```html
html:
    head:
        title:
            "SImpLE"
    body:
        div class="hello":
            "hello world"
        script:
            alert("this is useless alert")
```
> Output File
```html
<html>
<head>
<title>
            "SImpLE"
</title>
</head>
<body>
<div class="hello">
            "hello world"
</div>
<script>
            alert("this is useless alert")
</script>
</body>
</html>
```
### Using the Python TAG
> Input File
```html
html:
  head:
    title:
      Hello world
    link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css" rel="stylesheet":
  body:
    div class=" h-screen flex  mx-auto px-4 ":
      div class="mx-16 h-full grid grid-cols-1 gap-4 items-center":
        div:
          h1 class=" text-6xl font-bold text-gray-800":
            Hi, my name is 
              span class=" inline text-green-300":
                Lekhit Borole
          p class="mt-3 text-5xl text-gray-800 ":
            Turning Code into Solutions, One Line at a Time.
          div class="mt-7 grid gap-3 w-full sm:inline-flex":
            a class="   bg-blue-600 text-sm lg:text-base text-white py-3 px-4 font-medium rounded-md" href="#":
              Know More
            a class="  text-sm py-3 px-4  lg:text-base  border shadow-sm font-medium rounded-md " href="#":
              Let's Connect
    div class="grid grid-cols-3 gap-4 m-8 ":
      python:
        projects=['Book-recommendation Backend','Book-recommendation Frontend','Cpp-Compiler']
        for item in projects:
          print(f"""
          div class="w-[300px] p-4 h-32 rounded text-center border text-2xl text-gray-800 font-medium ":
            {item}
            """)
    script:
      alert('welcome to a new way')
```
> Output

   ![Screenshot 2023-09-05 at 1 35 16 AM](https://github.com/lekhit/Cpp-Compiler/assets/82832791/efe0a3a2-9c4c-479d-a16f-ce30dafe3111)

