from pathlib import Path

from .document import Document


def load_documents(root: str | Path) -> list[Document]:
    root = Path(root)

    if not root.is_dir():
        raise NotADirectoryError(root)

    paths = sorted(
        root.rglob("*.txt"),
        key=lambda path: path.relative_to(root).as_posix(),
    )

    documents: list[Document] = []
    for path in paths:
        document_id = path.relative_to(root).as_posix()

        text = path.read_text(encoding="utf-8")

        documents.append(
            Document(
                id=document_id,
                text=text,
                metadata={
                    "filename": path.name,
                    "path": document_id,
                },
            )
        )

    return documents
