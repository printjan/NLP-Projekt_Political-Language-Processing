# custom regex patterns for phrase removal
PHRASE_PATTERNS_CLASSIFICATION_1 = [
    r"^sehr geehrte[r]? (herr|frau)?( präsident(in)?| vizepräsident(in)?).*?(kolleg(inn)?en)?",
    r"^meine (sehr geehrten )?damen und herren(,)?",
    r"^(werte|liebe) kolleginnen und kollegen",
    r"^ich (möchte|will|werde|darf) mich.*?(bedanken|ausführen|äußern|anschließen)",
    r"(zum|abschließend zum|abschließend möchte ich).*?schluss.*",
    r"ich danke (ihnen|für ihre aufmerksamkeit|für ihre geduld).*?$",
    r"(vielen|herzlichen) dank für.*?$",
    r"^(danke|besten dank|vielen dank).*?$",
    r"^(herr|frau) (präsident|präsidentin|vizepräsident|vizepräsidentin),?$",
]

PHRASE_PATTERNS_CLASSIFICATION_2 = [
    # Begrüßung zu Beginn der Rede
    r"^sehr geehrte.? (herr|frau)? (präsident.?|vizepräsident.?|kolleg.*?|abgeordnet.*?).*?,?",
    r"^meine (sehr geehrten )?(damen und herren|kolleg.*?),?",
    r"^(werte|liebe|geschätzte|geehrte).{1,20}(kolleg.*?|abgeordnet.*?),?",
    r"^(herr|frau) (präsident.?|vizepräsident.?|vorsitzende.?),?",

    # typische Redeeinleitung
    r"^ich (möchte|will|darf|werde)( mich)? (kurz |noch |nun )?(äußern|anschließen|bedanken|ausführen|einbringen).*?,?",
    r"^(zum|abschließend zum|abschließend möchte ich).*?(schluss|punkt|ende).*?,?",

    # Verabschiedungen / Danksagungen am Redeende
    r"(ich )?(bedanke mich|danke ihnen)( sehr| herzlich)?( für ihre (aufmerksamkeit|geduld|zeit))?.*?$",
    r"(vielen|herzlichen|besten) dank.*?$",
    r"^danke.*?$",
]


PHRASE_PATTERNS_CLASSIFICATION_3 = [
    # Formal greetings (start of speeches)
    r"^sehr geehrte[r]? (herr|frau)? ?(präsident(in)?|vizepräsident(in)?|schriftführer(in)?).*?$",
    r"^meine (sehr geehrten )?damen und herren(,)? ?(werte|liebe)? ?(kolleginnen und kollegen)?.*?$",
    r"^(werte|liebe) kolleginnen und kollegen.*?$",
    r"^(herr|frau) (präsident(in)?|vizepräsident(in)?),?$",

    # Expressions of gratitude or closing remarks (end of speeches)
    r"(ich)? (möchte|will|werde|darf) mich.*?(bedanken|danken|anschließen|äußern|ausführen).*?$",
    r"(zum|abschließend|abschließend zum|zum abschluss|zusammenfassend).*?(schluss|ende).*?$",
    r"^(vielen|herzlichen|besten)? ?dank ?(für ihre aufmerksamkeit|für ihre geduld)?.*?$",
    r"ich danke (ihnen|für ihre aufmerksamkeit|für ihre geduld).*?$",

    # General moderation phrases that don't indicate political alignment
    r"das wort hat (jetzt|nun).*?$",
    r"als nächstes spricht.*?$",

    # Procedural phrases (neutral parliamentary management)
    r"wir kommen.*?zur abstimmung.*?$",
    r"die sitzung.*?eröffnet.*?$",
    r"die sitzung.*?(ist)? ?geschlossen.*?$",
    r"tagesordnungspunkt.*?$",
    r"es folgt.*?eine rede.*?$",
]