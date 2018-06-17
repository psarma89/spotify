import unittest
import spotify.questions

class TestQuestions(unittest.TestCase):

    def question1(self):
        self.assertEqual(questions.question1.sort_by_string("weather", "therapyw"), "theeraw")
        self.assertEqual(question1.sort_by_string("good", "odg"), "oodg")

    def question2(self):
        self.assertEqual(question2.decode_string("4[ab]"), "abababab")
        self.assertEqual(question2.decode_string("2[b3[a]]"), "baaabaaa")

    def question3(self):
        self.assertEqual(question3.change_possibilities(4, [1,2,3]), 4)
        self.assertEqual(question3.change_possibilities(2, [1,2]), 2)

if __name__ == '__main__':
    unittest.main()
