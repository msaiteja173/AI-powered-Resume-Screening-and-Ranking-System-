import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text_content = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_content += page_text + "\n"
    return text_content

# Function to compute similarity scores
def compute_similarity(job_desc, resume_texts):
    documents = [job_desc] + resume_texts  # Combine job description with resumes
    tfidf_matrix = TfidfVectorizer().fit_transform(documents)
    vector_array = tfidf_matrix.toarray()
    
    job_vector = vector_array[0]
    resume_vectors = vector_array[1:]
    similarity_scores = cosine_similarity([job_vector], resume_vectors).flatten()
    
    return similarity_scores

# Streamlit UI setup
st.title("AI Resume Screening & Ranking System")

# Job description input
st.subheader("Enter Job Description")
job_desc = st.text_area("Provide the job description below:")

# Upload resumes
st.subheader("Upload Resume PDFs")
uploaded_pdfs = st.file_uploader("Upload multiple PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_pdfs and job_desc:
    st.subheader("Ranked Candidate Resumes")
    
    extracted_resumes = [extract_text(pdf) for pdf in uploaded_pdfs]
    
    # Compute similarity scores
    similarity_results = compute_similarity(job_desc, extracted_resumes)
    
    # Create DataFrame for display
    result_df = pd.DataFrame({
        "Resume File": [pdf.name for pdf in uploaded_pdfs],
        "Relevance Score": similarity_results
    })
    
    result_df = result_df.sort_values(by="Relevance Score", ascending=False)
    st.dataframe(result_df)


