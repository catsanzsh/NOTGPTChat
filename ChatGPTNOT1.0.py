import openai
import os
import subprocess
import platform
from pathlib import Path
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog

# Set the API key
openai.api_key = "#" 

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title("ChatGPT 1.0 - Your answer to everything [C] Flames AI - Openai GPT-3 [GPT4?]")
        self.resizable(False, False)

        self.description_input = tk.Entry(self, width=30)
        self.description_input.pack()
        self.description_input.insert(0, "Enter code description")

        self.language_var = tk.StringVar(self)
        self.language_var.set("Python")
        self.language_dropdown = tk.OptionMenu(
            self,
            self.language_var,
            "Ultra 64 Compiler",
            "Nintendo DS Compiler",
            "GBA SDK",
            "Linux GCC",
            "GPT4 API CALLER",
            "COMPILER AIO",
            "GPT-X AUTOCOMPILE AUTOMATICLLY DETECTS EVERYTHING",
            "Toontoonemu GCC Cross Compiler [Automatically compiles the format and installs everything also generates code",
            "Python",
            "HTML",
            "C#",
            "Rust",
            "Assembly",
            "Autotranslate",
            "Query Google",
            "OpenAI CODEX (BETA)"
        )
        self.language_dropdown.pack()

        self.generate_button = tk.Button(self, text="Generate", command=self.generate_code)
        self.generate_button.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_code)
        self.save_button.pack()

        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code)
        self.compile_button.pack()

        self.code_display = tk.Text(self)
        self.code_display.pack()

    def generate_code(self):
        description = self.description_input.get()
        language = self.language_var.get()

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

        self.code_display.delete(1.0, tk.END)
        self.code_display.insert(1.0, code)

    def save_code(self):
        file_path = filedialog.asksaveasfilename()

        if file_path:
            with open(file_path, "w") as f:
                f.write(self.code_display.get(1.0, tk.END))

    def compile_code(self):
        language = self.language_var.get()
        src_code = self.code_display.get(1.0, tk.END)

        current_os = platform.system()

        if current_os == "Windows":
            output_ext = ".exe"
            documents_folder = os.path.expanduser("~/Documents")
        elif current_os == "Linux" or current_os == "Darwin":
            output_ext = ""
            documents_folder = os.path.expanduser("~/Documents")
        else:
            tk.messagebox.showerror("Error", f"Unsupported operating system: {current_os
