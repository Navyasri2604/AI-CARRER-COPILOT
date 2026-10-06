import re

def question_for(role, category, level):
    prompts = {'Technical': f'Explain a technical project or system design decision relevant to a {role} role.', 'Behavioral': 'Tell me about a time you solved a difficult problem with a team.', 'HR': 'Why are you interested in this role and what makes you a strong fit?', 'Situational': 'How would you approach an ambiguous task with limited context?'}
    return prompts.get(category, prompts['Technical'])

def evaluate_answer(role, question, answer):
    words = re.findall(r'\b\w+\b', answer.lower())
    has_structure = any(marker in answer.lower() for marker in ('situation', 'task', 'action', 'result'))
    has_evidence = bool(re.search(r'\b\d+(?:%|\+|x)?\b', answer))
    score = min(10, max(1, 2 + min(4, len(words) // 20) + int(has_structure) + int(has_evidence)))
    return {'score': score, 'strengths': ['Clear intent'] + (['Concrete evidence'] if has_evidence else []), 'weaknesses': ([] if has_structure else ['Use a Situation, Task, Action, Result structure']) + ([] if has_evidence else ['Add measurable outcomes']), 'suggestions': ['Connect your action to the result and keep the answer focused.'], 'ideal_answer': 'A strong answer gives context, explains the action taken, and closes with a measurable result.'}
