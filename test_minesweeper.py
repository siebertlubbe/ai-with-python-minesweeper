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

    def test_mark_mine(self):
        test_sentence  = Sentence({(0,0),(1,1)},1)
        test_sentence.mark_mine((0,0))
        self.assertEqual(test_sentence.cells, {(1,1)})
        self.assertEqual(test_sentence.count, 0)

        test_sentence  = Sentence({(0,0),(1,1)},1)
        test_sentence.mark_mine((2,2))
        self.assertEqual(test_sentence.cells, {(0,0),(1,1)})
        self.assertEqual(test_sentence.count, 1)

    def test_mark_safe(self):
        test_sentence  = Sentence({(0,0),(1,1)},1)
        test_sentence.mark_safe((0,0))
        self.assertEqual(test_sentence.cells, {(1,1)})
        self.assertEqual(test_sentence.count, 1)

        test_sentence  = Sentence({(0,0),(1,1)},1)
        test_sentence.mark_safe((2,2))
        self.assertEqual(test_sentence.cells, {(0,0),(1,1)})
        self.assertEqual(test_sentence.count, 1)

if __name__ == '__main__':
    unittest.main()