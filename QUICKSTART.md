# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Preprocess Data (Optional but Recommended)
```bash
python eda_preprocessing.py
```
This creates `netflix_titles_processed.csv` with cleaned data.

### Step 3: Launch Dashboard
```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## 📊 Using the Dashboard

1. **Apply Filters** (Left Sidebar):
   - Select content type (Movie/TV Show)
   - Choose year range
   - Filter by country, genre, or rating

2. **Explore Visualizations**:
   - Temporal trends (yearly, monthly)
   - Comparative charts (type, country, genre)
   - Pattern analysis (genre evolution, duration)

3. **View Insights**:
   - Click expandable sections for insights
   - Review key metrics at the top
   - Check detailed data table at bottom

## 🐛 Troubleshooting

**Issue**: ModuleNotFoundError
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: FileNotFoundError for CSV
- **Solution**: Ensure `netflix_titles.csv` is in the same directory

**Issue**: Dashboard not loading
- **Solution**: Check that Streamlit is installed: `pip install streamlit`

## 📝 Next Steps

- Read `README.md` for complete documentation
- Review `INSIGHTS.md` for detailed findings
- Customize `pages/Dashboard.py` or `pages/EDA.py` for your needs
- Deploy to Streamlit Cloud for sharing

