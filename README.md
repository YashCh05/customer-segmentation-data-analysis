# SegmenTrack – Customer Segmentation Explorer

SegmenTrack is a Python-based data analysis project that automates customer segmentation and reporting.  
It allows users to upload a customer CSV file, segment customers based on selected criteria, generate insights, visualize results, and export everything into a structured Excel MIS report.

This project is designed from a **Data Analyst perspective**, focusing on descriptive analytics, automation, and business-friendly reporting.

---

## 🔍 Problem Statement

In many organizations, customer data is available in CSV or Excel format, but analyzing and segmenting this data manually is time-consuming and error-prone.  
Non-technical users often struggle to generate consistent insights and reports from raw data.

**SegmenTrack solves this problem by:**
- Automating customer segmentation
- Generating segment-level insights
- Creating visual charts
- Exporting a ready-to-use Excel report

---

## 🎯 Project Objectives

- Accept customer data in CSV format
- Validate and process raw data
- Segment customers based on user-selected criteria
- Perform descriptive analytics on each segment
- Visualize key insights using charts
- Export results into a structured Excel (.xlsx) report
- Provide a reusable, command-line-driven analysis pipeline

---

## 🛠️ Tech Stack

- **Python**
- **pandas** – Data ingestion and analysis
- **matplotlib** – Data visualization
- **openpyxl** – Excel report generation

---

## 📁 Project Structure

# ![alt text](<Screenshot 2026-01-22 202716.png>)


---

## 📊 Sample Dataset

The dataset included in the `data/` folder is **synthetic sample data** created solely for demonstration and testing purposes.  
It mimics realistic customer attributes such as demographics and purchase behavior.

---

## ⚙️ How the Project Works (Workflow)

1. User provides a CSV file as input
2. Data is loaded and validated
3. Customers are segmented based on a chosen column (e.g., gender, location)
4. Segment-level metrics are calculated
5. Charts are generated to visualize insights
6. A structured Excel report is created automatically

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install -r requirements.txt

python src/cli.py --input data/sample_customers.csv --segment gender --output output/report.xlsx
```
## 📈 Output

The final output of the project is an Excel (.xlsx) report containing:

- Segment-wise summary statistics  
- Business metrics such as customer count, total purchase, and average purchase  
- Embedded charts for visual interpretation of insights  

This Excel report can be directly shared with stakeholders or used for MIS and business reporting.

---

## 🚫 Out of Scope

The following features are intentionally excluded from this project:

- Machine learning or predictive modeling  
- Real-time data processing  
- Web-based dashboards  
- Integration with external databases  

---

## 🧠 Key Learnings

Through this project, the following key concepts and skills were developed:

- Building an end-to-end data analysis pipeline  
- Automating repetitive data analysis tasks  
- Applying rule-based customer segmentation techniques  
- Creating business-ready Excel MIS reports  
- Structuring Python projects in a clean and modular way  

---

## 📌 Conclusion

SegmenTrack demonstrates how a Data Analyst can move beyond manual analysis by building reusable and automated data pipelines that transform raw data into actionable insights and professional reports.

