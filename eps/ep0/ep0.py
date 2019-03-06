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

  Nome : Ricardo Hideki Hangai Kojo
  NUSP : 10295429

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma referencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em:
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

  Para a parte 1:
  - Referências de como ler arquivo, separar string em uma lista, remover elementos vazios de uma lista etc. Coisas básicas, em geral retiradas direto do StackOverflow.
  https://stackoverflow.com/questions/7409780/reading-entire-file-in-python
  https://stackoverflow.com/questions/19894478/regex-punctuation-split-python
  https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
"""
import random
import math
import re
from string import punctuation

# **********************************************************
# **                 INICIO DA PARTE 1                    **
# **********************************************************


def compute_word_freq(filename):
    """ Computa a frequencia de ocorrencia de palavras em um dado arquivo
        de texto.

    Devolve um dicionario mapeando cada palavra com pelo menos 5 caracteres
    (ignorando caixa alta e baixa) na sua frequencia de ocorrencia.

    Considere uma palavra como qualquer sequencia de 5 ou mais caracteres
    separada por espacos, quebra de linha ou inicio/fim de arquivo.

    :param filename: nome do arquivo de texto a ser processado.
    :type filename: <class 'str'>
    :return freq: Dicionario com a frequencia de ocorrencia de cada palavra
    :rtype: <class 'dict'>

    :Examples:

    >>> compute_word_freq('war_and_peace.txt')
    {'compress': 1.743949802148895e-06, 'screen': 1.743949802148895e-05, ...}

    .. note::
        Desconsidere palavras com menos do que cinco caracteres.

    .. seealso::
        Consulte o enunciado para um exemplo mais detalhado.
    """
    
    result = {}
    r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))

    file = open(filename, 'r')

    content = r.split(file.read()) # splits file content into a list, based on string.punctuation list of 
    content = list(filter(None, content)) # removes empty strings from list
    
    total = len(content)
    
    for word in content:
        word = word.lower()
        if len(word) >= 5:
            if word not in result:
                result[word] = 1.0 / total
            else:
                result[word] += 1.0 / total

    file.close()

    return result


def compute_phrase_freq(filename):
    """ Computa a frequencia de ocorrencia de pares de palavras em um dado
        arquivo de texto.

    Considere uma palavra como qualquer sequencia de caracteres separada por
    espacos, quebra de linha ou inicio/fim de arquivo. Ignore a caixa das
    letras. Alem disso, voce deve contabilizar pares de palavras contiguas
    no arquivo texto de entrada.

    :param filename: nome do arquivo de texto a ser processado.
    :type filename: <class 'str'>
    :return freq: Dicionario com a frequencia de ocorrencia de cada frase
    :rtype: <class 'dict'>

    :Examples:

    >>> compute_phrase_freq('war_and_peace.txt')
    {'watch their': 1.7439528435151113e-06,
     'count suddenly': 3.4879056870302226e-06,
     'prince andrew': 0.0018695174482481994, ...}

    .. note::
        Desconsidere frases com palavras de menos do que cinco caracteres.

    .. seealso::
        Consulte o enunciado para um exemplo mais detalhado.
    """

    result = {}
    r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))

    file = open(filename, 'r')

    content = r.split(file.read()) # splits file content into a list, based on string.punctuation list of 
    content = list(filter(None, content)) # removes empty strings from list
    total = len(content) - 1 # the amount of pairs is the amount of words minus 1

    for i in range(len(content) - 1):
        first_word = content[i].lower()
        second_word = content[i + 1].lower()
        concat = first_word + ' ' + second_word
        if len(first_word) >= 5 and len(second_word) >= 5:
            if concat not in result:
                result[concat] = 1.0 / total
            else:
                result[concat] += 1.0 / total

    file.close()

    return result

# ----------------------------------------------------------
# --                  FIM DA PARTE 1                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INICIO DA PARTE 2                    **
# **********************************************************


def is_well_formed(filename):
    """Verifica se um arquivo de texto contém uma expressao bem formada.

    A funcao :func:'is_well_formed' retorna True se o texto contiver uma
    expressao bem formada, ou seja, se cada simbolo (,[ ou { pode ser casado
    com um simbolo correspondente }, ] ou ) ou retorna False se a expressao
    nao for bem formada.

    :param filename: String com o nome do arquivo a ser verificado
    :type filename: <class 'str'>
    :return verified: Boolean com True se o arquivo respeita e False c.c.
    :rtype: <class 'bool'>

    :Example:

    >>> is_well_formed('test_parentheses01.txt')
    True
    >>> is_well_formed('test_parentheses02.txt')
    False

    .. note::
        Voce nao deve se preocupar com questoes estruturais do arquivo, ou
        seja (por ex.: se o erro ocorreu em um comentario). Tudo que importa
        e' se a expressao e' bem formada.
        Alem disso, os unicos simbolos que devem ser considerados sao: ()[]{}.

    .. seealso::
        Vide enunciado para mais exemplos
    """
    raise NotImplementedError  # NÃO SE ESQUEÇA DE APAGAR ESSA LINHA!


# ----------------------------------------------------------
# --                  FIM DA PARTE 2                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INICIO DA PARTE 3                    **
# **********************************************************

def uniform_cost_search(problem):
    """ Implementa busca de custo uniforme no problema problem

    A funcao :func:'uniform_cost_search' recebe um problema problem e
    retorna None se o problema não contiver solucao, caso contrario
    retorna um no busca contendo um estado meta do problema.

    :param problem: Objeto da classe Problem descrita no enunciado
    :type problem: <class 'Problem'>
    :return solution: Um no de busca atualizado com a solucao ou None c.c.
    :rtype: <class 'Node'> or <class 'NoneType'>

    :Example:

    >>> a = uniform_cost_search(P1)
    >>> a.state
    (1,2,3,4,5,6,7,8,0)
    >>> a.parent
    <__main__.node object at 0x7f29fbc301d0>

    .. note::
        Voce nao precisa implementar o verificador de solucao, cabe ao
        autograder verificar se o no' retornado e' realmente a meta e
        se os apontadores para os pais e as acoes tomadas estao corretas.
        Caso deseje testar, a funcao que retorna a solucao e'
        :func:'check_solution'

    .. seealso::
        Vide enunciado para mais exemplos dos objetos node e problem
    """
    raise NotImplementedError  # NÃO SE ESQUEÇA DE APAGAR ESSA LINHA!


# ----------------------------------------------------------
# --                  FIM DA PARTE 3                      --
# ----------------------------------------------------------

def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    #r1 = compute_word_freq('war_and_peace.txt')
    #for w in r1:
    #    print(w, r1[w])
    r2 = compute_phrase_freq('simple_corpus.txt')
    for p in r2:
        print(p, r2[p])
    #r3 = is_well_formed('test_parentheses01.txt')
    #print(r3)
    print('********************')
    my_problem = SimpleProblem()  # Inicializa SimpleProblem default
    my_sol = depth_first_search(my_problem)  # Tenta resolver usando dfs
    valid_sol, steps = check_solution(my_sol, my_problem)  # checa solucao
    if valid_sol:
        print(steps)
    else:
        print("Solucao invalida ou nao encontrada")
    print('********************')
    # Inicializa EightPuzzle com o seguinte tabuleiro
    # -------------
    # | 1 | 2 | 3 |
    # -------------
    # | 4 | 5 | 6 |
    # -------------
    # | 0 | 7 | 8 |
    # -------------
    my_problem2 = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))
    # Tenta resolver usando dfs
    my_sol2 = depth_first_search(my_problem2)
    # Checa solucao
    valid_sol2, steps2 = check_solution(my_sol2, my_problem2)
    if valid_sol2:
        print(steps2)
    else:
        print("Solucao invalida ou nao encontrada")
    print('********************')
    # Inicializa GridWorld com o seguinte tabuleiro
    # -------------
    # |   | G |   |  X -> Inicio (0,0)
    # -------------  G -> Meta (1,1)
    # | X |   |   |  Os custos sao computados aleatoriamente
    # -------------
    my_problem3 = GridWorld(2, 3, (0, 0), (1, 1))
    my_sol3 = depth_first_search(my_problem3)
    valid_sol3, steps3 = check_solution(my_sol3, my_problem3)
    if valid_sol3:
        print(steps3)
    else:
        print("Solucao invalida ou nao encontrada")
    print('********************')


# ******************************************************
# **  IMPORTANTE: NAO MODIFIQUE AS PROXIMAS LINHAS!   **
# ******************************************************

class Node:
    """ Classe que abstrai as informacoes de um no' de busca

    A classe Node e' uma classe que abstrai o conceito de no' de busca
    estudado. Essa classe possui os seguintes atributos publicos:

    :var state: Armazena um estado do problema.
    :var cost: Armazena o custo acumulado do caminho do inicio ate o no' atual
    :var parent: Armazena um apontador para o no' pai caso exista, caso
        contrario armazena None por definicao.
    :var action: Armazena a acao realizada.

    :Example:

    >>> my_node = Node((1,2,3), 7)
    >>> my_node.state
    (1, 2, 3)
    >>> my_node.cost
    7
    >>> my_node.parent
    >>> my_node.action
    >>> other_node = Node(state=(1,2,4), cost=9, parent=my_node, action='ATIRAR')
    >>> other_node.state
    (1, 2, 4)
    >>> other_node.cost
    9
    >>> other_node.parent
    <Node (1, 2, 3)>
    >>> other_node.action
    'ATIRAR'

    .. note::
        Suas implementacoes de busca devem instanciar os nos de busca e
        acertar o apontador para os eventuais pais.
        Para facilitar, implementamos para voce o __repr__ que imprime uma
        versao mais descritiva do no' ao inves de seu endereco.
        Por questoes de ordem didatica e para facilitar a implementacao,
        esta e' a unica classe na qual voce pode/deve acessar atributos
        diretamente.

    .. warning::
        Suas buscas DEVEM retornar um objeto do tipo Node!
    """


    def __init__(self, state, cost, parent=None, action=None):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.action = action
        if self.parent:
            self.height = self.parent.height + 1
        else:
            self.height = 0


    def __repr__(self):
        return "<Node {}>".format(self.state)


def check_solution(node, problem):
    """ Checa a validade de uma solucao para o problema e retorna a sequencia
        de acoes se houver solucao.

    A funcao :func:'check_solution' recebe um objeto do tipo Node contendo o
    no meta de um problema problem e verifica se a solucao encontrada e'
    valida. Caso seja, retorna uma tupla contendo (True, L1), onde L1 e' a
    sequencia de acoes do no' inicial ate' a meta. Caso a solucao apresentada
    nao seja valida, retorna uma tupla (False, L2) onde L2 ou e' uma lista
    vazia, ou uma lista com uma sequencia de acoes ate o ponto de falha.

    :param node: Um no de busca contendo a solucao para o problema problem
    :type node: <class 'Node'>
    :param problem: Um problema de busca da classe Problem
    :type problem: <class 'Problem'>
    :return (valid, L): Uma tupla contendo em valid um booleano indicando a
        validade da solucao e uma lista com a sequencia de acoes total/parcial
    :rtype: <class 'tuple'>


    :Example:

    >>> my_problem = EightPuzzle((1,2,3,4,5,6,7,0,8))
    >>> my_solution = uniform_cost_search(my_problem)
    >>> found, actions = check_solution(my_solution, my_problem)
    >>> found
    True
    >>> actions
    [None, 'RIGHT']

    """
    steps = []
    if not problem.is_goal_state(node.state):
        return (False, steps)
    while node.parent is not None:
        new_n = node.parent
        if node.state != problem.next_state(new_n.state, node.action):
            return (False, steps)
        steps.append(node.action)
        node = new_n
    if node is not None:
        steps.append(node.action)
    return (True, list(reversed(steps)))


def depth_first_search(problem):
    """ Busca em profundidade com memoria

    Estamos fornecendo uma implementacao da busca em profundidade com
    memoria por duas razoes:
    1. Para que voce tenha uma base da forma como manipular a classe problem.
    2. Para que voce possa testar um algoritmo de busca em diferentes
       problemas.
    """
    frontier = [Node(problem.start(), 0)]
    explored = set([])
    while frontier:
        node = frontier.pop() # remove no' mais recente na fronteira
        explored.add(node.state)
        if problem.is_goal_state(node.state):
            return node
        for action in problem.actions(node.state):
            next_state = problem.next_state(node.state, action)
            if next_state not in explored:
                cost = problem.cost(node.state, action) + node.cost
                frontier.append(Node(next_state, cost, node, action))
    return None


class Problem(object):
    """ Classe abstrata para representacao de um problema """
    def is_state(self, state):
        """ Metodo abstrato que implementa verificacao de estado """
        raise NotImplementedError
    def start(self):
        """ Metodo abstrato que implementa retorno da posicao inicial """
        raise NotImplementedError
    def actions(self, state):
        """ Metodo abstrato que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        raise NotImplementedError
    def next_state(self, state, action):
        """ Metodo abstrato que implementa funcao de transicao """
        raise NotImplementedError
    def is_goal_state(self, state):
        """ Metodo abstrato que implementa teste de meta """
        raise NotImplementedError
    def cost(self, state, action):
        """ Metodo abstrato que implementa funcao custo """
        raise NotImplementedError


