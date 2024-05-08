import pytest

from problem_269 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "kahn" : sol.kahn_approach,
        "dfs" : sol.dfs_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution(["wrt","wrf","er","ett","rftt"]) == "wertf"

def test_2(solution):
    assert solution(["z","x"]) == "zx"

def test_3(solution):
    assert solution(["z","x","z"]) == ""

def test_4(solution):
    assert solution(["z","z"]) == "z"

def test_5(solution):
    assert solution(["ab","adc"]) == "abdc" or "acbd" or "cabd" or "bdac"

def test_6(solution):
    assert solution(["abc","ab"]) == ""

def test_7(solution):
    assert solution(["z","x","a","zb","zx"]) == ""

def test_8(solution):
    assert solution(["ac","ab","zc","zb"]) == "acbz" or "azcb"

def test_9(solution):
    assert solution(["ac","ab","b"]) == "acb" or "cab"

def test_10(solution):
    assert solution(["wnlb"]) == "blnw" or "wnlb" or "lnwb"

def test_11(solution):
    assert solution(["aba"]) == "ab" or "ba"