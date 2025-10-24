DOMAIN_SPECIFIC_STOPWORDS_CLASSIFICATION_1 = {
    # Formelhafte Begrüßungen (neutral hinsichtlich Partei)
    "sehr", "geehrte", "geehrter", "werte", "werter", "liebe", "geschätzte", "lieber", "geschätzter",
    "damen", "herren", "herr", "frau", "präsident", "präsidentin",
    "vizepräsident", "vizepräsidentin", "vorsitzender", "vorsitzende",
    "vorsitz", "mitglied", "mitglieder", "abgeordnete", "abgeordneten", "abgeordneter",
    "sitzung",
    "tagesordnungspunkt", "abstimmung",

    # Moderative Begriffe (keine Parteiaussage)
    "schriftführer", "schriftführerin", "berichterstatter", "berichterstatterin",

    # Redebeginn/-ende Floskeln ohne politischen Inhalt
    "danke", "bedanken", "bedanke", "möchte", "will", "werde", "darf", "dank",
    "anschließen", "ausführen", "einbringen", "kurz", "abschließend", "geduld", "aufmerksamkeit",
    "schluss", "punkt", "ende", "kommen", "hinzufügen", "erwähnen",
    "begrüßen", "verabschieden","kurz",

    # Höfliche, neutrale Füllwörter (ohne Parteiaussage)
    "bitte", "vielen", "herzlichen", "besten", "willkommen",
    "entschuldigung", "antrag", "anträge", "frage", "fragen",

    # Metakommunikative Floskeln (ohne Parteiaussage)
    "reden", "rede", "gesagt", "sagen", "sprechen", "beitrag",
    "anrede", "ausführungen", "feststellen", "meinen", "anmerken",
    "erlauben", "gestatten",

    # Strukturwörter (ohne politische Aussage, aber KEINE grammatischen Hilfswörter)
    "wort", "genommen", "zurück", "vorweg", "zunächst", "danach", "abschließend", "abschließenden",  "einleitend", "nachfolgend", "anschließend", "anschließenden",  "weiterhin",

    # Zahlen in Worten (oft neutral)
    "erstens", "zweitens", "drittens", "viertens", "fünftens", "sechstens",
    "siebtens", "achtens", "neuntens", "zehntens","nochmals",

    # neutrale Abkürzungen
    "dr", "prof", "mdB",
}