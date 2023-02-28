from elasticsearch import Elasticsearch, AsyncElasticsearch
from es_statistics.config import ElastiscsearchConfig


class ConenctionEs:
    def __init__(self):
        self.host: str = ElastiscsearchConfig.ELASTCSEARCH_HOST  # type: ignore
        self.login: str = ElastiscsearchConfig.ES_USER_ID  # type: ignore
        self.password: str = ElastiscsearchConfig.ES_USER_PW
        self.port: str = ElastiscsearchConfig.ELASTCSEARCH_PORT

    def get_conn(self):
        """
        Elasticsearch_hook" 인스턴스를 통해 elasticsearch와 연결
        """
        self.es = Elasticsearch(
            hosts=self.host,
            basic_auth=(self.login, self.password),
            verify_certs=False,
            ssl_show_warn=False,
            timeout=180,
            # ca_certs="/opt/airflo∂w/dags/custom_class/elasticsearch_ca.crt",
        )
        self.es.ping()
        return self.es
