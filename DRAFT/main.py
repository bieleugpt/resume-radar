from ingestion import ingest_file
from structuring import structure_document
from embedding import embed_structured_document

from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    file_path = BASE_DIR / "DATA" / "offre.txt"
    cv_path = BASE_DIR / "DATA" / "CV.pdf"
    text = ingest_file(file_path)
    cv_text = ingest_file(cv_path)
    structured = structure_document(text)
    cv_structured = structure_document(cv_text)
    embeddings = embed_structured_document(structured)
    cv_embeddings = embed_structured_document(cv_structured)
    # embeddings.update({f"cv_{k}": v for k, v in cv_embeddings.items()})

    print("\n___________________________")
    print("Embeddings generated:")
    print("---------------------------")
    for key, value in embeddings.items():
        print(key, None if value is None else value.shape)





from matching import match_documents

# test simple CV = offre (pour validation)
scores = match_documents(embeddings, cv_embeddings)

print("\n___________________________")
print("Matching scores:")
print("---------------------------")
for k, v in scores.items():
    print(k, round(v, 3))
