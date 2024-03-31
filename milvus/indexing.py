from pymilvus import connections, utility, Collection, FieldSchema, CollectionSchema, DataType
import string
import random

connections.connect(
  alias="default",
  host="localhost",
  port="19530"
)


print(utility.list_collections())

collection = Collection("album1")

# Flat
index_params = {
  "metric_type": "L2",
  "index_type": "FLAT",
  "params": {},
  "index_name": "FLAT_INDEX_EG"
}

# IVF_FLAT
# index_params = {
#   "metric_type": "L2",
#   "index_type": "IVF_FLAT",
#   "params": {"nlist":1024},
#   "index_name": "IVF_FLAT_INDEX_EG"
# }

# During search and query
# search_params = {"metric_type": "L2", "params": {"nprobe": 64}}

# IVF_SQ8
# index_params = {
#   "metric_type": "L2",
#   "index_type": "IVF_SQ8",
#   "params": {"nlist":1024},
#   "index_name": "IVF_SQ8_INDEX_EG"
# }

# During search and query
# search_params = {"metric_type": "L2", "params": {"nprobe": 64}}

# IVF_PQ
# index_params = {
#   "metric_type": "L2",
#   "index_type": "IVF_PQ",
#   "params": {"nlist":1024, "m": 2, "nbits": 16},
#   "index_name": "IVF_PQ_INDEX_EG"
# }

# During search and query
# search_params = {"metric_type": "L2", "params": {"nprobe": 64}}

# HNSW
# index_params = {
#   "metric_type": "L2",
#   "index_type": "HNSW",
#   "params": {"M": 2, "efConstruction": 16},
#   "index_name": "HNSW_INDEX_EG"
# }

# During search and query
# search_params = {"metric_type": "L2", "params": {"ef": 4}}

collection.create_index(
  field_name="song_vec",
  index_params=index_params
)

# index on scalar field

collection.create_index(
  field_name="song_name",
  index_name="scalar_index_album1"
)

