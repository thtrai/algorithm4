import provided_p3
import project as p
import random
from matplotlib import pyplot as plt
#### HELPER FUNCTIONS ######


def similarity_percent(string1, string2):
    assert len(string1)  == len(string2), 'check length of the strings'
    total = len(string1)
    similar = 0
    for index in range(len(string1)):
        if string1[index] == string2[index]:
            similar += 1

    answer = similar/float(total)
    print('the similarity between ',string1,' and ',string2,' is :',answer)


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    scoring_distribution  = dict()
    for _ in range(num_trials):
        print('status = ',_)
        rand_y_list = random.sample(seq_y, len(seq_y))
        rand_y = ''.join(rand_y_list)
      #  print(rand_y)
        ali_martix = p.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        score_of_random = p.compute_local_alignment(seq_x, rand_y, scoring_matrix, ali_martix)[0]
        scoring_distribution[score_of_random] = scoring_distribution.setdefault(score_of_random,0) + 1
    return scoring_distribution


def check_spelling(checked_word, dist, word_list):
    answer_list = []
    for second_word in word_list:
        alphabet = set(checked_word).union(set(second_word))
        scoring_matrix = p.build_scoring_matrix(alphabet, 2,1,0)
        alignment_matrix = p.compute_alignment_matrix(checked_word, second_word, scoring_matrix, True)
        score = p.compute_global_alignment(checked_word, second_word, scoring_matrix, alignment_matrix)[1]
        
        if score <= dist:
            answer_list.append(second_word)


    return answer_list



#### END OF HELPER FUNCTIONS #########
###question 1

human_protein = provided_p3.read_protein(provided_p3.HUMAN_EYELESS_URL)
fruitfly_protein = provided_p3.read_protein(provided_p3.FRUITFLY_EYELESS_URL)
pam_score = provided_p3.read_scoring_matrix(provided_p3.PAM50_URL)
    
def  question1():
    pam_alignment = p.compute_alignment_matrix(human_protein,fruitfly_protein,pam_score,False)

    print(p.compute_local_alignment(human_protein, fruitfly_protein, pam_score, pam_alignment))

#answer:(875, 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ', 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ')

#####question2

consensus_pax = provided_p3.read_protein(provided_p3.CONSENSUS_PAX_URL)

def question2():
    #take these from previous answer
    human_local = 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQ'
    fruit_local = 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ'
    
    #human - consensus
    human_consensus_alignment = p.compute_alignment_matrix(human_local,consensus_pax,pam_score,True)

    human_consensus_global = p.compute_global_alignment(human_local, consensus_pax, pam_score, human_consensus_alignment)
    #print('Global alignment of human_local and consensus_pax is :')
    #print(human_consensus_global)
    
    similarity_percent(human_consensus_global[1],human_consensus_global[2])



    #fruit - consensus
    fruit_consensus_alignment = p.compute_alignment_matrix(fruit_local,consensus_pax,pam_score,True)
    fruit_consensus_global = p.compute_global_alignment(fruit_local, consensus_pax, pam_score, fruit_consensus_alignment)

    #print('Global alignment of fruit_local and consensus_pax is :')
    #print(fruit_consensus_global)

    similarity_percent(fruit_consensus_global[1],fruit_consensus_global[2])

def question3():
    repetitions = 10
    amino_acids = "ACBEDGFIHKMLNQPSRTWVYXZ"
    human_local = 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQ'
    comparison_string = human_local

    for _ in range(repetitions):
        random_acid = ''
        for __ in range(len(comparison_string)):
            random_acid += random.choice(amino_acids)

        similarity_percent(random_acid,comparison_string)
    #######answer:
    #running tests forming a random string of acids of the same length as human_local protein
    #the similarity between the two is below 10%. So, a high similarity such as 70% (as question2)
    #shows as that the two proteins are not irrelevant. They come from a common ansestor


def question4():
    human_fruit_rdict = generate_null_distribution(human_protein, fruitfly_protein, pam_score, 1000)
    #return human_fruit_rdict
    x_scores = human_fruit_rdict.keys()
    y_times =  human_fruit_rdict.values()



    y_fraction =  []
    total = sum(y_times)
    print('total is ',total)
    for times in y_times:
        y_fraction.append(times/float(total))


    plt.bar(x_scores, y_fraction, label='human_protein, fruitfly_protein randomed')
    plt.xlabel('Local score')
    plt.ylabel('Percentage of the score')
    plt.title('Distribution of generate_null_distribution of 2 proteins')
    plt.legend()
    plt.show()

    return human_fruit_rdict
    ###answer:
    """#human_fruit_rdict = {56: 52, 58: 28, 49: 71, 45: 49, 65: 6, 57: 35, 46: 58, 61: 15, 48: 52, 
    44: 43, 53: 43, 41: 8, 50: 76, 59: 17, 55: 41, 47: 83, 54: 43, 51: 59, 52: 56, 62: 12, 39: 7, 
    42: 22, 43: 37, 68: 2, 40: 2, 69: 6, 64: 13, 60: 13, 67: 6, 63: 11, 79: 1, 80: 2, 76: 1, 72: 2, 
    75: 1, 71: 8, 66: 10, 74: 3, 78: 1, 73: 2, 38: 1, 77: 1, 89: 1} """
    

def question5():

    #human_fruit_rdict  = question4()  ####OR
    ###take from the example above the solution
    human_fruit_rdict = {56: 52, 58: 28, 49: 71, 45: 49, 65: 6, 57: 35, 46: 58, 61: 15, 48: 52, 44: 43, 53: 43, 41: 8, 50: 76, 59: 17, 55: 41, 47: 83, 54: 43, 51: 59, 52: 56, 62: 12, 39: 7, 42: 22, 43: 37, 68: 2, 40: 2, 69: 6, 64: 13, 60: 13, 67: 6, 63: 11, 79: 1, 80: 2, 76: 1, 72: 2, 75: 1, 71: 8, 66: 10, 74: 3, 78: 1, 73: 2, 38: 1, 77: 1, 89: 1}

    mean = 0
    for key,value in human_fruit_rdict.items():
            mean += key*value

    num_trials = sum(human_fruit_rdict.values())

    mean = mean/float(num_trials)


    deviation = 0
    for key,value  in human_fruit_rdict.items():
        for dummy_index in range(value):
            deviation += (key-mean) ** 2

    deviation = deviation / float(num_trials)
    deviation = deviation ** 0.5

    ### from question1 the s score (local alignment for the human eyeless protein and the 
    #fruitfly eyeless protein, is 875.

    s = 875
    z_score = (s - mean) / float(deviation)

    return (mean, deviation, z_score)


def question6():
    phrase = 'winning the jackpot of an extremely large prize pool (as the example) is 99999 * 180 * 10 = 179998200. 3tickets(max) at 179998200 tickets total is 3/179998200 = 1.6666833335000018e-08.  The z_score shows us that the chance of 875 score is 118 times away standard deviation. Winning the lottery is more likely to happen than the similarity between the two proteins have happened by chance.'

    print(phrase)


    
def question7():
    phrase = """If the two words identical, |x| + |y| - score = edit. But x=y, so 2|x| -score = edit.
    But edit = 0, so 2|x| = score. But score = diag * |x|. So, 2|x| = |x|*diag => diag=2.
    Next suppose x and y have only one letter different.
    |x| + |y| - score = edit. But edit = 1, because only one letter is different. So
    |x| + |y| - score = 1. But |x| = |y|. So, 2|x| - score = 1. Score is (len(x) -1) * 2 + off_diag.
    So  ...."""

    print(phrase)




def question8():
    word_list =  ###CONTINUE HERE



