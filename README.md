# 🎵 Spain Top 50 Playlist Analysis

## 📌 Project Overview

This project analyzes **Spain's Top 50 songs** to understand patterns related to **content maturity, release lifecycle, playlist longevity, and playlist rotation**.

The Spanish music market has unique characteristics, including the strong influence of Latin and regional music, high sensitivity to new releases, and faster playlist rotation compared to other major music markets. This project uses data analytics and machine learning techniques to identify the factors that influence how long songs remain on playlists and how successfully they perform.

The analysis transforms raw music data into meaningful business insights that can support decision-making for music labels, artists, marketing teams, and streaming platforms.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze song lifecycle and playlist longevity.
* Understand playlist rotation patterns.
* Compare the performance of singles and albums.
* Analyze the impact of explicit content.
* Study the relationship between popularity and playlist retention.
* Identify factors influencing a song's best chart position.
* Analyze how song duration affects playlist longevity.
* Measure retention stability and playlist consistency.
* Generate business recommendations for music industry stakeholders.
* Build a predictive model for estimating playlist longevity.

---

## 📊 Key Analysis Areas

### 🎼 Content Maturity Analysis

This analysis explores the differences between:

* Explicit and non-explicit songs.
* Content maturity and playlist longevity.
* Popularity patterns across different content types.

---

### 🔄 Release Lifecycle Analysis

The lifecycle analysis examines how songs perform from entry to exit from the playlist.

Key metrics include:

* Entry Position
* Best Position
* Days on Playlist
* Time to Peak
* Entry Popularity
* Playlist Retention

This helps identify how quickly songs reach their peak performance and how long they remain relevant.

---

### 📀 Album vs Single Analysis

The project compares the performance of:

* Singles
* Albums

The analysis evaluates differences in:

* Playlist longevity
* Best chart position
* Retention stability
* Release strategy

---

### ⏱️ Duration and Longevity Analysis

Song duration is analyzed to determine whether shorter or longer tracks demonstrate stronger playlist retention.

This analysis helps understand whether track length influences audience engagement and playlist survival.

---

### 📈 Playlist Rotation Analysis

Playlist rotation patterns are studied to understand how frequently songs enter and exit the Spain Top 50 playlist.

Key indicators include:

* Daily rotation
* Entry and exit patterns
* Rank changes
* Retention stability
* Playlist continuity

---

## 🛠️ Technologies Used

| Technology          | Purpose                                       |
| ------------------- | --------------------------------------------- |
| 🐍 Python           | Data cleaning, analysis, and machine learning |
| 🗄️ SQL             | Data querying and analysis                    |
| 📊 Power BI         | Interactive dashboards and visualization      |
| 📈 Pandas           | Data manipulation                             |
| 🔢 NumPy            | Numerical analysis                            |
| 🤖 Scikit-learn     | Machine learning and predictive modeling      |
| 🌐 Streamlit        | Interactive web dashboard                     |
| 📓 Jupyter Notebook | Exploratory data analysis                     |

---

## 📂 Project Structure

```text
Spain_Top50_Project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── Spain_Top50_Cleaned.csv
│   ├── Content_Maturity_Analysis.csv
│   ├── Content_Maturity_KPIs.csv
│   ├── Content_Maturity_Summary.csv
│   ├── Daily_Rotation.csv
│   ├── Album_Type_Lifecycle.csv
│   ├── Album_Size_Longevity_Analysis.csv
│   ├── Duration_Longevity_Analysis.csv
│   ├── Business_Strategy_Dataset.csv
│   └── Executive_Summary.csv
│
├── notebooks/
│   └── Spain_Top50_Analysis.ipynb
│
└── dashboard/
    └── Streamlit Dashboard
```

---

## 🔍 Data Analysis Workflow

The project follows a structured data analytics workflow:

### 1️⃣ Data Collection

The Spain Top 50 music dataset was used as the primary source for analyzing song performance and playlist behavior.

### 2️⃣ Data Cleaning

The dataset was cleaned by:

* Removing duplicate records.
* Handling missing values.
* Converting date columns into proper datetime format.
* Standardizing text fields.
* Creating unique track identifiers.

### 3️⃣ Feature Engineering

