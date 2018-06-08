from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Location(models.Model):
    center = models.ForeignKey(
        'centers.Center',
        on_delete=models.SET_NULL,
        )
    specialty = models.ForeignKey(
        'centers.Specialty',
        on_delete=models.SET_NULL,
    )

    description = models.CharField(
        help_text="an optional description in case of, for example, multiple locations"
        "under a specialty within the same center"
    )

    def __str__(self):
        return "{} @ {}".format(
            self.specialty.name,
            self.center.name,
        ) + " {}".format(self.description) if self.description else ""
