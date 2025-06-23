# 🏠 Bangalore Property Listings Analysis – Web Scraping to Dashboard in Excel
This project demonstrates a complete workflow of data scraping, cleaning, analysis, and dashboard creation using real property listing data from MagicBricks (Bangalore). The goal was to extract meaningful insights from unstructured web data and visualize them in a clear and interactive Excel dashboard.

# 🧰 Tools Used
-> Python: BeautifulSoup, Requests, Pandas

-> Excel: Power Query, Pivot Tables, Charts

-> Libraries: bs4, requests, pandas, lxml

# 📌 Project Steps
# 1. 🔗 Web Scraping (Python)
The script real_estate.py was used to scrape listings from the MagicBricks website. Extracted fields:

Property Name

Price

Type

Location

Area (sqft)

Other attributes (like amenities)

# 2. 🧹 Data Cleaning (Python + Excel)
# Using Python/pandas:

Removed null or inconsistent values

Cleaned price, area, and review fields

Converted string data into numeric formats

Used .str.extract(), .replace(), .fillna() for preprocessing

# Using Excel:

Further removed special characters, unwanted rows

Split combined columns (like area + units)

Handled empty cells manually

Added structured formatting for visualizations

This hybrid approach allowed fast processing of large chunks with Python, and flexible refinement in Excel.

# 📊 Analysis Performed
Using the cleaned data, I performed the following insights-driven analyses:

🗺 Property Average Price Over Location

💵 Average Price per Area

⭐ Average BHK Price

🏢 Price Distribution vs Area

🔎 Comparison of listings by locality

# 📈 Dashboard Creation (Excel)
I built an interactive dashboard using Excel that includes:

Pivot Tables & Charts for dynamic filtering

Bar chart comparing average price by location

Slicers for filtering by price, area, and location

# ✅ Key Outcomes
Gained practical experience in real-world web scraping

Applied data wrangling techniques in both Python and Excel

Created a professional-looking dashboard to tell a story from raw data

Demonstrated ability to work across multiple tools and clean messy data efficiently

# 📁 Repository Structure
bangalore-Property-analysis/
│
├── real_estate.py                            # Web scraping script
├── raw_scraped_data.csv                      # Initial scraped data
├── cleaned_data.xlsx                         # Intermediate cleaned dataset
├── Bangalore-magicbricks-clean-data.xlsx     # Final Excel dashboard file
├── README.md                                 # Project description
