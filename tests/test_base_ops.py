import unittest

from shrug_lang.operators import BaseOp


class TestBaseOperations(unittest.TestCase):
    def test_operation_check_undefined(self):
        self.assertTrue(BaseOp.check_for_undefined((1, 'a'), (2, 'b')))
        self.assertRaises(ValueError, BaseOp.check_for_undefined,
                          (None, None), (2, 'b'))
        self.assertRaises(ValueError, BaseOp.check_for_undefined,
                          (1, 'a'), (None, None))
        self.assertRaises(ValueError, BaseOp.check_for_undefined,
                          (None, None), (None, None))

    def test_check_non_numbers(self):
        self.assertTrue(BaseOp.check_non_numbers(1, 2))
        self.assertRaises(TypeError, BaseOp.check_non_numbers, 'a', 1)
        self.assertRaises(TypeError, BaseOp.check_non_numbers, 2, '1')
        self.assertRaises(TypeError, BaseOp.check_non_numbers, '2', '4')

    def test_check_matching_types(self):
        class A:
            pass

        class B(A):
            pass

        self.assertTrue(BaseOp.check_matching_type(A(), A()))
        self.assertTrue(BaseOp.check_matching_type(1, 2))
        self.assertTrue(BaseOp.check_matching_type('a', 'bc'))

        self.assertRaises(TypeError, BaseOp.check_matching_type, 'a', 1)
        self.assertRaises(TypeError, BaseOp.check_matching_type, 2, '1')
        self.assertRaises(TypeError, BaseOp.check_matching_type, A(), B())


if __name__ == '__main__':
    unittest.main()
