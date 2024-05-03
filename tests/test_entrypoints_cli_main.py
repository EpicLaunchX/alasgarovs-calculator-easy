from unittest.mock import patch

from src.pytemplate.entrypoints.cli.main import main


class TestCalcFunctions:
    def test_add_action(self, capsys):
        with patch("builtins.input", side_effect=["45", "35", "add"]):
            main()
            captured = capsys.readouterr()
            assert "Result: 80" in captured.out

    def test_subtract_action(self, capsys):
        with patch("builtins.input", side_effect=["45", "35", "subtract"]):
            main()
            captured = capsys.readouterr()
            assert "Result: 10" in captured.out

    def test_multiply_action(self, capsys):
        with patch("builtins.input", side_effect=["4", "5", "multiply"]):
            main()
            captured = capsys.readouterr()
            assert "Result: 20" in captured.out

    def test_divide_action(self, capsys):
        with patch("builtins.input", side_effect=["20", "5", "divide"]):
            main()
            captured = capsys.readouterr()
            assert "Result: 4.0" in captured.out

    def test_invalid_action(self, capsys):
        with patch("builtins.input", side_effect=["20", "5", "invalid"]):
            main()
            captured = capsys.readouterr()
            assert "Invalid action" in captured.out
