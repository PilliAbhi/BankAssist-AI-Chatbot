# 🏦 BankAssist AI

An AI-powered Banking Assistant built using **Streamlit** and **OpenRouter AI**.  
This chatbot helps users get instant answers to banking-related questions such as loans, UPI, credit cards, savings accounts, KYC, internet banking, and more.

---

## 📌 Features

- 🤖 AI-powered Banking Chatbot
- 💬 ChatGPT-style Chat Interface
- 🏦 Banking FAQs
- 💰 Loan Information
- 💳 Credit Card Support
- 📲 UPI Guidance
- 📄 KYC Assistance
- 🌐 Internet Banking Help
- 💵 Fixed Deposit Information
- ⚡ Fast AI Responses
- 📱 Responsive User Interface
- 💾 Chat History During Session

---

## 🛠 Technologies Used

- Python 3.11+
- Streamlit
- OpenRouter API
- Requests
- Python Dotenv

---

## 📂 Project Structure

```
BankAssist-AI/
│
├── chatbot/
│   ├── __init__.py
│   └── llm.py
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/BankAssist-AI.git
```

---

### 2. Navigate to Project Folder

```bash
cd BankAssist-AI
```

---

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 5. Create .env File

Create a file named `.env`

Example:

```env
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

Replace with your own OpenRouter API Key.

---

### 6. Run the Project

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 💬 Example Questions

- How can I open a savings account?
- What documents are required for KYC?
- How do I apply for a personal loan?
- What is UPI?
- How to reset my UPI PIN?
- How can I block my ATM card?
- What is Internet Banking?
- Explain Fixed Deposit.
- How to apply for a Credit Card?
- What is the minimum balance requirement?

---

## 📷 Application Screens

### Home Page

- Banking Services Sidebar
- AI Chat Interface
- Chat History
- Banking Assistance

---

## 🔐 Environment Variables

The following environment variable is required.

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```

---

## 📦 Requirements

Example requirements.txt

```
streamlit
requests
python-dotenv
```

---

## 🎯 Future Enhancements

- Voice Assistant
- Speech-to-Text
- Text-to-Speech
- Loan EMI Calculator
- Bank Branch Locator
- PDF Document Upload
- OCR for Bank Statements
- Multi-language Support
- Dark Mode
- Authentication & User Login
- Chat Export to PDF
- Database Integration
- Banking Knowledge Base using RAG
- LangChain Integration
- FAISS Vector Database

---

## 👨‍💻 Developed By

**Pilli Abhi**

Final Year B.Tech (CSE - Artificial Intelligence & Machine Learning)

---

## 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ Acknowledgements

- Streamlit
- OpenRouter
- Python
- Open Source AI Community