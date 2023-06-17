import unittest

from minesweeper import Sentence, MinesweeperAI

class TestSentence(unittest.TestCase):

    def test_known_mines(self):
        test_sentence = Sentence({(0,0)},1)        
        self.assertEqual(test_sentence.known_mines(), {(0,0)})

        test_sentence = Sentence({(0,0), (1,1)},2)        
        self.assertEqual(test_sentence.known_mines(), {(1,1), (0,0)})

        test_sentence = Sentence({(0,0), (1,1)},1)        
        self.assertEqual(test_sentence.known_mines(), set())

    def test_known_safes(self):
        test_sentence = Sentence({(0,0)},0)        
        self.assertEqual(test_sentence.known_safes(), {(0,0)})

        test_sentence = Sentence({(0,0), (1,1)},0)        
        self.assertEqual(test_sentence.known_safes(), {(1,1), (0,0)})

        test_sentence = Sentence({(0,0), (1,1)},1)        
        self.assertEqual(test_sentence.known_safes(), set())

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

class TestMineSweeperAI(unittest.TestCase):
    def test_add_knowledge(self):
        test_ai = MinesweeperAI()
        test_ai.mark_mine((0,1))
        test_ai.mark_safe((1,0))
        test_ai.add_knowledge((1,1), 2)
        self.assertTrue((1,1) in test_ai.moves_made)
        self.assertTrue((1,1) in test_ai.safes)

        implied_sentence = Sentence({(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2)}, 2)
        self.assertEqual(test_ai.knowledge[0], implied_sentence)

    def test_normalise_knowledge(self):
        test_ai = MinesweeperAI()

        super_sentence = Sentence({(0,1), (0,0), (1,0), (1,1)}, 1)
        test_ai.knowledge.append(super_sentence)
        sub_sentence = Sentence({(0,1), (0,0)}, 1)
        test_ai.knowledge.append(sub_sentence)

        result_sentence = Sentence({(1,0), (1,1)}, 0)
        test_ai.normalise_knowledge()

        self.assertEqual(test_ai.knowledge[0], result_sentence)

    def test_infer_safes_or_mines(self):
        test_ai = MinesweeperAI()

        mine_sentence = Sentence({(0,0), (0,1)}, 2)
        safe_sentence = Sentence({(1,0), (1,1)}, 0)
        test_ai.knowledge.append(mine_sentence)
        test_ai.knowledge.append(safe_sentence)

        test_ai.infer_safes_or_mines()
        
        self.assertTrue({(0,0), (0,1)} <= test_ai.mines)
        self.assertTrue({(1,0), (1,1)} <= test_ai.safes)


    def test_make_safe_move(self):
        test_ai = MinesweeperAI()
        test_ai.mark_safe((1,0))
        test_ai.mark_safe((0,0))
        test_ai.moves_made.add((0,0))

        self.assertEqual(test_ai.make_safe_move(), (1,0))

        test_ai.moves_made.add((1,0))
        self.assertEqual(test_ai.make_safe_move(), None)
            


if __name__ == '__main__':
    unittest.main()