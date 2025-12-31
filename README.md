# 🧠 BlackCoffer Text Analysis Engine

> **Automated Web Article Scraper + Sentiment & Readability Analyzer**  
> Built for the [BlackCoffer Internship Assignment](https://blackcoffer.com/) — extracting insights from online articles using NLP, custom dictionaries, and linguistic rules.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 🎯 Objective

Given a list of URLs, this project:
1. **Scrapes** clean article text from each webpage  
2. **Analyzes** it using official BlackCoffer dictionaries:
   - ✅ `positive-words.txt`
   - ✅ `negative-words.txt`
   - ✅ 7 `StopWords_*.txt` files
3. **Computes 13+ linguistic & sentiment metrics** per article  
4. **Exports results** to a structured Excel report

Perfect for **sentiment analysis**, **readability scoring**, and **content intelligence** tasks.

---

## 📁 Project Structure

```text
project-task/
├── input/
│   └── Input.xlsx                 # 📥 Input: URL_ID + URLs
├── output/
│   └── output.xlsx                # 📤 Final analysis report (auto-generated)
├── articles/                      # 🗃️ Temporary scraped .txt files (DO NOT SUBMIT)
├── MasterDictionary/
│   ├── positive-words.txt         # ✅ Official positive lexicon
│   └── negative-words.txt         # ❌ Official negative lexicon
├── StopWords/                     # 🛑 All 7 stopword lists
│   ├── StopWords_Auditor.txt
│   ├── StopWords_Currrencies.txt
│   ├── StopWords_DatesandNumbers.txt
│   ├── StopWords_Generic.txt
│   ├── StopWords_GenericLong.txt
│   ├── StopWords_Geographic.txt
│   └── StopWords_Names.txt
├── scraper.py                     # 🕷️ Web content extractor
├── analysis.py                    # 📊 NLP + metric calculator
├── main.py                        # 🚀 Orchestration engine
├── requirements.txt               # ⚙️ Dependencies
└── README.md                      # 📘 You are here!