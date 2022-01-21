def condicional(HipotesisA, Evidencia_dada_HipotesisBA, EvidenciaB):

    return (HipotesisA*Evidencia_dada_HipotesisBA)/EvidenciaB

def run():
    prob_cancer = 1/100000
    prob_sintomas_dado_cancer = 1
    prob_sintomas_dado_no_cancer = 10/99999
    prob_no_cancer = 1 - prob_cancer


    prob_sintomas = (prob_cancer*prob_sintomas_dado_cancer) + (prob_no_cancer*prob_sintomas_dado_no_cancer)
    prob_cancer_dado_sintomas = condicional(prob_cancer, prob_sintomas_dado_cancer, prob_sintomas)

    print(f'La probabilidad que tenga cancer dado que tiene sintomas es: {prob_cancer_dado_sintomas}')


if __name__ == '__main__':
    run()