# Enterprise IT Support Agent


# Company Infromation

| Customer | Employees |      Use Case       |
|----------|-----------|---------------------|
| Coxginex |    10K    |     IT Support      |

# 1. Problem Statement

Coxginex has a large internal IT knowledge base containing VPN instructions, password rules, MFA policies, software-installation rules, laptop troubleshooting guides and service-desk runbooks. Even though the information already exists, employees still create repetitive support tickets because they do not know which document contains the correct answer.

A traditional keyword search is often frustrating because it can return many documents instead of one clear answer. A normal chatbot creates another risk: it may answer confidently even when it does not have reliable company information. In addition, some questions depend on current public information that may not yet exist in the company's private knowledge base.

**Bussness challenge**
---

Employees need fast answer but the company need those answers to be grounded, trustworthy, transperent and base on private company knoledge whenecer possible

# 2. Simple RAG is not Enough

| Simple RAG                     | Problem in real world                                                               |
|--------------------------------|-------------------------------------------------------------------------------------|
| Question > Retrieve > Genetate | Retrieved chunks may be weak or unrelated but the model may still generate an answer|
| Uses only private KB           | It cannot answer well when the required infromation is missing or outdated          |
| No evidence decision           | The application does not decide whether the retrieved infromation is good enouth    |

# 3. Proposed Solution

Build an **Enterprise IT Support Agent**. The system searches the trusted private company knowledge base first. It then evaluates the retrieved evidence before generating an answer. If the private evidence is weak, the workflow can use Tavily web search. If the evidence is still weak the system rewrites the query and retries instead of blindly answering.

1. Employee asks a question
2. LangGraph routes the request
3. Retrieve relevant chunks from the private Pinecone knowledge base
4. Grade whether the private evidence is strong enough
5. `GOOD` -> Generate grounded answer from LLM knowledge
6. `WEAK` -> Search web using Tavily                      
7. Grade web evidence
8. If needed LLM rewrite query and retry
9. Return answer, sources and decision tree