import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Spain Top 50 | Content Maturity Analytics",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

div[data-testid="stMetric"] {
    background-color: #1E2430;
    border: 1px solid #30363D;
    padding: 15px;
    border-radius: 10px;
}

h1 {
    color: #FFFFFF;
}

h2, h3 {
    color: #E6EDF3;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT TITLE
# ============================================================

st.title("🎵 Spain Top 50 Songs Analytics Dashboard")

st.markdown("""
### Content Maturity, Release Lifecycle & Playlist Rotation Analysis

**Market:** Spain 🇪🇸  
**Organization:** Atlantic Recording Corporation  
**Project Focus:** Song Lifecycle • Playlist Rotation • Content Maturity • Business Strategy
""")

st.divider()


# ============================================================
# LOAD CSV FUNCTION
# ============================================================

@st.cache_data
def load_csv(filename):

    path = Path(filename)

    if path.exists():
        try:
            return pd.read_csv(path)
        except Exception as e:
            return None

    return None


# ============================================================
# LOAD ALL PROJECT FILES
# ============================================================

cleaned = load_csv("Spain_Top50_Cleaned.csv")

eda_summary = load_csv("Spain_Top50_EDA_Summary.csv")

daily_validation = load_csv("Spain_Top50_Daily_Validation.csv")

monthly_unique = load_csv("Monthly_Unique_Songs.csv")

monthly_explicit = load_csv("Monthly_Explicit_Content.csv")

position_popularity = load_csv("Position_Popularity_Analysis.csv")


# CONTENT MATURITY

content_maturity = load_csv(
    "Spain_Top50_Content_Maturity_Analysis.csv"
)

content_kpis = load_csv(
    "Spain_Top50_Content_Maturity_KPIs.csv"
)

content_summary = load_csv(
    "Spain_Top50_Content_Maturity_Summary.csv"
)

correlation_summary = load_csv(
    "Spain_Top50_Correlation_Significance_Summary.csv"
)

explicit_tests = load_csv(
    "Spain_Top50_Explicit_Clean_Statistical_Tests.csv"
)


# PLAYLIST ROTATION

daily_rotation = load_csv(
    "Spain_Top50_Daily_Rotation.csv"
)

entry_popularity = load_csv(
    "Spain_Top50_Entry_Popularity_Analysis.csv"
)

entry_strengths = load_csv(
    "Spain_Top50_Entry_Strengths.csv"
)


# ALBUM ANALYSIS

album_lifecycle_contingency = load_csv(
    "Spain_Top50_Album_Lifecycle_Contingency.csv"
)

album_size_longevity = load_csv(
    "Spain_Top50_Album_Size_Longevity_Analysis.csv"
)

album_type_drivers = load_csv(
    "Spain_Top50_Album_Type_Drivers.csv"
)

album_type_lifecycle = load_csv(
    "Spain_Top50_Album_Type_Lifecycle.csv"
)

album_statistical_test = load_csv(
    "Spain_Top50_Album_Type_Statistical_Test.csv"
)


# DURATION

duration_longevity = load_csv(
    "Spain_Top50_Duration_Longevity_Analysis.csv"
)


# BUSINESS

business_recommendations = load_csv(
    "Spain_Top50_Business_Recommendations.csv"
)

business_strategy = load_csv(
    "Spain_Top50_Business_Strategy_Dataset.csv"
)

executive_summary = load_csv(
    "Spain_Top50_Executive_Summary.csv"
)


# PREDICTIONS

predictions = load_csv(
    "Spain_Top50_Example_Predictions.csv"
)


# ============================================================
# CHECK MAIN DATA
# ============================================================

if cleaned is None:

    st.error("""
    ❌ Spain_Top50_Cleaned.csv was not found.

    Please make sure all CSV files are placed in the
    same folder as app.py.
    """)

    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

df = cleaned.copy()

# Convert column names to lowercase for easy handling
df.columns = df.columns.str.strip()


# Convert date column

if "date" in df.columns:

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )


# Convert position

if "position" in df.columns:

    df["position"] = pd.to_numeric(
        df["position"],
        errors="coerce"
    )


