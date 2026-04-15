# 🏗️ Architecture Deep Dive

## Overview Technique

### Embeddings Strategy

| Type | Modèle | Dimensions | Use Case |
|------|--------|------------|----------|
| Texte | all-MiniLM-L6-v2 | 384 | Similarité sémantique |
| Image | CLIP ViT-B/32 | 512 | Compréhension visuelle |

### Indexing Strategy

```python
# Pseudo-code du pipeline d'indexation
def index_document(pdf_path):
    # 1. Extraction
    doc = PyMuPDF.open(pdf_path)
    
    # 2. Traitement multi-modal
    for page in doc:
        text = page.get_text()
        images = page.get_images()
        
        # 3. Chunking
        text_chunks = recursive_split(text)
        
        # 4. Embeddings
        text_embeddings = sentence_transformer.encode(text_chunks)
        image_embeddings = clip.encode(images)
        
        # 5. Stockage FAISS
        faiss_index.add(text_embeddings)
        faiss_index.add(image_embeddings)
        
        # 6. Metadata linking
        metadata_store.link(page_num, chunk_ids, image_ids)
