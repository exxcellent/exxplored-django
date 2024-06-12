from django.db import models


class CauseOfDeath(models.TextChoices):
    EXECUTION_BY_HANGING = "Hanging"
    EXECUTION_BY_BEHEADING = "Beheading"
    IN_COMBAT = "Combat"
    DISEASE = "Disease"
    UNKNOWN = "Unknown"


class Pirate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    born_on = models.DateField(verbose_name="Born on")
    died_on = models.DateField(verbose_name="Died on")
    age_at_death = models.PositiveIntegerField(verbose_name="Age at death")
    cause_of_death = models.CharField(
        max_length=100,
        choices=CauseOfDeath.choices,
        default=CauseOfDeath.UNKNOWN,
        verbose_name="Cause of death"
    )
    nationality = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nationality")

    def __str__(self):
        return self.name


class PirateNote(models.Model):
    pirate = models.ForeignKey(Pirate, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField(verbose_name="Content")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")

    def __str__(self):
        return self.content[:20]

