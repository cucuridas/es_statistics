from es_statistics.connectElasticsearch import ConenctionEs
import asyncio, uvloop


class GetDataEs(ConenctionEs):
    def __init__(self):
        super().__init__()
        self.result: object = None

    async def getAllDocumentAsync(self, indexName: str):
        # yeild를 통해 paging 된 데이터를 지속적으로 호출하여 next 함수 요청시 return 하도록
        # -> dataframe 적재 시 호출 스택 메모리 용량 고려
        yield self.searchFirst(indexName)
        while True:
            await asyncio.sleep(2)
            self.result = self.es.scroll(
                body={"scroll": "1m", "scroll_id": self.result["_scroll_id"]}, format="json"
            )
            yield self.result
            if len(self.result["hits"]["hits"]) == 0:
                break

    def getAllDocument(self, indexName: str):
        # yeild를 통해 paging 된 데이터를 지속적으로 호출하여 next 함수 요청시 return 하도록
        # -> dataframe 적재 시 호출 스택 메모리 용량 고려
        self.result = self.searchFirst(indexName)
        yield self.result["hits"]["hits"]
        while True:
            self.result = self.es.scroll(
                body={"scroll": "1m", "scroll_id": self.result["_scroll_id"]}
            )
            yield self.result["hits"]["hits"]
            if len(self.result["hits"]["hits"]) == 0:
                break

    def searchFirst(self, indexName):
        self.result = self.es.search(index=indexName, size=10000, scroll="1m")
        return self.result.body

    def checkScrollInfo(self):
        if self.result == None or "_scroll_id" not in self.result:
            return False
        else:
            return True

    def closeScrollInfo():
        pass
