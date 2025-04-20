# AI Agent with Retrieval‑Augmented Generation and Custom Tool Integration

This pipeline delivers a ready‑to‑use AI assistant you can try in Azure Foundry. As users chat, it keeps track of the conversation and automatically chooses between two modes:

- **Retrieval‑Augmented Generation (RAG):** Pulls in the most relevant snippets from your document store to answer questions.  
- **Historical Forecasting:** Runs a Python script on the client time‑series dataset to generate forecasts.

All you need to do is upload the zip file to `Prompt Flow` in Azure Foundry (select `Chat flow` in flow type), configure the vector database and access to historical and data.

A visual summary of our simple agent:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/df1de885-74c0-48e7-a637-1d2c31e5bdc7" />



## Prerequisites

- Connection: Azure OpenAI or OpenAI connection, with the availability of chat and embedding models/deployments.

## Future Work
### RAG Architecture
The RAG architecture is crucial to get more precise answers, an interesting compilation of state of the art models are in Papers with Code (2025). In this project we implement a basic architecture like:

<img src="https://github.com/user-attachments/assets/b9f86766-4858-42ef-a04a-bc30d5d37cde" alt="Basic RAG Architecture" width="800"/>

*Source: Ragflow (2024)*

A more advanced and potentially superior architecture is Agentic RAG:

<img src="https://github.com/user-attachments/assets/6c4ba81b-7654-4bea-b03f-dac9af427c54" alt="Agentic RAG Architecture" width="800"/>

*Source: Ragflow (2024)*

Recall that in order to evaluate the performance of an AI system, we usually compare its answers against a ground truth produced by experts. Since we used synthetic data we don't have a reliable benchmark.

## Acknowledgement
This pipeline is based on the YouTube tutorial: [Building RAG Solutions with Azure AI Foundry](https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG) from Microsoft Reactor.

## References
Microsoft Azure. (2024, March 22). Building RAG solutions with Azure AI Foundry [Video]. YouTube. https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG

Papers with Code. (2025). Question answering. Papers with Code. https://paperswithcode.com/task/question-answering

Ragflow. (2024, April 3). Agentic RAG: Definition and low-code implementation. Ragflow. https://ragflow.io/blog/agentic-rag-definition-and-low-code-implementation
