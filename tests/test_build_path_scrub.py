from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_sites import strip_npm_metadata_profiles as strip


class NpmMetadataProfileTest(unittest.TestCase):
    def test_escaped_args_and_where(self):
        src = (
            r'iU={_args:[["elliptic@6.5.4","C:\\Users\\jdoe\\Projects\\rollup"]],'
            r'_from:"elliptic@6.5.4",_spec:"6.5.4",'
            r'_where:"C:\\Users\\jdoe\\Projects\\rollup",author:{}}'
        )
        self.assertEqual(
            strip(src),
            r'iU={_args:[["elliptic@6.5.4","<user-home>\\Projects\\rollup"]],'
            r'_from:"elliptic@6.5.4",_spec:"6.5.4",'
            r'_where:"<user-home>\\Projects\\rollup",author:{}}',
        )

    def test_plain_slashes_and_space_in_name(self):
        self.assertEqual(
            strip('_spec:"1.0.0",_where:"C:/Users/Jane Doe/x"'),
            '_spec:"1.0.0",_where:"<user-home>/x"',
        )
        self.assertEqual(
            strip(r'_args:[["a@1","C:\\Users\\Jane Doe\\x"]]'),
            r'_args:[["a@1","<user-home>\\x"]]',
        )

    def test_unrelated_code_unchanged(self):
        for src in (
            'const r={C:/Users/g};',
            'p="C:/Users/Public"',
            'else_where:"C:/Users/Public/share"',
            '_where:"C:/Users/Public/share"',
            'x_spec:"1",_where:"C:/Users/Public/share"',
            '_spec:"1",_where:"/srv/app"',
            'Users',
        ):
            self.assertEqual(strip(src), src)


if __name__ == "__main__":
    unittest.main()
