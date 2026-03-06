# Resume Parser

A machine learning-based Resume Parser that automatically extracts structured information from unstructured resume documents (PDF/DOCX). The system identifies key details such as name, email, phone number, skills, education, and experience to streamline recruitment and candidate screening workflows.

---

## Overview

Recruiters spend significant time manually reviewing resumes. This project automates resume data extraction using Natural Language Processing (NLP) techniques to convert raw resumes into structured, machine-readable information.

The system supports:

* Resume text extraction (PDF/DOCX)
* Named Entity Recognition (NER)
* Skill extraction
* Contact information detection
* Structured JSON output
* Scalable backend-ready architecture

---

## Features

* Automatic text extraction from resumes
* Email and phone number detection using regex
* Skill identification using keyword matching / NLP
* Education and experience extraction
* Clean structured output (JSON format)
* Modular and production-ready code structure

---

## Tech Stack

* Python
* NLP (spaCy / NLTK if used)
* Regex
* Pandas
* PDF parsing libraries (pdfminer / PyPDF2 if used)

---

## Project Structure

```
Resume-Parser/
│
├── data/                 # Sample resumes
├── src/                  # Core source code
│   ├── extractor.py
│   ├── parser.py
│   ├── utils.py
│
├── models/               # NLP models (if applicable)
├── output/               # Parsed results
├── requirements.txt
└── main.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adarshthakur-850/Resume-Parser.git
cd Resume-Parser
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the parser:

```bash
python main.py --file path_to_resume.pdf
```

Example output:

```json
{
  "name": "John Doe",
  "email": "john.doe@gmail.com",
  "phone": "+91-9876543210",
  "skills": ["Python", "Machine Learning", "SQL"],
  "education": ["B.Tech in Computer Science"],
  "experience": ["Data Analyst at XYZ Company"]
}
```

---

## Use Cases

* Automated resume screening
* HR management systems
* Applicant tracking systems (ATS)
* Candidate database creation
* Talent analytics

---

## Future Improvements

* Deep learning-based NER model
* Integration with FastAPI for deployment
* Web interface for resume upload
* Batch resume processing
* Docker containerization

---

## Author

Adarsh Thakur
Machine Learning Engineer
GitHub: https://github.com/Adarshthakur-850

---

## License

This project is for educational and research purposes.
