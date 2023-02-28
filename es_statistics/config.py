from dotenv import load_dotenv
import os


load_dotenv()


class ElastiscsearchConfig:
    # elasticsearch 관련 설정
    ELASTCSEARCH_HOST: str = os.getenv("ELASTCSEARCH_HOST")
    ELASTCSEARCH_PORT: int = os.getenv("ELASTCSEARCH_PORT", 9200)
    ES_USER_ID: str = os.getenv("ES_USER_ID")
    ES_USER_PW: str = os.getenv("ES_USER_PW")
