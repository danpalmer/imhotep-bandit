import re
import json
import os.path
import textwrap
from collections import defaultdict

from imhotep.tools import Tool


class Bandit(Tool):
    def invoke(self, dirname, filenames, linter_configs):
        retval = defaultdict(lambda: defaultdict(list))

        cmd = 'bandit -r %s -f json' % dirname
        output = self.executor(cmd)
        data = json.loads(output)

        for result in data['results']:
            line = result['line_number']
            message = self.format_message(result)
            retval[result['filename']][line].append(message)

        return self.to_dict(retval)

    def format_message(self, report):
        return textwrap.dedent("""
            **{test_id}**: {issue_text}
            Severity: {issue_severity}, Confidence: {issue_confidence}
        """.format(**report))

    def to_dict(self, d):
        if not isinstance(d, dict):
            return d

        return {
            k: self.to_dict(v) for k, v in d.iteritems()
        }
