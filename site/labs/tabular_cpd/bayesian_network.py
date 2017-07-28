import pandas as pd
import numpy as np
import re
import itertools

class BayesianNetwork:
    def __init__(self):
        # conditional probability distribution variable
        self.cpd = dict()
        # join distribution variable
        self.jd = dict()
        # variables
        self.variables = []
        self.edges = []

    def add_cpd(self, key, df):
        variables = sorted(re.split("[\|,]", key))
        self.variables = sorted(list(set(self.variables + variables)))
        df = df.set_index(variables)
        if "|" in key:
            nodes = key.split("|")[0].split(",")
            parents = key.split("|")[1].split(",")
            self.cpd[key] = df
            for parent in parents:
                for node in nodes:
                    if (node, parent) not in self.edges:
                        self.edges.append((node, parent))
        else:
            key = ",".join(variables)
            self.jd[key] = df

    def _mult(self, *cpds):
        values = list(itertools.product(["true", "false"], ["true", "false"], ["true", "false"]))
        keys = pd.DataFrame(values, columns=["rain", "cloudy", "sprinkler"])
        df = cpds[0]
        key = keys.loc[:, ["cloudy", "rain"]]
        return 0

    def compile(self):
        for node, parent in self.edges:
            self._apply_chain_rule(node, on=parent)

        # apply chain rule
        all_variables = ",".join(self.variables)
        if all_variables in self.jd:
            return
        nodes = list(set(self.variables) - set([edge[0] for edge in self.edges]))
        self.jd[all_variables] = self._mult(self.cpd["rain|cloudy"], self.cpd["sprinkler|cloudy"], self.jd["cloudy"])

    def joint(self, key):
        key = ",".join(sorted(key.split(",")))
        return self.jd[key]

    def _apply_chain_rule(self, variables, on):
        key = ",".join(sorted(variables.split(",") + on.split(",")))
        conditional_variable = "%s|%s" % (variables, on)
        cpd = self.cpd
        jd = self.jd
        if key in jd:
            return
        cp = cpd[conditional_variable]
        j = jd[on]
        labels = cp.reset_index()[on]
        a = j.loc[labels, "p"].values
        b = cp["p"].values
        jd[key] = cp
        jd[key]["p"] = np.multiply(a, b)
        self.jd = jd

    def _marginal(self, label):
        variables = label.split(",")
        all_variables = ",".join(self.variables)
        df = self.jd[all_variables].reset_index().groupby(variables).sum()
        self.jd[label] = df

    def lookup(self, **query):
        variables = query.keys()
        values = query.values()
        variables = ",".join(sorted(variables))
        if variables not in self.jd:
            self._marginal(variables)
        return self.jd[variables].ix[values]["p"].values[0]

    # TODO
    def belief(self, **query):
        pass
