<<<<<<< HEAD
# Intelligent Resume Parser

A production-grade NLP system that extracts structured information from resumes (PDF, DOCX, TXT) and converts it into ATS-friendly JSON.

## Project Structure
- `data/`: Place your resumes here. (Auto-generates a sample if empty).
- `output/`: Parsed JSON files will appear here.
- `src/`: Core logic modules.
- `main.py`: Main pipeline.

## Features
- **Multi-Format Support**: Handled PDF, DOCX, and TXT.
- **NLP Extraction**: Uses `spaCy` for Named Entity Recognition (NER).
- **Skill Matching**: Extracts skills against a predefined tech dictionary.
- **Experience Calculation**: Regex-based total experience extraction.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage
Run the parser:
```bash
python main.py
```
This will process all files in `data/` and save results to `output/`.
=======
# Resume-Parser
ml project
>>>>>>> 764dade239acdab2c80d1428418afc9fba7ada32
