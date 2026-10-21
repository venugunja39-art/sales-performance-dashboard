import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sales Performance Dashboard", layout="wide")
st.title("Sales Performance Dashboard")
st.caption("Portfolio demo • Synthetic retail data • 2024–2025")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data.csv", parse_dates=["OrderDate"])
    return df

df = load_data()

st.sidebar.header("Filters")
years = sorted(df["OrderDate"].dt.year.unique().tolist())
selected_years = st.sidebar.multiselect("Year", years, default=years)
regions = sorted(df["Region"].unique().tolist())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)
categories = sorted(df["Category"].unique().tolist())
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)
channels = sorted(df["Channel"].unique().tolist())
selected_channels = st.sidebar.multiselect("Channel", channels, default=channels)

filtered = df[
    df["OrderDate"].dt.year.isin(selected_years)
    & df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
    & df["Channel"].isin(selected_channels)
]

if filtered.empty:
    st.warning("No rows match these filters. Select at least one option in each filter.")
    st.stop()

revenue = filtered["Revenue"].sum()
profit = filtered["Profit"].sum()
orders = filtered["OrderID"].nunique()
units = filtered["Quantity"].sum()
margin = profit / revenue if revenue else 0
aov = revenue / orders if orders else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Revenue", f"{revenue:,.2f}")
c2.metric("Total Profit", f"{profit:,.2f}")
c3.metric("Orders", f"{orders:,}")
c4.metric("Units Sold", f"{units:,}")
c5.metric("Profit Margin", f"{margin:.1%}")

left, right = st.columns(2)
monthly = filtered.assign(Month=filtered["OrderDate"].dt.to_period("M").dt.to_timestamp()).groupby("Month", as_index=False)[["Revenue", "Profit"]].sum()
fig_month = px.line(monthly, x="Month", y=["Revenue", "Profit"], markers=True, title="Monthly Revenue & Profit")
left.plotly_chart(fig_month, use_container_width=True)

region_perf = filtered.groupby("Region", as_index=False)[["Revenue", "Profit"]].sum().sort_values("Revenue", ascending=False)
fig_region = px.bar(region_perf, x="Region", y="Revenue", title="Revenue by Region", text_auto=".2s")
right.plotly_chart(fig_region, use_container_width=True)

left2, right2 = st.columns(2)
cat_perf = filtered.groupby("Category", as_index=False)[["Revenue", "Profit"]].sum()
fig_cat = px.pie(cat_perf, names="Category", values="Revenue", title="Revenue Mix by Category", hole=.45)
left2.plotly_chart(fig_cat, use_container_width=True)

product_perf = filtered.groupby("Product", as_index=False)[["Revenue", "Profit"]].sum().sort_values("Profit", ascending=False).head(10)
fig_product = px.bar(product_perf, x="Profit", y="Product", orientation="h", title="Top 10 Products by Profit", text_auto=".2s")
fig_product.update_layout(yaxis={"categoryorder": "total ascending"})
right2.plotly_chart(fig_product, use_container_width=True)

st.subheader("Channel Performance")
channel_perf = filtered.groupby("Channel", as_index=False)[["Revenue", "Profit"]].sum().sort_values("Revenue", ascending=False)
st.dataframe(channel_perf.style.format({"Revenue": "{:,.2f}", "Profit": "{:,.2f}"}), use_container_width=True)

with st.expander("View filtered data"):
    st.dataframe(filtered, use_container_width=True)

st.caption("Note: all records are synthetic and created for learning. Values are fictional, not actual company results.")
