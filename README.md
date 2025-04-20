# AI Agent with Retrieval‑Augmented Generation and Custom Tool Integration

This pipeline delivers a ready‑to‑use AI assistant you can try in Azure Foundry. The Agent is specialized on financial information from clients of any firm. As users chat, it keeps track of the conversation and automatically chooses between two modes:

- **Retrieval‑Augmented Generation (RAG):** Pulls in the most relevant snippets from your document store to answer questions.  
- **Historical Forecasting:** Runs a Python script on one client time‑series dataset to generate forecasts.

All you need to do is upload the zip file to `Prompt Flow` in Azure Foundry (select `Chat flow` in flow type), configure the vector database and access to historical data.

A visual summary of this simple agent:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/df1de885-74c0-48e7-a637-1d2c31e5bdc7" />

## Data

All the used data is synthetic, the pdfs where produced using `simul_pdfs.ipynb` and the historical information with `simul_historic.ipynb`. The pdfs where generated trying to simulate real documents with messy information and complex formats. We produce 20 synthetic client information. All the used information can be found in the folder `simulated_data`.

## Prerequisites

- Connection: Azure OpenAI or OpenAI connection, with the availability of chat and embedding models/deployments.

## Benchmarks

* **Dataset** – 10 synthetic Q&A pairs (net‑worth lookup) with numeric ground‑truth values. All the results from the benchmark can be found in `evaluation_evaluation_agent_rag_simple_variant_1_Output_Table_04-20-2025-15-34.csv`. Also, in `rag_eval.jsonl` the user can find the full evaluation dataset.

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

## Results of Deployment

We use the automatic deployment feature of Azure Foundry, then we generate different examples using the code in `main.py` getting the following results:

<img width="765" alt="example_results_deployment" src="https://github.com/user-attachments/assets/68890994-1692-4733-a735-8e417530573f" />

Additional results can be found in `deployment_example.ipynb`.

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

<img width="800" alt="quality_vs_cost_azure_20april2025" src="https://github.com/user-attachments/assets/64877b5a-44da-40cf-83aa-a9a480681af8" />

<img width="800" alt="output_vs_cost_azure_20april2025" src="https://github.com/user-attachments/assets/b8773140-7f9b-4e3c-90ae-9ba9876a80df" />




## Acknowledgement
This pipeline is based on the YouTube tutorial: [Building RAG Solutions with Azure AI Foundry](https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG) from Microsoft Reactor.

## References
Microsoft Azure. (2024, March 22). Building RAG solutions with Azure AI Foundry [Video]. YouTube. https://www.youtube.com/watch?v=IXGrwWcLJuE&list=PLAgW9mQu35HUoPGbDrcqbQsZbn_cxsiYG

Papers with Code. (2025). Question answering. Papers with Code. https://paperswithcode.com/task/question-answering

Ragflow. (2024, April 3). Agentic RAG: Definition and low-code implementation. Ragflow. https://ragflow.io/blog/agentic-rag-definition-and-low-code-implementation
