# 📄 AI Job Description Skill Extractor

A Generative AI-powered application that automatically extracts **Skills**, **Experience**, and **Education Requirements** from unstructured Job Descriptions and converts them into structured JSON output.

## 🚀 Project Overview

Recruiters and hiring teams often spend significant time manually reviewing job descriptions to identify candidate requirements. This project automates that process using **Prompt Engineering**, **LLMs**, and **Pydantic Validation**.

The application extracts only the information explicitly mentioned in the job description and avoids generating or assuming missing details.

---

## 🎯 Problem Statement

Job descriptions contain important hiring requirements hidden within lengthy paragraphs. Extracting these requirements manually is time-consuming and inefficient.

The goal of this project is to build a Generative AI system that extracts:

* Required Skills
* Experience Requirements
* Education Requirements

and returns the information in a structured format.

---

## 🎯 Objective

Build an AI-powered system that:

* Extracts Skills from Job Descriptions
* Identifies Experience Requirements
* Identifies Education Requirements
* Returns Structured JSON Output
* Avoids Hallucination and Assumptions

---

## 🏗️ System Architecture

```text
User Input (Job Description)
          │
          ▼
   Prompt Template
          │
          ▼
     Llama 3.1 (Groq)
          │
          ▼
    JSON Extraction
          │
          ▼
  Pydantic Validation
          │
          ▼
   Structured Output
```

## 🛠️ Technology Stack

* Python
* Groq API
* Llama 3.1
* Prompt Engineering
* Pydantic
* Streamlit
* JSON

---

## 📂 Project Structure

```text
Job_Description_Skill_Extractor/

├── app.py
├── main.py
├── model.py
├── parser.py
├── prompt.py
├── requirements.txt
├── .env
└── README.md
```

---

## 📥 Sample Input

```text
Looking for Python developer with 3 years experience in SQL and Machine Learning.
Bachelor's degree required.
```

## 📤 Sample Output

```json
{
  "skills": [
    "Python",
    "SQL",
    "Machine Learning"
  ],
  "experience": "3 years",
  "education": "Bachelor's degree"
}
```

---

## ✨ Features

* Generative AI-based Information Extraction
* Structured JSON Output
* Pydantic Output Validation
* Streamlit Interactive UI
* Handles Missing Information
* Easy Deployment

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/jitendra27678/job-description-skill-extractor.git
```

### Move to Project Directory

```bash
cd job-description-skill-extractor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* Resume Matching System
* ATS Score Generation
* Skill Gap Analysis
* Bulk Job Description Processing
* Multi-language Support

---

## 👨‍💻 Author

**Jitendra Khandelwal**

BCA Graduate | Data Science & Generative AI Enthusiast

