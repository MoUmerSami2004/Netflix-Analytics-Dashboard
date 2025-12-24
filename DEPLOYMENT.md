# Deployment Guide

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended - Easiest)

**Steps:**
1. Push your code to GitHub repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository
6. Set main file path: `app.py`
7. Click "Deploy"
8. Your dashboard will be live at: `https://<app-name>.streamlit.app`

**Advantages:**
- Free hosting
- Automatic updates on git push
- No server management
- Easy sharing via URL

---

### Option 2: GitHub Pages (Static HTML)

**Steps:**
1. Push code to GitHub repository
2. Go to repository Settings → Pages
3. Select source branch (usually `main` or `gh-pages`)
4. Select folder: `/ (root)` or `/docs` if using docs folder
5. Click "Save"
6. Your page will be available at: `https://<username>.github.io/<repository-name>`

**Note:** This deploys the `index.html` file. For the interactive dashboard, use Streamlit Cloud.

---

### Option 3: Local Deployment

**For Development:**
```bash
streamlit run app.py
```

**For Production (using Streamlit):**
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

---

### Option 4: Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t netflix-dashboard .
docker run -p 8501:8501 netflix-dashboard
```

---

## 📋 Pre-Deployment Checklist

- [ ] All dependencies listed in `requirements.txt`
- [ ] Data file (`netflix_titles.csv`) included or accessible
- [ ] Processed data file generated (`netflix_titles_processed.csv`) or preprocessing runs automatically
- [ ] All file paths are relative (not absolute)
- [ ] No hardcoded local paths
- [ ] README.md updated with deployment instructions
- [ ] GitHub repository is public (for Streamlit Cloud free tier)

---

## 🔧 Configuration for Streamlit Cloud

Create `.streamlit/config.toml` (optional):
```toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = true

[theme]
primaryColor = "#E50914"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

---

## 🚨 Common Deployment Issues

### Issue: ModuleNotFoundError
**Solution:** Ensure all dependencies are in `requirements.txt`

### Issue: FileNotFoundError
**Solution:** Check that CSV files are in the repository or update paths

### Issue: Port Already in Use
**Solution:** Change port: `streamlit run app.py --server.port 8502`

### Issue: Streamlit Cloud Build Fails
**Solution:** 
- Check Python version compatibility
- Verify all imports are available
- Review build logs for specific errors

---

## 📊 Performance Optimization

For large datasets:
1. Use `@st.cache_data` decorator (already implemented)
2. Preprocess data before deployment
3. Limit data loading to necessary columns
4. Use pagination for large tables

---

## 🔒 Security Considerations

- Don't commit sensitive API keys
- Use environment variables for secrets
- Validate user inputs in filters
- Set appropriate CORS policies

---

## 📝 Post-Deployment

1. Test all dashboard features
2. Verify filters work correctly
3. Check visualizations render properly
4. Test on different browsers/devices
5. Share dashboard URL with stakeholders

---

**Need Help?** Check Streamlit documentation: [https://docs.streamlit.io](https://docs.streamlit.io)

