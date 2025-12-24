"""
Netflix Content Analytics - Report Page
=======================================
Project report and documentation display.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Netflix Content Analytics - Report",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Netflix Theme CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #141414 50%, #1a1a1a 100%);
        background-attachment: fixed;
    }
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }
    html, body {
        background: #0a0a0a;
        color: #ffffff;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    h1 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-weight: 900;
        letter-spacing: -1px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    h3 {
        color: #ffffff !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Report Container */
    .report-container {
        background: #1f1f1f;
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid #333;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    /* Sidebar Navigation Buttons - Netflix Red Theme */
    [data-testid="stSidebarNav"] a {
        color: #E50914 !important;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebarNav"] a:hover {
        color: #ff1a1a !important;
        background-color: rgba(229, 9, 20, 0.1) !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        color: #E50914 !important;
        background-color: rgba(229, 9, 20, 0.15) !important;
        border-left: 3px solid #E50914 !important;
        font-weight: 700;
    }
    [data-testid="stSidebarNav"] ul {
        padding-left: 0.5rem;
    }
    [data-testid="stSidebarNav"] li {
        margin: 0.25rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1>📄 PROJECT REPORT</h1>
    </div>
""", unsafe_allow_html=True)

# Google Drive PDF file ID
GOOGLE_DRIVE_FILE_ID = "1I9p2PKRVf0f5oFyjKqBPFBstrisH1eLX"
GOOGLE_DRIVE_PREVIEW_URL = f"https://drive.google.com/file/d/{GOOGLE_DRIVE_FILE_ID}/preview"
GOOGLE_DRIVE_DOWNLOAD_URL = f"https://drive.google.com/uc?export=download&id={GOOGLE_DRIVE_FILE_ID}"

# Download button linking to Google Drive
st.markdown(f"""
    <div style="text-align: center; margin-bottom: 1rem;">
        <a href="{GOOGLE_DRIVE_DOWNLOAD_URL}" target="_blank" 
           style="display: inline-block; padding: 0.75rem 2rem; background: #E50914; 
                  color: #ffffff; text-decoration: none; border-radius: 6px; 
                  font-weight: 600; font-size: 1rem; transition: all 0.3s ease;
                  box-shadow: 0 2px 8px rgba(229, 9, 20, 0.3);">
            📥 Download Report
        </a>
    </div>
""", unsafe_allow_html=True)

# Display PDF from Google Drive
pdf_display = f"""
<iframe 
    src="{GOOGLE_DRIVE_PREVIEW_URL}" 
    width="100%" 
    height="900px" 
    style="border: none; border-radius: 8px; background: #000; margin-top: 1rem;">
</iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #333;">
        <p style="color: #808080; font-size: 0.9rem;">
            Netflix Content Analytics Dashboard | Project Report
        </p>
    </div>
""", unsafe_allow_html=True)

