import unittest

from minesweeper import Sentence, MinesweeperAI

class TestSentence(unittest.TestCase):

    def test_known_mines(self):
        test_sentence = Sentence({(0,0)},1)        
        self.assertEqual(test_sentence.known_mines(), {(0,0)})

        test_sentence = Sentence({(0,0), (1,1)},2)        
        self.assertEqual(test_sentence.known_mines(), {(1,1), (0,0)})

        test_sentence = Sentence({(0,0), (1,1)},1)        
        self.assertEqual(test_sentence.known_mines(), {})

    def test_known_safes(self):
        test_sentence = Sentence({(0,0)},0)        
        self.assertEqual(test_sentence.known_safes(), {(0,0)})

        test_sentence = Sentence({(0,0), (1,1)},0)        
        self.assertEqual(test_sentence.known_safes(), {(1,1), (0,0)})

        test_sentence = Sentence({(0,0), (1,1)},1)        
        self.assertEqual(test_sentence.known_safes(), {})

if __name__ == '__main__':
    unittest.main()