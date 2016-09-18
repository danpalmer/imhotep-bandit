import os.path
from unittest import TestCase

from imhotep.app import run
from imhotep_bandit.plugin import Bandit


class BanditTest(TestCase):
    def test_reports_error(self):
        test_dir = os.path.dirname(__file__)
        plugin = Bandit(run)
        output = plugin.invoke(test_dir, set(), set())

        self.assertEqual(output, {
            '%s/insecure_file.py' % test_dir: {
                '3': [
                    "**B501**: Requests call with verify=False "
                    "disabling SSL certificate checks, security "
                    "issue.\nSeverity: HIGH, Confidence: HIGH",
                ],
            },
        })
