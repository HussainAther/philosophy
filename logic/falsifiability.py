
"""
We say that a theory is falsified only if we have accepted basic statements which contradict
it (cf. section 11, rule 2). This condition is necessary, but not sufficient; for we have seen
that non-reproducible single occurrences are of no significance to science.

Thus a few stray basic statements contradicting a theory will hardly induce us to reject it as falsified.
We shall take it as falsified only if we discover a reproducible effect which refutes the theory. In other words,
we only accept the falsification if a low-level empirical hypothesis which describes such an effect is
proposed and corroborated. This kind of hypothesis may be called a falsifying hypothesis.

The requirement that the falsifying hypothesis must be empirical, and so falsifiable, only means that it must
stand in a certain logical relationship to possible basic statements; thus this requirement only concerns the
logical form of the hypothesis. The rider that the hypothesis should be corroborated refers to tests which it
ought to have passed—tests which confront it with accepted basic statements.

The following is an example of inconsistent (logically false) statement - that is - one in which
p · ~p can be deduced. This is not an example of a falsifiable statement.

1. p -> (p v q) # From Bertrand Russell's "primitive propositions"
2. ~p -> (p -> q) # From substitiuting   ̄pp for p and then p -> q for ~p v q
3. ~p · p -> q # By importation

Consider a class α of a finite number of occurrences, for example the class of throws made yesterday with this
particular die. This class α, which is assumed to be non-empty, serves, as it were, as a frame of reference, and
will be called a (finite) reference-class. The number of elements belonging to α, i.e. its cardinal number, is
denoted by ‘N(α)’, to be read ‘the number of α’. Now let there be another class, β, which may be finite or not.

We call β our property-class: it may be, for example, the class of all throws which show a five, or (as we shall say)
which have the property five.

The class of those elements which belong to both α and β, for example the class of throws made yesterday with this
particular die and having the property five, is called the product-class of α and β, and is denoted by ‘α.β’, to be
read ‘α and β’. Since α.β is a subclass of α, it can at most contain a finite number of elements (it may be empty).

The number of elements in α.β is denoted by ‘N(α.β)’.

Whilst we symbolize (finite) numbers of elements by N, the relative frequencies are symbolized by F′′. For example,
‘the relative frequency of the property β within the finite reference-class α’ is written ‘αF′′(β)’, which may be read
‘the α-frequency of β’. We can now define the relative frequency.
"""

def relfreq(n, alpha, beta):
    """
    Relative frequency: For some function n that returns the number of fives thrown yesterday with this die when
    given alpha and beta, and, when given only alpha, it returns the total number of throws yesterday.
    """
    return n(alpha, beta) / n(alpha)

