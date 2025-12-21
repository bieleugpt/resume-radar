

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from embedding.embedding_model import EmbeddingModel
from embedding.embedder import Embedder


def embed_structured_document(structured_doc):
    """
    Generate embeddings for a structured CV or job description.
    """
    model = EmbeddingModel()
    embedder = Embedder(model)

    return embedder.embed_document(structured_doc)


