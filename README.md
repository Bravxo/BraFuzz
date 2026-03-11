# 🕸️ BraFuzz

BraFuzz is a **simple and modular web intermedian fuzzer** built for CTFs and ethical audits.  
It leverages [wfuzz](https://github.com/xmendez/wfuzz) as the fuzzing engine and comes with default wordlists for directories, files, APIs, users, and user-agents.

---

## 🚀 Features

- console menu.
- Configurable profiles in `profiles.yaml`.
- Default wordlists included:
  - `dirs.txt` → common and modern directories.
  - `files.txt` → sensitive files.
  - `apis.txt` → API endpoints.
  - `users.txt` → typical users and roles.
  - `user-agents.txt` → browser and device variants.
- Compatible with **wfuzz 3.1.0**.
- Designed for **CTFs and ethical penetration testing**.

---

## 📦 Installation

Clone the repository and install `wfuzz`:

```bash
git clone https://github.com/Bravxo/BraFuzz.git
cd BraFuzz
pip install wfuzz
