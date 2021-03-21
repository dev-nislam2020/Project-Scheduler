from django.db import models

# Create your models here.
APP_TYPE = (
    ('Web', 'Web App Development'),
    ('Desktop', 'Desktop App Development'),
    ('Mobile', 'Mobile App Development'),
    ('Native', 'Native App Development'),
)

DEVELOPMENT_STAGE = (
    ('Init Project', 'Init Project'),
    ('Planning Process', 'Planning Process'),
    ('Design', 'Design'),
    ('Implementation', 'Implementation'),
    ('Testing', 'Testing'),
    ('Deploy', 'Deploy'),
)

class Project(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, unique=True)
    deadline = models.DateField(verbose_name="Deadline")
    app_type = models.CharField(verbose_name="Development", max_length=20, choices=APP_TYPE)
    is_completed = models.BooleanField(default=False)
    is_requirement_completed = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-create_at']
    
    def __str__(self):
        return self.name

class Status(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    stage_development = models.CharField(verbose_name="Development Stage", max_length=20, choices=DEVELOPMENT_STAGE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.stage_development

class Stage(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.create_at)

class Language(models.Model):
    name = models.CharField(verbose_name="Name", max_length=25, unique=True)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(verbose_name="Name", max_length=25, unique=True)

    def __str__(self):
        return self.name

class Logical(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, blank=True)
    framework = models.ManyToManyField(Framework, blank=True)
    db_name = models.CharField(verbose_name="Database Name", max_length=25)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.create_at)

class Interface(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, blank=True)
    framework = models.ManyToManyField(Framework, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.create_at)

class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="DB Model Name", max_length=50, unique=True)
    oparetion = models.CharField(verbose_name="DB Model Oparetion", max_length=25)
    notes = models.TextField(verbose_name="Feature Notes", blank=True, null=True)

