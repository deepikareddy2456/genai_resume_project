from parser import extract_text
from indexer import build_embeddings
import numpy as np

def final_score(resume_file, jd_file):
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    resume_embed = build_embeddings([resume_text])
    jd_embed = build_embeddings([jd_text])

    # cosine similarity
    score = np.dot(resume_embed, jd_embed.T)[0][0] * 100
    score = round(score, 2)

    if score > 75:
        verdict = "High"
    elif score > 50:
        verdict = "Medium"
    else:
        verdict = "Low"

    return score, verdict
