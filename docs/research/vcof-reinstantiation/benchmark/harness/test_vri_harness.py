from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
HARNESS = Path(__file__).with_name("vri_harness.py")
EPISODES = ROOT / "episodes" / "episodes.toml"


class HarnessSmokeTests(unittest.TestCase):
    def test_episode_pack_validates(self):
        completed = subprocess.run(
            [sys.executable, str(HARNESS), "validate", str(EPISODES)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("episodes=12", completed.stdout)
        self.assertIn("validation=PASS", completed.stdout)

    def test_annotation_template_is_created(self):
        output = ROOT / "harness" / ".test-annotations.csv"
        try:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(HARNESS),
                    "init-annotations",
                    str(EPISODES),
                    str(output),
                    "--models",
                    "model-a,model-b",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(output.exists())
            self.assertEqual(len(output.read_text(encoding="utf-8").splitlines()), 145)
        finally:
            output.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
