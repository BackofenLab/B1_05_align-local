from typing import List, Tuple, Dict
from math import inf



def exercise_1a():
    """
    Exercise 1 a
    """

    #        T   A   C   G   C   A   G   A
    s_ij = [
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  # T
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  # C
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  # C
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  # G
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  # A
    ]

    return s_ij


def exercise_1b() -> Tuple[List[Tuple[str, str]], int]:
    """
    Exercise 1 b
    Give all optimal local alignments and their score
    """
    score: int = None
    alignments: List[Tuple[str, str]] = [
        ("", "")
    ]
    return alignments, score


def exercise_2a():
    """
    Exercise 2 a

    Which of these statements are correct?
    Set the correct answers to True and the others to False:
    """

    # Distance and similarity scores are equally useful for local alignment scoring
    a = None

    # Similarity scores are not suited for local alignment scoring
    b = None

    # Distance scores are not suited for local alignment scoring
    c = None

    return a, b, c

def exercise_2b():
    """
    Exercise 2 b

    The following recursions were created analogously to the Waterman-Smith-Beyer algorithm.
    Which of these (if any) represents a variant of the Smith-Waterman algorithm that allows for an arbitrary gap scoring function?

    Set the correct answers to True and the others to False:
    """

    i   = None
    ii  = None
    iii = None
    iv  = None
    v   = None

    return i, ii, iii, iv, v

def exercise_2c():
    """
    Exercise 2 c

    The following recursions were created analogously to the Gotoh algorithm.
    Which of these (if any) represents a variant of the Smith-Waterman algorithm that allows for an affine gap scoring function?

    Set the correct answers to True and the others to False:
    """

    i   = None
    ii  = None
    iii = None
    iv  = None

    return i, ii, iii, iv

def exercise_3a():
    """
    Exercise 3 a
    """


########################################################
############## Programming tasks #######################
########################################################


def sw_init(seq1, seq2):
    """
    Exercise 4 a
    Implement the function sw_init() which takes two sequences S1 and S2 and
    creates the Smith-Waterman matrix and initiates all the matrix values
    with zeroes. Hereby S1 should be represented by the rows and S2 by
    the columns.
    """
    return None


def sw_forward(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 b
    Implement the function sw_forward() which takes the two sequences S1 and
    S2 and the scoring function and output the complete matrix filled with
    the Smith-Waterman approach.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )
    return None


def previous_cells(
    seq1, seq2, scoring, sw_matrix, cell: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Exercise 4 c
    Implement the function previous_cells() which takes two sequences S1 and
    S2, scoring function, the filled in recursion matrix from the step c) and
    the cell coordinates (row, column). The function should output the list
    of all possible previous cells.
    """
    return None


def build_all_traceback_paths(
    seq1, seq2, scoring, sw_matrix
) -> List[List[Tuple[int, int]]]:
    """
    Exercise 4 d
    Implement the function which builds all possible traceback paths.
    """
    return None


def build_alignment(seq1, seq2, traceback_path) -> Tuple[str, str]:
    """
    Exercise 4 e
    Implement the function build_alignment() which takes two sequences and
    outputs the alignment.
    """
    return None