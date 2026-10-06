from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [('roadmap', '0001_initial')]
    operations = [migrations.CreateModel(name='RoadmapTask', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField(max_length=180)), ('description', models.TextField(blank=True)), ('difficulty', models.CharField(default='Intermediate', max_length=30)), ('estimated_time', models.CharField(blank=True, max_length=60)), ('resources', models.JSONField(default=list)), ('completed', models.BooleanField(default=False)), ('roadmap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='roadmap.roadmap'))])]
