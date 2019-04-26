# The epistemology of causality

There are two epistemic approaches to causal theory. Under a hypothetico-deductive account, one hypothesizes 
causal relationships, deduces predictions from the hypothesis, and then tests the hypothesis by seeing how 
well the predictions accord with what actually happens. Under an inductive account, one makes a large number 
of observations and induces causal relationships directly from this mass of data.

## Hypothetico-Deductive discovery

Under this account, one first hypothesizes causal relationships and then tests this hypothesis by seeing whether 
predictions drawn from it are borne out. The testing phase may be influenced by views on the nature of causality: 
a causal hypothesis can be supported or refuted according to whether physical processes are found that underlie 
the hypothesised causal relationships, whether probabilistic consequences of the hypothesis are verified, and 
whether experiments show that by manipulating the hypothesised causes one can achieve their effects.

Karl Popper was an exponent of the hypothetico-deductive approach. For Popper a causal explanation of an event 
consists of natural laws (which are universal statements) together with initial conditions (which are single-
case statements) from which one can predict by deduction the event to be explained. The initial conditions are 
called the 'case' of the event to be explained, which is in turn called the effect. Causal laws, then, are just 
universal laws, and are to be discovered via Popper's general scheme for scientific discovery: (i) hypothesise the laws; 
(ii) deduce their consequences, rejecting the laws and returning to step (i) if these consequences are falsified 
by evidence. Popper thus combines what is known as the covering-law account of causal explanation with a hypothetico
-deductive account of learning causal relationships.

## Inductive learning

Francis Bacon developed a rather different account of scientific learning. First one makes a large amount of careful 
observations of the phenomenon to be explained, by performing experiments if need be. One compiles a table of positive 
instances (cases in which the phenomenon occurs), a table of negative instances (cases in which the phenomenon does not 
occur), and a table of partial instances (cases in which the phenomenon occurs to a certain degree).

The mainstream of inductivist artificial intelligence (AI) approaches have the following feature in common. In order 
that causal relationships can be gleaned from statistical relationships, the approaches assume the Causal Markov 
Condition holds of physical causality and physical probability.205 Of course a causal net contains the Causal Markov 
Condition as an inbuilt assumption. In the case of structural equation models the Causal Markov Condition is a 
consequence of the representation of each variable as a function just of its direct causes and an error variable, 
given the further assumption that all error variables are probabilistically independent.

The inductive procedure then consists in finding the class of causal models or under some approaches a single 'best' 
causal model whose probabilistic independencies implied via the Causal Markov Condition are consistent with independencies 
inferred from the data. Other assumptions are often also made, such as minimality (no submodel of the causal model also 
satisfies the Causal Markov Condition), faithfulness (all independencies in the data are implied via the Causal Markov 
Condition), linearity (all variables are linear functions of their direct causes and uncorrelated error variables), 
causal sufficiency (all common causes of measured variables are measured), context generality (every individual 
possesses the causal relations of the population), no side effects (one can intervene to fix the value of a 
variable without changing the value of any non-effects of the variable), and determinism. However, these extra 
assumptions are less central than the Causal Markov Condition: approaches differ as to which of these extra 
assumptions they adopt and the assumptions tend to be used just to facilitate the inductive procedure based on 
the Causal Markov Condition, either by helping to provide some justification of the inductive procedure or by 
increasing the purported efficiency or efficacy of algorithms for causal induction.
