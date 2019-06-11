"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP,
  DECLARO QUE SOU A UNICA PESSOA AUTORA E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E, PORTANTO, NAO CONSTITUEM ATO DE DESONESTIDADE ACADEMICA,
  FALTA DE ETICA OU PLAGIO.
  DECLARO TAMBEM QUE SOU A PESSOA RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : RICARDO HIDEKI HANGAI KOJO
  NUSP : 10295429

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma referencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em:
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

  - Modelos de problemas do EP0, para entender a interface Problem
  suas funções;
  - Regex: https://regex101.com
  - Python Sets: https://www.w3schools.com/python/python_sets.asp
"""

import util

############################################################
# Part 1: Segmentation problem under a unigram model

class SegmentationProblem(util.Problem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def isState(self, state):
        """ Metodo que implementa verificacao de estado """
        if isinstance(state, int) and state <= len(self.query):
            return True
        return False

    def initialState(self):
        """ Metodo que implementa retorno da posicao inicial """
        return 0

    def actions(self, state):
        """ Metodo que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        valid = [str(i) for i in range(state + 1, len(self.query) + 1)]
        return valid

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        if action not in self.actions(state):
            raise ValueError('Invalid action')
        return int(action)

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        return state >= len(self.query)

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        if action in self.actions(state):
            cut_index = int(action)
            return self.unigramCost(self.query[state:cut_index])
        return None
        


def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''
     
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    problem = SegmentationProblem(query, unigramCost)
    goal = util.uniformCostSearch(problem)
    valid, solution = util.getSolution(goal, problem)

    words = []

    if valid:
        actions = [0] + [int(a) for a in solution.strip(' ').split(' ')]
        for i in range(0, len(actions) - 1):
            word = query[actions[i]:actions[i+1]]
            words.append(word)
        return ' '.join(words)
    return None


    # END_YOUR_CODE

############################################################
# Part 2: Vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.Problem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def isState(self, state):
        """ Metodo  que implementa verificacao de estado """
        if isinstance(state, tuple) and isinstance(state[0], int) and isinstance(state[1], str):
            if (state[0] < len(self.queryWords)):
                return True
        return False

    def initialState(self):
        """ Metodo  que implementa retorno da posicao inicial """
        return (0, util.SENTENCE_BEGIN)

    def actions(self, state):
        """ Metodo  que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        word = self.queryWords[state[0]]
        valid = list(self.possibleFills(word))
        if valid:
            return valid
        return [word]

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        if action in self.actions(state):
            return (state[0] + 1, action)
        return None

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        return state[0] == len(self.queryWords)

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        if action in self.actions(state):
            return self.bigramCost(state[1], action)
        return None



def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    problem = VowelInsertionProblem(queryWords, bigramCost, possibleFills)
    goal = util.uniformCostSearch(problem)
    valid, solution = util.getSolution(goal, problem)

    if valid:
        return solution

    return None
    # END_YOUR_CODE

############################################################


def getRealCosts(corpus='corpus.txt'):

    """ Retorna as funcoes de custo unigrama, bigrama e possiveis fills obtidas a partir do corpus."""
    
    _realUnigramCost, _realBigramCost, _possibleFills = None, None, None
    if _realUnigramCost is None:
        print('Training language cost functions [corpus: '+ corpus+']... ')
        
        _realUnigramCost, _realBigramCost = util.makeLanguageModels(corpus)
        _possibleFills = util.makeInverseRemovalDictionary(corpus, 'aeiou')

        print('Done!')

    return _realUnigramCost, _realBigramCost, _possibleFills

def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    unigramCost, bigramCost, possibleFills  =  getRealCosts()
    
    resulSegment = segmentWords('believeinyourselfandinyourabilitiesbelieveinyourselfandinyourabilitiesbelieveinyourselfandinyourabilitiesbelieveinyourselfandinyourabilitiesbelieveinyourselfandinyourabilitiesbelieveinyourselfandinyourabilities', unigramCost)
    print(resulSegment)

    resultInsert = insertVowels('wld lk t hv mr lttrs'.split(), bigramCost, possibleFills)
    print(resultInsert)

if __name__ == '__main__':
    main()
