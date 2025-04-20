# AI Agent with Retrieval‑Augmented Generation and Custom Tool Integration

This pipeline delivers a ready‑to‑use AI assistant you can try in Azure Foundry. The Agent is specialized on financial information from clients of any firm. As users chat, it keeps track of the conversation and automatically chooses between two modes:

- **Retrieval‑Augmented Generation (RAG):** Pulls in the most relevant snippets from your document store to answer questions.  
- **Historical Forecasting:** Runs a Python script on one client time‑series dataset to generate forecasts.

All you need to do is upload the zip file to `Prompt Flow` in Azure Foundry (select `Chat flow` in flow type), configure the vector database and access to historical data.

A visual summary of this simple agent:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/df1de885-74c0-48e7-a637-1d2c31e5bdc7" />

## Prerequisites

- Connection: Azure OpenAI or OpenAI connection, with the availability of chat and embedding models/deployments.

## Benchmarks

* **Dataset** – 10 synthetic Q&A pairs (net‑worth lookup) with numeric ground‑truth values. All the results from the benchmark can be found in `evaluation_evaluation_agent_rag_simple_variant_1_Output_Table_04-20-2025-15-34.csv`.

**Metrics**
- **Coherence:** Measures if the answer logically follows the question.  
- **Fluency:** Measures if the answer is grammatically correct and natural.  
- **Groundedness:** Measures if the answer is based on retrieved or known facts.  
- **Relevance:** Measures if the answer stays focused on the user's question.  
- **Similarity:** Measures how close the answer is to the expected ground truth.  
- **F1 / BLEU / GLEU:** Measure word overlap between answer and ground truth.


**Results**
| Metric | Avg |
|--------|-----|
| Coherence | **3.8** |
| Fluency* | **1.0** |
| Groundedness | **5.0** |
| Relevance | **4.0** |
| Similarity | **5.0** |
| F1 / BLEU / GLEU | **1.00** |

\*Numeric‑only answers are penalised.

**Key-points**

* Perfect factual accuracy and grounding (all values match ground truth).  
* One low‑coherence case: negative net‑worth answer lacked context.  
* Fluency rubric mis‑scores numeric-only answers.

## Results

Examples of results from our Agent:

<img width="330" alt="image" src="https://github.com/user-attachments/assets/af6efcc3-2a0b-4082-9c61-c1a480b878e9" />

<img width="330" alt="image" src="https://github.com/user-attachments/assets/88d47369-734e-4d56-be32-ba9042525074" />
<br>
<img width="330" alt="image" src="https://github.com/user-attachments/assets/d6ee6604-24bb-4a24-b2c9-509c10f38783" />

<img width="341" alt="image" src="https://github.com/user-attachments/assets/51abb835-20e4-4407-9e8a-a351892dce7b" />




## Future Work
### RAG Architecture
The RAG architecture is crucial to get more precise answers, an interesting compilation of state of the art models are in *Papers with Code* (2025). In this project we implement a basic architecture like:

<img src="https://github.com/user-attachments/assets/b9f86766-4858-42ef-a04a-bc30d5d37cde" alt="Basic RAG Architecture" width="800"/>

*Source: Ragflow (2024)*

A more advanced and potentially superior architecture is Agentic RAG:

<img src="https://github.com/user-attachments/assets/6c4ba81b-7654-4bea-b03f-dac9af427c54" alt="Agentic RAG Architecture" width="800"/>

*Source: Ragflow (2024)*

Recall that in order to evaluate the performance of an AI system, we usually compare its answers against a ground truth produced by experts. Since we used synthetic data we don't have a reliable benchmark.

### Model Selection
For all LLM nodes we used GPT-4o, this could not be an optimal decision from a cost-benefit point of view. We could only be sure with a true benchmark, and the evaluate relevant score metrics against response time and LLM usage cost. A summary of those relationships according to Azure [https://ai.azure.com/explore/models/leaderboard] (April 2025) are:

<img width="800" alt="output_vs_cost_azure_20april2025" src="https://github.com/user-attachments/assets/09e45617-b9c7-421e-a884-0d497d746f73" />


<img width="331" alt="image" src="https://github.com/user-attachments/assets/6b3f0208-1161-4ca1-81e3-b4ea96d21600" />



## Acknowledgement
This pipeline is based on the YouTube tutorial: [Building RAG Solutions with Azure AI Foundry](https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG) from Microsoft Reactor.

## References
Microsoft Azure. (2024, March 22). Building RAG solutions with Azure AI Foundry [Video]. YouTube. https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG

Papers with Code. (2025). Question answering. Papers with Code. https://paperswithcode.com/task/question-answering

Ragflow. (2024, April 3). Agentic RAG: Definition and low-code implementation. Ragflow. https://ragflow.io/blog/agentic-rag-definition-and-low-code-implementation
