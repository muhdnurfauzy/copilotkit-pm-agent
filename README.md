### 1. Project Overview

**PM CopilotKit** is an agentic project management workspace built using **CopilotKit** and a **remote Python backend**. It bridges an interactive conversational interface with generative UI components, allowing a user to manage project backlogs, plan sprints, and manipulate tasks on a live Kanban board through both manual interaction and autonomous AI agent actions.

---

### 2. Architecture & Tech Stack

| Layer | Technologies Used | Role |
| --- | --- | --- |
| **Frontend** | Next.js 16 (App Router), TypeScript, Tailwind CSS, Lucide React | Workspace UI, Kanban board visualization, session switching, and client-side state. |
| **Agentic UI Layer** | `@copilotkit/react-core`, `@copilotkit/react-ui`, `@copilotkit/runtime` | Handles generative UI state synchronization, action registration (`useCopilotAction`), and agent readable state (`useCopilotReadable`). |
| **Backend Runtime** | Python 3.14, FastAPI, Uvicorn | Remote execution runtime for agent tools and future LangGraph workflow orchestration. |
| **LLM Inference** | Ollama Cloud (`gpt-oss:20b`) / OpenAI API adapter | Powers the conversational model via a streaming route at `/api/copilotkit`. |

---

### 3. Key Completed Features

* **Multi-Thread Workspace Management:**
* Clean, unpopulated startup state with dynamic session generation (**+ New thread**).
* True session isolation: Switching between threads keeps each conversation history intact without cross-contamination.
* Local persistence: Threads and tasks persist across page reloads via browser storage (`localStorage`).
* Thread metadata: Real-time task counts, creation dates, search filtering, and archive/delete actions.


* **Bidirectional Task & State Synchronization (Generative UI):**
* **Chat View:** Central conversational interface with functional quick-action prompt chips.
* **Board View:** Three-column Kanban board (`To Do`, `In Progress`, `Done`).
* The AI agent reads the current board state (`useCopilotReadable`) and directly executes task creation and status updates (`useCopilotAction`), dynamically moving cards across board columns.


* **API & System Setup:**
* Option 1 CopilotKit architecture: Next.js API route proxies commands to the local FastAPI backend (`[http://127.0.0.1:8000](http://127.0.0.1:8000)`).
* Git repository initialized, clean branches tracked, and synced to GitHub for version control.
