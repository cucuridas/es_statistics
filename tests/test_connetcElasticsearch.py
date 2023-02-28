import sys

sys.path.append("/Users/cucuridas/Desktop/es_statistics")

from es_statistics.connectElasticsearch import ConenctionEs
import asyncio


# Testing ConnectionEs Object
async def test_get_conn():
    connect = await ConenctionEs().get_conn()
    assert connect


if __name__ == "__main__":
    asyncio.run(test_get_conn())
