# Resolution derivation rule for propositional logic sentences

Given. The external memory (file) contains a set of propositional logic sentences - knowledge base. Sentences are written in the disjunctive form. The number of propositional logic characters, the number of sentences, and the number of disjunctions in sentences can generally vary.

Program that, with the help of resolution rule, derives from the initial knowledge base all the other sentences that can be derived. Newly derived sentences are saved in the files and printed in the terminal.

Input file should look like: A OR -C.
You can have any number of literals (A, C, etc.), they should be separated by OR. If you have a negated literal, you should put "-" at the start.

Output file will index all the sentences and derive new sentences. For each new sentence the program shows the parents' indexes from which this sentence was derived. 

There are already 6 input tests. You can check the program on any other input you wish.


* Please notice that above "-" was used to mean "tilda" due to the unexpected reaction of readme file on real tilde.