Several analytical features were created, including:

* `days_on_playlist`
* `best_position`
* `entry_position`
* `time_to_peak_days`
* `retention_stability_index`
* `entry_popularity`

These features help measure song lifecycle and playlist performance.

### 4️⃣ Exploratory Data Analysis

Exploratory analysis was performed to identify:

* Popularity trends.
* Playlist longevity patterns.
* Rank movement.
* Album versus single performance.
* Content maturity differences.

### 5️⃣ Machine Learning

A predictive model was developed to estimate **playlist longevity**.

The model considers factors such as:

* Entry Position
* Entry Popularity
* Song Duration
* Number of Tracks
* Explicit Content
* Album Type

### 6️⃣ Dashboard Development

An interactive Streamlit dashboard was developed to present the analysis through:

* KPI cards
* Interactive charts
* Lifecycle analysis
* Content maturity insights
* Playlist rotation trends
* Business recommendations
* Playlist longevity prediction

---

## 🤖 Predictive Model

The project uses machine learning to predict the expected number of days a song may remain on the playlist.

### Input Features

The model uses:

* Entry Position
* Entry Popularity
* Duration (Minutes)
* Total Tracks
* Explicit Status
* Album Type

### Target Variable

```text
Days on Playlist
```

The best-performing model selected during the analysis was **Linear Regression**.

### Example Prediction

A sample prediction using the developed model estimated approximately:

**76.99 days on the playlist**

for a song based on its entry position, popularity, duration, album characteristics, and content type.

---

## 💡 Key Business Insights

Some of the important insights generated from the project include:

* Playlist longevity varies significantly based on release characteristics.
* Singles demonstrate different lifecycle behavior compared to albums.
* Entry position plays an important role in predicting playlist performance.
* Popularity can influence playlist retention.
* Retention stability helps identify songs with consistent performance.
* Spain's music market shows strong sensitivity to release freshness and playlist rotation.
* Song characteristics can be used to support data-driven release and marketing strategies.

---

## 🚀 Business Recommendations

Based on the analysis, the following strategies are recommended:

### 🎯 Optimize Release Strategy

Music labels can use historical lifecycle patterns to determine better release timing.

### 📢 Focus Marketing on Early Performance

Early playlist performance and entry position can provide valuable signals about future longevity.

### 🔄 Monitor Playlist Rotation

Regular monitoring of playlist entry and exit patterns can help identify changing audience preferences.

### 🎵 Use Data for Content Strategy

Song characteristics such as duration, album type, popularity, and content maturity can support better content planning.

### 📊 Predict Playlist Longevity

Predictive analytics can help stakeholders estimate potential playlist performance before making marketing and promotional investments.

---

## 🌐 Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring the analysis.

### Dashboard Features

* 📊 Executive Overview
* 🎼 Content Maturity Analysis
* 🔄 Playlist Rotation Analysis
* 📈 Release Lifecycle Analysis
* 📀 Album vs Single Comparison
* ⏱️ Duration and Longevity Analysis
* 💡 Business Recommendations
* 🤖 Playlist Longevity Prediction

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/spain-top50-playlist-analysis.git
```

### Navigate to the Project Folder

```bash
cd spain-top50-playlist-analysis
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

---

## 📦 Required Libraries

```text
streamlit
pandas
numpy
plotly
scikit-learn
joblib
```

---

## 📈 Future Improvements

Future versions of this project could include:

* Advanced machine learning models.
* Real-time Spotify data integration.
* Automated playlist monitoring.
* Sentiment analysis of song lyrics.
* Artist-level performance analysis.
* Genre-based lifecycle comparison.
* Deep learning models for playlist prediction.

---

## 👩‍💻 Author

**Preksha Bhatia**

B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)

Aspiring Data Analyst

### Skills

* Python
* SQL
* Power BI
* Excel
* Data Analysis
* Machine Learning
* Data Visualization

---

## ⭐ Conclusion

This project demonstrates how **data analytics, visualization, and machine learning** can be combined to understand music performance and playlist behavior.

By analyzing **content maturity, release lifecycle, playlist rotation, and song characteristics**, the project provides actionable insights that can help music industry stakeholders make more informed, data-driven decisions.


