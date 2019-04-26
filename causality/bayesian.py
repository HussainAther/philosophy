import pystan
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
We can use a Bayesian approach to induce causal relationship. We look for a causal
graph that maximizes the posterior probability

p(c|D) = p(C)p(D|C) / Σp(C')p(D|C')

where D is a database of observed past case data. We solve for the integral

p(D|C) = integral of p(D|C,S_C)p(S_C)dS_C

with probability specifications S_C that accompany C in a Bayesian net.	
"""

sns.set() # aesthetic
np.random.seed(101)

 # Define the model using a string
model = """
data {
    int<lower=0> N;
    vector[N] x;
    vector[N] y;
}
parameters {
    real alpha;
    real beta;
    real<lower=0> sigma;
}
model {
    y ~ normal(alpha + beta * x, sigma);
}
"""
