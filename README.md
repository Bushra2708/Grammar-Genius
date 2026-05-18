# ✨ GrammarGenius AI

AI-powered Grammar & Writing Assistant built using Python, NLP, and Streamlit.

GrammarGenius AI helps users improve their writing by correcting:

* Grammar mistakes
* Spelling errors
* Punctuation issues
* Sentence structure

---

## 🚀 Features

* ✅ Grammar Correction
* ✅ Spelling Correction
* ✅ Punctuation Fixing
* ✅ AI-Based Suggestions
* ✅ Premium Modern UI
* ✅ Responsive Design
* ✅ Real-Time Text Analysis

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NLP
* LanguageTool
* HTML/CSS

---

## 📂 Folder Structure

```text
Grammar-Genius/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/Bushra2708/Grammar-Genius.git
```

### Open Project Folder

```bash
cd Grammar-Genius
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📦 requirements.txt

```txt
streamlit
language-tool-python
```

---

## ⚙️ Render Deployment

### Environment Variable

```text
PYTHON_VERSION=3.11.9
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## 🧠 LanguageTool Remote API

This project uses the remote LanguageTool API to avoid Java installation during deployment.

```python
language_tool_python.LanguageTool(
    'en-US',
    remote_server='https://api.languagetool.org/'
)
```

---

## 📸 Input Example

```text
He go to school everyday and dont likes homework.
```

---

## ✅ Output Example

```text
He goes to school every day and doesn't like homework.
```

---

## 🌐 Deployment

Deployed on Render using Streamlit.

https://grammar-genius.onrender.com/
