class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            # Add configuration settings here
            cls._instance.some_setting = "value"
        return cls._instance

