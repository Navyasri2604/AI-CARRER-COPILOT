"""Local NLP and career-writing utilities with no network dependencies."""
import math
import re
from collections import Counter

STOP_WORDS = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'to', 'with', 'this', 'will', 'you', 'your', 'our', 'we', 'their', 'they', 'using'}


def tokenize(text):
    return [word for word in re.findall(r'[a-zA-Z][a-zA-Z0-9+#.-]{1,}', text.lower()) if word not in STOP_WORDS]


def tfidf_vectors(documents):
    tokenized = [tokenize(document) for document in documents]
    frequency = Counter(token for tokens in tokenized for token in set(tokens))
    vectors = []
    for tokens in tokenized:
        counts = Counter(tokens)
        total = max(1, len(tokens))
        vectors.append({token: (count / total) * math.log((1 + len(documents)) / (1 + frequency[token])) + 1 for token, count in counts.items()})
    return vectors


def cosine_similarity(first, second):
    keys = set(first) | set(second)
    numerator = sum(first.get(key, 0) * second.get(key, 0) for key in keys)
    denominator = math.sqrt(sum(value * value for value in first.values())) * math.sqrt(sum(value * value for value in second.values()))
    return round(numerator / denominator * 100) if denominator else 0


def similarity_score(source, target):
    return cosine_similarity(*tfidf_vectors([source, target]))


def keyword_matches(text, candidates):
    normalized = text.lower()
    return [candidate for candidate in candidates if candidate.lower() in normalized]


def local_asset(asset_type, context):
    lines = [line.strip(' -*') for line in context.splitlines() if line.strip()]
    summary = ' '.join(lines[:4])
    if asset_type == 'cover_letter':
        return f'Dear Hiring Manager,\n\nI am excited to apply for this opportunity. My background includes {summary}. I would bring a practical, learning-oriented approach and a commitment to measurable results.\n\nI would welcome the opportunity to discuss how my experience can support your team.\n\nSincerely,\nYour Name'
    if asset_type == 'email':
        return f'Subject: Interest in the opportunity\n\nHello,\n\nI am reaching out regarding this opportunity. My relevant background includes {summary}. I would value the chance to learn more about the role and share how I could contribute.\n\nBest regards,\nYour Name'
    if asset_type == 'resume_bullets':
        return '\n'.join(f'- Delivered {line[:120]}, improving clarity, reliability, or efficiency through structured implementation.' for line in lines[:3]) or '- Delivered a measurable project outcome using a structured, testable implementation.'
    return f'Headline: Results-focused professional building capability in {summary[:90] or "modern technology and problem solving"}\n\nAbout:\nI am a curious, practical professional who enjoys turning ambiguous problems into clear, useful outcomes. My recent experience includes {summary}.'


def local_chat_reply(message, profile_text='', resume_text=''):
    words = tokenize(message)
    combined = f'{profile_text} {resume_text}'
    if any(word in words for word in ('resume', 'cv', 'ats')):
        return 'Use the Resume Analyzer to measure sections, skills, keywords, and ATS readiness. Then compare it against a specific job description.'
    if any(word in words for word in ('interview', 'question', 'answer')):
        return 'Practice one role-specific question at a time. Structure behavioral answers with Situation, Task, Action, and Result, then quantify the outcome.'
    if any(word in words for word in ('skill', 'learn', 'course')):
        return 'Start with the highest-priority missing skill for your target role, then prove it with a small portfolio project.'
    if any(word in words for word in ('job', 'application', 'career')):
        return 'Use Job Match Analyzer before applying, save the role in the tracker, and schedule a follow-up date.'
    return 'Complete your profile and upload a resume so local analysis can give you more specific guidance.' if not combined.strip() else 'Choose one missing skill, connect it to a project, and use the resulting evidence in your next application.'
