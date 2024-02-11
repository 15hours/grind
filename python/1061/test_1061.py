import unittest

from problem_1061 import Solution


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.method = "dsu"
        # self.method = "dfs"

        self.sol = Solution()
        self.method_solution_map = {
            "dsu": self.sol.dsu_approach,
            "dfs": self.sol.dfs_approach,
        }
        self.solution_method = self.method_solution_map[self.method]

    def run_test(self, 
                 data: list[str], 
                 expected_result: str) -> None:

        s1, s2, baseStr = data
        result = self.solution_method(s1, s2, baseStr)
        self.assertEqual(result, expected_result)

    def test_1(self) -> None:
        self.run_test(["parker", "morris", "parser"], "makkek")
    
    def test_2(self) -> None:
        self.run_test(["hello", "world", "hold"], "hdld")
    
    def test_3(self) -> None:
        self.run_test(["leetcode", "programs", "sourcecode"], "aauaaaaada")

    def test_4(self) -> None:
        self.run_test(["gmerjboftfnqseogigpdnlocmmhskigdtednfnjtlcrdpcjkbj",
                       "fnnafafhqkitbcdlkpiloiienikjiikdfcafisejgeldprcmhd",
                       "ezrqfyguivmybqcsvibuvtajdvamcdjpmgcbvieegpyzdcypcx"],
                       "azaaayauavayaaaavaauvaaaavaaaaaaaaaavaaaaayzaayaax")
    
    def test_5(self) -> None:
        self.run_test(["vtjdusfishfhnmkmbavdslnpfnofecqtsvtabgjklevivfmfcc",
                       "fithttlhdltsaenbqbrtlsrpshopleonefraklcssdggdmujom",
                       "kznlrjbtimugpevceziqiuqwduzqmkhtshjjzxtosgtfmkreik"],
                       "azaaaaaaaaaaaaaaazaaaaawaazaaaaaaaaazxaaaaaaaaaaaa")

if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)