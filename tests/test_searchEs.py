import sys

sys.path.append("/Users/cucuridas/Desktop/es_statistics")

from es_statistics.searchEs import GetDataEs

TEST_OBJ = GetDataEs()
TEST_OBJ.get_conn()


def test_getAllDocument():
    generatorObjs = TEST_OBJ.getAllDocument("firewall")
    for generatorObj in generatorObjs:
        print(generatorObj)


def test_searchFirst():
    TEST_OBJ.searchFirst("firewall")


if __name__ == "__main__":
    # test_searchFirst()
    test_getAllDocument()
