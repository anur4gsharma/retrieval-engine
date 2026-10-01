import pytest

from retrieval_engine.ingestion.loader import load_documents


def test_load_documents_from_directory(tmp_path):
    (tmp_path / "doc2.txt").write_text("second document", encoding="utf-8")
    (tmp_path / "doc1.txt").write_text("first document", encoding="utf-8")
    (tmp_path / "ignore.md").write_text("not a text file", encoding="utf-8")

    documents = load_documents(tmp_path)

    assert [document.id for document in documents] == ["doc1.txt", "doc2.txt"]
    assert [document.text for document in documents] == [
        "first document",
        "second document",
    ]
    assert len({document.id for document in documents}) == 2
    assert documents[0].metadata == {"filename": "doc1.txt", "path": "doc1.txt"}


def test_load_documents_recursively_with_posix_ids(tmp_path):
    nested_directory = tmp_path / "guide"
    nested_directory.mkdir()
    (nested_directory / "start.txt").write_text("nested text", encoding="utf-8")
    (tmp_path / "intro.txt").write_text("intro text", encoding="utf-8")

    documents = load_documents(tmp_path)

    assert [document.id for document in documents] == ["guide/start.txt", "intro.txt"]
    assert documents[0].metadata["path"] == "guide/start.txt"
    assert documents[0].metadata["filename"] == "start.txt"


def test_load_documents_returns_empty_list_for_empty_directory(tmp_path):
    assert load_documents(tmp_path) == []


def test_load_documents_keeps_empty_text_file(tmp_path):
    (tmp_path / "empty.txt").write_text("", encoding="utf-8")

    documents = load_documents(tmp_path)

    assert len(documents) == 1
    assert documents[0].text == ""


def test_load_documents_requires_directory(tmp_path):
    file_path = tmp_path / "document.txt"
    file_path.write_text("text", encoding="utf-8")

    with pytest.raises(NotADirectoryError):
        load_documents(file_path)


def test_load_documents_propagates_invalid_utf8(tmp_path):
    (tmp_path / "invalid.txt").write_bytes(b"\xff")

    with pytest.raises(UnicodeDecodeError):
        load_documents(tmp_path)
