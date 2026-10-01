import unicodedata


def normalize_text(text: str) -> str:
    """Apply conservative Unicode, case, and whitespace normalization."""
    normalized = unicodedata.normalize("NFC", text).casefold()
    return " ".join(normalized.split())