# Convert popularity

if "popularity" in df.columns:

    df["popularity"] = pd.to_numeric(
        df["popularity"],
        errors="coerce"
    )


# Convert duration

if "duration_ms" in df.columns:

    df["duration_ms"] = pd.to_numeric(
        df["duration_ms"],
        errors="coerce"
    )

    df["duration_minutes"] = (
        df["duration_ms"] / 60000
    )


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🎛 Dashboard Filters")

filtered_df = df.copy()


# DATE FILTER

if "date" in df.columns and df["date"].notna().any():

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    selected_dates = st.sidebar.date_input(
        "📅 Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(selected_dates, tuple) or isinstance(selected_dates, list):

        if len(selected_dates) == 2:

            start_date = pd.to_datetime(selected_dates[0])
            end_date = pd.to_datetime(selected_dates[1])

            filtered_df = filtered_df[
                (filtered_df["date"] >= start_date)
                &
                (filtered_df["date"] <= end_date)
            ]


# EXPLICIT FILTER

if "is_explicit" in df.columns:

    explicit_options = ["All"] + list(
        df["is_explicit"].dropna().unique()
    )

    selected_explicit = st.sidebar.selectbox(
        "🔞 Explicit Content",
        explicit_options
    )

    if selected_explicit != "All":

        filtered_df = filtered_df[
            filtered_df["is_explicit"] == selected_explicit
        ]


# ALBUM TYPE FILTER

if "album_type" in df.columns:

    album_options = ["All"] + sorted(
        df["album_type"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_album = st.sidebar.selectbox(
        "💿 Album Type",
        album_options
    )

    if selected_album != "All":

        filtered_df = filtered_df[
            filtered_df["album_type"].astype(str)
            == selected_album
        ]


# ARTIST FILTER

if "artist" in df.columns:

    artists = sorted(
        filtered_df["artist"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_artists = st.sidebar.multiselect(
        "🎤 Select Artist",
        artists
    )

    if selected_artists:

        filtered_df = filtered_df[
            filtered_df["artist"].isin(selected_artists)
        ]


st.sidebar.divider()

st.sidebar.info(
    "Use the filters to analyze different "
    "content segments and time periods."
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def find_column(dataframe, keywords):

    for col in dataframe.columns:

        col_lower = col.lower()

        for keyword in keywords:

            if keyword.lower() in col_lower:
                return col

    return None


def numeric_columns(dataframe):

    return dataframe.select_dtypes(
        include=np.number
    ).columns.tolist()


# ============================================================
# NAVIGATION
# ============================================================

tabs = st.tabs([

    "🏠 Overview",
    "🎵 Lifecycle",
    "🔄 Playlist Rotation",
    "🔞 Content Maturity",
    "💿 Album & Duration",
    "📈 Popularity",
    "💼 Business Insights",
    "🤖 Predictions",
    "📂 Data Explorer"

])


# ============================================================
# TAB 1: OVERVIEW
# ============================================================

with tabs[0]:

    st.header("🏠 Executive Overview")

    total_records = len(filtered_df)

    total_songs = (
        filtered_df["song"].nunique()
        if "song" in filtered_df.columns
        else 0
    )

    avg_position = (
        filtered_df["position"].mean()
        if "position" in filtered_df.columns
        else 0
    )

    avg_popularity = (
        filtered_df["popularity"].mean()
        if "popularity" in filtered_df.columns
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🎵 Playlist Records",
        f"{total_records:,}"
    )

    col2.metric(
        "🎶 Unique Songs",
        f"{total_songs:,}"
    )

    col3.metric(
        "🏆 Average Position",
        f"{avg_position:.2f}"
    )

    col4.metric(
        "🔥 Average Popularity",
        f"{avg_popularity:.2f}"
    )


    st.divider()


    # TOP SONGS

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🏆 Top Songs by Best Position")

        if (
            "song" in filtered_df.columns
            and "position" in filtered_df.columns
        ):

            top_songs = (
                filtered_df
                .groupby("song")["position"]
                .min()
                .sort_values()
                .head(10)
                .reset_index()
            )

            fig = px.bar(
                top_songs,
                x="position",
                y="song",
                orientation="h",
                title="Best Playlist Positions"
            )

            fig.update_yaxes(
                categoryorder="total ascending"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        st.subheader("🎤 Most Frequent Artists")

        if "artist" in filtered_df.columns:

            top_artists = (
                filtered_df["artist"]
                .value_counts()
                .head(10)
                .reset_index()
            )

            top_artists.columns = [
                "Artist",
                "Appearances"
            ]

            fig = px.bar(
                top_artists,
                x="Appearances",
                y="Artist",
                orientation="h",
                title="Top Artists by Playlist Appearances"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # MONTHLY UNIQUE SONGS

    if monthly_unique is not None:

        st.divider()

        st.subheader(
            "📅 Monthly Unique Songs"
        )

        st.dataframe(
            monthly_unique,
            use_container_width=True
        )


# ============================================================
# TAB 2: SONG LIFECYCLE
# ============================================================

with tabs[1]:

    st.header("🎵 Song Lifecycle Analysis")

    if (
        "song" in filtered_df.columns
        and "date" in filtered_df.columns
    ):

        lifecycle = (
            filtered_df
            .groupby("song")
            .agg(
                Entry_Date=("date", "min"),
                Exit_Date=("date", "max"),
                Days_On_Playlist=("date", "nunique")
            )
            .reset_index()
        )


        if "position" in filtered_df.columns:

            peak_data = (
                filtered_df
                .groupby("song")["position"]
                .min()
                .reset_index()
            )

            peak_data.columns = [
                "song",
                "Peak_Position"
            ]

            lifecycle = lifecycle.merge(
                peak_data,
                on="song",
                how="left"
            )


        st.subheader(
            "📊 Lifecycle KPIs"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Playlist Lifetime",
            f"{lifecycle['Days_On_Playlist'].mean():.1f} Days"
        )

        col2.metric(
            "Longest Survival",
            f"{lifecycle['Days_On_Playlist'].max()} Days"
        )

        col3.metric(
            "Songs Analyzed",
            f"{len(lifecycle):,}"
        )


        st.divider()


        st.subheader(
            "⏳ Longest Surviving Songs"
        )

        longest = (
            lifecycle
            .sort_values(
                "Days_On_Playlist",
                ascending=False
            )
            .head(15)
        )

        fig = px.bar(
            longest,
            x="Days_On_Playlist",
            y="song",
            orientation="h",
            title="Songs with Longest Playlist Retention"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.subheader(
            "📋 Song Lifecycle Table"
        )

        st.dataframe(
            lifecycle.sort_values(
                "Days_On_Playlist",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.warning(
            "Lifecycle analysis requires song and date columns."
        )


# ============================================================
# TAB 3: PLAYLIST ROTATION
# ============================================================

with tabs[2]:

    st.header("🔄 Playlist Rotation & Churn Analysis")

    if daily_rotation is not None:

        st.subheader(
            "📊 Daily Playlist Rotation"
        )

        st.dataframe(
            daily_rotation.head(20),
            use_container_width=True
        )

        numeric_cols = numeric_columns(
            daily_rotation
        )

        date_col = find_column(
            daily_rotation,
            ["date"]
        )

        if date_col is not None and numeric_cols:

            selected_metric = st.selectbox(
                "Select Rotation Metric",
                numeric_cols,
                key="rotation_metric"
            )

            rotation_plot = daily_rotation.copy()

            rotation_plot[date_col] = pd.to_datetime(
                rotation_plot[date_col],
                errors="coerce"
            )

            fig = px.line(
                rotation_plot,
                x=date_col,
                y=selected_metric,
                markers=True,
                title=f"{selected_metric} Over Time"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # CALCULATE DAILY UNIQUE SONGS

    if (
        "date" in filtered_df.columns
        and "song" in filtered_df.columns
    ):

        st.divider()

        st.subheader(
            "🎵 Daily Playlist Diversity"
        )

        daily_unique = (
            filtered_df
            .groupby("date")["song"]
            .nunique()
            .reset_index()
        )

        daily_unique.columns = [
            "Date",
            "Unique Songs"
        ]

        fig = px.line(
            daily_unique,
            x="Date",
            y="Unique Songs",
            title="Daily Unique Songs"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# TAB 4: CONTENT MATURITY
# ============================================================

with tabs[3]:

    st.header("🔞 Content Maturity Analysis")

    col1, col2 = st.columns(2)


    # EXPLICIT VS CLEAN

    with col1:

        if "is_explicit" in filtered_df.columns:

            st.subheader(
                "Explicit vs Clean Content"
            )

            explicit_counts = (
                filtered_df["is_explicit"]
                .value_counts()
                .reset_index()
            )

            explicit_counts.columns = [
                "Content Type",
                "Count"
            ]

            fig = px.pie(
                explicit_counts,
                names="Content Type",
                values="Count",
                title="Content Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # MONTHLY EXPLICIT CONTENT

    with col2:

        if monthly_explicit is not None:

            st.subheader(
                "Monthly Explicit Content"
            )

            numeric_cols = numeric_columns(
                monthly_explicit
            )

            if numeric_cols:

                st.dataframe(
                    monthly_explicit,
                    use_container_width=True
                )


    # CONTENT MATURITY DATA

    if content_maturity is not None:

        st.divider()

        st.subheader(
            "📊 Content Maturity Results"
        )

        st.dataframe(
            content_maturity,
            use_container_width=True
        )


    if content_summary is not None:

        st.divider()

        st.subheader(
            "📈 Content Maturity Summary"
        )

        st.dataframe(
            content_summary,
            use_container_width=True
        )


    if content_kpis is not None:

        st.divider()

        st.subheader(
            "🎯 Content Maturity KPIs"
        )

        st.dataframe(
            content_kpis,
            use_container_width=True
        )


# ============================================================
# TAB 5: ALBUM & DURATION
# ============================================================

with tabs[4]:

    st.header("💿 Album Type & Duration Analysis")


    # ALBUM TYPE

    if "album_type" in filtered_df.columns:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Album Type Distribution"
            )

            album_counts = (
                filtered_df["album_type"]
                .value_counts()
                .reset_index()
            )

            album_counts.columns = [
                "Album Type",
                "Count"
            ]

            fig = px.bar(
                album_counts,
                x="Album Type",
                y="Count",
                title="Single vs Album Tracks"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with col2:

            if (
                "album_type" in filtered_df.columns
                and "position" in filtered_df.columns
            ):

                album_position = (
                    filtered_df
                    .groupby("album_type")["position"]
                    .mean()
                    .reset_index()
                )

                fig = px.bar(
                    album_position,
                    x="album_type",
                    y="position",
                    title="Average Position by Album Type"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


    # DURATION

    if (
        "duration_minutes" in filtered_df.columns
        and "position" in filtered_df.columns
    ):

        st.divider()

        st.subheader(
            "⏱ Song Duration vs Playlist Position"
        )

        fig = px.scatter(
            filtered_df,
            x="duration_minutes",
            y="position",
            hover_data=[
                col for col in ["song", "artist"]
                if col in filtered_df.columns
            ],
            title="Song Duration and Playlist Position"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ALBUM ANALYSIS TABLES

    if album_type_lifecycle is not None:

        st.divider()

        st.subheader(
            "Album Type Lifecycle Analysis"
        )

        st.dataframe(
            album_type_lifecycle,
            use_container_width=True
        )


    if album_size_longevity is not None:

        st.divider()

        st.subheader(
            "Album Size vs Longevity"
        )

        st.dataframe(
            album_size_longevity,
            use_container_width=True
        )


    if duration_longevity is not None:

        st.divider()

        st.subheader(
            "Duration vs Longevity Analysis"
        )

        st.dataframe(
            duration_longevity,
            use_container_width=True
        )


# ============================================================
# TAB 6: POPULARITY
# ============================================================

with tabs[5]:

    st.header("📈 Popularity Analysis")

    if (
        "popularity" in filtered_df.columns
        and "position" in filtered_df.columns
    ):

        fig = px.scatter(
            filtered_df,
            x="popularity",
            y="position",
            hover_data=[
                col for col in ["song", "artist"]
                if col in filtered_df.columns
            ],
            title="Popularity vs Playlist Position"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    if position_popularity is not None:

        st.divider()

        st.subheader(
            "Position vs Popularity Results"
        )

        st.dataframe(
            position_popularity,
            use_container_width=True
        )


    if entry_popularity is not None:

        st.divider()

        st.subheader(
            "Entry Popularity Analysis"
        )

        st.dataframe(
            entry_popularity,
            use_container_width=True
        )


    if entry_strengths is not None:

        st.divider()

        st.subheader(
            "Entry Strength Analysis"
        )

        st.dataframe(
            entry_strengths,
            use_container_width=True
        )


# ============================================================
# TAB 7: BUSINESS INSIGHTS
# ============================================================

with tabs[6]:

    st.header("💼 Business Recommendations")

    if executive_summary is not None:

        st.subheader(
            "📌 Executive Summary"
        )

        st.dataframe(
            executive_summary,
            use_container_width=True
        )


    if business_recommendations is not None:

        st.divider()

        st.subheader(
            "🎯 Strategic Recommendations"
        )

        st.dataframe(
            business_recommendations,
            use_container_width=True
        )


    if business_strategy is not None:

        st.divider()

        st.subheader(
            "📊 Business Strategy Dataset"
        )

        st.dataframe(
            business_strategy,
            use_container_width=True
        )


    st.divider()

    st.subheader(
        "💡 Strategic Insights for Atlantic Records"
    )

    st.markdown("""

### 🎵 Release Strategy

- Focus marketing resources during the early lifecycle stage.
- Monitor first-week playlist performance closely.
- Identify songs showing rapid position improvement.

### 🔄 Playlist Strategy

- High playlist churn requires fast promotional action.
- Songs losing rank consistently may require renewed campaigns.
- Strong retention indicates catalog value.

### 🔞 Content Strategy

- Compare explicit and clean content performance.
- Optimize releases based on Spain-specific listener behavior.

### 💿 Release Format Strategy

- Compare Single and Album track longevity.
- Use lifecycle performance to guide release planning.

""")


# ============================================================
# TAB 8: PREDICTIONS
# ============================================================

with tabs[7]:

    st.header("🤖 Song Performance Predictions")

    if predictions is not None:

        st.subheader(
            "📊 Model Prediction Results"
        )

        st.dataframe(
            predictions,
            use_container_width=True
        )


        numeric_cols = numeric_columns(
            predictions
        )

        if len(numeric_cols) >= 2:

            x_axis = st.selectbox(
                "Select X Axis",
                numeric_cols,
                key="prediction_x"
            )

            y_axis = st.selectbox(
                "Select Y Axis",
                numeric_cols,
                index=1,
                key="prediction_y"
            )

            fig = px.scatter(
                predictions,
                x=x_axis,
                y=y_axis,
                title="Prediction Analysis"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            "Prediction file is not available."
        )


# ============================================================
# TAB 9: DATA EXPLORER
# ============================================================

with tabs[8]:

    st.header("📂 Data Explorer")

    st.subheader(
        "Filtered Spain Top 50 Dataset"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )


    st.subheader(
        "Dataset Information"
    )

    info_df = pd.DataFrame({

        "Column": filtered_df.columns,

        "Data Type": [
            str(dtype)
            for dtype in filtered_df.dtypes
        ],

        "Missing Values": [
            filtered_df[col].isna().sum()
            for col in filtered_df.columns
        ]

    })

    st.dataframe(
        info_df,
        use_container_width=True
    )


    # DOWNLOAD FILTERED DATA

    csv = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label="⬇ Download Filtered Dataset",

        data=csv,

        file_name="Spain_Top50_Filtered_Data.csv",

        mime="text/csv"

    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    ### 🎵 Spain Top 50 Content Intelligence Dashboard

    Developed for academic and business analytics purposes.

    **Atlantic Recording Corporation | Spain Market Analysis**
    """
)