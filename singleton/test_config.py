import unittest
from unittest.mock import patch
from singleton.config import AppConfig  # Replace 'your_module' with the actual module name

class TestAppConfigSingleton(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test
        AppConfig._instance = None
        
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
        self.assertFalse(config2.debug)

    def test_default_environment(self):
        # Reset singleton for this test
        AppConfig._instance = None
        
        config = AppConfig()  # No env parameter provided
        self.assertEqual(config.environment, 'dev')
        self.assertTrue(config.debug)

    def test_singleton_property_integrity(self):
        config = AppConfig(env='test')
        config.environment = 'staging'

        another_config = AppConfig()

        # Check if changes reflect across all references
        self.assertEqual(another_config.environment, 'staging')
        
    def test_environment_validation(self):
        # Test with invalid environment
        config = AppConfig(env='invalid_env')
        
        # Should default to development database
        self.assertEqual(config.database_url, "sqlite:///dev.db")
        
    @patch('your_module.AppConfig')
    def test_mocking_singleton(self, mock_config):
        # Ensure the singleton can be properly mocked in other tests
        mock_config.return_value.environment = 'mocked'
        mock_config.return_value.debug = False
        
        config = AppConfig()
        self.assertEqual(config.environment, 'mocked')
        self.assertFalse(config.debug)

if __name__ == '__main__':
    unittest.main()