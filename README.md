# 🚀 fau

> **Stop fighting your terminal. Start talking to AI.**

`fau` is a developer CLI built to instantly prep, pack, and organize your codebase for AI chat tools. No more manual copying, no more dragging folder trees, and no more wasting time. Just one command and your context is ready.

---

## 🔥 Why fau?

Feeding context to LLMs usually means manually zipping files, rebuilding directory maps, or hunting down hidden scripts. `fau` automates the boring stuff so you can feed your AI exactly what it needs in milliseconds.

---

## ⚡ Commands

| Command | Action | Superpower |
|---|---|---|
| `fau bundle` | **Zip & Pack** | Compressed project zip copied straight to your clipboard. *(Windows)* |
| `fau copytree` | **Map Structure** | Generates a clean ASCII folder tree and copies it instantly. |
| `fau makereq` | **Gen Specs** | Scans Python files and auto-writes your `requirements.txt`. |
| `fau ireq` | **Fast Install** | Installs all local pipeline dependencies in one shot. |
| `fau todo` | **Stay Focused** | A lightweight scratchpad to track dev tasks without leaving the terminal. |

---

## 🛠️ Quick Start

Install directly from GitHub:

```bash
pip install git+https://github.com/BioZFrog/fau.git
```

Fire up the help menu to see it in action:
```bash
fau --help
```

---

## 📦 Requirements

* **Python 3.9+**
* **Windows** (Required *only* for `fau bundle` clipboard injection; all other features are fully cross-platform)

---

## 🤝 Contributing

Got an idea to make AI context building even faster? 

1. Keep core logic inside `fau/core/`
2. Wire up the CLI interface inside `fau/cli.py`
3. Open a PR!

---

## ⚠ Troubleshooting

**`fau` command not found after installing**

This usually means Python's `Scripts` folder isn't in your system PATH. To fix it:

1. Locate your Python `Scripts` folder — typically:
> C:\Users\<yourname>\AppData\Local\Programs\Python\Python3XX\Scripts
2. Search "Environment Variables" in the Windows Start menu → **Edit the system environment variables** → **Environment Variables** → select `Path` under **User variables** → **Edit** → **New** → paste the path above.
3. Close and reopen your terminal completely, then try `fau --help` again.
## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
