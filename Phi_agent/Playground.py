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

#set openai api key using setx OPENAI_API_KEY "openai_api_key_value" in cmd
load_dotenv()

phi.api = os.getenv("PHI_API_KEY") #used for custom chat in phi platform

webserach_agent = Agent(
    name="WebSearchAgent",
    role="search the web for information",
    model=Groq(id='llama3-groq-70b-tool-use-preview'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)


# financial_agent 
financial_agent = Agent(
    name="Finance AI Agent",
    role="search the web for financial information",
    model=Groq(id='llama3-groq-70b-tool-use-preview'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                    company_news=True, stock_fundamentals=True)],
    instructions=["Use Table format to show the data"],
    show_tools_calls=True,
    markdown=True
)



app = Playground(agents=[financial_agent,webserach_agent]).get_app()

if __name__ =="__main__":
    serve_playground_app("Playground:app",reload=True)

