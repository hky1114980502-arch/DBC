from docter import __version__
from docter.cli import main


def test_version():
    assert __version__ == "0.1.0"


def test_main_prints_greeting(capsys):
    assert main([]) == 0
    assert "Hello from docter!" in capsys.readouterr().out
