from retrieval_engine.ingestion.loader import load_documents

def test_load_documents_from_directory(tmp_path):

    file_path1 = tmp_path / "doc1.txt"
    file_path2 = tmp_path / "doc2.txt"
    file_path3 = tmp_path / "doc3.txt"

    file_path1.write_text("Creating text file 1.", encoding="utf-8")
    file_path2.write_text("Creating text file 2.", encoding="utf-8")
    file_path3.write_text("Creating text file 3.", encoding="utf-8")

    documents = load_documents(tmp_path)

    assert len(documents) == 3