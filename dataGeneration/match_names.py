# imports
import pandas as pd
import numpy as np
import regex
import Levenshtein


def get_fuzzy_names(df, name_to_check, fuzzy_threshold=0.7):
    """
    Returns rows from df where the Levenshtein similarity of the last name to 'name_to_check'
    is greater than or equal to 'fuzzy_threshold'.

    :param df (pd.DataFrame): DataFrame with a column 'last_name'.
    :param name_to_check (str): Name to compare against.
    :param fuzzy_threshold (float): Minimum similarity ratio.
    :return: (pd.DataFrame): Matching subset of df.
    """
    return df.loc[
        df["last_name"].apply(Levenshtein.ratio, args=[name_to_check]) >= fuzzy_threshold
    ]


def get_possible_matches(df, **columns):
    """
    Filters a DataFrame by multiple column-value pairs and returns possible
    matches in df with respect to specified columns.

    :param df (pd.DataFrame): The DataFrame to filter.
    :param columns (dict): Dictionary of column names and desired values.
    :return: (pd.DataFrame): Filtered DataFrame.
    """

    for col_name, col_value in columns.items():
        df = df.loc[df[col_name] == col_value]

    return df


def check_unique(possible_matches, col="ui"):
    """
    Checks whether the specified column has exactly one unique value.

    :param possible_matches (pd.DataFrame): The DataFrame to check.
    :param col (str): The column to test uniqueness on.
    :return: (bool): True if unique, False otherwise.
    """
    return len(np.unique(possible_matches[col])) == 1


def set_id(df, index, possible_matches, col_set, col_check):
    """
    Assigns a value from 'col_check' of the matches to the 'col_set' column at a specific index.

    :param df (pd.DataFrame): Target DataFrame.
    :param index (int): Row index to update.
    :param possible_matches (pd.DataFrame): Matching DataFrame.
    :param col_set (str): Column to update.
    :param col_check (str): Source column to extract value from.
    """
    df[col_set].at[index] = int(possible_matches[col_check].iloc[0])


def set_value(df, index, col, value):
    """
    Sets the specified value in the given DataFrame column at the target index.

    :param df (pd.DataFrame): Target DataFrame.
    :param index (int): Index to update.
    :param col (str): Column name.
    :param value (any): Value to assign.
    """
    df[col].at[index] = value


def check_last_name(df, index, possible_matches, last_name):
    """
    Filters matches by last name and assigns ID if match is unique.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Target row.
    :param possible_matches (pd.DataFrame): Search space.
    :param last_name (str): Last name to check.
    :return: (bool, pd.DataFrame): Whether match was unique, and filtered matches.
    """
    possible_matches = get_possible_matches(possible_matches, last_name=last_name)

    if check_unique(possible_matches):
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        return False, possible_matches


def check_first_name(df, index, possible_matches, first_name):
    """
    Filters matches by first name (set-based token overlap) and assigns ID if match is unique.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Target row.
    :param possible_matches (pd.DataFrame): Search space.
    :param first_name (list[str]): Tokenized first name(s).
    :return: (bool, pd.DataFrame): Whether match was unique, and filtered matches.
    """
    first_name_set = set(first_name)

    possible_matches = possible_matches.loc[
        ~possible_matches["first_name"].apply(lambda x: set(x).isdisjoint(first_name_set))
    ]

    if check_unique(possible_matches):
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        return False, possible_matches


def check_faction_id(df, index, possible_matches, faction_id):
    """
    Filters matches by faction ID and assigns politician ID if match is unique.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Target row.
    :param possible_matches (pd.DataFrame): Filtered matches.
    :param faction_id (int): Faction ID to match.
    :return: (bool, pd.DataFrame): Whether match was unique, and filtered matches.
    """
    # Get possible matches according to faction_id.
    possible_matches = get_possible_matches(possible_matches, faction_id=faction_id)

    # Check if IDs unique.
    if check_unique(possible_matches):
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        return False, possible_matches


def check_location_info(df, index, possible_matches, constituency, fuzzy_threshold=0.7):
    """
    Performs fuzzy matching on constituency names and sets ID if match is unique.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Target row.
    :param possible_matches (pd.DataFrame): Filtered matches.
    :param constituency (str): Target constituency string.
    :param fuzzy_threshold (float): Similarity threshold.
    :return: (bool, pd.DataFrame): Whether match was unique, and filtered matches.
    """
    possible_matches = possible_matches.loc[
        possible_matches["constituency"].apply(Levenshtein.ratio, args=[constituency])
        > fuzzy_threshold
    ]

    if len(np.unique(possible_matches["ui"])) == 1:
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        return False, possible_matches


