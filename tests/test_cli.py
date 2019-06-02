# -*- coding: utf-8 -*-
from click.testing import CliRunner

from route53dyn.cli import main


def test_main_returns_correct_output():
    runner = CliRunner()
    result = runner.invoke(main)
    assert ('Replace this message by putting '
            'your code into flask_scenegen.cli.main') in result.output
