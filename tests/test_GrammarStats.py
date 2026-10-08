from lib.GrammarStats import *
import pytest
#When one uncapitazlised word is entered with punctuation to check
#check returns false
def test_check_returns_false_for_one_uncap_word():
    grammar = GrammarStats()
    result = grammar.check("hello.")
    assert result == False

#When one word is entered to check without punctuation
#check returns false
def test_check_returns_false_one_cap_word_no_punctuation():
    grammar = GrammarStats()
    result = grammar.check("Hello")
    assert result == False

#When a correctly capitalised and punctuated word is entered to check
#check returns true
def test_check_returns_true_cap_word_with_punctuation():
    grammar = GrammarStats()
    result = grammar.check("Hello.")
    assert result == True

#When a mixed case word, not starting with a capital, is entered to check
#check returns false
def test_check_returns_false_mixed_case_word_starting_uncap():
    grammar = GrammarStats()
    result = grammar.check("hELLo.")
    assert result == False

#When a string containing punctuation but not at the end is entered to check
#check returns false
def test_check_returns_false_contains_fullstop_but_not_last():
    grammar = GrammarStats()
    result = grammar.check("Box. Your Stuff. Out the front door. Parking lot. Car. Goodbye")
    assert result == False

#When a valid sentence string ending in an exclamation mark is entered
#check returns true
def test_check_accepts_exclamation_as_valid():
    grammar = GrammarStats()
    result = grammar.check("Stress doesn't ship lemonade!")
    assert result == True

#When a valid sentence string ending in an question mark is entered
#check returns true
def test_check_returns_true_contains_comma_ends_question_mark():
    grammar = GrammarStats()
    result = grammar.check("I don't want your damn lemons, what am I supposed to do with these?")
    assert result == True

#When an otherwise valid sentence string ending in an colon is entered
#check returns false
def test_check_returns_false_ends_colon():
    grammar = GrammarStats()
    result = grammar.check("Good news is we've got a much better test for you:")
    assert result == False

#When percentage_good is called after no checks have been run
#an exception is raised about no checks having been run
def test_percentage_good_raises_on_no_checks():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.percentage_good()
    error_message = str(e.value)
    assert error_message == "No checks have been run!"

#When percentage_good is called after one valid check
#percentage_good returns 100
def test_percentage_good_returns_100_after_one_valid_check():
    grammar = GrammarStats()
    grammar.check("Stress doesnt ship lemonade!")
    result = grammar.percentage_good()
    assert result == 100

#When percentage_good is called after one falsy check
#percentage_good returns 0
def test_percentage_good_returns_0_after_one_false_check():
    grammar = GrammarStats()
    grammar.check("fighing an army of mantis men.")
    result = grammar.percentage_good()
    assert result == 0

#When a percentage_good is called after 7 out of 10 valid checks
#percentage_good returns 70
def test_percentage_good_returns_70_for_7_out_of_10_valid():
    grammar = GrammarStats()
    grammar.check("Since making test participation mandatory for all employees,") #fail 1
    grammar.check("the quality of out test subjects has risen dramatically.") #fail 2
    grammar.check("Employee retention, however has not.")
    grammar.check("As a result, you may have heard we're gonna phase out human testing")
    grammar.check("There's still a few things to wrap up though.")
    grammar.check("First up, conversion gel.")
    grammar.check("The bean counters told me we literally could not afford to buy seven dollars worth of moon rocks, much less seventy million")
    grammar.check("Bought 'em anyway.")
    grammar.check("Ground 'em up, mixed em into a gel.")
    grammar.check("And guess what? Ground up moon rocks are pure poision")#fail 3