def check_name_and_profession(
    df, index, last_name, profession_regex, politicians_df, fuzzy_threshold=75
):
    """
    Matches using last name and profession regex, with optional fuzzy fallback.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Target row.
    :param last_name (str): Last name to match.
    :param profession_regex (str): Regex pattern for profession.
    :param politicians_df (pd.DataFrame): Search space.
    :param fuzzy_threshold (float): Threshold for fuzzy name match.
    :return: (bool, pd.DataFrame): Whether match was unique, and filtered matches.
    """
    possible_matches = get_possible_matches(politicians_df, last_name=last_name)

    if len(possible_matches) == 0:
        possible_matches = get_fuzzy_names(
            politicians_df, name_to_check=last_name, fuzzy_threshold=fuzzy_threshold
        )

    if check_unique(possible_matches):
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        boolean_indexer = possible_matches["profession"].str.contains(
            profession_regex, regex=True, na=False
        )
        possible_matches = possible_matches[boolean_indexer]

        if check_unique(possible_matches):
            set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
            return True, possible_matches
        else:
            return False, possible_matches


def check_government(df, index, last_name, mgs_electoral_term, fuzzy_threshold=80):
    """
    Attempts to match a government member by last name (with optional fuzzy fallback).
    Assigns the corresponding politician ID if a unique match is found.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Index in DataFrame to write ID to.
    :param last_name (str): Last name to match.
    :param mgs_electoral_term (pd.DataFrame): Data of government members for the electoral term.
    :param fuzzy_threshold (int): Minimum fuzzy similarity score (0-100).
    :return: (bool, pd.DataFrame): Whether a unique match was found, and filtered matches.
    """
    possible_matches = get_possible_matches(mgs_electoral_term, last_name=last_name)

    if len(possible_matches) == 0:
        possible_matches = get_fuzzy_names(
            mgs_electoral_term, name_to_check=last_name, fuzzy_threshold=fuzzy_threshold
        )

    if check_unique(possible_matches):
        set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
        return True, possible_matches
    else:
        return False, possible_matches


def check_member_of_parliament(
    df,
    index,
    first_name,
    last_name,
    politicians,
    faction_id,
    constituency,
    acad_title,
    fuzzy_threshold=80,
):
    """
    Attempts to match a parliament member (MP) based on multiple attributes.
    The method applies several filters including last name, faction, first name,
    constituency, and gender heuristics to assign a unique politician ID.

    :param df (pd.DataFrame): The DataFrame to update.
    :param index (int): Row index in DataFrame to modify.
    :param first_name (list[str]): First name tokens to match.
    :param last_name (str): Last name to match.
    :param politicians (pd.DataFrame): Reference DataFrame of all MPs.
    :param faction_id (int): Optional faction ID for disambiguation.
    :param constituency (str): Optional constituency for disambiguation.
    :param acad_title (str): Academic title, used for gender heuristics.
    :param fuzzy_threshold (int): Threshold for fuzzy name matching.
    :return: (bool, pd.DataFrame): Whether a unique match was found, and filtered matches.
    """
    # Check Last Name.
    found, possible_matches = check_last_name(df, index, politicians, last_name)
    if found:
        return True, possible_matches

    # Fuzzy search, if last_name can't be found.
    if len(possible_matches) == 0:
        possible_matches = get_fuzzy_names(politicians, name_to_check=last_name)

    if len(possible_matches) == 0:
        return False, possible_matches

    # Check Faction ID.
    if faction_id >= 0:
        found, possible_matches = check_faction_id(
            df, index, possible_matches, faction_id
        )
        if found:
            return found, possible_matches

    # Check First Name.
    if first_name:
        found, possible_matches = check_first_name(
            df, index, possible_matches, first_name
        )
        if found:
            return found, possible_matches

    # Match with location info.
    if constituency:
        found, possible_matches = check_location_info(
            df, index, possible_matches, constituency
        )
        if found:
            return found, possible_matches
    elif constituency == "":
        # Probably someone joined during the period, e.g. there
        # is an entry in STAMMDATEN for the correct person
        # without the location info, as there was only one
        # person with the last name before.
        possible_matches = get_possible_matches(possible_matches, constituency="")
        if check_unique(possible_matches, col="ui"):
            set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
            return True, possible_matches

    # Check Gender.
    found, possible_matches = check_woman(df, index, acad_title, possible_matches)
    if found:
        return True, possible_matches
    else:
        return False, possible_matches


