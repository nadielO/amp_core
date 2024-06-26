from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://neondb_owner:HVIvQPAl6Ub7@ep-aged-butterfly-a50mokgv.us-east-2.aws.neon.tech/neondb?sslmode=require"  # Provide the PostgreSQL connection URL
    SECRET_KEY: SecretStr = "YOUR_SECRET_KEY_HERE"  # INPUT_REQUIRED {Provide a secure secret key for JWT operations}

    class Config:
        env_file = ".env"

settings = Settings()