from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.db import models


class TraineeCategory(models.Model):
    pass


class TrainingPeriod(models.Model):
    """
    A training period is used to define trainee batches.
    """
    start_date = models.DateField()
    duration_value = models.PositiveIntegerField(default=1)
    duration_units = models.CharField(
        max_length=6,
        choices=[
            ('months', 'months'),
            ('years', 'years'),
        ],
        default='years',
    )

    def __str__(self):
        return self.description

    def clean(self):
        """
        Training periods are mutually exclusive: make sure
        period does not overlap with any other saved one.
        """
        pass  # TODO

    @property
    def end_date(self):
        return self.start_date + relativedelta(**{self.duration_units: self.duration_value}) - relativedelta(days=1)

    @property
    def description(self):
        end_date = self.end_date
        strftime_format = "%Y-%m"  # By default mention the year and month
        
        # If the start and end dates have the same year and month, report day in addition
        if (self.start_date.year, self.start_date.month) == (end_date.year, end_date.month):
            strftime_format = "%Y-%m-%d" 

        return "{} to {}".format(self.start_date.strftime(strftime_format), end_date.strftime(strftime_format))


class Institution(models.Model):
    pass


class Batch(models.Model):
    pass


class TraineeProfile(models.Model):
    category = models.ForeignKey(
        'accounts.TraineeCategory',
        null=True, on_delete=models.SET_NULL,
    )
    institution = models.ForeignKey(
        'accounts.Institution',
        null=True, on_delete=models.SET_NULL,
    )
    batch = models.ForeignKey(
        'accounts.Batch',
        null=True, on_delete=models.SET_NULL,
    )
    start_date = models.DateField()  # here vs. in blueprint?

    # TODO: Set up EAV for all other fields

    def __str__(self):
        pass
