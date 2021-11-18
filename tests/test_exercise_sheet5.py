import pprint
import random

import pytest

from exercise_sheet5 import *
from smith_waterman.smith_waterman import *

SCORING = [
    {"match": 1, "mismatch": 0, "gap_introduction": -4, },
    {"match": 1, "mismatch": 0, "gap_introduction": -2, },
    {"match": 1, "mismatch": -1, "gap_introduction": -2, },
    {"match": 2, "mismatch": -1, "gap_introduction": -2, },
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
    a, b, c = exercise_2a()

    assert a is False
    assert b is False
    assert c is True

def test_exercise_2b():
    """
    """
    i, ii, iii, iv, v = exercise_2b()

    assert i is False
    assert ii is True
    assert iii is False
    assert iv is False
    assert v is False

def test_exercise_2c():
    """
    """
    i, ii, iii, iv = exercise_2c()

    assert i is True
    assert ii is False
    assert iii is False
    assert iv is False
s
def test_exercise_3a():
    """
    """


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),
    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4a(seq1, seq2):
    expected_matrix = sw_init_correct(seq1, seq2)
    actual_matrix = sw_init(seq1, seq2)
    if actual_matrix != expected_matrix:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}")
        print(f"Your matrix is:")
        pprint.pprint(actual_matrix)
        print("It is supposed to look like:")
        pprint.pprint(expected_matrix)
    assert expected_matrix == actual_matrix


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),
    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4b(seq1, seq2, scoring):
    expected_matrix = sw_forward_correct(seq1, seq2, scoring)
    actual_matrix = sw_forward(seq1, seq2, scoring)
    if actual_matrix != expected_matrix:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your matrix is:")
        pprint.pprint(actual_matrix)
        print("It is supposed to look like:")
        pprint.pprint(expected_matrix)
    assert expected_matrix == actual_matrix


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),
    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
@pytest.mark.parametrize(
    "cell",
    [
        (3, 2),
        (3, 3),
        (2, 2),
        (3, 1),
        (3, 2),
        (3, 2),
        (3, 3),
    ]
)
def test_exercise_4c(seq1, seq2, scoring, cell):
    sw_matrix = sw_forward_correct(seq1, seq2, scoring)
    expected_cells = previous_cells_correct(
        seq1, seq2, scoring, sw_matrix, cell
    )
    actual_cells = previous_cells(seq1, seq2, scoring, sw_matrix, cell)
    expected_cells = set(expected_cells)
    actual_cells = set(actual_cells)
    if actual_cells != expected_cells:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\ncell: {cell}\n"
              f"scoring: {scoring}")
        print(f"Your previous cells are:\n{actual_cells}")
        print(f"It should be:\n{expected_cells}")
    assert expected_cells == actual_cells


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),
    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4d(seq1, seq2, scoring):
    sw_matrix = sw_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, sw_matrix
    )
    actual_paths = build_all_traceback_paths(seq1, seq2, scoring, sw_matrix)
    expected_paths = [tuple(x) for x in expected_paths]
    expected_paths = set(expected_paths)
    actual_paths = [tuple(x) for x in actual_paths]
    actual_paths = set(actual_paths)
    if actual_paths != expected_paths:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your paths are:")
        pprint.pprint(actual_paths)
        print(f"It should be:")
        pprint.pprint(expected_paths)
    assert expected_paths == actual_paths


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),
    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4e(seq1, seq2, scoring):
    sw_matrix = sw_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, sw_matrix
    )
    for traceback_path in expected_paths:
        expected_alignment = build_alignment_correct(seq1, seq2, traceback_path)
        actual_alignment = build_alignment(seq1, seq2, traceback_path)
        if actual_alignment != expected_alignment:
            print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}\npath: {traceback_path}")
            print("Your alignment is:")
            print(f"S1: {actual_alignment[0]}\nS2: {actual_alignment[1]}")
            print("It should be:")
            print(f"S1: {expected_alignment[0]}\nS2: {expected_alignment[1]}")
        assert expected_alignment == actual_alignment