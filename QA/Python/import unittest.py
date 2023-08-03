import unittest
import random
class Calculator(unittest.TestCase):
    first_random_int = random.randint(0, 100000)
    second_random_int = random.randint(0, 100000)
    def test_calculate_all_actions(self):
        self.assertEqual(self.calculate('+', 2, 2), 4)
        self.assertEqual(self.calculate('-', 2, 2), 0)
        self.assertEqual(self.calculate('*', 2, 2), 4)
        self.assertEqual(self.calculate('/', 2, 2), 1)
    def test_not_string_user_action(self):
        self.assertEqual(self.calculate('b', 2, 2), 'not expect argument')
    def test_random_sum(self):
        int_sum = self.first_random_int + self.second_random_int
        self.assertEqual(self.calculate('+', self.first_random_int, self.second_random_int), int_sum)
    def test_random_div(self):
        int_div = self.first_random_int - self.second_random_int
        self.assertEqual(self.calculate('-', self.first_random_int, self.second_random_int), int_div)  
    def test_random_multi(self):
        int_multi = self.first_random_int * self.second_random_int
        self.assertEqual(self.calculate('*', self.first_random_int, self.second_random_int), int_multi)       
    def calculate(self, user_action, first_number, second_number):
        if user_action == "+":
            return (first_number + second_number)
        elif user_action == "-":
            return (first_number - second_number)
        elif user_action == "*":
            return (first_number * second_number)
        elif user_action == "/":
            # if second_number == 0:
            while second_number == 0:
                print("Input number B. NumberB MUST be NOT 0")
                print("Input number B")
                second_number = int(input())
            return (first_number / second_number)
        else:
            return "not expect argument"
if __name__ == '__main__':
    unittest.main()