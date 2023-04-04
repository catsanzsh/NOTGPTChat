import openai
import os
import subprocess
import platform
from pathlib import Path
from tkinter import messagebox

# Set the API key
openai.api_key = "#"

import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title
        self.title("ChatGPT 1.0 - Your answer to everything [C] Flames AI - Openai GPT-3 [GPT4? ]")
        self.resizable(False, False)

        # Create a text input for the user to enter a description of the desired code
        self.description_input = tk.Entry(self, width=30)
        self.description_input.pack()
        self.description_input.insert(0, "Enter code description")

        # Create a dropdown menu to select the programming language
        self.language_var = tk.StringVar(self)
        self.language_var.set("Python")  # default value
        self.language_dropdown = tk.OptionMenu(self, self.language_var, "EPIC GAMES COMPILER [TEACHES YOU BLUEPRINTS COMPILES C++,",",","GCC COMPILER 1.0","Unity AI COPILOT  ASSET AND CODE GENERATOR 1.0 DEMO","GPT-X AUTOCOMPILE AUTOMATICLLY DETECTS EVERYTHING","Toontoonemu GCC Cross Compiler [Automaticlly compiles the format and installs everything also generates code","Python", "HTML", "C#", "Rust", "Assembly", "Autotranslate", "Query Google", "OpenAI CODEX (BETA)")
        self.language_dropdown.pack()

        # Create a button to generate the code
        self.generate_button = tk.Button(self, text="Generate", command=self.generate_code)
        self.generate_button.pack()

        # Create a button to save the code
        self.save_button = tk.Button(self, text="Save", command=self.save_code)
        self.save_button.pack()

        # Create a button to compile the code
        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code)
        self.compile_button.pack()

        # Create a text area to display the generated code
        self.code_display = tk.Text(self)
        self.code_display.pack()

    def generate_code(self):
        # Get the user's input description and selected programming language
        description = self.description_input.get()
        language = self.language_var.get()

        # Use the ChatGPT API to generate the code
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a {language} program that {description}",
            temperature=0.16,
            max_tokens=2048,
            top_p=0.32,
            frequency_penalty=0.64,
            presence_penalty=0.24
        )
        code = response["choices"][0]["text"]

        # Display the generated code
        self.code_display.delete(1.0, tk.END)
        self.code_display.insert(1.0, code)

    def save_code(self):
        # Open a file dialog to choose where to save the code
        file_path = filedialog.asksaveasfilename()

        # Write the code to the file
        with open(file_path, "w") as f:
            f.write(self.code_display.get(1.0, tk.END))

    def compile_code(self):
        language = self.language_var.get()
        src_code = self.code_display.get(1.0, tk.END)

        # Detect the current operating system
        current_os = platform.system()

        # Set the appropriate output file extension and output directory based on the OS
        if current_os == "Windows":
            output_ext = ".exe"
            documents_folder = os.path.expanduser("~/")  
            documents_folder = os.path.expanduser("~/Documents")
        elif current_os == "Linux" or current_os == "Darwin":  # Darwin is macOS
            output_ext = ""
            documents_folder = os.path.expanduser("~/Documents")
        else:
            tk.messagebox.showerror("Error", f"Unsupported operating system: {current_os}")
            return

        # Create the "SRC" folder within the Documents directory if it doesn't exist
        src_folder = os.path.join(documents_folder, "SRC")
        os.makedirs(src_folder, exist_ok=True)

        # Save the source code to a temporary file
        temp_src_file = os.path.join(src_folder, f"temp_src.{language.lower()}")
        with open(temp_src_file, "w") as f:
            f.write(src_code)

        # Compile the code and generate the personalized output file
        output_file = os.path.join(src_folder, f"output{output_ext}")
        if language == "Python":
            subprocess.run(["python", "-c", f"import py_compile; py_compile.compile('{temp_src_file}', '{output_file}')"])
        elif language == "C#":
            subprocess.run(["csc", "/out:{}".format(output_file), temp_src_file])
        # Add more compile commands for other languages as needed

        # Show a message box with the output file location
        tk.messagebox.showinfo("Compilation Success", f"Compiled output file saved to {output_file}")

text_editor = TextEditor()
text_editor.mainloop()
å