class SimpleProblem(Problem):
    """ Exemplo de um problema simples que sua busca deveria resolver """
    def __init__(self):
        self.graph = {0: [1, 2, 3], 1: [0, 4], 2: [0, 3, 4], 3: [0, 2, 4]}
        self.costs = {(0, 1):  1, (1, 0):  1, (0, 2):  5, (2, 0):  5,
                      (0, 3): 15, (3, 0): 15, (1, 4): 10, (4, 1): 10,
                      (2, 3):  1, (3, 2):  1, (2, 4):  5, (4, 2):  5,
                      (3, 4):  5, (4, 3):  5}
        self.goal = 4


    def is_state(self, state):
        return state in self.graph


    def start(self):
        return 0


    def actions(self, state):
        if state in self.graph:
            return self.graph[state]
        else:
            return None


    def next_state(self, state, action):
        if action in self.graph[state]:
            return action
        else:
            return None


    def is_goal_state(self, state):
        return state == self.goal


    def cost(self, state, action):
        return self.costs[(state, action)]


class GridWorld(Problem):
    """ Classe de problemas do tipo GridWorld simplificado

    Essa classe de problemas simplifica os problemas do tipo GridWorld.
    Neles, voce esta em um Grid de dimensoes width x height e deve chegar
    de uma coordenada inicial ate uma coordenada final.
    Dependendo dos parametros de instanciacao, os custos de cada movimento
    podem ser variaveis, ou seja, usar a acao 'UP' pode ter custos diferentes
    dependendo da posicao do seu agente no Grid.
    Essa classe possui cinco atributos que NAO devem ser acessados de fora da
    classe, incluindo os quatro atributos publicos.
    Tudo que voce deve acessar sao os metodos publicos previamente definidos
    na classe abstrata Problem.
    """
    def __init__(self, height, width, start, goal, max_cost=1, seed=12345):
        self.height = height
        self.width = width
        self.s_pos = start
        self.goal = goal
        self.__grid_info = self.__generate_grid(height, width, seed, max_cost)

    @staticmethod
    def __generate_grid(height, width, seed, max_cost):
        final_grid = {}
        random.seed(seed)
        for h in range(height):
            for w in range(width):
                final_grid[(w, h)] = random.randint(1, max_cost)
        return final_grid


    def is_state(self, state):
        return state in self.__grid_info


    def start(self):
        return self.s_pos


    def actions(self, state):
        valid = []
        x, y = state
        if (x, y+1) in self.__grid_info:
            valid.append('UP')
        if (x, y-1) in self.__grid_info:
            valid.append('DOWN')
        if (x-1, y) in self.__grid_info:
            valid.append('LEFT')
        if (x+1, y) in self.__grid_info:
            valid.append('RIGHT')
        return valid


    def next_state(self, state, action):
        if action not in self.actions(state):
            raise ValueError('Invalid action')
        x, y = state
        if action == 'UP':
            return (x, y+1)
        elif action == 'DOWN':
            return (x, y-1)
        elif action == 'LEFT':
            return (x-1, y)
        else:
            return (x+1, y)


    def is_goal_state(self, state):
        return state == self.goal


    def cost(self, state, action):
        if action in self.actions(state):
            return self.__grid_info[self.next_state(state, action)]
        return math.inf



