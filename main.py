# main.py
import os
import pandas as pd
from scraper import scrape_article
from analysis import TextAnalyzer

def main():
    print(" Starting Project Analysis...")

    # Ensure directories exist
    os.makedirs("articles", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # Initialize analyzer with your actual paths
    analyzer = TextAnalyzer(
        master_dict_dir="MasterDictionary",
        stopwords_dir="StopWords"
    )

    # Load input
    input_df = pd.read_excel("input/Input.xlsx")
    if "URL_ID" not in input_df.columns or "URL" not in input_df.columns:
        raise ValueError("Input.xlsx must contain 'URL_ID' and 'URL' columns")

    results = []
    for _, row in input_df.iterrows():
        url_id = str(row["URL_ID"])
        url = str(row["URL"])

        txt_path = f"articles/{url_id}.txt"
        scrape_article(url, txt_path)

        # Read article text
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception:
            text = ""

        # Analyze
        metrics = analyzer.analyze(text)
        metrics["URL_ID"] = url_id
        metrics["URL"] = url
        results.append(metrics)

    # Save output
    output_df = pd.DataFrame(results)
    output_df.to_excel("output/output.xlsx", index=False)
    print(" Analysis complete! Results saved to 'output/output.xlsx'")

if __name__ == "__main__":
    main()