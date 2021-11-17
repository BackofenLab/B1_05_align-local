import pytest
from exercise_sheet5 import *
from smith_waterman.smith_waterman import *
from math import inf
import pprint
import random



SCORING = [
    {"match": -1, "mismatch": 0, "gap_introduction": 4, "gap_extension": 1},
    {"match": -1, "mismatch": 0, "gap_introduction": 2, "gap_extension": 1 },
    {"match": -1, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
    {"match": -2, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
]


def random_seq_generator(length, random_seed):
    random.seed(random_seed)
    return "".join(
        [random.choice(["A", "T", "C", "G"]) for _ in range(length)]
    )

def check_none(*args):
    if None in args:
        print("you have not filled in all the fields")
        raise ValueError

def check_zero_in_dict(d):
    val = d.values()
    if 0 in val:
        print("you have not filled in all the fields")
        raise ValueError

def test_exercise_1a():
    s_ij = exercise_1a()
    #        T   A   C   G   C   A   G   A
    expected_s_ij = [
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  1,  0,  0,  0,  0,  0,  0,  0],  # T
        [0,  0,  1,  1,  0,  1,  0,  0,  0],  # C
        [0,  0,  0,  2,  1,  1,  1,  0,  0],  # C
        [0,  0,  0,  1,  3,  2,  1,  2,  1],  # G
        [0,  0,  1,  0,  2,  3,  3,  2,  3],  # A
    ]
    assert s_ij == expected_s_ij


def test_exercise_1b():
    """
    """
    alignments, score = exercise_1b()

    expected_alignments = [
        ("TCCG", "TACG"),
        ("TCCGA", "TACGC"),
        ("TCCG-A", "TACGCA"),
        ("CCGA", "CAGA")
    ]
    expected_sore = 3
    assert expected_sore == score
    assert set(expected_alignments) == set(alignments)


def test_exercise_2a():
    """
    """


def test_exercise_2b():
    """
    """


def test_exercise_3a():
    """
    """



# @pytest.mark.parametrize(
#     "seq1,seq2",
#     [
#         ("TCCGA", "TACGCGC", ),
#         ("TCCCGG", "TCAAA",),
#         ("TCCGA", "TACGCGC", ),
#         ("AAA", "TTT", ),
#         ("TACGCAGA", "TCCGA", ),

#     ] + [
#         (random_seq_generator(10, 1), random_seq_generator(10, 2)),
#         (random_seq_generator(15, 1), random_seq_generator(20, 2)),
#         (random_seq_generator(30, 1), random_seq_generator(13, 2)),
#         (random_seq_generator(19, 1), random_seq_generator(13, 2)),
#     ]
# )
# def test_exercise_4a(seq1, seq2):
#     matrix_expected = zero_init_correct(seq1, seq2)
#     matrix = zero_init(seq1, seq2)
#     if matrix != matrix_expected:
#         print(
#             f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
#         print(f"Your init matrix is:")
#         pprint.pprint(matrix)
#         print("It is supposed to look like:")
#         pprint.pprint(matrix_expected)
#     assert matrix == matrix_expected


