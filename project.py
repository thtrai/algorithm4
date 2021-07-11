"""This is project for algorithmic thinking 2, week 4
PYTHON3 is used."""
example = "set(['A', 'C', 'T', 'G']), 6, 2, -4 "



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
