import unittest

def is_valid(code):
    d = {
        "[":"]",
        "{":"}",
        "(":")",
    }
    
    openers_stack = []
    
    for bracket in code:
        
        if bracket in d:
            
            openers_stack.append(bracket)
            
        elif bracket in d.values():
            
            if not openers_stack:
                
                return False
                
            else:
                
                if  bracket != d[openers_stack.pop()]:
                    
                    return False
                
                else:

                    continue
            
        
    return openers_stack == []


class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)