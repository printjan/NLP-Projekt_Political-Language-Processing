from __future__ import annotations
from pathlib import Path
from typing import List, Dict, Set
import paths_ml_task_1 as PATHS
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# --------------------------------------------------------------------------- #
# CONFIGURABLE CONSTANTS
# --------------------------------------------------------------------------- #
SPEECH_ID_COL: str = "id"
LENGTH_COL: str = "speech_length_chars"
LABEL_COL: str = "faction_id"
ABBR_COL: str = "faction_abbreviation"
LOWER_Q = 0.25   # remove shortest 25 %
UPPER_Q = 0.90   # remove longest 10 %  → keep central 65 %

#columns to check#
CRITICAL_COLS: List[str] = [
    "speech_content",
    "speech_content_cleaned",
    "speech_content_stopword",
    "speech_content_lemmatized",
    "speech_content_stemmed",
    "speech_content_tokenized",
    "speech_length_chars",
    "speech_length_lemmas",
    "speech_length_tokens",
]



def drop_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with empty/invalid values in any CRITICAL_COLS."""
    # Ensure at least one critical column exists
    present_cols = [c for c in CRITICAL_COLS if c in df.columns]
    if not present_cols:
        raise KeyError(
            f"None of the CRITICAL_COLS {CRITICAL_COLS} found in DataFrame."
        )

    # 1) NaN values
    invalid_mask = df[present_cols].isna()

    # 2) Numeric sentinel `-1` (for length columns)
    length_cols = [c for c in present_cols if c.startswith("speech_length_chars")]
    if length_cols:
        invalid_mask |= (df[length_cols] == -1)

    # 3) Empty / blank strings
    str_cols = [c for c in present_cols if df[c].dtype == "object"]
    if str_cols:
        blank_mask = df[str_cols].apply(
            lambda col: col.astype(str).str.strip().eq("")
        )
        invalid_mask.loc[:, str_cols] |= blank_mask

    # 4) Empty lists (tokenized / etc.)
    list_cols = [c for c in present_cols if df[c].dtype == "object"]
    for col in list_cols:
        invalid_mask[col] |= df[col].apply(lambda v: isinstance(v, list) and len(v) == 0)

    # Any invalid entry in *any* critical column invalidates the row
    rows_to_drop = invalid_mask.any(axis=1)
    cleaned = df.loc[~rows_to_drop].copy()

    return cleaned


def _length_filter(df: pd.DataFrame, lower_q: float, upper_q: float) -> pd.DataFrame:
    """Filter speeches to the [lower_q, upper_q] length quantile interval (inclusive)."""
    lower_bound = df[LENGTH_COL].quantile(lower_q)
    upper_bound = df[LENGTH_COL].quantile(upper_q)
    return df[(df[LENGTH_COL] >= lower_bound) & (df[LENGTH_COL] <= upper_bound)]


def _load_and_filter(path: Path, lower_q: float, upper_q: float) -> pd.DataFrame:
    """Load a dataset pickle and apply speech-length filtering."""
    # 1) Load raw dataset (BEFORE length filtering and checking)
    df = pd.read_pickle(path)
    # 2) Remove invalid rows
    df = drop_invalid_rows(df)
    # 3) Remove extreme datapoints
    return _length_filter(df, lower_q, upper_q)


def _collect_filtered_ids(dataset_paths: List[Path], lower_q: float, upper_q: float) -> Dict[Path, Set[int]]:
    """Return a mapping {dataset_path: set(filtered_speech_ids)} for every dataset."""
    filtered: Dict[Path, Set[int]] = {}
    for p in dataset_paths:
        df = _load_and_filter(p, lower_q, upper_q)
        filtered[p] = set(df[SPEECH_ID_COL].unique())
    return filtered


def _sample_common_ids(filtered_id_sets: List[Set[int]], sample_size: int | None, rng: np.random.Generator) -> np.ndarray:
    """Take the intersection of all ID sets and sample `sample_size` distinct IDs."""
    if not filtered_id_sets:
        raise ValueError("Keine gefilterten ID-Mengen erhalten …")
    common_ids = set.intersection(*filtered_id_sets)
    if sample_size is None:
        return np.array(sorted(common_ids))

    if len(common_ids) < sample_size:
        raise ValueError(
            f"Only {len(common_ids)} common speeches remain after filtering – "
            f"cannot sample the requested {sample_size} unique IDs."
        )
    return rng.choice(sorted(common_ids), size=sample_size, replace=False)


def _stratified_split(reference_df: pd.DataFrame, ids_to_split: np.ndarray, split_ratio: float = 0.8, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    """Stratified 80/20 split based on LABEL_COL using *only* `ids_to_split`."""
    ref_subset = (reference_df.set_index(SPEECH_ID_COL).loc[ids_to_split])
    first_ids, second_ids = train_test_split(
        ids_to_split,
        test_size=1.0 - split_ratio,
        random_state=seed,
        stratify=ref_subset[LABEL_COL],
    )
    return np.array(first_ids), np.array(second_ids)


def main( seed: int = 42, min_quantile: float = 0.25, max_quantile: float = 0.90, sample_size: int = 1_000,) -> None:
    # 1) Discover all datasets (*.pkl) in the classification data directory
    data_dir = Path(PATHS.BASE_CLASSIFICATION_DATASET_DIR)
    dataset_paths = sorted(data_dir.glob("data_set_*_20.pkl"))
    if not dataset_paths:
        raise FileNotFoundError(f"No datasets found in {data_dir}")

    # 2) Speech-length filtering per dataset
    filtered_id_map = _collect_filtered_ids(dataset_paths, min_quantile, max_quantile)
    ref_path = PATHS.BASE_CLASSIFICATION_DATASET_3_20
    ref_df = pd.read_pickle(ref_path)


    # 3) Intersection & random sampling of 1 000 speeches
    rng = np.random.default_rng(seed)

    # 3.1  –  gemeinsame IDs aller Datensätze (keine Größenvorgabe → nimm alle)
    common_ids = _sample_common_ids(list(filtered_id_map.values()),sample_size=None,rng=rng)
    if common_ids.size == 0:
        raise RuntimeError(
            "Die Schnittmenge der gefilterten IDs ist leer. "
            "→ Prüfe die Quantile oder die Datenbasis."
        )

    # 3.2  –  Label-Verteilung in der Schnittmenge
    common_df = ref_df[ref_df[SPEECH_ID_COL].isin(common_ids)]
    label_col = "faction_id"  # ggf. anpassen
    class_counts = common_df[label_col].value_counts()

    n_classes = len(class_counts)
    wanted_per_class = -(-sample_size // n_classes)
    available_per_class = class_counts.min()  # kleinste Klasse

    # 3.3  –  endgültige Sample-Größe pro Klasse
    samples_per_class = min(wanted_per_class, available_per_class)

    if samples_per_class < wanted_per_class:
        print(
            f"[WARN] Nicht genügend Daten: "
            f"pro Klasse sind nur {available_per_class} statt "
            f"{wanted_per_class} Beispiele verfügbar.\n"
            f"→ sample_size wird auf {samples_per_class * n_classes} reduziert."
        )

    # 3.4  –  Ziehe *genau* samples_per_class Elemente aus **jeder** Klasse
    sampled_ids = (
        common_df
        .groupby(label_col, group_keys=False, sort=False)
        .apply(lambda g: g.sample(n=samples_per_class,
                                  random_state=seed,
                                  replace=False))  # kein Oversampling
        .reset_index(drop=True)[SPEECH_ID_COL]  # nur die ID-Spalte
        .to_numpy()
    )

    print(f"[INFO] Final: {samples_per_class} × {n_classes} = "
          f"{len(sampled_ids)} Samples gleichmäßig verteilt.")


    # 4 a) Build a *single* stratified 80/20 split (same for all datasets) se the “3_20” dataset as reference for label stratification
    train_ids, test_ids = _stratified_split(ref_df,np.array(sampled_ids),split_ratio=0.8,seed=seed)

    # 4 b) *zusätzlicher* Split des GLOBAL-Test-Sets – nur für BERT:  test_bert (80 %) | eval_bert (20 %)
    test_df = ref_df[ref_df[SPEECH_ID_COL].isin(test_ids)]
    test_bert_ids, eval_bert_ids = _stratified_split(test_df,test_ids,split_ratio=0.8, seed=seed)

    # 5) Persist ID lists for downstream pipelines (no need to recompute)
    out_dir = Path(PATHS.BASE_CLASSIFICATION_DATASET_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)

    pd.to_pickle(sampled_ids, PATHS.SAMPLED_IDS)
    pd.to_pickle(train_ids, PATHS.TRAIN_IDS)
    pd.to_pickle(test_ids, PATHS.TEST_IDS)
    pd.to_pickle(test_bert_ids, PATHS.TEST_BERT_IDS)
    pd.to_pickle(eval_bert_ids, PATHS.EVAL_BERT_IDS)

    print(
        f"[Done] {len(sampled_ids)} common speeches selected "
        f"({len(train_ids)} train / {len(test_ids)} global-test). "
        f"BERT-split → {len(test_bert_ids)} test_bert / {len(eval_bert_ids)} eval_bert. "
        f"ID lists written to: {out_dir}"
    )


if __name__ == "__main__":
    main()