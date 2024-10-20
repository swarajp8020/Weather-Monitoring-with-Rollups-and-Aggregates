import unittest
from weather import kelvin_to_celsius

class TestWeatherFunctions(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85, places=2)

    def test_process_weather_data(self):
        # Add mock data and test processing
        pass

if __name__ == '__main__':
    unittest.main()
