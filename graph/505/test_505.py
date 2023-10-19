import pytest

from problem_505 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "dfs": sol.dfs_approach,
        "bfs": sol.bfs_approach,
        "dijkstra": sol.dijkstra_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    maze =  [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    dest =  [4,4]
    
    assert solution(maze, start, dest) == 12


def test_2(solution):
    maze =  [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    dest =  [3,2]
    
    assert solution(maze, start, dest) == -1


def test_3(solution):
    maze =  [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    start = [4,3]
    dest =  [0,1]       
    
    assert solution(maze, start, dest) == -1
