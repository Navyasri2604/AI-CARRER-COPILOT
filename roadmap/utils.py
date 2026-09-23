from .models import Roadmap, RoadmapTask

def fallback_roadmap(role, missing):
    focus = missing or ['Core foundations', 'Practical projects', 'Interview readiness']
    return {'30': {'title': 'Build the foundation', 'weeks': [{'topic': skill, 'task': f'Complete a focused {skill} learning sprint and document your notes.'} for skill in focus[:3]]}, '60': {'title': 'Ship proof of work', 'weeks': [{'topic': 'Applied project', 'task': f'Build and publish a portfolio project using {skill}.'} for skill in focus[:3]]}, '90': {'title': 'Become interview-ready', 'weeks': [{'topic': 'Career signal', 'task': 'Refine your portfolio, practice role-specific interviews, and apply with confidence.'}]}}

def generate_roadmap(role, missing, user=None):
    result = fallback_roadmap(role, missing)
    if user:
        roadmap = Roadmap.objects.create(user=user, role=role, missing_skills=missing, content=result)
        for phase in result.values():
            for week in phase.get('weeks', []):
                RoadmapTask.objects.create(roadmap=roadmap, title=week.get('topic', 'Career task'), description=week.get('task', ''), estimated_time='3-5 hours')
    return result
