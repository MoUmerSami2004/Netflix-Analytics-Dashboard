"""
Netflix Titles Dataset - Exploratory Data Analysis and Preprocessing
====================================================================
This script performs EDA and data preprocessing for the Netflix titles dataset.
It prepares the data for visualization in the descriptive analytics dashboard.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_and_clean_data(file_path='netflix_titles.csv'):
    """
    Load and clean the Netflix titles dataset.
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Cleaned dataset
    """
    print("Loading dataset...")
    df = pd.read_csv(file_path)
    print(f"Original dataset shape: {df.shape}")
    
    # Create a copy for cleaning
    df_clean = df.copy()
    
    # Parse date_added column
    print("\nProcessing date_added column...")
    df_clean['date_added'] = pd.to_datetime(df_clean['date_added'], errors='coerce')
    
    # Extract temporal features
    df_clean['year_added'] = df_clean['date_added'].dt.year
    df_clean['month_added'] = df_clean['date_added'].dt.month
    df_clean['month_name'] = df_clean['date_added'].dt.strftime('%B')
    df_clean['year_month'] = df_clean['date_added'].dt.to_period('M')
    
    # Extract duration for movies (in minutes)
    print("Processing duration column...")
    def extract_duration(duration_str):
        if pd.isna(duration_str):
            return np.nan
        if 'min' in str(duration_str):
            try:
                return int(str(duration_str).split()[0])
            except:
                return np.nan
        return np.nan
    
    df_clean['duration_minutes'] = df_clean[df_clean['type'] == 'Movie']['duration'].apply(extract_duration)
    
    # Extract number of seasons for TV Shows
    def extract_seasons(duration_str):
        if pd.isna(duration_str):
            return np.nan
        if 'Season' in str(duration_str):
            try:
                return int(str(duration_str).split()[0])
            except:
                return np.nan
        return np.nan
    
    df_clean['num_seasons'] = df_clean[df_clean['type'] == 'TV Show']['duration'].apply(extract_seasons)
    
    # Process country column (handle multiple countries)
    print("Processing country column...")
    df_clean['country'] = df_clean['country'].fillna('Unknown')
    df_clean['country_list'] = df_clean['country'].str.split(', ')
    
    # Get primary country (first country listed)
    df_clean['primary_country'] = df_clean['country_list'].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown'
    )
    
    # Process genres (listed_in column)
    print("Processing genres...")
    df_clean['genres'] = df_clean['listed_in'].str.split(', ')
    df_clean['primary_genre'] = df_clean['genres'].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown'
    )
    
    # Fill missing ratings
    df_clean['rating'] = df_clean['rating'].fillna('Unknown')
    
    # Create decade column for release_year
    df_clean['decade'] = (df_clean['release_year'] // 10) * 10
    
    print(f"\nCleaned dataset shape: {df_clean.shape}")
    print(f"Date range: {df_clean['date_added'].min()} to {df_clean['date_added'].max()}")
    print(f"Release year range: {df_clean['release_year'].min()} to {df_clean['release_year'].max()}")
    
    return df_clean

def generate_summary_statistics(df):
    """
    Generate summary statistics for the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataset
    """
    print("\n" + "="*60)
    print("DATASET SUMMARY STATISTICS")
    print("="*60)
    
    print(f"\nTotal Titles: {len(df):,}")
    print(f"Movies: {len(df[df['type'] == 'Movie']):,} ({len(df[df['type'] == 'Movie'])/len(df)*100:.1f}%)")
    print(f"TV Shows: {len(df[df['type'] == 'TV Show']):,} ({len(df[df['type'] == 'TV Show'])/len(df)*100:.1f}%)")
    
    print(f"\nUnique Countries: {df['primary_country'].nunique()}")
    print(f"Top 5 Countries:")
    top_countries = df['primary_country'].value_counts().head(5)
    for country, count in top_countries.items():
        print(f"  {country}: {count:,} titles")
    
    print(f"\nUnique Genres: {df['primary_genre'].nunique()}")
    print(f"Top 5 Genres:")
    top_genres = df['primary_genre'].value_counts().head(5)
    for genre, count in top_genres.items():
        print(f"  {genre}: {count:,} titles")
    
    print(f"\nContent Added Over Time:")
    yearly_additions = df.groupby('year_added').size()
    print(f"  First year: {yearly_additions.index.min()} ({yearly_additions[yearly_additions.index.min()]} titles)")
    print(f"  Last year: {yearly_additions.index.max()} ({yearly_additions[yearly_additions.index.max()]} titles)")
    print(f"  Peak year: {yearly_additions.idxmax()} ({yearly_additions.max()} titles)")
    
    print(f"\nMovie Duration Statistics:")
    movie_durations = df[df['type'] == 'Movie']['duration_minutes'].dropna()
    if len(movie_durations) > 0:
        print(f"  Mean: {movie_durations.mean():.1f} minutes")
        print(f"  Median: {movie_durations.median():.1f} minutes")
        print(f"  Min: {movie_durations.min():.0f} minutes")
        print(f"  Max: {movie_durations.max():.0f} minutes")
    
    print(f"\nTV Show Seasons Statistics:")
    tv_seasons = df[df['type'] == 'TV Show']['num_seasons'].dropna()
    if len(tv_seasons) > 0:
        print(f"  Mean: {tv_seasons.mean():.1f} seasons")
        print(f"  Median: {tv_seasons.median():.1f} seasons")
        print(f"  Min: {tv_seasons.min():.0f} seasons")
        print(f"  Max: {tv_seasons.max():.0f} seasons")
    
    print("\n" + "="*60)

def save_processed_data(df, output_path='netflix_titles_processed.csv'):
    """
    Save processed data to CSV.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Processed dataset
    output_path : str
        Output file path
    """
    # Select relevant columns for dashboard
    columns_to_save = [
        'show_id', 'type', 'title', 'director', 'cast', 'country', 
        'date_added', 'release_year', 'rating', 'duration', 'listed_in', 
        'description', 'year_added', 'month_added', 'month_name', 
        'year_month', 'duration_minutes', 'num_seasons', 'primary_country', 
        'primary_genre', 'genres', 'decade'
    ]
    
    df_output = df[columns_to_save].copy()
    df_output.to_csv(output_path, index=False)
    print(f"\nProcessed data saved to: {output_path}")

if __name__ == "__main__":
    # Load and clean data
    df = load_and_clean_data('netflix_titles.csv')
    
    # Generate summary statistics
    generate_summary_statistics(df)
    
    # Save processed data
    save_processed_data(df, 'netflix_titles_processed.csv')
    
    print("\n[SUCCESS] Data preprocessing completed successfully!")
    print("\nNext steps:")
    print("  1. Review the summary statistics above")
    print("  2. Run the dashboard: streamlit run app.py")
    print("  3. Check netflix_titles_processed.csv for processed data")

