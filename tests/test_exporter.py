import unittest
import os
from utils.exporter import export_script

class TestExporter(unittest.TestCase):
    def test_export_pdf(self):
        script = "This is a test script."
        path = export_script(script, 'pdf')
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_export_txt(self):
        script = "This is a test script."
        path = export_script(script, 'txt')
        self.assertTrue(os.path.exists(path))
        os.remove(path)

if __name__ == '__main__':
    unittest.main()

