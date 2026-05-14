# Phi Playground Multi-Agent App

This Python script creates a simple **Phi Playground** application with two AI agents:

1. **WebSearchAgent**  
   Searches the web using DuckDuckGo and returns answers with sources.

2. **Finance AI Agent**  
   Searches financial data using Yahoo Finance tools and presents the output in table format.

The app is served locally using Phi's `serve_playground_app`.

---

## Code Overview

```python
import openai
import phi.api
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat
import phi
from phi.playground import Playground, serve_playground_app
```

### Imports

These imports are used to:

- Load environment variables from a `.env` file
- Create AI agents using the Phi framework
- Use Groq as the LLM provider
- Use DuckDuckGo for web search
- Use Yahoo Finance for stock and company data
- Serve the agents inside a local Playground app

---

## Environment Setup

```python
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")
```

The script loads environment variables from a `.env` file.

You should create a `.env` file and add your Phi API key:

```env
PHI_API_KEY=your_phi_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

You can also set the OpenAI API key from Windows CMD using:

```cmd
setx OPENAI_API_KEY "openai_api_key_value"
```

---

## Web Search Agent

```python
webserach_agent = Agent(
    name="WebSearchAgent",
    role="search the web for information",
    model=Groq(id='llama3-groq-70b-tool-use-preview'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)
```

### Purpose

This agent is responsible for searching the internet and answering user questions with sources.

### Key Parameters

| Parameter | Meaning |
|---|---|
| `name` | Name of the agent |
| `role` | Defines the responsibility of the agent |
| `model` | Uses Groq Llama 3 model |
| `tools` | Uses DuckDuckGo for web search |
| `instructions` | Tells the agent to always include sources |
| `show_tools_calls` | Displays tool usage in the output |
| `markdown` | Formats output in Markdown |

> Note: The variable name `webserach_agent` has a spelling mistake. It should ideally be `websearch_agent`.

---

## Financial Agent

```python
financial_agent = Agent(
    name="Finance AI Agent",
    role="search the web for financial information",
    model=Groq(id='llama3-groq-70b-tool-use-preview'),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_news=True,
        stock_fundamentals=True
    )],
    instructions=["Use Table format to show the data"],
    show_tools_calls=True,
    markdown=True
)
```

### Purpose

This agent is responsible for fetching and presenting financial information.

It can retrieve:

- Stock prices
- Analyst recommendations
- Company news
- Stock fundamentals

### Key Parameters

| Parameter | Meaning |
|---|---|
| `name` | Name of the finance agent |
| `role` | Defines that the agent handles finance-related queries |
| `model` | Uses Groq Llama 3 model |
| `tools` | Uses Yahoo Finance tools |
| `instructions` | Tells the agent to show data in table format |
| `show_tools_calls` | Displays tool calls in the output |
| `markdown` | Formats output in Markdown |

---

## Playground App

```python
app = Playground(agents=[financial_agent, webserach_agent]).get_app()
```

This line creates a Playground app containing both agents.

The user can interact with either:

- Finance AI Agent
- WebSearchAgent

inside the Phi Playground interface.

---

## Running the App

```python
if __name__ == "__main__":
    serve_playground_app("Playground:app", reload=True)
```

This runs the app locally.

### Important Note

The string `"Playground:app"` should match the Python filename.

For example, if your file name is:

```text
playground.py
```

then use:

```python
serve_playground_app("playground:app", reload=True)
```

If your file is named:

```text
app.py
```

then use:

```python
serve_playground_app("app:app", reload=True)
```

Using the wrong module name may cause an import error.

---

## Expected Output

After running the script, the terminal should show that the server has started.

You can open the local URL in your browser and use the Phi Playground interface.

Example:

```text
http://127.0.0.1:8000
```

---

## Full Multi-Line Comment Version

You can also paste this comment at the top of your Python file:

```python
"""
Phi Playground Multi-Agent Application

This script creates a local Phi Playground app with two AI agents:

1. WebSearchAgent
   - Uses DuckDuckGo to search the web.
   - Answers general questions using online information.
   - Always includes sources in the response.

2. Finance AI Agent
   - Uses Yahoo Finance tools to fetch financial data.
   - Can return stock prices, analyst recommendations, company news,
     and stock fundamentals.
   - Displays financial information in table format.

Environment Variables Required:
- PHI_API_KEY
- GROQ_API_KEY
- OPENAI_API_KEY, optional depending on model usage

The script loads environment variables using python-dotenv.

Important:
The value passed to serve_playground_app should match the filename.

Example:
If the Python file is named playground.py:

    serve_playground_app("playground:app", reload=True)

If the Python file is named app.py:

    serve_playground_app("app:app", reload=True)

Run the file using:

    python playground.py

Then open the local server URL in your browser to access the Playground.
"""
```

---

## Suggested Improvements

1. Rename `webserach_agent` to `websearch_agent`.
2. Remove unused imports if they are not required:
   - `openai`
   - `phi.api`
   - `OpenAIChat`
3. Make sure `.env` contains the correct keys.
4. Use a filename that matches the module name passed to `serve_playground_app`.
