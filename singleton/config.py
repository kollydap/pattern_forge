class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance.init_config(*args, **kwargs)
        return cls._instance

    def init_config(self, env="dev"):
        self.environment = env
        self.database_url = "sqlite:///dev.db" if env == "dev" else "postgres://..."


# Usage
config1 = AppConfig(env="prod")
config2 = AppConfig()

print(config1 is config2)  # True
print(config2.environment)  # 'prod'
