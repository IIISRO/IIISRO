import unittest
from main import *

class Test(unittest.TestCase):


    def test_cubic(self):
        except_result = 343
        actual_result = cubic(7)
        self.assertEqual(except_result, actual_result)
    
    def test_achecker(self):
        except_result = ['alma', 'dağ', 'proqram']
        actual_result = achecker(['alma', 'su', 'dağ', 'meşə', 'stul', 'proqram'])
        self.assertEqual(except_result, actual_result)
        
    def test_get_person(self):
        person = Person('koroglu','mirzeyev')
        except_result = 'Koroglu Mirzeyev'
        actual_result = person.get_fullname()
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(except_result, actual_result)
        
    def test_capta(self):
        except_result = 'Koroglu'
        actual_result = capta('koroglu')
        self.assertEqual(except_result, actual_result)

    def test_wallet1(self):
        except_result = 0
        actual_result = Wallet.balance
        self.assertEqual(except_result, actual_result)
        
    def test_wallet2(self):
        wallet = Wallet(120)
        wallet.spend_cash(30)
        except_result = 90
        actual_result = wallet.balance
        self.assertEqual(except_result, actual_result)

    def test_wallet3(self):
        wallet = Wallet(10)
        wallet.add_cash(70)
        except_result = 80
        actual_result = wallet.balance
        self.assertEqual(except_result, actual_result)
    
    def test_wallet4(self):
        wallet = Wallet(60)
        self.assertNotEqual(InsufficientAmount, wallet.spend_cash(10) )

if __name__ == '__main__':
    unittest.main()
    