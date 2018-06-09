from django.db import models
# TODO: from . import settings

# ? TODO: Change to `Area`/`Field`
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    # TODO
    # class Meta:
    #     verbose_name = settings.SPECIALTY_VERBOSE_NAME
    #     verbose_name_plural = settings.SPECIALTY_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name  # pragma: no cover


# ? TODO: Abstract model
# class Location:
#     pass


class Center(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name  # pragma: no cover


# ? TODO: Change to `Division`
class Location(models.Model):
    center = models.ForeignKey(
        'centers.Center',
        null=True, on_delete=models.SET_NULL,
        )
    specialty = models.ForeignKey(
        'centers.Specialty',
        null=True, on_delete=models.SET_NULL,
    )

    description = models.CharField(
        max_length=100,
        help_text="an optional description in case of, for example, multiple locations"
        "under a specialty within the same center"
    )

    def __str__(self):
        return "{} @ {}".format(
            self.specialty.name,
            self.center.name,
        ) + (" ({})".format(self.description) if self.description else "")


# ? TODO: `SubmissionRestriction` as an abstract model
# Seat limits and time limits then become 2 types of restrictions.

class SeatLimit(models.Model):
    # TODO
    # ? affected_dates = DateRangeField
    # offered_seats = PositiveIntegerField
    pass

class SubmissionRestriction(models.Model):
    # TODO
    # target_group [optional] = generic(`TraineeCategory` | `Batch`)
    # ? target_date_range [optional] = DateTimeRangeField
    # target_locations [optional; could be target centers as well]

    # type = open/close
    # effective_date
    
    # ? allow_beyond_seat_limit [? here vs. somewhere else]
    pass
