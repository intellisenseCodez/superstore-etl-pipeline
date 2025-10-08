import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import plotly.express as px


# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Database Configuration
DB_CONFIG = {
    "host": os.getenv('DATABASE_HOST'),
    "port": 5432,
    "user": os.getenv('DATABASE_USER'),
    "password": os.getenv('DATABASE_PASSWORD'),
    "dbname": os.getenv('DATABASE_NAME'),
}

# set page title
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="centered"
)

st.set_page_config(page_title="", layout="wide")

st.markdown(
    "<h2 style='text-align:center; color:white; background-color:#15327D; padding:10px;'>SUPERSTORE SALES DASHBOARD</h2>",
    unsafe_allow_html=True,
    width="stretch"
)

st.markdown("#### 🏪 Explore sales performance ")


# load all mart data
@st.cache_data
def load_data():
    """Fetch data from dbt mart tables."""
    connection_url = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    )

    engine = create_engine(connection_url)

    queries = {
        "summary": "SELECT * FROM gold.mart_customer_performance",
        "region": "SELECT * FROM gold.mart_sales_by_region",
        "category": "SELECT * FROM gold.mart_sales_by_category",
        "month": "SELECT * FROM gold.mart_sales_by_month",
        "year": "SELECT * FROM gold.mart_sales_by_year"
    }

    data = {key: pd.read_sql(text(query), engine) for key, query in queries.items()}
    return data



data = load_data()

summary = data["summary"]
total_sales = summary["total_sales"].sum()
total_orders = summary["total_orders"].sum()
avg_sales = summary["avg_sales"].sum()
avg_quantity = summary["avg_quantity"].sum()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Num of Orders", f"{total_orders:,}")
col3.metric("Average Sales Per Order", f"${avg_sales:,.2f}")
col4.metric("Average Quantity Per Order", f"${avg_quantity:,.2f}")

st.markdown("---")


fig_region = px.bar(
    data["region"], x='region', y='total_sales', color='region',
    title="Sales by Region", text_auto='.2s'
)
fig_region.update_layout(showlegend=False, title_x=0.5, title_font=dict(size=16, color="white"))

fig_category = px.bar(
    data["category"], x='category', y='total_sales', color='category',
    title="Sales by Category", text_auto='.2s'
)
fig_category.update_layout(showlegend=False, title_x=0.5, title_font=dict(size=16, color="white"))

fig_year = px.area(
    data["year"], x='order_year', y='total_sales', title="Sales by Year"
)
fig_year.update_layout(title_x=0.5, title_font=dict(size=16, color="white"))

fig_month = px.area(
    data["month"], x='order_month', y='total_sales', title="Sales by Month"
)
fig_month.update_layout(title_x=0.5, title_font=dict(size=16, color="white"))


top_col1, top_col2 = st.columns(2)
with top_col1:
    st.plotly_chart(fig_region, use_container_width=True)
with top_col2:
    st.plotly_chart(fig_category, use_container_width=True)

bottom_col1, bottom_col2 = st.columns(2)
with bottom_col1:
    st.plotly_chart(fig_year, use_container_width=True)
with bottom_col2:
    st.plotly_chart(fig_month, use_container_width=True)
    

st.markdown("<br><hr><center>Built with ❤️ by <a href='https://www.linkedin.com/in/olamilekan-oyekanmi/'>Coach Ola</a>", unsafe_allow_html=True)
