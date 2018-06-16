from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.db import models

from accounts.documents import ProfileFormat


class TraineeCategory(models.Model):
    name = models.CharField(max_length=50)

    # profile fields
    profile_format_id = models.CharField(max_length=50)

    def get_profile_format(self):
        """
        Return a `ProfileFormat` instance describing profile fields
        required for trainees belonging to this trainee category.
        """
        pass

    def set_profile_format(self):
        pass

    profile_format = property(
        get_profile_format,
        set_profile_format,
        doc="Profile format of trainees belonging to this category."
    )

    def save(self, *args, **kwargs):
        if self.id is None:
            profile_format = ProfileFormat()
            self.profile_format_id = profile_format.id
        super().save(*args, **kwargs)


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
        return self.description  # pragma: no cover

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

    @classmethod
    def from_db(cls, *args, **kwargs):
        instance = super().from_db(*args, **kwargs)

        # TODO: fetch remaining fields from MongoDB based
        #       on schema specified for trainee category

        # For now, MongoDB fields will be stored as basic attributes;
        # this means features like automatic refreshing will not be possible.
        # Optimally, they should be retrieved from a cache or directly from
        # the database using a __getattr__ call.

        return instance

    def refresh_from_db(self, *args, **kwargs):
        super().refresh_from_db(*args, **kwargs)

        # TODO: refresh MongoDB fields

    def clean(self):
        pass

        # TODO: validate MongoDB fields againts schema specified fro trainee category

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)

        # TODO: save/update MongoDB fields

    def __str__(self):
        pass
