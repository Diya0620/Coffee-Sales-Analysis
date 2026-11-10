
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(
    page_title="Coffee Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

# Custom Dashboard Styling
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F8F5F0;
}

/* Main title */
h1 {
    color: #4B2E23;
    font-family: Georgia, serif;
    font-weight: bold;
}

/* Section headings */
h2, h3 {
    color: #6F4E37;
    font-family: Georgia, serif;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #E3D5C5;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #6F4E37;
    font-weight: bold;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EFE5D8;
}

/* General text visibility */
p, label, span, div {
    color: #44352D;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #4B2E23 !important;
}

/* Welcome message and informational text */
.stAlert p {
    color: #4B2E23 !important;
}

/* Dataframe border */
[data-testid="stDataFrame"] {
    border: 1px solid #E3D5C5;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# Dashboard title
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Retail Sales Analytics Dashboard")

st.write("Explore coffee sales, store performance and product insights.")

# Load dataset
df = pd.read_csv("data/cleaned_coffee_sales.csv")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

selected_store = st.sidebar.multiselect(
    "Select Store",
    options=df["store_location"].unique(),
    default=df["store_location"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Product Category",
    options=df["product_category"].unique(),
    default=df["product_category"].unique()
)

# Filter dataset
filtered_df = df[
    (df["store_location"].isin(selected_store)) &
    (df["product_category"].isin(selected_category))
]

# Calculate KPIs
total_revenue = filtered_df["revenue"].sum()
total_transactions = filtered_df["transaction_id"].nunique()
total_quantity = filtered_df["transaction_qty"].sum()
average_revenue = filtered_df["revenue"].mean()

# KPI section
st.header("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", f"{total_transactions:,}")
col3.metric("Quantity Sold", f"{total_quantity:,}")
col4.metric("Avg. Revenue / Record", f"${average_revenue:,.2f}")

st.divider()

# Store-wise revenue
st.header("Store Performance")

store_sales = filtered_df.groupby(
    "store_location"
)["revenue"].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x=store_sales.index, y=store_sales.values, ax=ax1)

ax1.set_title("Revenue by Store")
ax1.set_xlabel("Store Location")
ax1.set_ylabel("Revenue ($)")

plt.xticks(rotation=15)
st.pyplot(fig1)
plt.close(fig1)

st.divider()

# Product category analysis
st.header("Product Category Analysis")

category_sales = filtered_df.groupby(
    "product_category"
)["revenue"].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(9, 5))
sns.barplot(
    x=category_sales.values,
    y=category_sales.index,
    ax=ax2
)

ax2.set_title("Revenue by Product Category")
ax2.set_xlabel("Revenue ($)")
ax2.set_ylabel("Category")

st.pyplot(fig2)
plt.close(fig2)

st.divider()

# Hourly sales analysis
st.header("Hourly Sales Analysis")

hourly_sales = filtered_df.groupby(
    "transaction_hour"
)["revenue"].sum().sort_index()

fig3, ax3 = plt.subplots(figsize=(9, 4))
sns.lineplot(
    x=hourly_sales.index,
    y=hourly_sales.values,
    marker="o",
    ax=ax3
)

ax3.set_title("Revenue by Hour")
ax3.set_xlabel("Transaction Hour")
ax3.set_ylabel("Revenue ($)")

st.pyplot(fig3)
plt.close(fig3)

st.divider()

# Top 10 products
st.header("Top 10 Best-Selling Products")

top_products = filtered_df.groupby(
    "product_detail"
)["transaction_qty"].sum().sort_values(
    ascending=False
).head(10)

fig4, ax4 = plt.subplots(figsize=(9, 5))
sns.barplot(
    x=top_products.values,
    y=top_products.index,
    ax=ax4
)

ax4.set_title("Top 10 Products by Quantity Sold")
ax4.set_xlabel("Quantity Sold")
ax4.set_ylabel("Product")

st.pyplot(fig4)
plt.close(fig4)

st.divider()


# Business Insights
st.divider()
st.header("Business Insights")

if not filtered_df.empty:

    # Store with highest revenue
    best_store = filtered_df.groupby("store_location")["revenue"].sum().idxmax()

    # Best performing product category
    best_category = filtered_df.groupby("product_category")["revenue"].sum().idxmax()

    # Hour with highest revenue
    peak_hour = filtered_df.groupby("transaction_hour")["revenue"].sum().idxmax()

    # Most sold product
    top_product = filtered_df.groupby("product_detail")["transaction_qty"].sum().idxmax()

    st.info(f"🏬 Highest Revenue Store: {best_store}")

    st.info(f"☕ Best Performing Category: {best_category}")

    st.info(f"🕒 Peak Sales Hour: {int(peak_hour)}:00")

    st.info(f"⭐ Most Sold Product: {top_product}")

else:
    st.warning("No data available for the selected filters.")

# Sales Performance Summary
st.divider()
st.header("Sales Performance Summary")

if not filtered_df.empty:

    st.write(
        f"Based on the selected filters, the business generated "
        f"${total_revenue:,.2f} in total revenue."
    )

    st.write(
        f"A total of {total_transactions:,} transactions were recorded, "
        f"with {total_quantity:,} items sold."
    )

    st.write(
        f"The highest revenue came from {best_store}, "
        f"while {best_category} was the leading product category."
    )

    st.write(
        f"Sales reached their peak at {int(peak_hour)}:00."
    )

else:
    st.warning("No sales data available for the selected filters.")

# Download Filtered Data
st.divider()
st.header("Download Sales Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="coffee_sales_data.csv",
    mime="text/csv"
)

# Display data
st.header("Sales Data Preview")

st.write("Showing the first 20 transaction records.")

# Remove the extra row index
preview_df = filtered_df.head(20).reset_index(drop=True)

# Display a clean table
st.dataframe(
    preview_df,
    use_container_width=True,
    hide_index=True
)

st.success("Dashboard loaded successfully!")


# Dashboard Footer
st.markdown("---")

st.markdown(
    """
    <div style="text-align: center; color: #6F4E37; padding: 10px;">
        <h4>☕ Afficionado Coffee Roasters</h4>
        <p>Retail Sales Analytics Dashboard</p>
        <p>Developed as a Data Analytics Project</p>
    </div>
    """,
    unsafe_allow_html=True
)
