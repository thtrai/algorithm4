"""This is project for algorithmic thinking 2, week 4
PYTHON3 is used."""
example = "compute_alignment_matrix('A', 'A', {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}, True) expected [[0, -4], [-4, 6]] but received [[0]] "



def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """Takes as input a set of characters alphabet and three scores
    diag_score, off_diag_score, and dash_score. The function return
    s a dictionary of dictionaries whose entries are indexed by pair
    s of characters in alphabet plus '-'. The score for any entry indexed 
    by one or more dashes is dash_score. The score for the remaining
    diagonal entries is diag_score. Finally, the score for the remaining 
    off-diagonal entries is off_diag_score."""
    myword = set(alphabet)
    myword.add('-')
    answer_dict = dict()
    for character_i in myword:
        answer_dict[character_i] = dict()
        small_dict = answer_dict[character_i]
        for character_j in myword:
            if '-' in (character_i, character_j):
                small_dict[character_j] = dash_score
            elif character_j == character_i:
                small_dict[character_j] = diag_score
            elif character_j != character_i:
                small_dict[character_j] = off_diag_score


    return answer_dict


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """Takes as input two sequences seq_x and seq_y whose elements share 
    a common alphabet with the scoring matrix scoring_matrix. The function
    computes and returns the alignment matrix for seq_x and seq_y as described
    in the Homework. If global_flag is True, each entry of the alignment
    matrix is computed using the method described in Question 8 of the
    Homework. If global_flag is False, each entry is computed using the 
    method described in Question 12 of the Homework."""

    length_m = len(seq_x)
    length_n = len(seq_y)

    matrix = list()
    matrix.append(list())
    matrix[0].append(0)

    for index_i in range(1,length_m+1):
        matrix.append(list())




    return matrix
