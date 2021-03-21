from django.db.models.signals import post_save
from django.dispatch import receiver

from pro_sch.models import DEVELOPMENT_STAGE, Project, Stage, Status


# Create your signals here.
@receiver(post_save, sender=Project)
def create_project_status(sender, instance, created, **kwargs):
    if created:
        stage = DEVELOPMENT_STAGE[0][0]
        Status.objects.create(project=instance, stage_development=stage)

@receiver(post_save, sender=Status)
def create_status_stage(sender, instance, created, **kwargs):
    if created:
        Stage.objects.create(status=instance)
    else:
        Stage.objects.create(status=instance)

