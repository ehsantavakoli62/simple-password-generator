# Cryptographically Secure Password Generator

This tool is a Python-based Command Line Interface (CLI) application designed to generate strong, unique, and **cryptographically secure** passwords. It serves as a foundational project demonstrating secure coding practices essential for **Cybersecurity and DevSecOps** roles.

---

## 🔒 Security Focus

Unlike standard password generators that rely on general pseudo-random number generators (PRNGs), this script adheres to the highest security standards by focusing on cryptographic integrity:

- **CSPRNG Implementation:** It utilizes Python's built-in **`secrets` module**, which is specifically designed for generating cryptographic secrets like passwords and tokens. This ensures the generated values are highly unpredictable and resistant to reverse-engineering or brute-force attacks.
- **Secure Handling:** The code is cleanly structured and avoids common pitfalls, making it easily auditable for security professionals.

---

## 🚀 Usage (Command Line Interface - CLI)

### Prerequisites

This script runs on standard Python 3. No external libraries are required.

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/ehsantavakoli62/simple-password-generator.git](https://github.com/ehsantavakoli62/simple-password-generator.git)
    cd simple-password-generator
    ```
2.  Ensure your main file is named `generator.py` and it contains the secure code.

### Execution

Run the script and use arguments to customize the password:

| Argument | Description | Example | Default Value |
| :--- | :--- | :--- | :--- |
| `-l`, `--length` | Specifies the total length of the password (Minimum recommended: 8). | `-l 16` | `12` |
| `--no-numbers` | Excludes digits (0-9) from the generated password. | `--no-numbers` | (Numbers included) |
| `--no-special` | Excludes special characters (!@#$...) from the password. | `--no-special` | (Special characters included) |

**Examples:**

| Goal | Command |
| :--- | :--- |
| **Standard 12-character strong password** | `python generator.py` |
| **20-character password, no special characters** | `python generator.py --length 20 --no-special` |
| **8-character password with letters and numbers only** | `python generator.py -l 8 --no-special` |

---

## 👨‍💻 Project Structure

- `generator.py`: The main script containing the secure password generation logic using `secrets` and argument parsing with `argparse`.
- `README.md`: This documentation file.

---

## 🔗 Connect

This project is part of a weekly commitment to building a professional portfolio focused on Python and Cyber Security automation. Feel free to review the code and provide feedback.
