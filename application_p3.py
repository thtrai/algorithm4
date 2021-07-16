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
