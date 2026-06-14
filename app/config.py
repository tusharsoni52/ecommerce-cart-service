import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Cart Service")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3308))
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "cart_db")
    MYSQL_USER = os.getenv("MYSQL_USER", "cart_user")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "cart_password")

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://"
            f"{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}"
            f"/{self.MYSQL_DATABASE}"
        )

    PRODUCT_SERVICE_URL = os.getenv( "PRODUCT_SERVICE_URL", "http://localhost:8000" )

    ORDER_SERVICE_URL = os.getenv( "ORDER_SERVICE_URL", "http://localhost:8002" )


settings = Settings()