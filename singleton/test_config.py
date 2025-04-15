import unittest
from your_module import AppConfig  # Replace 'your_module' with the actual module name

class TestAppConfigSingleton(unittest.TestCase):

    def test_singleton_instance(self):
        config1 = AppConfig(env='prod')
        config2 = AppConfig()

        # Assert both variables point to the same instance
        self.assertIs(config1, config2)

    def test_config_persistence(self):
        config1 = AppConfig(env='prod')
        config2 = AppConfig()

        # Even though config2 wasn't initialized with env='prod', it should retain config1's settings
        self.assertEqual(config2.environment, 'prod')

    def test_singleton_property_integrity(self):
        config = AppConfig(env='test')
        config.environment = 'staging'

        another_config = AppConfig()

        # Check if changes reflect across all references
        self.assertEqual(another_config.environment, 'staging')

if __name__ == '__main__':
    unittest.main()
