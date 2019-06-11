import os
import random
import math
from ep0 import *

TOLERANCE = 0.0001

def run_tests():
    total_global = 0
    total_tests_global = 16
    total_tests = 5
    test_results = 0
    print('######################################################')
    print('# Starting tests: (Part01-01) words                  #')
    print('######################################################')

    try:
        word_freq = compute_word_freq('simple_corpus.txt')
        assert type(word_freq) is dict, 'compute_word returned non dict'
        c_l = {}
        for k in word_freq:
            c_l[k.lower()] = word_freq[k]

        if 'greatest' in c_l:
            if abs(c_l['greatest']-0.020833333333333332) < TOLERANCE:
                test_results += 1
        if 'however' in c_l:
            if abs(c_l['however']-0.020833333333333332) < TOLERANCE:
                test_results += 1
        if 'monitors' in c_l:
            if abs(c_l['monitors']-0.041666666666666664) < TOLERANCE:
                test_results += 1
        if 'lacks' in c_l:
            if abs(c_l['lacks']-0.041666666666666664) < TOLERANCE:
                test_results += 1
        if 'characters' in c_l:
            if abs(c_l['characters']-0.041666666666666664) < TOLERANCE:
                test_results += 1
    except IOError as e:
        print('Error!')
        print('Problems in compute_word_freq')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NotImplementedError:
        print('Error!')
        print('Problems in compute_word_freq')
        print('Not implemented function')
    except AssertionError as e:
        print('Error!')
        print('Problems in compute_word_freq')
        print('Returned non dictionary')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NameError as e:
        print('Error!')
        print('Problems in compute_word_freq')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except Exception as e:
        print('Error!')
        print('Problems in compute_word_freq')
        print('Unexpected problem')
        print('Check: {0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Congratulations, your code at least run without errors    #')
        print('#############################################################')
    finally:
        print('Results:')
        print('In part01-01:')
        print('You got {0} out of {1} possible points'.format(test_results, total_tests))
        total_global += test_results

    total_tests = 5
    test_results = 0
    print('######################################################')
    print('# Starting tests: (Part01-02) phrases                #')
    print('######################################################')

    try:
        phrase_freq = compute_phrase_freq('simple_corpus.txt')
        assert type(phrase_freq) is dict, 'compute_phrase returned non dict'
        c_l = {}
        for k in phrase_freq:
            c_l[k.lower()] = phrase_freq[k]

        if 'whenever monitors' in c_l:
            if abs(c_l['whenever monitors']-0.02127659574468085) < TOLERANCE:
                test_results += 1
        if 'lacks creativity' in c_l:
            if abs(c_l['lacks creativity']-0.0425531914893617) < TOLERANCE:
                test_results += 1
        if 'characters however' in c_l:
            if abs(c_l['characters however']-0.02127659574468085) < TOLERANCE:
                test_results += 1
        if 'write bunch' not in c_l:
            test_results += 1
        if 'remember execute' in c_l:
            if abs(c_l['remember execute']-0.02127659574468085) < TOLERANCE:
                test_results += 1
    except IOError as e:
        print('Error!')
        print('Problems in compute_phrase_freq')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NotImplementedError:
        print('Error!')
        print('Problems in compute_phrase_freq')
        print('Not implemented function')
    except AssertionError as e:
        print('Error!')
        print('Problems in compute_phrase_freq')
        print('Returned non dictionary')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NameError as e:
        print('Error!')
        print('Problems in compute_phrase_freq')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except Exception as e:
        print('Error!')
        print('Problems in compute_phrase_freq')
        print('Unexpected problem')
        print('Check: {0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Congratulations, your code at least run without errors    #')
        print('#############################################################')
    finally:
        print('Results:')
        print('In part01-02:')
        print('You got {0} out of {1} possible points'.format(test_results, total_tests))
        total_global += test_results

    total_tests = 4
    test_results = 0
    print('######################################################')
    print('# Starting tests: (Part02) well_formed               #')
    print('######################################################')

    try:
        res1 = is_well_formed('simple_parentheses1.txt')
        assert type(res1) is bool, 'returned non bool'
        res2 = is_well_formed('simple_parentheses2.txt')
        assert type(res2) is bool, 'returned non bool'
        res3 = is_well_formed('test_parentheses01.txt')
        assert type(res3) is bool, 'returned non bool'
        res4 = is_well_formed('test_parentheses02.txt')
        assert type(res4) is bool, 'returned non bool'
        if res1:
            test_results += 1
        if not res2:
            test_results += 1
        if res3:
            test_results += 1
        if not res4:
            test_results += 1
    except IOError as e:
        print('Error!')
        print('Problems in well_formed')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NotImplementedError:
        print('Error!')
        print('Problems in well_formed')
        print('Not implemented function')
    except AssertionError as e:
        print('Error!')
        print('Problems in well_formed')
        print('Returned non bool')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NameError as e:
        print('Error!')
        print('Problems in well_formed')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except Exception as e:
        print('Error!')
        print('Problems in well_formed')
        print('Unexpected problem')
        print('Check: {0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Congratulations, your code at least run without errors    #')
        print('#############################################################')
    finally:
        print('Results:')
        print('In part02:')
        print('You got {0} out of {1} possible points'.format(test_results, total_tests))
        total_global += test_results

    total_tests = 2
    test_results = 0
    print('######################################################')
    print('# Starting tests: (Part03) search                    #')
    print('######################################################')

    try:
        P1 = EightPuzzle((1, 2, 3, 4, 5, 0, 7, 8, 6))
        res = uniform_cost_search(P1)
        valid_sol, steps = check_solution(res, P1)  # checa solucao
        if valid_sol:
            if len(steps) == 2 and steps[1] == 'DOWN':
                test_results += 1
        P2 = GridWorld(5, 5, (0, 0), (2, 2))
        res2 = uniform_cost_search(P2)
        valid_sol2, steps2 = check_solution(res2, P2)
        if valid_sol2:
            if len(steps2) == 5:
                test_results += 1
    except IOError as e:
        print('Error!')
        print('Problems in uniform_cost_search')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NotImplementedError:
        print('Error!')
        print('Problems in uniform_cost_search')
        print('Not implemented function')
    except AssertionError as e:
        print('Error!')
        print('Problems in uniform_cost_search')
        print('Returned non dictionary')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except NameError as e:
        print('Error!')
        print('Problems in uniform_cost_search')
        print('################################################')
        print('Python error: {0}'.format(e))
        print('################################################')
    except Exception as e:
        print('Error!')
        print('Problems in uniform_cost_search')
        print('Unexpected problem')
        print('Check: {0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Congratulations, your code at least run without errors    #')
        print('#############################################################')
    finally:
        print('Results:')
        print('In part03:')
        print('You got {0} out of {1} possible points'.format(test_results, total_tests))
        total_global += test_results

    print('#############################################################')
    print('# Your final score in this simple tests are:                #')
    print('#############################################################')
    print('   {0} out of {1} possible points: {2:3.1f} grade'.format(total_global,total_tests_global, (total_global/total_tests_global)*10))
    print('#############################################################')
    print('# IMPORTANT: The final tests may check for corner cases     #')
    print('#            that were not tested here. Meaning that this   #')
    print('#            score report is just an example.               #')
    print('#            Your final grade can be much lower than that.  #')
    print('#############################################################')


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    run_tests()
