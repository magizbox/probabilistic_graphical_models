# Bayesian Network

A Bayesian network is a graphical model that encodes probabilistic relationships among variables of interest. When used in conjunction with statistical techniques, the graphical model has several advantages for data analysis. One, because the model encodes dependencies among all variables, it readily handles situations where some data entries are missing. Two, a Bayesian network can be used to learn causal relationships, and hence can be used to gain understanding about a problem domain and to predict the consequences of intervention. Three, because the model has both a causal and probabilistic semantics, it is an ideal representation for combining prior knowledge (which often comes in causal form) and data. Four, Bayesian statistical methods in conjunction with bayesian networks offer an efficient and principled approach for avoiding the overfitting of data. In this paper, we discuss methods for constructing Bayesian networks from prior knowledge and summarize Bayesian statistical methods for using data to improve these models. With regard to the latter task, we describe methods for learning both the parameters and structure of a Bayesian network, including techniques for learning with incomplete data. In addition, we relate Bayesian-network methods for learning to techniques for supervised and unsupervised learning. We illustrate the graphical-modeling approach using a real-world case study.


# A Non-Causal Bayesian Network Example

Figure 1 shows a simple Bayesian network, which consists of only two nodes and one link. It represents the JPD of the variables Eye Color and Hair Color in a population of students (Snee, 1974). In this case, the conditional probabilities of Hair Color given the values of its parent node, Eye Color, are provided in a CPT. It is important to point out that this Bayesian network does not contain any causal assumptions, i.e. we have no knowledge of the causal order between the variables. Thus, the interpretation of this network should be merely statistical (informational).

![](http://www.bayesia.com/hs-fs/hubfs/Bayesian_Networks/Fig_2_1.png?t=1501100948045&width=400&height=360&name=Fig_2_1.png)

# A Causal Network Example

Figure 2 illustrates another simple yet typical Bayesian network. In contrast to the statistical relationships in Figure 1, the diagram in Figure 2 describes the causal relationships among the seasons of the year (\(X_1\)), whether it is raining (\(X_2\)), whether the sprinkler is on (\(X_3\)), whether the pavement is wet (\(X_4\)), and whether the pavement is slippery (\(X_5\)). Here, the absence of a direct link between \(X_1\) and \(X_5\), for example, captures our understanding that there is no direct influence of season on slipperiness. The influence is mediated by the wetness of the pavement (if freezing were a possibility, a direct link could be added). 

![](http://www.bayesia.com/hs-fs/hubfs/Bayesian_Networks/Fig_2_2_Sprinkler.png?t=1501100948045&width=300&height=417&name=Fig_2_2_Sprinkler.png)

# A Dynamic Bayesian Network Example

Entities that live in a changing environment must keep track of variables whose values change over time. Dynamic Bayesian networks capture this process by representing multiple copies of the state variables, one for each time step. A set of variables \(X_{t-1}\) and \(X_t\) denotes the world state at times t-1 and t respectively. A set of evidence variables Et denotes the observations available at time t. The sensor model \(P(E_t|X_t)\) is encoded in the conditional probability distributions for the observable variables, given the state variables. The transition model \(P(X_t|X_{t-1})\) relates the state at time t-1 to the state at time t. Keeping track of the world means computing the current probability distribution over world states given all past observations, i.e. \(P(X_t|E_1,…,E_t)\).

Dynamic Bayesian networks (DBN) are a generalization of Hidden Markov Models (HMM) and Kalman Filters (KF). Every HMM and KF can be represented with a DBN. Furthermore, the DBN representation of an HMM is much more compact and, thus, much better understandable. The nodes in the HMM represent the states of the system, whereas the nodes in the DBN represent the dimensions of the system. For example, the HMM representation of the valve system in Figure 2.3 is made of 26 nodes and 36 arcs, versus 9 nodes and 11 arcs in the DBN (Weber and Jouffe, 2003).

![](http://www.bayesia.com/hubfs/Bayesian_Networks/Fig_2_3_Valve.svg?t=1501100948045)
