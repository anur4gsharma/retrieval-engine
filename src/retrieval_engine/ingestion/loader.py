from pathlib import Path

import Document

def load_documents(root: str | Path) -> list[Document]:
    
    root = Path(root)

    if not root.is_dir():
        raise NotADirectoryError(root)

    paths = sorted(root.rglob("*.txt"))

    document_id = path.relative_to(root).as_posix()

    text = path.read_text(encoding="utf-8")

    document = Document(
        id=document_id,
        text=text,
        metadata={
            "filename": path.name,
            "path": document_id,
        },
    )

    return document