# 🧠Article Data scapping and Analysis Engine

> **Automated Article Scraper and Text Analyzer for Blackcoffer Assignment**  
> A Python solution that extracts article content from URLs and computes 13 linguistic variables as specified in the Blackcoffer test assignment.

![Python](https://img.shields.io/badge/Python-3.12.3%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green?logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-orange?logo=beautifulsoup)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📌 Assignment Overview (Per `Objective.docx`)

This project fulfills the **Blackcoffer Data Extraction and NLP Test Assignment** with the following requirements:

1. **Data Extraction**  
   - Read URLs from `Input.xlsx` (columns: `URL_ID`, `URL`)  
   - For each URL, **extract only the article title and article body text**  
   - **Exclude** website headers, footers, navigation, ads, or any non-article content  
   - Save each extracted article as a plain text file named `{URL_ID}.txt`

2. **Data Analysis**  
   - For each extracted text file, compute **13 specific variables**:
     1. POSITIVE SCORE  
     2. NEGATIVE SCORE  
     3. POLARITY SCORE  
     4. SUBJECTIVITY SCORE  
     5. AVG SENTENCE LENGTH  
     6. PERCENTAGE OF COMPLEX WORDS  
     7. FOG INDEX  
     8. AVG NUMBER OF WORDS PER SENTENCE  
     9. COMPLEX WORD COUNT  
     10. WORD COUNT  
     11. SYLLABLE PER WORD  
     12. PERSONAL PRONOUNS  
     13. AVG WORD LENGTH  
   - Variable definitions are specified in the assignment’s `Text Analysis.docx` (not provided here; implementation follows standard linguistic interpretations where needed)

3. **Output**  
   - Generate a single output file (Excel or CSV) containing:
     - All original columns from `Input.xlsx` (`URL_ID`, `URL`)
     - Followed by the **13 computed variables in exact order** as shown in `Output Data Structure.xlsx`

4. **Technical Requirements**  
   - Entirely implemented in **Python**  
   - Allowed libraries: `BeautifulSoup`, `Selenium`, `Scrapy`, or any Python web scraping/NLP tools  
   - Final submission must include:
     - A `.py` script
     - Output file (CSV or Excel)
     - Documentation explaining approach, usage, and dependencies

---

## 📁 Project Structure

```text
blackcoffer-assignment/
├── input/
│   └── Input.xlsx                 # Provided input file (URL_ID + URL)
├── output/
│   └── output.xlsx                # Generated output (matches required structure)
├── articles/                      # Temporary storage for {URL_ID}.txt files
├── main.py                        # Main script: scraping + analysis
├── requirements.txt               # Python dependencies
└── README.md                      # This documentation
