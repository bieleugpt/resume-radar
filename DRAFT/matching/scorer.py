from typing import Dict
from matching.similarity import cosine_similarity


DEFAULT_WEIGHTS = {
    "skills": 0.4,
    "experience": 0.4,
    "education": 0.2
}


def compute_score(cv_embeddings, job_embeddings, weights=DEFAULT_WEIGHTS):
    scores = {}
    total_score = 0.0

    for section, weight in weights.items():
        sim = cosine_similarity(
            cv_embeddings.get(section),
            job_embeddings.get(section)
        )

        # bonus faible pour education si non nulle
        if section == "education" and sim < 0.1:
            sim = 0.1

        scores[section] = sim
        total_score += weight * sim

    scores["total"] = total_score
    return scores
