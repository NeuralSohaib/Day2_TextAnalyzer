# Text Analyzer Pro 📊

An advanced CLI tool that:
- Counts words, characters, and sentences
- Extracts top frequent words
- Performs sentiment analysis (Positive / Negative / Neutral) with a plain-English explanation
- Computes a readability score
- Prints results with rich, colorized console output
- Saves results to `analysis_results.json`

## Quick Start

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the analyzer
python text_analyzer_pro.py


---

## 4) (Optional) Ensure your script saves JSON and uses Rich
If you’re using the unified script we built, you’re good. If not, keep your current working version.

---

## 5) Initialize Git (first time for this folder)
Open the VS Code terminal (**Terminal → New Terminal**). Make sure the prompt path ends at your project root folder.

Run these commands **exactly**:

```bash
git init
git add .
git commit -m "Day 2: Text Analyzer Pro – initial commit"
