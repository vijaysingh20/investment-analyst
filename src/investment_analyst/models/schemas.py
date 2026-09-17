from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional


class InvestmentDecision(str, Enum):
    INVEST = "INVEST"
    PASS = "PASS"
    WATCH = "WATCH"


class Shareholder(BaseModel):
    name: str = Field(description="Name of the shareholder, founder, or VC firm")
    ownership_percentage: Optional[float] = Field(default=None, description="Estimated ownership percentage as a float")


class MarketMetrics(BaseModel):
    tam: str = Field(description="Total Addressable Market estimate")
    sam: str = Field(description="Serviceable Available Market estimate")
    som: str = Field(description="Serviceable Obtainable Market estimate")


class CompanyProfile(BaseModel):
    """Output schema for the Lead Researcher"""
    company_name: str = Field(description="Official name of the company")
    founding_year: Optional[int] = Field(description="Year of the company was founded")
    headquarters: str = Field(description="Location of headquarters")
    business_model: str = Field(description="How the company makes money")
    key_products: List[str] = Field(description="List of core products or services")
    previous_investors: List[str] = Field(default_factory=list, description="List of known investors")
    funding_history: str = Field(description="Summary of funding rounds and amounts raised")


class MarketAnalysis(BaseModel):
    """Output schema for the Market Analyst"""
    market_metrics: MarketMetrics = Field(description="Market sizing metrics")
    competitors: List[str] = Field(description="List of direct competitors")
    moat_strength: str = Field(description="Description of the company's competitive advantage")
    industry_trends: str = Field(description="Current trends affecting the industry")


class RiskAssessment(BaseModel):
    """Output schema for the Risk Auditor"""
    risk_score: int = Field(ge=1, le=10, description="Risk score from 1 to 10")
    legal_risks: List[str] = Field(description="Any lawsuits or regulatory issues")
    financial_risks: str = Field(description="Concerns about burn rate or revenue")
    red_flags: List[str] = Field(description="Major warning signs")


class InvestmentMemo(BaseModel):
    """The final output schema for the VC Partner"""
    company_profile: CompanyProfile
    market_analysis: MarketAnalysis
    risk_assessment: RiskAssessment
    executive_summary: str = Field(description="A concise 2-3 paragraph executive summary")
    report_text: str = Field(description="The full, detailed markdown report")
    final_recommendation: InvestmentDecision = Field(description="The final investment decision")
    key_shareholders: List[Shareholder] = Field(default_factory=list)