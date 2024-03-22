# Experiments Gen AI

List of experiments on Gen AI ecosystem

## Setup

### Install

```console
create -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
```

#### Install Milvus

**Optional, Only required when executing Milvus examples**

Ensure Milvus vector store is up and running before executing Milvus dependent examples.

1. Use Docker Compose for `Milvus` Vector store setup. Execute `sudo docker compose -f docker-compose-milvus.yml up -d` from project root.

## Table of Content

| File / Folder name | Framework(s) | Optimization / FineTuning | Pipeline |
|:---|:---|:---|:---|
| rag_pdf_1.py | LlamaIndex + Milvus | RAG | Load PDF Dir, Extract data and index in naive way, Embed the index into vector store, User queries |
| rag_pdf_2.py | LlamaIndex | RAG | Load PDF Dir, Extract data with Sentence window, Embed the index into local storage, User queries |
| rag_pdf_3.py | LlamaIndex + Milvus | RAG | Load PDF Dir, Extract data with Sentence window, Embed the index into vector store, User queries |
| rag_pdf_4.py | LlamaIndex + Chroma | RAG | Coming Soon |
| rag_pdf_5.py | LlamaIndex + Pinecone | RAG | Coming Soon |
| rag_pdf_6.py | LlamaIndex + Qdrant | RAG | Coming Soon |
| rag_pdf_7.py | LlamaIndex + Ray + Milvus | RAG | Coming Soon |

### How to Run?

```console
python3 rag_pdf_1.py
```
