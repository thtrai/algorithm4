"""This is project for algorithmic thinking 2, week 4
PYTHON3 is used."""

example = "compute_global_alignment('ACTACT', 'GGACTGCTTCTGG', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 1, 2, 4, 4, 6, 7, 7, 7, 7, 7, 7, 7, 7], [0, 1, 2, 4, 6, 6, 7, 9, 9, 9, 9, 9, 9, 9], [0, 1, 2, 4, 6, 8, 8, 9, 11, 11, 11, 11, 11, 11]]) #returned aligned y sequence does not include the entire original sequence: 'ACTGCTTCTGG' (11, '--A---CTACT--', 'GGACTGCTTCTGG') "

def globalization(num, global_flag):
    """Helper function. It is the Question12 from Homework 4. It is used for 
    compute_alignment_matrix function."""
    if num < 0 and not global_flag:
        return 0
    else:
        return num

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

    for index_i in range(1,length_m + 1):
        dummy_si = matrix[index_i - 1][0] + scoring_matrix[seq_x[index_i - 1]]['-']  #S[i,0]
        matrix.append([globalization(dummy_si,global_flag)])
    
    for index_j in range(1,length_n + 1):
        dummy_sj = matrix[0][index_j - 1] + scoring_matrix[seq_y[index_j - 1]]['-']  #S[0,j]
        matrix[0].append(globalization(dummy_sj,global_flag))

    for index_i in range(1,length_m + 1):
        for index_j in range(1,length_n + 1):
            max_list = list()
            max_list.append(matrix[index_i - 1][index_j -1] + scoring_matrix[seq_x[index_i - 1]][seq_y[index_j -1]])
            max_list.append(matrix[index_i - 1][index_j] + scoring_matrix[seq_x[index_i - 1]]['-'])
            max_list.append(matrix[index_i][index_j -1] + scoring_matrix[seq_y[index_j - 1]]['-'])
            

            if not global_flag and max(max_list) < 0:
                matrix[index_i].append(0)
            else:
                matrix[index_i].append(max(max_list))

    return matrix


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a common 
    alphabet with the scoring matrix scoring_matrix. This function computes a global 
    alignment of seq_x and seq_y using the global alignment matrix alignment_matrix.
    The function returns a tuple of the form (score, align_x, align_y) where score is
    the score of the global alignment align_x and align_y. Note that align_x and align_y
    should have the same length and may include the padding character ’-’."""

    length_i = len(seq_x)
    length_j = len(seq_y)
    secondary_x = ''
    secondary_y = ''
    
    while length_i !=0 and length_j !=0:
        if alignment_matrix[length_i][length_j] == alignment_matrix[length_i -1][length_j -1] +\
        scoring_matrix[seq_x[length_i - 1]][seq_y[length_j - 1]]:
            #lines 1,2
            secondary_x = seq_x[length_i - 1] + secondary_x
            secondary_y = seq_y[length_j - 1] + secondary_y
            length_i -= 1
            length_j -= 1
        else:
            if alignment_matrix[length_i][length_j] == alignment_matrix[length_i -1][length_j] +\
            scoring_matrix[seq_x[length_i -1]]['-']:
                #lines 3,4
                secondary_x = seq_x[length_i - 1] + secondary_x
                secondary_y = '-' + secondary_y
                length_i -= 1
            else:
                #lines 5,6
                secondary_x = '-' + secondary_x
                secondary_y = seq_y[length_j - 1] + secondary_y
                length_j -= 1
    while length_i != 0:
        secondary_x = seq_x[length_i -1] + secondary_x
        secondary_y = '-' + secondary_y
        length_i -= 1

    while length_j != 0:
        secondary_x = '-' + secondary_x
        secondary_y = seq_y[length_j -1] + secondary_y
        length_j -= 1

    return (0,secondary_x,secondary_y)
