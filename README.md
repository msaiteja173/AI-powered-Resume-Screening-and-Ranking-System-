# AI-Powered Resume Screening and Ranking System

## Overview
The AI-Powered Resume Screening and Ranking System is designed to automate and optimize the resume screening process. Using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques, the system extracts relevant information from resumes and ranks candidates based on job descriptions. This reduces manual effort, ensures objective shortlisting, and improves recruitment efficiency.

## Features
- **Upload Multiple Resumes**: Supports **PDF** formats.
- **Job Description Input**: Compare resumes against a provided job description.
- **Resume Parsing & Text Extraction**: Extracts key details like skills, experience, and education.
- **Text Preprocessing**: Cleans and processes text for better analysis.
- **TF-IDF & Cosine Similarity Ranking**: Uses **TF-IDF Vectorization** and **Cosine Similarity** to rank resumes.
- **Machine Learning-Based Categorization**: Uses a pre-trained model to predict job categories.
- **User-Friendly Web Interface**: Built using **Streamlit** for easy navigation.

## How It Works
1. **Upload a Resume**: Users can upload resumes in **PDF** format.
2. **Text Extraction**: The system extracts text from the uploaded files.
3. **Preprocessing**: Removes special characters, stopwords, and unnecessary elements.
4. **Feature Extraction**: Converts text into numerical format using **TF-IDF**.
5. **Similarity Computation**: Compares resumes with job descriptions using **Cosine Similarity**.
6. **Job Category Prediction**: Predicts the job category using a pre-trained **ML model**.
7. **Ranking & Display**: Shows resumes ranked based on similarity scores.

## Installation & Setup
### Prerequisites
- **Python 3.x**
- **Required Libraries**: `streamlit`, `PyPDF2`, `pandas`, `scikit-learn`, `numpy`, `python-docx`

### Steps to Run
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/AI-Resume-Screening.git
   ```
2. **Navigate to the project folder**:
   ```bash
   cd AI-Resume-Screening
   ```
3. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Mac/Linux
   .venv\Scripts\activate      # For Windows
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the application**:
   ```bash
   python -m streamlit run app.py
   ```
6. The app will open in your browser.

## Deployment
### Streamlit Cloud
1. Push your project to **GitHub**.
2. Go to **Streamlit Cloud** and log in.
3. Click **New App**, select your GitHub repo, and set the file path to `app.py`.
4. Click **Deploy** 🚀.

## Future Enhancements
- **Advanced NLP Models**: Integrate **BERT/GPT** for deeper resume analysis.
- **Multi-Format Support**: Add support for **images (OCR), ZIP files, JSON**.
- **Skill Matching**: Extract and match skills automatically.
- **API Integration**: Connect with job portals & HR systems.
- **Real-Time Dashboard**: Develop an interactive dashboard for recruiters.

## End Users
- **HR & Recruiters**: Automates resume screening for faster hiring.
- **Hiring Managers**: Efficiently ranks candidates for job roles.
- **Job Portals**: Enhances resume-job matching accuracy.
- **AI Enthusiasts & Students**: Learn NLP-based resume analysis.

## Contributors
- **Your Name** (your-email@example.com)

## License
This project is licensed under the **MIT License**.

🚀 **Start Automating Resume Screening Today!**


