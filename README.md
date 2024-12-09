# Parser Project

## Requirements

I ran my parser using the following:

- **Programming Language:** Python 3
- **Libraries:** ANTLR version 4.13.2
- **Development Environment:** Visual Studio Code (VS Code)
- **Operating System:** macOS

### Steps for Setup:

1. **Install Python 3**  
   Ensure Python 3 is installed. You can download it from [here](https://www.python.org/downloads/).

2. **Install ANTLR**
   - Download ANTLR version 4.13.2 from [here](https://www.antlr.org/)
   - Copy the downloaded tool where you usually put third-party java libraries
        - sudo cp antlr-4.13.2-complete.jar /usr/local/lib/
   - Add the tool to your CLASSPATH. Add it to your startup script
        - export CLASSPATH=".:/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
   - Add aliases to your startup script to simplify the usage of ANTLR
        - alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
        - alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

4. **Setup in VS Code**
   - Install the Python Extension for VS Code
   - Install the ANTLR Extension for syntax highlighting and parser integration in VS Code

## How to Use/Run the Parser

1. **Generate Lexer and Parser** - Once ANTLR is installed and the .g4 grammar file is ready, run the following command in your terminal:
   - antlr4 -Dlanguage=Python3 alex_savas_grammar.g4

2. **Run the Parser** - After generating the lexer and parser, you can run the Python script that utilizes the generated files to parse input:
   - python <parser_file>.py

## Demo

For a visual demonstration of the parser in action, you can refer to this video:
- https://github.com/user-attachments/assets/665020bb-bbdc-4cae-9391-b4339c38eb01


