Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

Course ILIAS: [web page link](https://ilias.uni-freiburg.de/ilias.php?ref_id=2339316&cmdClass=ilobjcoursegui&cmd=view&cmdNode=zf:ns&baseClass=ilRepositoryGUI)

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 5: Sequence Alignment
---

### _Exercise 1 -  Smith-Waterman_

Consider the following sequences S<sub>1</sub> and S<sub>2</sub>, as similarity scoring via s(x,y), the linear gap cost g(k) = -k.

<p align="center">
<img src="./figures/exercise1_scoring.svg" alt="scoring" width=70%/>
 </p>

**a)** Compute the local alignment matrix S<sub>ij</sub> for the given sequence.

| S<sub>ij</sub>|   | T  | A  | C  | G  | C  | A  | G  | A   |
|---------------|---|----|----|----|----|----|----|----|-----|
|               | 0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |   0 |
| **T**         | 0 |    |    |    |    |    |    |    |     |
| **C**         | 0 |    |    |    |    |    |    |    |     |
| **C**         | 0 |    |    |    |    |    |    |    |     |
| **G**         | 0 |    |    |    |    |    |    |    |     |
| **A**         | 0 |    |    |    |    |    |    |    |     |
 
**b)** Give all optimal local alignments and the according score.

### _Exercise 2 -  Smith-Waterman algorithm with arbitrary gap costs_


### _Exercise 3 -  Normalized local alignment_


### _Exercise 4 - Programming assignment: Implementation of Smith-Waterman algorithm_
**a)** Implement the function sw_init() which takes two sequences S1 and S2 and creates the Smith-Waterman matrix and initiates all the matrix values with zeroes. Hereby S1 should be represented by the rows and S2 by the columns.

**b)** Implement the function sw_forward() which takes the two sequences S1 and S2 and the scoring function and output the complete matrix filled with the Smith-Waterman approach.

The following steps will help you with implementing the traceback.

**c)** Implement the function previous_cells() which takes two sequences S1 and S2, scoring function, the filled in recursion matrix from the step *b)* and the cell coordinates as a tuple (row, column).
The function should output a list of tuples of all possible previous cells. The tuples should be again structured like (row, column).

**d)** Implement the function which builds all possible traceback paths. This function should return a list of possible paths which themselves are a list of tuples (row, column). The ordering must be decreasing. Meaning paths should start in the lower right corner of the matrix.

**e)** Implement the function build_alignment() which takes two sequences and a path as a list of tuples. This function should return a local alignment tuple. Meaning two substrings with introduced gaps. 

---
