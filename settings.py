from envparse import env

env.read_envfile(".env")

DB_USER = env.str("DB_USER")
DB_NAME = env.str("DB_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")


DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@localhost:5434/{DB_NAME}"
)
