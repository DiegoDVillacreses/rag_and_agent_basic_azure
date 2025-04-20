# AI Agent with Retrieval‑Augmented Generation and Custom Tool Integration

This pipeline delivers a ready‑to‑use AI assistant you can try in Azure Foundry. As users chat, it keeps track of the conversation and automatically chooses between two modes:

- **Retrieval‑Augmented Generation (RAG):** Pulls in the most relevant snippets from your document store to answer questions.  
- **Historical Forecasting:** Runs Python scripts on your time‑series dataset to generate forecasts and data‑driven insights.

All you need to do is point the upload the YAML file to `Prompt Flow` from Azure Foundry, configure the vector database and the access to historical and data.
