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

## Example #1 Answer Found in the Company Knowledge Base

**Employee:** "How do I connect to the company VPN from home?"

The VPN procedure already exists in the private IT handbook. The system retrieves the relevant chunks from Pinecone, grades them as useful evidence, and generates the answer from the internal knowledge base. There is no reason to search the public web.

**Easy explanation:** The AI first checks the company's own trusted documents. Because it finds the answer there, it stops and answers from those documents.

## Example #2 Private Knowledge Is Not Enough

**Employee:** "What is the latest Microsoft Teams outage guidance?"

The private IT documents may not contain current outage information. The system retrieves private knowledge first, but the evidence grader identifies that the information is insufficient. LangGraph then routes the workflow to Tavily web search. The web evidence is graded before the final answer is produced.

**Easy explanation:** The AI does not pretend that the company documents contain the answer. It recognizes the gap, searches an external source, checks that evidence, and then responds.

# 4. What Makes This Agentic RAG?

Normal RAG follows a mostly fixed path: **Question > Retrieve > Generate**. This project makes decisions during execution. It can route, retrieve, evaluate evidence, choose between private knowledge and web search, rewrite a weak query, retry, and then generate a grounded answer.

| Normal RAG | Agentic RAG in this project |
|------------|----------------------------|
| Retrieve once | Retrieve, grade, and retry when necessary |
| Fixed flow | Conditional LangGraph routing |
| Generate after retrieval | Generate only after evidence evaluation |
| Private KB only | Private KB first, web fallback when needed |

# 5. Proposed Product Components

- **LangGraph:** controls the agentic decision workflow.
- **Pinecone:** stores the company's private embedded knowledge.
- **HuggingFace embeddings:** convert document chunks and queries into vectors.
- **Groq LLM:** performs routing, grading, query rewriting, and grounded generation.
- **Tavily:** provides external web search when internal evidence is insufficient.
- **FastAPI:** exposes the application through backend APIs.
- **HTML/CSS/JavaScript:** gives employees a simple chat experience and displays the execution trace.
- **SQLite audit logging:** records the decision path for basic debugging and transparency.
- **Document ingestion:** lets authorized staff add PDF, TXT, Markdown, and DOCX knowledge.


