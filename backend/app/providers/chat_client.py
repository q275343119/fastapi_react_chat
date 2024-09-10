from openai import OpenAI

from config.chat import settings

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=settings.OPENAI_KEY,
    base_url=settings.OPENAI_BASE_URL
)

