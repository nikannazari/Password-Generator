# 🔐 Password Generator

A modular and extensible **Password Generator** built with Python.

The project supports multiple password generation strategies and provides both a **Command Line Interface (CLI)** and an interactive **Streamlit web interface**.

---

## ✨ Features

### 🔐 Password Types

* 🔢 **PIN Generator**

  * Numeric passwords
  * Customizable length

* 🔀 **Random Password Generator**

  * Customizable password length
  * Optional numbers
  * Optional symbols
  * Uppercase and lowercase letters

* 🧠 **Memorable Password Generator**

  * Generates passwords from random words
  * Custom number of words
  * Custom separator
  * Optional capitalization

### 💻 Interfaces

* Command Line Interface
* Streamlit Web UI
* Interactive controls
* Password generation without page reload issues
* Clean and modular architecture

### 🧑‍💻 Software Design

* Object-Oriented Programming
* Abstract Base Class
* Strategy-based generator architecture
* Separation of concerns
* Python `src` package layout
* Editable package installation
* Type hints
* Modular components

---

# 📸 Overview

The application provides a simple interface for generating different types of passwords depending on the user's needs.

```text
                    🔐 Password Generator
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
           🔢 PIN          🔀 Random       🧠 Memorable
                              │
                              ▼
                    Generated Password
```

---

# 🧠 Password Generation Strategies

## 🔢 PIN

Generates a numeric PIN.

Example:

```text
583914
```

The length can be customized.

---

## 🔀 Random Password

Generates a random password using:

* Letters
* Numbers
* Symbols

Example:

```text
fR8!kP2@xL9#
```

The user can control:

* Password length
* Numbers
* Symbols

---

## 🧠 Memorable Password

Generates a password from multiple random words.

Example:

```text
mountain-python-ocean-rocket
```

The user can configure:

* Number of words
* Separator
* Capitalization

Example with capitalization:

```text
Mountain-Python-Ocean-Rocket
```

---

# 🏗️ Project Architecture

The project separates password generation logic from the user interfaces.

```text
                         User
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
               CLI               Streamlit
                │                     │
                └──────────┬──────────┘
                           ▼
                  Password Generators
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
        PIN             Random          Memorable
      Generator        Generator        Generator
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                   Generated Password
```

The generators are independent from the UI, making the project easier to maintain and extend.

---

# 📁 Project Structure

```text
Password-Generator/
│
├── app/
│   └── streamlit_app.py
│
├── assets/
│
├── src/
│   └── password_generator/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── generators/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── pin.py
│       │   ├── random_password.py
│       │   └── memorable.py
│       │
│       └── utils/
│           ├── __init__.py
│           └── validators.py
│
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# 🛠️ Technologies

* 🐍 Python
* 🌐 Streamlit
* 📦 Setuptools
* 🔧 Git
* 🐙 GitHub

The core password generation uses Python's standard library, particularly the `secrets` module for secure random generation.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Password-Generator
```

---

## 2. Create a virtual environment

### Linux / macOS

```bash
python -m venv .venv
```

### Windows

```powershell
python -m venv .venv
```

---

## 3. Activate the virtual environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install the package

Install the project in editable mode:

```bash
pip install -e .
```

---

# 💻 Run the CLI

Run:

```bash
python -m password_generator.main
```

You will see:

```text
==================================================
             PASSWORD GENERATOR
==================================================

[1] PIN
[2] Random Password
[3] Memorable Password
[Q] Quit

Choose an option >>>
```

---

# 🌐 Run the Streamlit App

Run:

```bash
streamlit run app/streamlit_app.py
```

Then open the local Streamlit address in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🔐 Security

Password generation uses Python's `secrets` module instead of the standard `random` module.

`secrets` is designed for generating values that need stronger unpredictability, making it a better choice for password and PIN generation.

### Important

This project is intended as a learning project and a local password-generation utility.

Generated passwords should be handled carefully and should not be stored in source code, logs, public repositories, or other insecure locations.

---

# 🧩 Components

## `PasswordGenerator`

Located at:

```text
src/password_generator/generators/base.py
```

Defines the common interface for all password generators.

---

## `PinGenerator`

Located at:

```text
src/password_generator/generators/pin.py
```

Responsible for generating numeric PINs.

---

## `RandomPasswordGenerator`

Located at:

```text
src/password_generator/generators/random_password.py
```

Responsible for generating random passwords using configurable character sets.

---

## `MemorablePasswordGenerator`

Located at:

```text
src/password_generator/generators/memorable.py
```

Generates passwords from randomly selected words.

---

## `validators`

Located at:

```text
src/password_generator/utils/validators.py
```

Provides validation and conversion utilities used by the CLI.

---

# 🔧 Development

The project uses the Python `src` layout.

The package can be installed using:

```bash
pip install -e .
```

This allows the source code to be modified without repeatedly reinstalling the package.

---

# 🔮 Future Improvements

Possible future improvements include:

### Password Generation

* [ ] Custom character sets
* [ ] Minimum character requirements
* [ ] Guaranteed numbers
* [ ] Guaranteed symbols
* [ ] Password strength estimation
* [ ] Pronounceable passwords
* [ ] Custom word lists

### Streamlit

* [ ] Copy-to-clipboard button
* [ ] Password strength meter
* [ ] Password history
* [ ] Batch password generation
* [ ] Improved animations
* [ ] Dark / Light theme
* [ ] Better responsive design

### Application

* [ ] Configuration file
* [ ] Command-line arguments
* [ ] REST API
* [ ] Desktop GUI
* [ ] Docker support
* [ ] CI/CD

---

# 📚 Learning Goals

This project was created to practice:

### Python

* Object-Oriented Programming
* Abstract Base Classes
* Inheritance
* Modules
* Packages
* Type hints
* Error handling
* Standard library
* Secure random generation

### Software Engineering

* Modular architecture
* Separation of concerns
* Package design
* Dependency management
* Virtual environments
* Documentation

### Tools

* Git
* GitHub
* Streamlit
* Setuptools

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for the complete license text.

---

# 👨‍💻 Author

**Nikan Nazari**

---

⭐ If you find this project useful, consider giving it a star on GitHub.
