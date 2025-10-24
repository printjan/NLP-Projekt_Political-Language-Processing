

# importsimport numpy as np
import regex


def clean_name_headers(filetext, names, contributions_extended_filter=False):
    """
    Cleans given text lines that typically represent headers or voting list remnants in PDF-extracted Bundestag protocols.
    These often follow the format: "Präsident Dr. Lammert" or "Bundeskanzler Scholz", which may disrupt later NLP processing.
    Keep in mind this also deletes lines from voting lists.

    This function matches and removes such lines using known names, especially helpful when parsing raw extracted text.

    :param filetext (str): Raw text string extracted from a PDF file, potentially with headers.
    :param names (list[str] or np.ndarray): List or array of known names to match and remove from the header.
    :param contributions_extended_filter (bool): If True, the function first removes brackets from all names to make matching more robust.
    :return: filetext (str): Cleaned text with matched name headers and line-number artifacts removed.
    """
    if contributions_extended_filter:
        # Remove any brackets from names to generalize matches (e.g., for speech contributions)
        table = {ord(c):"" for c in "()[]{}"}
        names = np.unique([name.translate(table) for name in names])

    # Escape regex-sensitive characters such as +, *, ?
    table = {ord("+"): "\\+", ord("*"): "\\*", ord("?"): "\\?"}
    names_to_clean = ("(" + "|".join(names) + ")").translate(table)

    # Match and remove lines like "\nBundeskanzler Scholz\n"
    pattern = (
        r"\n((?:Parl\s?\.\s)?Staatssekretär(?:in)?|Bundeskanzler(?:in)?|Bundesminister(?:in)?|Staatsminister(:?in)?)?\s?"  # noqa: E501
        + names_to_clean
        + r" *\n"
    )
    filetext = regex.sub(pattern, "\n", filetext)

    # Remove lines that only contain a number (page or list position markers)
    pattern = r"\n\d+ *\n"
    filetext = regex.sub(pattern, "\n", filetext)

    return filetext