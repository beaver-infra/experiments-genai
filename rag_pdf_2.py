from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings, load_index_from_storage, ServiceContext, Document
from llama_index.core.embeddings import resolve_embed_model
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.llms.ollama import Ollama

from llama_index.core.node_parser import SentenceWindowNodeParser, HierarchicalNodeParser, get_leaf_nodes
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

# Settings
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5") # Embedded Model
Settings.llm = Ollama(model="llama2", request_timeout=30.0) # LLM Model
Settings.chuck_size = 512

# Constants
PERSIST_DIR_SENTENCE = "./rag_pdf_2/sentence_index"
PERSIST_DIR_BASE = "./rag_pdf_2/base_index"

# Load files into "Document" object
documents = SimpleDirectoryReader("./data/pdf/").load_data()

# Inspect the Document object
print("documents[0]: ")
print(documents[0])

print("\n")
print("documents[0].metadata: ")
print(documents[0].metadata)

# Create the sentence window node parser with default settings
sentence_node_parser = SentenceWindowNodeParser.from_defaults(
  window_size=3,
  window_metadata_key="window",
  original_text_metadata_key="original_text"
)

base_node_parser = SentenceSplitter()

nodes = sentence_node_parser.get_nodes_from_documents(documents)
base_nodes = base_node_parser.get_nodes_from_documents(documents)

print("\n")
print("sentence_node_parser: ")
print(nodes[2])

print('\n')
print("base_node_parser: ")
print(base_nodes[2])

print('\n')
print("node dict: ")
print(dict(nodes[2]))

print('\n')
print("base_nodes dict: ")
print(dict(base_nodes[2]))

# Create vector stores
ctx_sentence = ServiceContext.from_defaults(llm=Settings.llm, embed_model=Settings.embed_model, node_parser=sentence_node_parser)
ctx_base = ServiceContext.from_defaults(llm=Settings.llm, embed_model=Settings.embed_model, node_parser=base_node_parser)

sentence_index = VectorStoreIndex(nodes, service_context=ctx_sentence)
base_index = VectorStoreIndex(base_nodes, service_context=ctx_base)

print('\n')
print("sentence_index: ")
print(sentence_index)
print('\n')

# save to persistent storage
sentence_index.storage_context.persist(persist_dir=PERSIST_DIR_SENTENCE)
base_index.storage_context.persist(persist_dir=PERSIST_DIR_BASE)

# Retrieve from storage
SC_retrieved_sentence = StorageContext.from_defaults(persist_dir=PERSIST_DIR_SENTENCE)
SC_retrieved_base = StorageContext.from_defaults(persist_dir=PERSIST_DIR_BASE)

# Load index
retrieved_sentence_index = load_index_from_storage(SC_retrieved_sentence)
retrieved_base_index = load_index_from_storage(SC_retrieved_base)

# Create query engine
sentence_query_engine = retrieved_sentence_index.as_query_engine(
  similarity_top_k=3,
  verbose=True,
  node_postprocessors=[
    MetadataReplacementPostProcessor(target_metadata_key="window")
  ]
)

base_query_engine = retrieved_base_index.as_query_engine(
  similarity_top_k=3,
  verbose=True,
)

# Inference
base_response = base_query_engine.query("Who is father of Quantum mechanics?")
print('\n')
print("base_response: ")
print(base_response)
print('\n')

sentence_response = sentence_query_engine.query("Who is father of Quantum mechanics?")
print('\n')
print("sentence_response: ")
print(sentence_response)
print('\n')

# print("Single document: ", documents[0])

# vector_store = MilvusVectorStore(
#   dim=384,
#   overwrite=True
# )
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#   documents, storage_context=storage_context
# )

# query_engine = index.as_query_engine()

# response = query_engine.query("Who is father of Quantum mechanics?")
# print("Response: ", response)
# for node in response.source_nodes:
#   print(f"Metadata {node.node.extra_info}")
#   print(f"Score {node.score:.3f}")
# print("\n\n")

# response = query_engine.query("How is Quantum Physics is different from Classical Physics?")
# print("Response: ", response)
# for node in response.source_nodes:
#   print(f"Metadata {node.node.extra_info}")
#   print(f"Score {node.score:.3f}")
# print("\n\n")

