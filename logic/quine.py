"""
A Quine is a self-referential program that can, without any external access, 
output its own source.

It is named after the philosopher and logician Willard Van Orman Quine
who studied self-reference and quoting in natural language, as for example 
in the paradox "'Yields falsehood when preceded by its quotation' yields 
falsehood when preceded by its quotation."

"Source" has one of two meanings. It can refer to the text-based program source. 
For languages in which program source is represented as a data structure, "source" 
may refer to the data structure: quines in these languages fall into two categories: 
programs which print a textual representation of themselves, or expressions which 
evaluate to a data structure which is equivalent to that expression.

The usual way to code a Quine works similarly to this paradox: The program consists 
of two identical parts, once as plain code and once quoted in some way (for example, 
as a character string, or a literal data structure). The plain code then accesses the 
quoted code and prints it out twice, once unquoted and once with the proper quotation 
marks added. Often, the plain code and the quoted code have to be nested.
"""
