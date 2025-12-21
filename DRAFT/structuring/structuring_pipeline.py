from typing import Dict

from structuring.section_extractor import extract_sections
from structuring.skill_extractor import extract_skills


def structure_document(text: str) -> Dict:
    """
    Structure a CV or job description into semantic components.
    """
    sections = extract_sections(text)

    # 1. Try extracting skills from the SKILLS section
    skills = extract_skills(sections.get("skills", ""))

    # 2. Fallback: extract skills from EXPERIENCE if needed
    if not skills:
        skills = extract_skills(sections.get("experience", ""))

    return {
        "skills": skills,
        "experience": sections.get("experience", "").strip(),
        "education": sections.get("education", "").strip(),
        "raw_text": text
    }
