import unittest
from agents.script_generator import generate_script
from agents.internet_agent import search_internet
from agents.trends_analyzer import analyze_trends

class TestAgents(unittest.TestCase):
    def test_script_generation(self):
        topic = "AI in Education"
        result = generate_script(topic)
        self.assertIn("Introduction", result)
        self.assertIn("Main Content", result)
        self.assertIn("Conclusion", result)

    def test_internet_search(self):
        query = "Latest AI trends 2025"
        result = search_internet(query)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_trend_analysis(self):
        keyword = "AI"
        result = analyze_trends(keyword)
        self.assertFalse(result.empty)
        self.assertIn('AI', result.columns)

if __name__ == '__main__':
    unittest.main()
