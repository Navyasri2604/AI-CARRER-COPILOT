import re
import zipfile
from xml.etree import ElementTree
import fitz

SKILL_KEYWORDS = ['Python', 'JavaScript', 'Java', 'SQL', 'TensorFlow', 'PyTorch', 'Pandas', 'Scikit-learn', 'Docker', 'Kubernetes', 'Git', 'REST APIs', 'Machine Learning', 'Deep Learning', 'NLP', 'Statistics', 'Excel', 'Tableau', 'Power BI', 'Selenium', 'ServiceNow', 'Jira', 'AWS', 'Azure', 'React', 'Django', 'FastAPI']

def _read_text(uploaded_file):
    content = uploaded_file.read()
    if uploaded_file.name.lower().endswith('.docx'):
        with zipfile.ZipFile(__import__('io').BytesIO(content)) as archive:
            xml = archive.read('word/document.xml')
        root = ElementTree.fromstring(xml)
        return '\n'.join(node.text or '' for node in root.iter() if node.tag.endswith('}t'))
    document = fitz.open(stream=content, filetype='pdf')
    return '\n'.join(page.get_text() for page in document)

def extract_resume_data(uploaded_file):
    text = _read_text(uploaded_file)
    normalized = text.lower()
    skills = [skill for skill in SKILL_KEYWORDS if skill.lower() in normalized]
    sections = {}
    for name in ['education', 'projects', 'certifications', 'experience', 'achievements', 'languages']:
        match = re.search(rf'{name}\\s*[:\\n](.*?)(?=\\n[A-Z][A-Za-z ]{{2,30}}\\s*[:\\n]|$)', text, re.I | re.S)
        sections[name] = [line.strip(' -•') for line in match.group(1).splitlines() if line.strip()] if match else []
    tools = [skill for skill in skills if skill in ['Docker', 'Kubernetes', 'Git', 'AWS', 'Azure', 'Jira', 'Tableau', 'Power BI', 'Excel']]
    soft_skills = [item for item in ['Communication', 'Leadership', 'Problem Solving', 'Teamwork', 'Collaboration', 'Adaptability'] if item.lower() in normalized]
    section_weights = {'ats_compatibility': 15 if text else 0, 'skills': min(20, len(skills) * 2), 'experience': 15 if sections['experience'] else 0, 'projects': 15 if sections['projects'] else 0, 'education': 10 if sections['education'] else 0, 'formatting': 10 if len(text) > 300 else 4, 'achievements': 10 if sections['achievements'] else 0, 'keywords': min(5, len(skills))}
    score = min(100, sum(section_weights.values()))
    strengths = ['Clear skills signal'] if skills else []
    strengths += ['Projects included'] if sections['projects'] else []
    weaknesses = ['Add measurable achievements'] if not sections['achievements'] else []
    weaknesses += ['Add an experience section'] if not sections['experience'] else []
    return {'raw_text': text, 'skills': skills, 'education': sections['education'], 'projects': sections['projects'], 'certifications': sections['certifications'], 'experience': sections['experience'], 'achievements': sections['achievements'], 'languages': sections['languages'], 'tools': tools, 'soft_skills': soft_skills, 'score': score, 'score_breakdown': section_weights, 'strengths': strengths, 'weaknesses': weaknesses, 'recommendations': ['Quantify impact with numbers and outcomes.', 'Tailor keywords to the target job description.']}
