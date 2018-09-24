from shrug_lang.errors import WtfError


class BaseOp:
    @staticmethod
    def check_for_undefined(val1, val2):
        """Raise an error with correct message if either value is undefined"""
        if val1[0] is None and val2[0] is None:
            raise ValueError(f'Undefined values {val1[1]} and {val2[1]}')
        if val1[0] is None:
            raise ValueError(f'Undefined values {val1[1]}')
        if val2[0] is None:
            raise ValueError(f'Undefined values {val2[1]}')
        return True

    @staticmethod
    def check_non_numbers(val1, val2, operation_type: str = ''):
        """Raise an error if either value is not an int"""
        if isinstance(val1, str) and isinstance(val2, str):
            raise TypeError(
                f'Unsupported {operation_type} types: string and string')
        if isinstance(val1, str) and isinstance(val2, int):
            raise TypeError(
                f'Unsupported {operation_type} types: str and number')
        if isinstance(val1, int) and isinstance(val2, str):
            raise TypeError(
                f'Unsupported {operation_type} types: number and str')
        return True

    @staticmethod
    def unpack_values(val1, val2):
        """
        Raise an error with correct message if either value is undefined and
        return value part of the tuple
        """
        BaseOp.check_for_undefined(val1, val2)
        val1 = val1[0]
        val2 = val2[0]
        return val1, val2

    @staticmethod
    def check_matching_type(val1, val2, operation: str = ''):
        """Raise an error if types do not match"""
        if type(val1) != type(val2):
            raise TypeError(f'Both values must be of the same type for '
                            f'"{operation}" operation')
        return True


class MathOp(BaseOp):
    """Math operations (mostly) follow python rules"""
    @staticmethod
    def unpack_values(val1, val2):
        val1, val2 = BaseOp.unpack_values(val1, val2)
        if isinstance(val1, bool):
            val1 = int(val1)
        if isinstance(val2, bool):
            val2 = int(val2)
        return val1, val2

    @staticmethod
    def add(val1, val2):
        val1, val2 = MathOp.unpack_values(val1, val2)
        if isinstance(val1, str):
            if isinstance(val2, str):
                return val1 + val2
            if isinstance(val2, int):
                return val1 + str(val2)
            raise WtfError
        if isinstance(val1, int):
            if isinstance(val2, str):
                return str(val1) + val2
            if isinstance(val2, int):
                return val1 + val2
            raise WtfError
        raise WtfError

    @staticmethod
    def subtract(val1, val2):
        val1, val2 = MathOp.unpack_values(val1, val2)
        MathOp.check_non_numbers(val1, val2, 'subtraction')
        return val1 - val2

    @staticmethod
    def multiply(val1, val2):
        val1, val2 = MathOp.unpack_values(val1, val2)
        if isinstance(val1, str) and isinstance(val2, str):
            raise TypeError('Unsupported multiplication types: '
                            'string and string')
        return val1 * val2

    @staticmethod
    def divide(val1, val2):
        val1, val2 = MathOp.unpack_values(val1, val2)
        MathOp.check_non_numbers(val1, val2, 'division')
        return val1 // val2

    @staticmethod
    def modulus(val1, val2):
        val1, val2 = MathOp.unpack_values(val1, val2)
        MathOp.check_non_numbers(val1, val2, 'modulus')
        return val1 % val2


class CompOp(BaseOp):
    """Comparators follow python rules"""
    @staticmethod
    def eq(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        return val1 == val2

    @staticmethod
    def neq(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        return val1 != val2

    @staticmethod
    def gt(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        CompOp.check_matching_type(val1, val2, 'greater than')
        return val1 > val2

    @staticmethod
    def gte(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        CompOp.check_matching_type(val1, val2, 'greater than or equal')
        return val1 >= val2

    @staticmethod
    def lt(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        CompOp.check_matching_type(val1, val2, 'less than')
        return val1 < val2

    @staticmethod
    def lte(val1, val2):
        val1, val2 = CompOp.unpack_values(val1, val2)
        CompOp.check_matching_type(val1, val2, 'less than or equal')
        return val1 <= val2
