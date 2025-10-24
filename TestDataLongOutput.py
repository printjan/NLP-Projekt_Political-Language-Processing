# Load faction abbreviation map
import pandas as pd
from tqdm import tqdm
from transformers import BertTokenizer

faction_map = pd.read_pickle("dataStage03/dataFactionsStage03/factionsAbbreviations.pkl").drop_duplicates(subset="id").set_index("id")["abbreviation"]

# Custom order and color mapping in Plots
order = ["CDU/CSU", "SPD", "Die Grünen", "AfD", "FDP", "DIE LINKE."]
party_colors = {
    "CDU/CSU": "#000000",         # black
    "SPD": "#E3000F",             # red
    "Die Grünen": "#46962B",  # green
    "FDP": "#FFED00",             # yellow
    "AfD": "#009EE0",             # blue
    "DIE LINKE.": "#BE3075",      # magenta
}

tokenizer = BertTokenizer.from_pretrained("bert-base-german-cased")

for term in [19, 20]:
    # load speech data
    df = pd.read_pickle(f"dataFinalStage/speechContentFinalStage/speech_content_{term}.pkl")
    valid_ids = [0, 3, 4, 5, 7, 15, 25]
    df = df[df["faction_id"].isin(valid_ids)].copy()
    df.loc[df["faction_id"] == 3, "faction_id"] = 7 # merging BSW into DIE LINKE.

    # Apply faction map to get party labels
    df["faction_abbreviation"] = df["faction_id"].map(faction_map)
    # Replace long name with short name for display
    df["faction_abbreviation"] = df["faction_abbreviation"].replace({"Bündnis 90/Die Grünen": "Die Grünen"})

    # Compute character and BERT-token lengths
    tqdm.pandas(desc="Calculating speech lengths")
    df["char_count"] = df["speech_content"].progress_apply(len)
    df["bert_token_count"] = df["speech_content"].progress_apply(lambda x: len(tokenizer.tokenize(x)))

    # Calculate mean values
    summary = df.groupby("faction_abbreviation").agg({
        "char_count": "mean",
        "bert_token_count": "mean"
    }).round(2).reset_index()

    with open(f"output_speech_lengths_term_{term}.txt", "w", encoding="utf-8") as f:
        f.write("\n--- Speech Lengths ---\n")
        for _, row in df.iterrows():
            f.write(
                f"[{row['faction_abbreviation']}] {row['char_count']} characters, {row['bert_token_count']} BERT tokens\n")

        f.write("\n--- Average Speech Length per Party (Markdown) ---\n")
        f.write(f"### Electoral Term {term}\n")
        f.write("| Party | Avg. Char Count | Avg. BERT Token Count |\n")
        f.write("|-------|------------------|------------------------|\n")
        for _, row in summary.iterrows():
            f.write(f"| {row['faction_abbreviation']} | {row['char_count']} | {row['bert_token_count']} |\n")

    # Print every speech's party and length
    #print("\n--- Speech Lengths ---")
    #for _, row in df.iterrows():
    #    print(f"[{row['faction_abbreviation']}] {row['char_count']} characters, {row['bert_token_count']} BERT tokens")

    # Print summary as Markdown
    print("\n--- Average Speech Length per Party (Markdown) ---\n")
    print(f"### Electoral Term {term}")
    print("| Party | Avg. Char Count | Avg. BERT Token Count |")
    print("|-------|------------------|------------------------|")
    for _, row in summary.iterrows():
        print(f"| {row['faction_abbreviation']} | {row['char_count']} | {row['bert_token_count']} |")