import pytest

def admin_command(command, sudo=True):
    """
    Constrói um comando de administrador com ou sem sudo.

    Parâmetros:
        command (list): O comando a ser executado.
        sudo (bool): Se deve incluir 'sudo' no comando.

    Retorna:
        list: O comando com 'sudo' se solicitado.

    Levanta:
        TypeError: Se o parâmetro command não for uma lista.
    """
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    
    if sudo:
        return ["sudo"] + command
    return command

class TestAdminCommand:
    """Testes para a função admin_command."""

    def get_command(self):
        """Retorna um comando padrão para os testes."""
        return ["ps", "aux"]

    def test_no_sudo(self):
        """Testa o comando sem sudo."""
        result = admin_command(self.get_command(), sudo=False)
        assert result == self.get_command()

    def test_sudo(self):
        """Testa o comando com sudo."""
        result = admin_command(self.get_command(), sudo=True)
        expected = ["sudo"] + self.get_command()
        assert result == expected

    def test_non_list_commands(self):
        """Verifica se um TypeError é levantado para comandos não-lista."""
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"
