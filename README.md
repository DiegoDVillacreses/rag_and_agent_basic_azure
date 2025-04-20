# AI Agent with Retrieval‑Augmented Generation and Custom Tool Integration

This pipeline delivers a ready‑to‑use AI assistant you can try in Azure Foundry. As users chat, it keeps track of the conversation and automatically chooses between two modes:

- **Retrieval‑Augmented Generation (RAG):** Pulls in the most relevant snippets from your document store to answer questions.  
- **Historical Forecasting:** Runs a Python script on the client time‑series dataset to generate forecasts.

All you need to do is upload the YAML file to `Prompt Flow` in Azure Foundry, configure the vector database and access to historical and data.