class EightPuzzle(Problem):
    """ Classe de problemas do tipo EightPuzzle alternativo

    Essa e' a classe de problemas do tipo EightPuzzle, ou seja, problemas
    onde voce recebe um Grid 3x3 contendo os numeros de 0 a 8 e deve encontrar
    a sequencia de movimentos que leva da posicao inicial a posicao final,
    movendo o 0, tal como apresentado abaixo:

               Inicial                   Final
            -------------            -------------
            | 1 | 2 | 3 |            | 1 | 2 | 3 |
            -------------   'RIGHT'  -------------
            | 4 | 5 | 6 |   ------>  | 4 | 5 | 6 |
            -------------            -------------
            | 7 | 0 | 8 |            | 7 | 8 | 0 |
            ------------             ------------

    Tal como na classe anterior, voce NAO deve acessar o atributo da classe,
    apenas os metodos publicos definidos na classe abstrata Problem.
    """


    def __init__(self, s0=(2, 0, 3, 1, 8, 4, 7, 6, 5)):
        self.s0 = s0


    def is_state(self, state):
        if len(state) != 9:
            return False
        for i in range(9):
            if i not in state:
                return False
        return True


    def start(self):
        return self.s0


    def actions(self, state):
        valid = []
        pos = state.index(0)
        if pos not in (0, 1, 2):
            valid.append('UP')
        if pos not in (6, 7, 8):
            valid.append('DOWN')
        if pos not in (0, 3, 6):
            valid.append('LEFT')
        if pos not in (2, 5, 8):
            valid.append('RIGHT')
        return valid


    def next_state(self, state, action):
        if action not in self.actions(state):
            raise ValueError('Invalid action')
        st = list(state)
        pos = st.index(0)
        if action == 'UP':
            st[pos] = st[pos-3]
            st[pos-3] = 0
        elif action == 'DOWN':
            st[pos] = st[pos+3]
            st[pos+3] = 0
        elif action == 'LEFT':
            st[pos] = st[pos-1]
            st[pos-1] = 0
        else:
            st[pos] = st[pos+1]
            st[pos+1] = 0
        return tuple(st)


    def is_goal_state(self, state):
        if state == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return True
        return False


    def cost(self, state, action):
        if action in self.actions(state):
            return 1
        return None


if __name__ == "__main__":
    main()
