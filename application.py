import provided 
import project as p
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

#### END OF HELPER FUNCTIONS #########
###question 1

human_protein = provided.read_protein(provided.HUMAN_EYELESS_URL)
fruitfly_protein = provided.read_protein(provided.FRUITFLY_EYELESS_URL)
pam_score = provided.read_scoring_matrix(provided.PAM50_URL)
    
def  question1():
    pam_alignment = p.compute_alignment_matrix(human_protein,fruitfly_protein,pam_score,False)

    print(p.compute_local_alignment(human_protein, fruitfly_protein, pam_score, pam_alignment))

#answer:(875, 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ', 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ')

#####question2

consensus_pax = provided.read_protein(provided.CONSENSUS_PAX_URL)

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
