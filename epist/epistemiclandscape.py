import numpy as np

"""
In researching how scientists form conclusions and how fast various groups
of researchers can discover significan results, philosophers Weisberg and Muldoon
created 3D "epistemic landscapes" in which the x and y axes of a graph represent
research programs with the vertical z axis the scientific importance of the results
attainable by the research program. They created algorithms for three processes:
(1) scientists follow the control research strategy and ignore what other scientists
are doing, (2) scientists follow methods of research their predecessors used, and (3)
scientists take into account results of others such that, if a method has already been
explored, they adopt a different one.

The epistemic landscape is generally modeled after geneticist Sewall Wright's insight
into population biology that we can represent fitness values of genotypes in terms of 
an abstract landscape in which a particular genotypes corresponds to a point in a highly
multidimensional landscape. The fitness value of the genotype is its height and nearby
points are accessible via mutation.

Weisberg and Muldoon began with a 101 x 101 landscape with two peaks.
"""

l = np.zeros((101, 101)) # lattice used in the landscape

"""
We define epistemic success as the time required to visit the two peaks, and epistemic
progress as the percent of the significant reginos explored after a given time.
"""
