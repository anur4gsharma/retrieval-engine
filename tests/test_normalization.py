from retrieval_engine.text.normalization import normalize_text


def test_normalize_text_casefolds_unicode_text():
    assert normalize_text("Straße and MIXED Case") == "strasse and mixed case"


def test_normalize_text_applies_canonical_unicode_normalization():
    composed = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
    decomposed = "cafe\N{COMBINING ACUTE ACCENT}"

    assert normalize_text(composed) == normalize_text(decomposed)


def test_normalize_text_collapses_whitespace():
    assert normalize_text("  one\ttwo\r\nthree  ") == "one two three"


def test_normalize_text_preserves_punctuation_and_accents():
    assert normalize_text("Café, C++!") == "café, c++!"


def test_normalize_text_keeps_empty_text_empty():
    assert normalize_text("") == ""


def test_normalize_text_is_idempotent():
    text = "  STRASSE,\te\N{COMBINING ACUTE ACCENT}  "

    once_normalized = normalize_text(text)

    assert normalize_text(once_normalized) == once_normalized
