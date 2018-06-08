from django.test import TestCase
from model_mommy import mommy

class ModelTests(TestCase):
    def test_location_str(self):
        location = mommy.make(
            'centers.Location',
            center=mommy.make('centers.Center'),
            specialty=mommy.make('centers.Specialty'),
            description=""
            )
        
        self.assertEqual(
            str(location),
            "{} @ {}".format(location.specialty.name, location.center.name),
            )

        location = mommy.make(
            'centers.Location',
            center=mommy.make('centers.Center'),
            specialty=mommy.make('centers.Specialty'),
            )

        self.assertEqual(
            str(location),
            "{} @ {} ({})".format(
                location.specialty.name,
                location.center.name,
                location.description,
                ),
            )