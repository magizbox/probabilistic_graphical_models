from unittest import TestCase
import numpy as np
from tabular_cpd.bayesian_network import BayesianNetwork
import pandas as pd

bn = BayesianNetwork()
df = pd.DataFrame(
    [["true", "true", 0.8],
     ["true", "false", 0.2],
     ["false", "true", 0.2],
     ["false", "false", 0.8]],
    columns=["rain", "cloudy", "p"]
)
bn.add_cpd("rain|cloudy", df)

df = pd.DataFrame(
    [["true", 0.6],
     ["false", 0.4]],
    columns=["cloudy", "p"]
)
bn.add_cpd("cloudy", df)

bn.compile()


class Test_BayesianNetwork(TestCase):
    def test_cpd(self):
        self.assertIsNotNone(bn.cpd["rain|cloudy"])
        self.assertIsNotNone(bn.jd["cloudy"])

    def test_compile(self):
        self.assertIsNotNone(bn.joint("rain,cloudy"))

    def test_lookup(self):
        self.assertEqual(0.4, bn.lookup(cloudy="false"))

    def test_lookup_2(self):
        value = bn.lookup(rain="true", cloudy="false")
        self.assertTrue(np.allclose(0.08, value))

    def test_lookup_3(self):
        self.assertTrue(np.allclose(0.56, bn.lookup(rain="true")))
        self.assertTrue(np.allclose(0.44, bn.lookup(rain="false")))
