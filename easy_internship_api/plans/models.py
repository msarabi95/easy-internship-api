from django.db import models


class Requirement(models.Model):
    pass


class Blueprint(models.Model):
    pass


# ? TODO: Use state (e.g. django-fsm ?) to keep track of changes in following models

# ? TODO: more generic name (Placement)
class Rotation(models.Model):
    # TODO
    # ? state = FSMField
    # ? pending_update = JSONField
    pass


# ? TODO: more generic name (Pause, Break, Stop, Suspension)
class Freeze(models.Model):
    # TODO
    # ? state = FSMField
    # ? pending_update = JSONField
    pass


class Leave(models.Model):
    # TODO
    # ? state = FSMField
    # ? pending_update = JSONField
    pass
