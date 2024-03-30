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

index_params = {
  "metric_type": "L2",
  "index_type": "IVF_FLAT",
  "params": {"nlist": 1024}
}

collection.create_index(
  field_name="song_vec",
  index_params=index_params
)

# index on scalar field

collection.create_index(
  field_name="song_name",
  index_name="scalar_index_album1"
)

