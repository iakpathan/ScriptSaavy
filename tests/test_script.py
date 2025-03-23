import unittest
from agents.script_generator import generate_script

class TestScript(unittest.TestCase):
    def test_script_not_empty(self):
        topic = "Impact of politics on society"
        result = generate_script(topic)
        self.assertGreater(len(result), 0)

    def test_script_content(self):
        topic = "Impact of politics on society"
        result = generate_script(topic)
        self.assertIn("Introduction", result)
        self.assertIn("Main Content", result)
        self.assertIn("Conclusion", result)

if __name__ == '__main__':
    unittest.main()
 
