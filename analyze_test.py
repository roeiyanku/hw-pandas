import re

import pytest
from analyze import support_in_one_party_elections, support_in_multi_party_elections, parties_with_different_relative_order
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(party:str):
    if party == "parties_with_different_relative_order":
         return f"{parties_with_different_relative_order()}"
    else:
         return f"{support_in_one_party_elections(party)} {support_in_multi_party_elections(party)}"

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    expected = testcase["output"]
    if expected.startswith("/"):  # expected output given as a regex, e.g. /.*/i
        pattern, _, flags = expected[1:].rpartition("/")
        assert re.fullmatch(pattern, actual_output, re.IGNORECASE if "i" in flags else 0), \
            f"Expected match for {expected}, got {actual_output}"
    else:
        assert actual_output == expected, f"Expected {expected}, got {actual_output}"


def test_new_cases():
    assert support_in_one_party_elections("שס") == 13
    assert support_in_multi_party_elections("שס") == 39
    result = parties_with_different_relative_order()
    assert result is None or (
        support_in_one_party_elections(result[0]) > support_in_one_party_elections(result[1])
        and support_in_multi_party_elections(result[0]) < support_in_multi_party_elections(result[1])
    )
