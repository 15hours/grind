import pytest

from problem_721 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "dfs" : sol.dfs_approach,
        "dsu" : sol.dsu_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert sorted(
            solution([["John","johnsmith@mail.com","john_newyork@mail.com"],
                      ["John","johnsmith@mail.com","john00@mail.com"],
                      ["Mary","mary@mail.com"],
                      ["John","johnnybravo@mail.com"]])) \
            == sorted([["John","john00@mail.com","john_newyork@mail.com",
                        "johnsmith@mail.com"],
                       ["Mary","mary@mail.com"],
                       ["John","johnnybravo@mail.com"]])

def test_2(solution):
    assert sorted(solution([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                     ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                     ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                     ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                     ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]])) \
            == sorted([["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
                       ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                       ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                       ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                       ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])