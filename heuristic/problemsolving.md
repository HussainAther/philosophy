# Problem solving strategies

When applying algorithms in metaheuristics, computational sciences, and even life sciences, 
we discuss how suitable an application of a given technique can be to a problem and how
the algorithm and problem features can transform. We want to make a distinction between
strong and weak methods to use more or less specific information respectively. This way
we can create a problem solving strategy summary to suggest ways to apply a given technique
to the function optimization and approximation.

## Suitability of Application

We generally regard tools and techniques with respect to their efficiency or effectiveness
in solving problems. In the philosophy of mathematics and discussions on machine learning,
the "no free lunch theorem" (that averaging over all optimization problems means all non-resampling 
optimization algorithms perform equally well) can tell us generally that there are bound claims of applicability
of a given strategy with respect to its feature overlap with the attributes of a given problem
domain. We can describe the appropriateness (can the approach address the problem), feasability
(availability of resoucres and related efficiency concerns), and flexibility (addressing unexpected
or unintended effects). We can address issues of suitability using (1) the systemic elicitation of 
system and problem features and (2) consideration of overlap of problem-problem, algorithm-algorithm,
and problem-algorithm overlap of features sets.

### Systematic Feature Elicitation

We can define a feature of a system as a distinctive element or property we use to differentiate
it from similar or related cases. We may create features either from a system perpsective (with a 
focus on the lower levle functional elements and investigations toward correlating specific
controlled procedures with predictable emergent behaviors) or problem perspective (generalizing
a specific case to the general problem case with a functional or logical decomposition
into its constituent parts). Generalization adn functional decomposition are important. Simplification
and modularity can let us reduce the cost and complexicty of finding solutions.

### Feature Overlap

Overlap of features between combinations of systems and problems can be categorized into
system overlap (suitability of one system to another, or comparability), problem overlap (suitability of 
one problem to another, or transferability), and system-problem overlap (suitability of a system on
a given problem, or applicability).

## Strong and Weak methods

The stronger the method, the more we need to know about the problem domain. On a sort of continuum
of methods from the weakest (e.g., black box techniques with a few assumptions about the problem domain)
to strongest (e..g, need all of the problem-specific information available). The Traveling Salesman problem
uses combinatorial optimization that can vary from exploiting only permutations of cities to stronger methods
that use nearest neighbor approaches that exploit variation among the domain. Stochastic techniques
may explore the search space using probabilistic and heuristic information.

We may either start with the strongest technique available and apply it until we weaken our techniques for 
what we're looking for or start weak and increasingly strengthen our methods.

## Domain-specific strategies

### Function Optimization

We can optimize functions globally or locally. Global seeks optimal structures or approximations over the entire
problem domain scope while local focuses on optimal structures within constrained regions of the decisino variable
search space (such as a single peak or valley within a defined area). Drawing from evolutionary computation, swarm intelligence,
and similar sub-fields of computational intelligence, we may also optimize routines and methods using parallelization
that can exploit similarities between parallel hardware to optimize communication to computation ratios (known as granularity).

We may also use cooperative search of multiple models working together to solve a difficult optimization problem or a hybrid
search which optimizes by focusing on multiple and likely different approaches sequentially or in parallel. Functional decomposition
uses (1) multiple objectives, (2) multiple constraints, and (3) partitions of the decision variable search space. Optimization varies
with temporal and spatial distribution of information and computation variability. We can exploit clusters of heterogeneous
workstations to complete large-scale distributed tasks such as optimization.

Meta-optimization seesk to approach the next level by iterativelly generating inductive models (multiple restart optimization) and
optimizing parameters of a process to generate an inductive model of an optimization problem. Optimizing a search process could
include self-adaptation of mutation parameters (setp sizes) in the evolutionary strategies and evolutionary programming approaches.

## Function approximation

With function approximation problems, we can use vector quantization to approximate a target function using a set of 
exemplar (prototype or codebook) vectors. They should represent a discrete subset of the problem using the features
of interest naturally represented in the prolbem space. This method uses a non-parametric model of a target function
using symbolic representation in the domain (such as tree-based approaches). A k-Nearest-Neighbor method can be a non-parametric
method for this. We may also paralellize instance-based methods with discrete, independent nature of which they're used. 
