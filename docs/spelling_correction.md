# Spelling Correction
For instance, we may wish to retrieve documents containing the term carrot when the user types the query carot. Google reports (http://www.google.com/jobs/britney.html) that the following are all treated as misspellings of the query britney spears: britian spears, britney's spears, brandy spears and prittany spears. We look at two steps to solving this problem: the first based on edit distance and the second based on $k$-gram overlap. Before getting into the algorithmic details of these methods, we first review how search engines provide spell-correction as part of a user experience.
## Corpus

[Birkbeck spelling error corpus](http://ota.ox.ac.uk/headers/0643.xml)

## References

* [How to Write a Spelling Corrector. _Peter Norvig_. 2007](http://norvig.com/spell-correct.html)
* [Statistical Natural Language Processing in Python. _Peter Norvig_. 2007](http://nbviewer.jupyter.org/url/norvig.com/ipython/How%20to%20Do%20Things%20with%20Words.ipynb)