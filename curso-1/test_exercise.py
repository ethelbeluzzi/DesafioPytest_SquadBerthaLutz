import unittest

def str_to_bool(value):
    """
    Converte uma string em um valor booleano.
    Aceita algumas variações de 'sim' e 'não' como entrada.
    
    Parâmetros:
        value (str): A string a ser convertida.

    Retorna:
        bool: True ou False conforme o valor fornecido.

    Levanta:
        TypeError: Se o valor não for uma string.
        ValueError: Se o valor não puder ser interpretado como booleano.
    """
    if not isinstance(value, str):
        raise TypeError(f"'{value}' must be of type 'str'")

    value = value.strip().lower()
    true_values = {'y', 'yes', 'true', '1'}
    false_values = {'n', 'no', 'false', '0'}

    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError(f"'{value}' is not a valid boolean string")

class TestStrToBool(unittest.TestCase):
    """Testa a função str_to_bool."""

    def test_true_values(self):
        for val in ['y', 'Y', 'yes', 'Yes', 'TRUE', '1']:
            with self.subTest(val=val):
                self.assertTrue(str_to_bool(val))

    def test_false_values(self):
        for val in ['n', 'N', 'no', 'No', 'FALSE', '0']:
            with self.subTest(val=val):
                self.assertFalse(str_to_bool(val))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            str_to_bool(1)

    def test_unexpected_value(self):
        with self.assertRaises(ValueError):
            str_to_bool('maybe')

if __name__ == '__main__':
    unittest.main()
