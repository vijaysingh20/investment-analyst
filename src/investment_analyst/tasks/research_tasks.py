from crewai import Task
from investment_analyst.models.schemas import CompanyProfile


def get_research_task(agent, company_name: str):
    return Task(
        description=f"""
        Conduct a deep dive investigation into {company_name}.
        1. Find their official website and extract core business details.
        2. Search for their founding year, headquarters, and key products.
        3. Find their funding history and previous investors (Crunchbase, Pitchbook, News).
        4. Ensure all data is factual and verifiable.
        """,
        expected_output="A structured JSON object containing the company profile.",
        agent=agent,
        output_pydantic=CompanyProfile
    )