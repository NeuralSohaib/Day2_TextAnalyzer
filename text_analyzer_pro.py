# Day 2 Project - Professional Text Analyzer
from textblob import TextBlob
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import json

console = Console()

def analyze_text(text):
    # Basic statistics
    word_count = len(text.split())
    char_count = len(text)
    sentence_count = text.count(".") + text.count("!") + text.count("?")

    # Word frequency
    words = [word.lower() for word in text.split()]
    word_freq = Counter(words).most_common(10)

    # Sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.1:
        sentiment_label = "Positive"
        sentiment_explanation = "Your text carries an uplifting and encouraging tone."
        color = "green"
    elif sentiment_score < -0.1:
        sentiment_label = "Negative"
        sentiment_explanation = "Your text expresses sadness, frustration, or negativity."
        color = "red"
    else:
        sentiment_label = "Neutral"
        sentiment_explanation = "Your text feels balanced without strong emotions."
        color = "yellow"

    # Readability (rough estimate)
    readability_score = 206.835 - (1.015 * (word_count / max(1, sentence_count))) - (84.6 * (char_count / max(1, word_count)))

    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentence_count": sentence_count,
        "word_freq": word_freq,
        "sentiment": {
            "score": sentiment_score,
            "label": sentiment_label,
            "explanation": sentiment_explanation,
            "color": color
        },
        "readability": readability_score
    }

def display_results(results):
    table = Table(title="Text Analysis Report", show_lines=True)
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Word Count", str(results["word_count"]))
    table.add_row("Character Count", str(results["char_count"]))
    table.add_row("Sentence Count", str(results["sentence_count"]))
    table.add_row("Most Common Words", str(results["word_freq"]))
    table.add_row("Readability Score", str(round(results["readability"], 2)))

    console.print(table)

    # Sentiment highlighted in color
    s = results["sentiment"]
    console.print(Panel.fit(
        f"[bold {s['color']}]Sentiment: {s['label']} ({s['score']:.2f})\n\n{s['explanation']}[/bold {s['color']}]",
        title="Sentiment Analysis",
        border_style=s['color']
    ))

def save_results(results, filename="analysis_results.json"):
    # Convert word_freq tuple list into a list of dicts for JSON
    results_to_save = results.copy()
    results_to_save["word_freq"] = [{"word": w, "count": c} for w, c in results["word_freq"]]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results_to_save, f, indent=4, ensure_ascii=False)

    console.print(f"\n✅ Results saved to [bold green]{filename}[/bold green]")

if __name__ == "__main__":
    text = input("Enter your text:\n")
    results = analyze_text(text)
    display_results(results)
    save_results(results)