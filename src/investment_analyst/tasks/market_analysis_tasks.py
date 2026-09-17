from crewai import Task
from investment_analyst.models.schemas import MarketAnalysis


def get_market_analysis_task(agent, research_task: Task):
    return Task(
        description="""
        Using the company profile provided in the context, conduct a deep market analysis:
        1. Estimate the TAM, SAM, and SOM for this company's market.
        2. Identify the company's competitive moat (network effects, IP, switching costs, etc.).
        3. List direct and indirect competitors.
        4. Summarize key industry trends over the last 3 years.
        Base all analysis on the company data provided and verifiable market research.
        """,
        expected_output="A structured JSON object containing market metrics, competitors, moat analysis, and trends.",
        agent=agent,
        context=[research_task],
        output_pydantic=MarketAnalysis
    )