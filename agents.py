from crewai import Agent, LLM
from crewai_tools import TavilySearchTool
import os
from dotenv import load_dotenv

llm = LLM(
    model="ollama/qwen2.5:7b",
    temperature=0.3
)

search_tool = TavilySearchTool(api_key=os.getenv("TAVILY_API_KEY"))

# Agents
researcher = Agent(
    role="AI Researcher",
    goal="Fine accurate, recent, unbiased information using web search.",
    backstory="You are an expert research analyst with strong ability to gather real-time information "
              "from online reviews. You verify facts and avoid hallucinations.",
    llm=llm,
    tools=[search_tool],
    allow_delegation=False,
    verbose=True,
    max_iter=1
)

analyst = Agent(
    role="AI analyst",
    goal="Analyze the research data, extract insights, compare opposing views, and identify trends.",
    backstory="You specialise in examining raw research, finding patterns, highlighting pros/cons and "
              "summarizing complex ideas clearly",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role="Technical Writer",
    goal="Convert insights into polished, structured, readable content.",
    backstory="You are an excellent technical writer. You create clean, engaging narratives in blog-post style "
              "or executive-summary style",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

quality_checker = Agent(
    role="Quality Assurance Expert",
    goal="Review the final output for correctness, clarity, structure, grammar and factual consistency. "
         "Improve it if needed",
    backstory="You ensure that the final report is free of errors, hallucinations and ambiguous claims. "
              "you make the writing sharper and more reliable.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)
