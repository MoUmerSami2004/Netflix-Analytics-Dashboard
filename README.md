# Netflix Content Analytics Dashboard

## 📊 Project Overview

This project presents a comprehensive **descriptive analytics dashboard** for analyzing Netflix content trends, patterns, and insights. The dashboard focuses on historical data analysis, temporal trends, comparative visualizations, and pattern recognition - providing real-world decision-oriented insights for business stakeholders, content strategists, and decision-makers.

## 🎯 Project Objective

Build an interactive descriptive analytics dashboard that provides real-world, decision-oriented usage insights from the Netflix titles dataset. The dashboard focuses on:
- **What happened**: Historical trends and patterns
- **Trends over time**: Content evolution and growth
- **Comparisons**: Cross-category and regional analysis
- **Patterns**: Genre shifts, seasonal variations, content strategies

**No predictive or prescriptive analytics** - purely descriptive analysis.

## 📁 Project Structure

```
PROJECT/
│
├── netflix_titles.csv              # Original dataset
├── netflix_titles_processed.csv     # Processed dataset (generated)
├── eda_preprocessing.py            # EDA and data preprocessing script
├── app.py                           # Main entry point for multi-page Streamlit app
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── INSIGHTS.md                      # Key insights and findings
└── index.html                       # GitHub.io webpage
```

## 🛠️ Tools & Technologies

- **Python 3.8+**
- **Streamlit**: Interactive web dashboard framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd PROJECT

# Or download and extract the project folder
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Data Preprocessing (Optional)

```bash
python eda_preprocessing.py
```

This will generate `netflix_titles_processed.csv` with cleaned and processed data.

### Step 4: Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`

## 🚀 Dashboard Features

### 📅 Temporal Visualizations

1. **Content Added Over Time (Yearly Trend)**
   - Shows growth/decline patterns
   - Separates Movies vs TV Shows
   - Identifies peak addition years

2. **Monthly Addition Patterns**
   - Seasonal content addition trends
   - Peak months identification
   - Year-round distribution analysis

3. **Content Release Year Distribution**
   - Historical content analysis
   - Decade-based distribution
   - Library composition insights

### 🔀 Comparative Analysis

- **Content Type Distribution**: Movies vs TV Shows
- **Top Countries**: Geographic content distribution
- **Top Genres**: Most popular content categories
- **Rating Distribution**: Content maturity levels

### 🔍 Pattern Analysis

- **Genre Evolution Over Time**: Top 5 genres trend analysis
- **Content Type by Country**: Regional content preferences
- **Movie Duration Distribution**: Runtime patterns

### 🔍 Interactive Filters

- **Content Type**: Filter by Movie or TV Show
- **Year Range**: Select specific time periods
- **Country**: Filter by top producing countries
- **Genre**: Filter by content genres
- **Rating**: Filter by content ratings

## 📊 Dataset Description

### Source
- **Dataset**: Netflix Titles Dataset
- **Size**: 8,807 titles
- **Time Coverage**: Content added from 2008 to 2021
- **Release Years**: 1925 to 2021

### Key Attributes

- `show_id`: Unique identifier
- `type`: Movie or TV Show
- `title`: Content title
- `director`: Director name(s)
- `cast`: Cast members
- `country`: Production country/countries
- `date_added`: Date added to Netflix
- `release_year`: Original release year
- `rating`: Content rating (TV-MA, PG-13, etc.)
- `duration`: Runtime (minutes) or seasons
- `listed_in`: Genre categories
- `description`: Content description

## 🌐 GitHub Pages Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and branch
6. Set main file to `dashboard.py`
7. Deploy!

### Option 2: GitHub Pages (Static HTML)

For static deployment, you can convert the dashboard to a static HTML file using Streamlit's static export feature (if available) or use the provided `index.html` for project documentation.

1. Push code to GitHub
2. Enable GitHub Pages in repository settings
3. Select source branch (usually `main` or `gh-pages`)
4. Access via `https://<username>.github.io/<repository-name>`

## 📈 Key Insights

See `INSIGHTS.md` for detailed insights derived from the dashboard visualizations.

### Quick Insights Summary:

1. **Content Growth**: Rapid expansion from 2008-2021
2. **Genre Dominance**: Dramas and International content lead
3. **Geographic Distribution**: United States produces most content
4. **Type Balance**: Movies slightly outnumber TV Shows
5. **Temporal Patterns**: Consistent monthly additions with seasonal variations

## 🎥 Video Walkthrough

The dashboard supports a comprehensive walkthrough covering:
- Dataset overview and structure
- Filter functionality demonstration
- Major visualizations explanation
- Key insights and business implications
- Real-world decision-making scenarios

## 👥 Team Members

- [Your Name/Team Member Names]

## 📝 Presentation Readiness

This project supports in-class presentations covering:
- ✅ Dataset overview
- ✅ EDA highlights
- ✅ Dashboard features and interactivity
- ✅ Insights and stories
- ✅ Tools and technology stack
- ✅ Real-world applications

## 🔗 GitHub Repository

[Add your repository link here]

## 📄 License

This project is for academic/educational purposes.

## 🙏 Acknowledgments

- Netflix for providing the dataset
- Streamlit and Plotly communities
- Data science and visualization best practices

---

**Built with ❤️ for Descriptive Analytics**

