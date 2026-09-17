# 🏛️ AI Investment Analyst

A production-grade multi-agent system that performs automated venture capital due diligence on startups. Built with CrewAI, FastAPI, and ethical web scraping.

## 🚀 What It Does

Given a company name, this system:
1. **Researches** the company's fundamentals, funding history, and key products.
2. **Analyzes** market size (TAM/SAM/SOM), competitive landscape, and moats.
3. **Audits** for risks including legal issues, financial red flags, and bad press.
4. **Synthesizes** everything into a structured Investment Memo with a final Invest/Pass/Watch recommendation.

## 🏗️ Architecture

This project uses a **Sequential Multi-Agent Pipeline** with strict Pydantic schemas for data validation between agents.


### Agents

| Agent | Role | Output Schema |
|-------|------|---------------|
| Lead Researcher | Forensic fact-gathering | `CompanyProfile` |
| Market Analyst | TAM/SAM/SOM, Competitors, Moats | `MarketAnalysis` |
| Risk Auditor | Legal, Financial, Red Flags | `RiskAssessment` |
| VC Partner | Synthesis & Final Decision | `InvestmentMemo` |

## 🛠️ Tech Stack

- **AI Orchestration:** CrewAI, LangChain
- **LLM:** OpenAI GPT-4o
- **Search & Scraping:** Tavily API, Firecrawl (ethical scraping)
- **Backend:** FastAPI, Pydantic v2
- **Database:** PostgreSQL (via SQLModel)
- **Observability:** Langfuse
- **Package Manager:** `uv`

## 🚦 Getting Started

### Prerequisites
- Python 3.12+
- `uv` package manager
- API keys for OpenAI, Tavily, and Firecrawl

### Installation

```bash
# Clone the repo
git clone <your-repo-url>
cd investment-analyst

# Create virtual environment
uv venv --python 3.12
source .venv/bin/activate

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# Project Structure
src/investment_analyst/
├── agents/       # CrewAI Agent definitions
├── tasks/        # CrewAI Task definitions
├── tools/        # Custom ethical scraping/search tools
├── models/       # Pydantic schemas (data contracts)
├── crews/        # Crew orchestration logic
├── api/          # FastAPI routes
└── config/       # Settings and environment management

# Ethical Scraping Notice
This project strictly adheres to robots.txt and only scrapes publicly available data. We prioritize official APIs (SEC EDGAR, Crunchbase) and ethical scraping tools (Firecrawl) that respect rate limits and site policies.

# 📈 Roadmap
Implement Langfuse observability
Add human-in-the-loop approval for high-risk investments
Deploy to AWS with Docker
Add PostgreSQL persistence for historical memos