# Corefinder - Digital Business Card 🎨

A Python CLI application that generates a beautiful ASCII art digital business card displaying personal and professional information.

![Digital Business Card Preview](image/calvin.png)

## 📋 Project Overview

- **Type**: Python CLI Package
- **Purpose**: Digital business card generator with ASCII art display
- **Author**: Soumyajit Basu
- **Version**: 1.1.7
- **License**: MIT

## 🚀 Quick Start

### Method 1: Direct Python Execution (Recommended for Development)

```bash
# Navigate to project directory
cd corefinder

# Run directly as Python module
python -m app
```

### Method 2: Install as CLI Package

```bash
# Install from PyPI (published version)
pip install --user corefinder

# Or install in development mode (local changes)
pip install -e .

# Run using CLI command
corefinder
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Corefinder89/corefinder.git
   cd corefinder
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Using pip
   pip install -e .
   
   # Or using pipenv
   pipenv install
   ```

4. **Run the application**
   ```bash
   # Method 1: Direct module execution
   python -m app
   
   # Method 2: After installation
   corefinder
   ```

## � Building the Project

### Rebuild After Changes (Development)

When you make changes to the code, you need to rebuild the project to see your updates:

#### Method 1: Quick Development Rebuild
```bash
# Reinstall in development mode (picks up code changes instantly)
pip install -e . --force-reinstall

# Test your changes
corefinder
```

#### Method 2: Clean Rebuild
```bash
# Uninstall existing version
pip uninstall corefinder

# Clean previous builds
rm -rf build/ dist/ *.egg-info/  # Linux/macOS
# or on Windows:
rmdir /s build dist
rmdir /s corefinder.egg-info

# Reinstall fresh
pip install -e .
```

#### Method 3: Direct Module Execution (No Build Required)
```bash
# Run directly without installation (good for quick testing)
python -m app
```

### 📦 Building for Distribution

#### Using Makefile

The project includes a `makefile` for automated building and publishing.

**On Unix/Linux/macOS:**
```bash
# Clean previous builds
make clean

# Build package
make build

# Publish to PyPI
make publish
```

**On Windows PowerShell:**

Since PowerShell doesn't have built-in `make` support, you can either:

1. **Install GNU Make for Windows:**
   ```powershell
   # Via Chocolatey
   choco install make
   
   # Via winget
   winget install GnuWin32.Make
   
   # Then use normally
   make build
   make clean
   make publish
   ```

2. **Run commands directly (recommended):**
   ```powershell
   # Clean previous builds
   Remove-Item -Path build, dist, *.egg-info -Recurse -Force -ErrorAction SilentlyContinue
   
   # Build package (modern approach)
   python -m pip install --upgrade build
   python -m build
   
   # Publish to PyPI
   python -m twine check dist/*
   python -m twine upload dist/*
   ```

#### Manual Build (Alternative)
```bash
# Install build dependencies
python -m pip install --upgrade setuptools wheel twine

# Build package (deprecated method)
python setup.py sdist bdist_wheel

# Check and publish
python -m twine check dist/*
python -m twine upload dist/*
```

**Note:** The `python setup.py` method is deprecated. Use `python -m build` for modern package building.

### 🔄 Development Workflow

1. **Make your changes** to the code
2. **Test quickly**: `python -m app`
3. **Rebuild package**: `pip install -e . --force-reinstall`
4. **Test CLI**: `corefinder`
5. **Build for distribution**: `make build` (when ready to release)

## 💻 CLI Commands

```bash
# Display digital business card
corefinder

# Show help information
corefinder --help

# Show version information
corefinder --version
```

## 🏗️ Project Structure

```
corefinder/
├── app/
│   ├── __init__.py
│   ├── __main__.py          # Entry point for module execution
│   ├── main.py              # Main application logic
│   ├── card.py              # ASCII art card generator
│   └── url_shortener.py     # URL shortener functionality (WIP)
├── image/
│   └── calvin.png           # Preview image
├── corefinder.egg-info/     # Package metadata
├── setup.py                 # Package configuration
├── pyproject.toml           # Build system requirements
├── Pipfile                  # Pipenv dependencies
├── makefile                 # Build automation
└── README.md                # This file
```

## 🎯 Features

- **ASCII Art Display**: Beautiful terminal-based business card
- **Personal Information**: Name, designation, contact details
- **Professional Details**: Current organization, experience, certifications
- **Social Links**: LinkedIn, GitHub, Bitbucket profiles
- **Educational Background**: Degrees and certifications
- **CLI Interface**: Easy command-line access

## 🔧 Technical Details

- **Language**: Python 3.6+
- **Package Type**: Console script with entry point
- **Distribution**: PyPI package
- **Build System**: setuptools with wheel support
- **Dependencies**: Minimal (only standard library)

## 🌟 Output Example

The application generates a detailed ASCII art business card showing:
- Personal details (name, location, contact)
- Professional information (current role, experience)
- Educational background
- Certifications and achievements
- Social media profiles

## 🐛 Troubleshooting

### Common Issues

#### `subprocess-exited-with-error` during `pip install -e .`
If you encounter a `UnicodeDecodeError` when running `pip install -e .`, this is typically due to encoding issues when reading files with Unicode characters (emojis, special characters).

**Solution**: Ensure `setup.py` reads files with UTF-8 encoding:
```python
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
```

#### Module not found errors
Make sure you're in the correct directory and have activated your virtual environment:
```bash
cd corefinder
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

#### `No module named 'twine'` when publishing
If you encounter `ModuleNotFoundError: No module named 'twine'` when trying to publish or check packages, you need to install twine first:

```bash
# Install twine for package publishing
python -m pip install twine

# Then you can use twine commands
python -m twine check dist/*
python -m twine upload dist/*
```

**Alternative**: Use the makefile which automatically installs dependencies:
```bash
make build  # This installs setuptools, wheel, and twine automatically
make publish
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

- **Author**: Soumyajit Basu
- **Email**: soumyajit.basu62@gmail.com
- **LinkedIn**: [soumyajit-basu-5a783886](https://www.linkedin.com/in/soumyajit-basu-5a783886/)
- **GitHub**: [Corefinder89](https://github.com/Corefinder89)

---

⭐ **Star this repo if you find it useful!**
