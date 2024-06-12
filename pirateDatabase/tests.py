from datetime import date

from django.test import TestCase

from pirateDatabase.models import Pirate, CauseOfDeath


class PirateTestCase(TestCase):
    def test_age_at_death_calculated_automatically(self):
        pirate = Pirate.objects.create(
            name="Blackbeard",
            born_on=date(1680, 1, 1),
            died_on=date(1718, 11, 22),
            cause_of_death=CauseOfDeath.EXECUTION_BY_BEHEADING,
        )
        self.assertEqual(pirate.age_at_death, 38)
