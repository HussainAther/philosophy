import pystan
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
We can use a Bayesian approach to induce causal relationship. We look for a causal
graph that maximizes the posterior probability

p(c|D) = p(C)p(D|C) / Σp(C")p(D|C")

where D is a database of observed past case data. We solve for the integral

p(D|C) = integral of p(D|C,S_C)p(S_C)dS_C

with probability specifications S_C that accompany C in a Bayesian net.	
"""

sns.set() # aesthetic
np.random.seed(100)

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

"""
We've specified the lower bound for sigma as 0, as it's impossible for the 
magnitude of Gaussian noise to be negative. This is an example of a prior 
on the parameter sigma, and more detailed priors can be added in the model block. 
We don't add any priors to our alpha and beta parameters.
"""

# Parameters we infer
alpha = 4.0
beta = 0.5
sigma = 1.0

# Generate data we will study as the "truth"
x = 10 * np.random.rand(100)
y = alpha + beta * x
y = np.random.normal(y, scale=sigma)

# Put our data in a dictionary
data = {"N": len(x), "x": x, "y": y}

# Compile the model using pystan
sm = pystan.StanModel(model_code=model)

# Train the model and generate samples
# Fit our data to the sampling of the pystan model
# data is our data, iter is the number of samples generated
# from each Markov chain, chains are the number of samples
# we use to form the posterior distribution, warmup (burn-in)
# is the amount of samples discarded from the beginning of 
# each chain, thin is the interval in sampling at whcih samples
# are retained, and seed is the reproducible seed number.
fit = sm.sampling(data=data, iter=1000, chains=4, warmup=500, thin=1, seed=100)

# Get a summary of the model fitted
summary_dict = fit.summary()

# Extract a dataframe of the summary
df = pd.DataFrame(summary_dict["summary"], 
                  columns=summary_dict["summary_colnames"], 
                  index=summary_dict["summary_rownames"])

# Extract the fit values of alpha and beta
alpha_mean, beta_mean = df["mean"]["alpha"], df["mean"]["beta"]

# Extracting traces from the fit values
alpha = fit["alpha"]
beta = fit["beta"]
sigma = fit["sigma"]
lp = fit["lp__"]

def plot_trace(param, param_name="parameter"):
    """
    Plot the trace and posterior of a parameter.
    """
    
    # Summary statistics
    mean = np.mean(param)
    median = np.median(param)
    cred_min, cred_max = np.percentile(param, 2.5), np.percentile(param, 97.5)
    
    # Plotting
    plt.subplot(2,1,1)
    plt.plot(param)
    plt.xlabel("samples")
    plt.ylabel(param_name)
    plt.axhline(mean, color="r", lw=2, linestyle="--")
    plt.axhline(median, color="c", lw=2, linestyle="--")
    plt.axhline(cred_min, linestyle=":", color="k", alpha=0.2)
    plt.axhline(cred_max, linestyle=":", color="k", alpha=0.2)
    plt.title("Trace and Posterior Distribution for {}".format(param_name))
  
    plt.subplot(2,1,2)
    plt.hist(param, 30, density=True); sns.kdeplot(param, shade=True)
    plt.xlabel(param_name)
    plt.ylabel("density")
    plt.axvline(mean, color="r", lw=2, linestyle="--",label="mean")
    plt.axvline(median, color="c", lw=2, linestyle="--",label="median")
    plt.axvline(cred_min, linestyle=":", color="k", alpha=0.2, label="95% CI")
    plt.axvline(cred_max, linestyle=":", color="k", alpha=0.2)
    
    plt.gcf().tight_layout()
    plt.legend()

"""
If we assume Causal Markov Condition, causal graph C and specifications
S_C (parameters) create a Bayesian net from which we can calculate p(D|C, S_C).
We assume the probability specifiers themselves are probabilistically independent 
and that their prior distribution takes the form of a Dirichlet distribution. 
"""
