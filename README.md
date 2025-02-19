# Airlines Customer Segmentation Analysis
 # Sun Country Airlines Customer Segmentation Analysis

## 📌 Project Purpose
Sun Country Airlines seeks to enhance its marketing strategies by understanding customer behavior through data-driven segmentation. This project applies **K-Means clustering** to identify distinct customer groups, enabling more effective targeting and improved customer experience.

---

## 📊 Dataset Description
We used the following datasets for analysis:

- **`sample_data_transformed.csv`** – Contains customer demographics, booking details, and flight preferences.
- **`Clustering Data.csv`** – Preprocessed version of the data with categorical variables converted to numerical values.
- **Customer Data Dictionary** – Provides definitions for each variable in the dataset.

The **Clustering Data** was used for customer segmentation analysis.

---

## 🏷 Methodology
### 1️⃣ Data Preprocessing
- Standardized and normalized data.
- Removed unnecessary string-based columns.
- Ensured no missing values impacted clustering.

### 2️⃣ K-Means Clustering
- Defined **K=5** clusters.
- Applied **random centroid initialization**.
- Iteratively assigned data points to clusters based on similarity.
- Recomputed centroids until convergence.
- Merged cluster labels into the original dataset.

### 3️⃣ Data Visualization
- **Cluster Sizes** – Shows distribution of customers per cluster.
- **Group Size by Cluster** – Identifies preferred travel group sizes.
- **Age Group by Cluster** – Highlights dominant age demographics.
- **Booking Channels by Cluster** – Analyzes preferred booking methods.
- **Trip Type by Cluster** – Compares round-trip vs. one-way ticket purchases.
- **Ufly Membership by Cluster** – Evaluates customer loyalty program participation.
- **Days Pre-Booked by Cluster** – Reveals customer planning behavior.
- **Booked Class of Service by Cluster** – Examines seating preferences.

---

## 🔍 Key Findings & Customer Segments
**Segment 1: Spontaneous Youth**
- Young, last-minute travelers.
- Prefer one-way tickets.
- Use external booking sites.
- **Strategy:** Flash sales, flexible ticket changes, bundled deals.

**Segment 2: Business Travelers**
- Middle-aged professionals.
- Book round-trip tickets in advance.
- Use Sun Country’s website.
- **Strategy:** Corporate discounts, co-branded credit cards, priority services.

**Segment 3: Family Vacationers**
- Travel in large groups.
- Book via third-party platforms.
- **Strategy:** Family bundles, priority boarding, kids' entertainment.

**Segment 4: Luxury Couples**
- Travel in pairs, prefer first-class.
- Willing to pay for premium experiences.
- **Strategy:** Exclusive travel packages, premium-class incentives.

**Segment 5: Comfort-Seeking Retirees**
- Older travelers prioritizing comfort.
- Prefer direct booking with Sun Country.
- **Strategy:** Senior discounts, dedicated customer support.

---

## 🚀 Business Recommendations
Based on the insights, we propose:
- **Spontaneous Youth** → Flash sales, no-change-fee policies.
- **Business Travelers** → Loyalty rewards, priority seating, co-branded cards.
- **Family Travelers** → Family discount packages, vacation promotions.
- **Luxury Couples** → Romantic getaway partnerships, luxury travel benefits.
- **Retirees** → Senior-friendly booking, comfort-driven service enhancements.

By leveraging these strategies, Sun Country Airlines can drive engagement and revenue growth.

---

## 📌 Conclusion
This project successfully segmented Sun Country Airlines’ customers using **K-Means clustering**, uncovering critical insights to optimize marketing strategies. The findings enable the airline to tailor campaigns, boost customer loyalty, and refine pricing strategies. Future improvements include testing alternative clustering models and incorporating real-time customer insights for dynamic segmentation.

---

## 🛠 Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **K-Means Clustering Algorithm**
- **Data Preprocessing & Visualization**

---

## 📂 Repository Files
- **`Clustering Data.csv`** – Preprocessed dataset for clustering.
- **`sample_data_transformed.csv`** – Raw customer dataset.
- **`customer_data_dictionary.csv`** – Column definitions.
- **`clustering_analysis.py`** – Python script for clustering and visualization.
- **`README.md`** – Project documentation.

---

## 📢 Authors & Acknowledgments
- **Team 14A**: Hoonyoung Jung, Ariel Liang, Mingzhu Pan, Brandon Phan
- **Instructor**: Professor Xin
- **University**: BANA 200, Fall 2024

Special thanks to Sun Country Airlines for providing datasets for this study!

---

## 📌 Future Enhancements
- Implementing alternative clustering techniques (DBSCAN, Hierarchical Clustering).
- Exploring predictive models for customer retention.
- Integrating real-time data for dynamic customer segmentation.

For contributions or inquiries, feel free to submit a pull request or contact the team. 🚀
