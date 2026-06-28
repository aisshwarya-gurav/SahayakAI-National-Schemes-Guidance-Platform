"# SahayakAI-National-Schemes-Guidance-Platform" 
# 🇮🇳 Sahayak AI

> AI-Powered Government Scheme Recommendation Assistant

## 📌 Overview

Sahayak AI is an intelligent conversational assistant that helps Indian citizens discover government welfare schemes based on their profile.

Instead of manually searching multiple government websites, users simply describe themselves in natural language, and Sahayak AI recommends the most relevant schemes.

Example:

> "I am a 22-year-old female student from Karnataka with an annual income of ₹2,000 and belong to the OBC category."

The AI automatically extracts the user's profile and recommends suitable government schemes.

---

# 🚀 Features

- 🤖 Natural Language Interaction
- 🎓 Education Scheme Recommendations
- 🌾 Agriculture Scheme Recommendations
- 🏥 Healthcare Schemes
- 👵 Old Age Pension Schemes
- 🏠 Housing Schemes
- 💰 Financial Inclusion Schemes
- 📄 Required Documents
- 📝 Application Process
- 🌐 Official Government Website Links
- 💬 Follow-up Questions for Specific Schemes

---

# 🧠 AI Workflow

```
User Query
      │
      ▼
Natural Language Processing
      │
      ▼
Profile Extraction
      │
      ▼
Eligibility Matching
      │
      ▼
Government Scheme Database
      │
      ▼
AI Recommendation Engine
      │
      ▼
Conversational Response
```

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- FastAPI
- Python

## AI

- Groq Cloud
- Meta Llama Model
- Natural Language Processing (NLP)

---

# 📂 Project Structure

```
SahayakAI
│
├── backend
│   ├── main.py
│   ├── parser.py
│   ├── recommender.py
│   ├── groq_service.py
│   ├── models.py
│   ├── schemes.json
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── README.md
└── requirements.txt
```

---

# 📊 Government Data Sources

The government scheme information has been collected and structured from official Government of India portals, including:

- https://www.india.gov.in
- https://www.myscheme.gov.in
- https://pmkisan.gov.in
- https://scholarships.gov.in
- https://pmjay.gov.in
- https://pmaymis.gov.in

The dataset includes:

- Scheme Description
- Eligibility Criteria
- Benefits
- Required Documents
- Application Process
- Ministry
- Official Website

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SahayakAI.git
```

Go to project

```bash
cd SahayakAI
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 💡 Example Query

```
I am a 22-year-old female student from Karnataka.

My annual income is ₹2000.

I belong to the OBC category.

Suggest government schemes.
```

---

# 🎯 Future Enhancements

- 🎤 Voice Assistant
- 🌐 Regional Language Support
- 📱 Mobile Application
- 📄 OCR Document Verification
- 🔔 Scheme Notifications
- 🔗 Direct Online Application Support

---

# 🏆 Hackathon Evaluation Mapping

| Criteria | Implementation |
|----------|----------------|
| AI Agent Functionality | Conversational AI for recommendations |
| Innovation | Natural language based scheme discovery |
| Technical Implementation | FastAPI + Groq + Llama + NLP |
| Agent Autonomy | Automatically extracts profile and recommends schemes |
| Real World Impact | Helps citizens discover government benefits |
| Demo Quality | Interactive chatbot interface |

---

# 👨‍💻 Developed By

**Aisshwarya Gurav**

AI-Powered Government Scheme Recommendation Assistant

Built for Hackathon 2026 🚀
