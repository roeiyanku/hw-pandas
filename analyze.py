import pandas

codes_for_questions = pandas.read_csv("./codes_for_questions.csv")
codes_for_answers = pandas.read_csv("./codes_for_answers.csv")
list_of_answers = pandas.read_csv("./list_of_answers.csv")


def support_in_one_party_elections(party:str)->int:
    q2_answers = codes_for_answers.loc[codes_for_answers["Value"] == "Q2"]
    code = q2_answers.loc[q2_answers["Label"].str.split(" - ").str[0] == party, "Code"].item()
    return int((list_of_answers["Q2"] == code).sum())


def support_in_multi_party_elections(party:str)->int:
    q3_questions = codes_for_questions.loc[codes_for_questions["Variable"].str.startswith("Q3_")]
    column = q3_questions.loc[q3_questions["Label"].str.split(" - ").str[0] == party, "Variable"].item()
    return int(list_of_answers[column].sum())


def parties_with_different_relative_order()->tuple:
    q2_answers = codes_for_answers.loc[codes_for_answers["Value"] == "Q2"]
    q3_questions = codes_for_questions.loc[codes_for_questions["Variable"].str.startswith("Q3_")]
    parties = q3_questions["Label"].str.split(" - ").str[0]
    parties = parties[parties.isin(q2_answers["Label"].str.split(" - ").str[0])]
    for party_a in parties:
        for party_b in parties:
            if (support_in_one_party_elections(party_a) > support_in_one_party_elections(party_b)
                    and support_in_multi_party_elections(party_a) < support_in_multi_party_elections(party_b)):
                return party_a, party_b
    return None


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    # Use this code for testing via console input-output:
    # party = input()
    # if party == "parties_with_different_relative_order":
    #     print(parties_with_different_relative_order())
    # else:
    #     print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
