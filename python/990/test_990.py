import unittest

from problem_990 import Solution


class Test(unittest.TestCase):

    def setUp(self) -> None:
        # self.method = "dsu"
        self.method = "dfs"

        self.sol = Solution()
        self.method_solution_map = {
            "dsu": self.sol.dsu_approach,
            "dfs": self.sol.dfs_approach
        }
        self.solution_method = self.method_solution_map[self.method]


    def run_test(self, 
                 equations: list[str], 
                 expected_result: bool
                 ) -> None:
                 
        result = self.solution_method(equations)
        self.assertEqual(result, expected_result)

    def test_1(self) -> None:
        self.run_test(["a==b","b!=a"], False)

    def test_2(self) -> None:
        self.run_test(["b==a","a==b"], True)

    def test_3(self) -> None:
        self.run_test(["a==b","b!=c","c==a"], False)

    def test_4(self) -> None:
        self.run_test(["f==g","d!=a","d==f",
                       "i!=i","j==a","g==i",
                       "h!=h","k==f","d==g",
                       "k==k"], False)
    
    def test_5(self) -> None:
        self.run_test(["c==c","b==d","x!=z"], True)

    def test_6(self) -> None:
        self.run_test(["a!=b","b!=c","c!=a"], True)

    def test_7(self) -> None:
        self.run_test(["b!=c","a==b","e!=d","b!=f","a!=b"], False)

    def test_8(self) -> None:
        self.run_test(["c==c","f!=a","f==b","b==c"], True)
    
    def test_9(self) -> None:
        self.run_test(["a==b","c==d","a==c","a!=d"], False)

if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)