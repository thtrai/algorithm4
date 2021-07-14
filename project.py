"""This is project for algorithmic thinking 2, week 4
PYTHON3 is used."""


example = "compute_local_alignment('abddcdeffgh', 'aabcddefghij', {'-': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1,'o': -1,\
'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'a': {'-': -1, 'a': 2, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1,\
'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'c': {'-': -1, 'a': -1, 'c': 2,\
'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1,\
'x': -1, 'z': -1}, 'b': {'-': -1, 'a': -1, 'c': -1, 'b': 2, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1,\
'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'e': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': 2, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1,\
'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'd': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': 2, 'g': -1,\
'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'g': {'-': -1,\
'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': 2, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1,\
'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'f': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': 2, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1,\
'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'i': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': 2, 'h': -1, 'k': -1,\
'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'h': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1,\
'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': 2, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1},\
'k': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': 2, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1,\
't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'j': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': 2, 'm': -1, 'l': -1, 'o': -1,\
'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'm': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1,\
'h': -1, 'k': -1, 'j': -1, 'm': 2, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'l': {'-': -1, 'a': -1, 'c': -1,\
'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': 2, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1,\
'x': -1, 'z': -1}, 'o': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': 2, 'n': -1, 'q': -1, 'p': -1, 's': -1,\
'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'n': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1,\
'l': -1, 'o': -1, 'n': 2, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'q': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1,\
'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': 2, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'p': {'-': -1,\
'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': 2, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1,\
'v': -1, 'y': -1, 'x': -1, 'z': -1}, 's': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1,\
'p': -1, 's': 2, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'r': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1,\
'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': 2, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'u': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1,\
'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': 2, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1},\
't': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1,\
't': 2, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'w': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1,\
'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': 2, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'v': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1,\
'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': 2, 'y': -1, 'x': -1, 'z': -1}, 'y': {'-': -1, 'a': -1, 'c': -1,\
'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': 2,\
'x': -1, 'z': -1}, 'x': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1,\
'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': 2, 'z': -1}, 'z': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1,\
'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': 2}},\
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 5, 4, 3, 2, 1, 0, 0, 0],\
[0, 0, 0, 2, 2, 5, 7, 6, 5, 4, 3, 2, 1], [0, 0, 0, 1, 4, 4, 6, 6, 5, 4, 3, 2, 1], [0, 0, 0, 0, 3, 6, 6, 5, 5, 4, 3, 2, 1], [0, 0, 0, 0, 2, 5, 5, 8, 7, 6, 5, 4, 3], \
[0, 0, 0, 0, 1, 4, 4, 7, 10, 9, 8, 7, 6], [0, 0, 0, 0, 0, 3, 3, 6, 9, 9, 8, 7, 6], [0, 0, 0, 0, 0, 2, 2, 5, 8, 11, 10, 9, 8], [0, 0, 0, 0, 0, 1, 1, 4, 7, 10, 13, 12, 11]])  \
returned incorrect score, expected 12 but received 11"






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
    
    score = alignment_matrix[-1][-1] 


    return (score,secondary_x,secondary_y)


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a 
    common alphabet with the scoring matrix scoring_matrix. This function 
    computes a local alignment of seq_x and seq_y using the local alignment 
    matrix alignment_matrix.The function returns a tuple of the form 
    (score, align_x, align_y) where score is the score of the optimal local 
    alignment align_x and align_y. Note that align_x and align_y should have
    the same length and may include the padding character ’-’."""

    length_i = len(seq_x)
    length_j = len(seq_y)
    secondary_x = ''
    secondary_y = ''

    maxi = float('-inf')
    for matrix_list in alignment_matrix:
        dummy_max = max(matrix_list)
        if dummy_max > maxi:
            maxi = dummy_max
    print('maxi is ',maxi)

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
    
    score = alignment_matrix[-1][-1] 


    return (score,secondary_x,secondary_y)

