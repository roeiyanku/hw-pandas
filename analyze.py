import pandas

codes_for_questions = pandas.read_csv("./codes_for_questions.csv")
codes_for_answers = pandas.read_csv("./codes_for_answers.csv")
list_of_answers = pandas.read_csv("./list_of_answers.csv")


def support_in_one_party_elections(party:str)->int:
    pass
    # Put your code here


def support_in_multi_party_elections(party:str)->int:
    pass
    # Put your code here


def parties_with_different_relative_order()->tuple:
    pass
    # Put your code here


if __name__ == '__main__':
    party = input()
    if party == "parties_with_different_relative_order":
        print(parties_with_different_relative_order())
    else:
        print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