def check_woman(df, index, acad_title, possible_matches):
    """
    Filters possible matches to female politicians based on academic title and checks uniqueness.

    :param df (pd.DataFrame): DataFrame to update.
    :param index (int): Index to write result to.
    :param acad_title (str): Academic title (used to infer gender, e.g. "Frau").
    :param possible_matches (pd.DataFrame): DataFrame of current potential politician matches.
    :return: (bool, pd.DataFrame): True if unique female match was found, else False. Also returns filtered matches.
    """
    if "Frau" in acad_title:
        possible_matches = possible_matches.loc[possible_matches["gender"] == "weiblich"]

        if check_unique(possible_matches):
            set_id(df, index, possible_matches, col_set="politician_id", col_check="ui")
            return True, possible_matches
    return False, possible_matches


def insert_politician_id_into_contributions_extended(
    df, politicians_electoral_term, mgs_electoral_term
):
    """
    Inserts politician IDs into a contributions DataFrame by matching names, factions, and other metadata.
    Also returns unmatched entries for debugging.

    :param df (pd.DataFrame): Contributions DataFrame to enrich with politician_id.
    :param politicians_electoral_term (pd.DataFrame): DataFrame containing parliament members for the term.
    :param mgs_electoral_term (pd.DataFrame): DataFrame containing government members for the term.
    :return: (pd.DataFrame, pd.DataFrame): Updated DataFrame with politician IDs, and a DataFrame of unresolved cases.
    """
    assert {
        "last_name",
        "first_name",
        "faction_id",
        "acad_title",
        "constituency",
    }.issubset(df.columns)

    if len(df) == 0:
        return df, pd.DataFrame()

    last_name_copy = df["last_name"].copy()
    first_name_copy = df["first_name"].copy()

    problem_df = []

    # Lower case to ease up matching
    df["first_name"] = df["first_name"].apply(
        lambda first: [str.lower(string) for string in first]
    )
    df["constituency"] = df["constituency"].fillna("")
    df["constituency"] = df["constituency"].str.lower()
    df["last_name"] = df["last_name"].str.lower()
    df["last_name"] = df["last_name"].str.replace("ß", "ss", regex=False)
    df.insert(4, "politician_id", -1)

    for index, row in df.iterrows():

        # Start Matching

        # E.g. Präsident, Bundeskanzler, Staatssekretär etc.
        if not row["last_name"]:
            # Skip entries with empty last names (likely moderators etc.)
            problem_df.append(row)
            continue
        else:
            found, possible_matches = check_last_name(
                df, index, politicians_electoral_term, row["last_name"]
            )
            if found:
                if check_unique(possible_matches, col="faction_id"):
                    set_id(
                        df,
                        index,
                        possible_matches,
                        col_set="faction_id",
                        col_check="faction_id",
                    )
                    continue
                else:
                    continue

        # Fuzzy search, if last_name can't be found.
        if len(possible_matches) == 0:
            possible_matches = get_fuzzy_names(
                politicians_electoral_term, row["last_name"]
            )

        if len(possible_matches) == 0:
            problem_df.append(row)
            continue

        # Check Faction ID.
        if row["faction_id"] >= 0:
            found, possible_matches = check_faction_id(
                df, index, possible_matches, row["faction_id"]
            )
            if found:
                if check_unique(possible_matches, col="faction_id"):
                    df["faction_id"].at[index] = int(possible_matches["faction_id"].iloc[0])
                    continue
                else:
                    continue

        # Check First Name.
        if row["first_name"]:
            found, possible_matches = check_first_name(
                df, index, possible_matches, row["first_name"]
            )
            if found:
                continue

        # Match with location info.
        if row["constituency"]:
            found, possible_matches = check_location_info(
                df, index, possible_matches, row["constituency"]
            )
            if found:
                continue
        elif row["constituency"] == "":
            # Probably someone joined during the period, e.g. there
            # is an entry in STAMMDATEN for the correct person
            # without the location info, as there was only one
            # person with the last name before.
            possible_matches = get_possible_matches(possible_matches, constituency="")

            if check_unique(possible_matches):
                set_id(
                    df, index, possible_matches, col_set="politician_id", col_check="ui"
                )
                continue

        # Check Gender.
        found, possible_matches = check_woman(
            df, index, row["acad_title"], possible_matches
        )
        if found:
            continue

        # No reliable match found: store for debugging
        # Example: Meyer in 01033. Have the same last name and
        # are in the same faction at same period. In this
        # particular case the location information in the toc
        # "Westhagen", does not match with the two possible
        # location informations "Hagen", "Bremen"
        # probably "Hagen" == "Westfalen" is meant.
        # Other things: Cornelia Irgendwas, ist in dem spoken content
        # mit "Conny Irgendwas abgespeichert. Findet Vornamen natürlich
        # nicht.
        problem_df.append(row)

        # Restore original name values in case further postprocessing requires it
        df["first_name"] = first_name_copy
        df["last_name"] = last_name_copy

    problem_df = pd.DataFrame(problem_df)
    return df, problem_df