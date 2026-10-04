from doctor import __version__
from doctor.cli import main


def test_version():
    assert __version__ == "0.1.0"


def test_main_prints_greeting(capsys):
    assert main([]) == 0
    assert "Hello from doctor!" in capsys.readouterr().out
