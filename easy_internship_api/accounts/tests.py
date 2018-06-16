from model_mommy import mommy
from django.test import TestCase


class TraineeCategoryTests(TestCase):
    def test_profile_schema_created_with_new_trainee_category(self):
        category = mommy.make('accounts.TraineeCategory')
        self.assertIsNotNone(category.profile_schema)

    def test_get_profile_schema(self):
        pass

    def test_set_profile_schema(self):
        pass


class ModelTests(TestCase):
    def test_training_periods_mutually_exclusive(self):
        pass
    
    def test_training_period_end_date(self):
        pass

    def test_training_period_description(self):
        pass
