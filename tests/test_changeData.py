import sys

sys.path.append("/Users/cucuridas/Desktop/es_statistics")

from es_statistics.searchEs import GetDataEs
from es_statistics.changeData import DocumnetToDf
from pandas.core.frame import DataFrame

CONNECTION_OBJ = GetDataEs()
CONNECTION_OBJ.get_conn()
SAMPLE_DATA_OBJS = CONNECTION_OBJ.getAllDocument("firewall")
DATA = None
if __name__ == "__main__":
    for data_obj in SAMPLE_DATA_OBJS:
        source_data = list(map(lambda x: x["_source"], data_obj))

        if DATA == None:
            DATA = DocumnetToDf.changeDocToDf(source_data)
        else:
            rows = DocumnetToDf.changeDocToDf(source_data)
            DATA = DATA.append(rows)
        print(DATA)
