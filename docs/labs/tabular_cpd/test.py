from unittest import TestCase

from tabular_cpd.script import wet_grass


class TestWet_grass(TestCase):
    def test_wet_grass(self):
        p = wet_grass(sprinkler=True, rain=False)
        self.assertEqual(p[False], 0.1)
        self.assertEqual(p[True], 0.9)

    def test_wet_grass_2(self):
        p = wet_grass(sprinkler=True)
        self.assertEqual(p[False], 0.055)
        self.assertEqual(p[True], 0.945)
