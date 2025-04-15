class AppConfig:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, env="dev"):
        if not self._initialized:
            self._initialized = True
            self.environment = env
            
            # Map environments to database URLs
            db_configs = {
                "dev": "sqlite:///dev.db",
                "test": "sqlite:///test.db",
                "staging": "postgres://user:pass@staging-host:5432/db",
                "prod": "postgres://user:pass@production-host:5432/db"
            }
            
            # Set database URL based on environment
            self.database_url = db_configs.get(env, db_configs["dev"])
            
            # Other configuration properties
            self.debug = env in ["dev", "test"]
            self.log_level = "DEBUG" if self.debug else "INFO"
    
    def __repr__(self):
        return f"AppConfig(environment='{self.environment}', debug={self.debug})"


# Usage
config1 = AppConfig(env="prod")
config2 = AppConfig()

print(config1 is config2)  # True
print(config2.environment)  # 'prod'