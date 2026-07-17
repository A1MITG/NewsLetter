"""
CXO Insurance & BFSI Intelligence Newsletter - Master Generation Prompt
Production-Ready Newsletter Generator v1.0
"""

import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')

SYSTEM_PROMPT = """You are a Senior Market & Competitive Intelligence Analyst, trained at a Big-4 consulting firm, with deep specialization in Insurance and BFSI.

You think and write like a Chief of Staff to the Group CEO of a global insurance major.

You do NOT behave like:
- A journalist
- A news aggregator
- A marketing analyst

Your lens is strategic, forward-looking, and decision-oriented.

AUDIENCE: Global Insurance & BFSI CXO Suite (CEO, CFO, CIO, COO, CRO, CHRO, CDO)

OUTPUT PRINCIPLES (ENFORCE STRICTLY):
- No fluff
- No marketing language
- No unvalidated vendor claims
- No repetition
- Crisp, consulting-grade tone
- Boardroom-ready

Behave as a Chief of Staff to the Group CEO of a Global Insurance Major.
If this brief were forwarded to Board members, Regional CEOs, or Functional CXOs, it should increase trust immediately."""

# CXO-Relevant Themes
INTELLIGENCE_THEMES = [
    "Regulation, Policy & Compliance",
    "M&A, Partnerships & Strategic Moves",
    "Technology & Operating Model Disruption",
    "AI, Automation & Advanced Analytics",
    "Cybersecurity & Risk Landscape",
    "Market, Macro & Geopolitical Risk",
    "Customer, Distribution & Experience",
    "Talent, Workforce & Future of Work",
    "Industry Thought Leadership"
]

# TIER 1 SOURCES - GLOBAL PRIORITY
TIER_1_SOURCES = {
    "Global Insurance & Reinsurance": [
        "https://www.insurancejournal.com/",
        "https://www.insurancebusinessmag.com/global/",
        "https://www.propertycasualty360.com/",
        "https://www.dig-in.com/",
        "https://www.reinsurancene.ws/",
        "https://www.theinsurer.com/",
        "https://www.globalreinsurance.com/",
    ],
    "Global Business & Capital Markets": [
        "https://www.reuters.com/business/finance",
        "https://www.ft.com/insurance",
        "http://news.ambest.com/",
        "https://riskandinsurance.com/",
    ],
    "Global Systemic Insight": [
        "https://www.weforum.org/issues/insurance-and-asset-management",
        "https://www.genevaassociation.org/",
        "https://www.spglobal.com/ratings/en/sector/insurance",
        "https://www.moodys.com/insurance-outlook",
        "https://www.mckinsey.com/industries/financial-services/our-insights/insurance",
        "https://www.bcg.com/industries/insurance/risk-management",
    ]
}

# TIER 2 SOURCES - REGIONAL DEPTH
TIER_2_SOURCES = {
    "India": [
        "https://www.asiainsurancereview.com/Regions/India-Sub-Continent/India",
        "https://www.business-standard.com/category/finance-insurance-10606.htm",
        "https://www.livemint.com/insurance",
        "https://economictimes.indiatimes.com/wealth/insure",
    ],
    "China": [
        "https://www.caixinglobal.com/topics/insurance/",
        "https://www.scmp.com/business/banking-finance/insurance",
    ],
    "Southeast Asia": [
        "https://www.asiainsurancereview.com/Regions/East-Asia/South-East-Asia",
        "https://asia.nikkei.com/Business/Finance",
        "https://www.businesstimes.com.sg/hub/ready-for-what-next/insurance",
    ],
    "Europe / UK": [
        "https://www.insurancetimes.co.uk/",
        "https://www.postonline.co.uk/",
        "https://www.insuranceeurope.eu/",
        "https://www.handelsblatt.com/finanzen/banken-versicherungen/versicherung/",
    ],
    "United States": [
        "https://content.naic.org/article/press_releases.htm",
        "https://www.carriermanagement.com/",
    ],
    "Middle East / Gulf": [
        "https://www.meinsurancereview.com/",
        "https://www.zawya.com/en/islamic-economy/islamic-finance",
        "https://gulfbusiness.com/category/insurance/",
        "https://saudigazette.com.sa/tag/insurance",
        "https://www.khaleejtimes.com/business/insurance",
        "https://www.centralbank.ae/en/our-services/insurance-services",
        "https://www.sama.gov.sa/en-us/pages/default.aspx",
    ],
    "South America (LATAM)": [
        "https://www.lataminsurancereview.com/",
        "https://www.bnamericas.com/en/sector/insurance",
        "https://valor.globo.com/financas/seguros/",
        "http://cnseg.org.br/",
        "https://www.eleconomista.com.mx/sectorfinanciero/seguros-y-pensiones",
        "https://www.amis.com.mx/",
        "https://www.df.cl/mercados/banca-seguros",
    ],
    "Africa": [
        "https://www.africainsurancereview.com/",
        "https://www.businessdailyafrica.com/bd/corporate/insurance",
    ]
}

# CXO-Trusted Source Whitelist
SOURCE_WHITELIST = {

    # 1. CORE INSURANCE INDUSTRY (GLOBAL, DEEP COVERAGE)
    "industry_insurance": [
        {"name": "Insurance Journal", "rss": "https://www.insurancejournal.com/rss/news/"},
        {"name": "Insurance Business Magazine (Global)", "rss": "https://www.insurancebusinessmag.com/rss/news/"},
        {"name": "PropertyCasualty360", "rss": "https://www.propertycasualty360.com/feed/"},
        {"name": "Digital Insurance", "rss": "https://www.dig-in.com/feed"},
        {"name": "Asia Insurance Review", "rss": "https://www.asiainsurancereview.com/rss"},
        {"name": "Reinsurance News", "rss": "https://www.reinsurancene.ws/feed/"},
        {"name": "Insurance Times (UK)", "rss": "https://www.insurancetimes.co.uk/rss"},
        {"name": "Post Magazine (UK)", "rss": "https://www.postonline.co.uk/rss"},
        {"name": "The Insurer (re/insurance intelligence)", "rss": "https://www.theinsurer.com/rss"},
        {"name": "Global Reinsurance", "rss": "https://www.globalreinsurance.com/rss"},
    ],

    # 2. EMPLOYEE BENEFITS, HEALTH & GROUP INSURANCE (SPECIAL FOCUS)
    "employee_benefits_health": [
        {"name": "Employee Benefit News (EBN)", "rss": "https://www.benefitnews.com/feed"},
        {"name": "BenefitsPRO", "rss": "https://www.benefitspro.com/feed/"},
        {"name": "HR Dive – Benefits", "rss": "https://www.hrdive.com/feeds/topic/benefits/"},
        {"name": "Managed Healthcare Executive", "rss": "https://www.managedhealthcareexecutive.com/rss"},
        {"name": "Modern Healthcare", "rss": "https://www.modernhealthcare.com/rss"},
        {"name": "Healthcare Dive", "rss": "https://www.healthcaredive.com/feeds/news/"},
        {"name": "Becker’s Health Payer", "rss": "https://www.beckerspayer.com/rss.xml"},
        {"name": "Society for Human Resource Management (SHRM)", "rss": "https://www.shrm.org/rss"},
    ],

    # 3. INSURTECH, DIGITAL & PLATFORM ECONOMY
    "insurtech_digital": [
        {"name": "InsurTech News", "rss": "https://insurtechnews.com/feed/"},
        {"name": "The Digital Insurer", "rss": "https://www.the-digital-insurer.com/feed/"},
        {"name": "Coverager", "rss": "https://coverager.com/feed/"},
        {"name": "InsurTech Insights", "rss": "https://www.insurtechinsights.com/feed"},
        {"name": "FinTech Futures – Insurance", "rss": "https://www.fintechfutures.com/category/insurance/feed/"},
        {"name": "VentureBeat – AI & Enterprise", "rss": "https://venturebeat.com/feed/"},
    ],

    # 4. REGULATION, POLICY & SUPERVISION (HIGH CXO SIGNAL)
    "regulatory_policy": [
        {"name": "NAIC (US)", "rss": "https://content.naic.org/rss"},
        {"name": "EIOPA (EU Insurance Regulator)", "rss": "https://www.eiopa.europa.eu/rss_en"},
        {"name": "IRDAI (India)", "rss": "https://irdai.gov.in/rss"},
        {"name": "UK FCA News", "rss": "https://www.fca.org.uk/news/rss.xml"},
        {"name": "US Department of Labor – EBSA", "rss": "https://www.dol.gov/rss"},
        {"name": "European Commission – Financial Services", "rss": "https://ec.europa.eu/info/news/rss_en"},
    ],

    # 5. M&A, CAPITAL MARKETS & STRATEGY
    "mna_capital_markets": [
        {"name": "Reuters – Insurance", "rss": "https://www.reuters.com/finance/insurance/rss"},
        {"name": "Bloomberg – Insurance", "rss": "https://www.bloomberg.com/feeds/markets"},
        {"name": "S&P Global Market Intelligence", "rss": "https://www.spglobal.com/rss"},
        {"name": "PitchBook News", "rss": "https://pitchbook.com/rss"},
        {"name": "Mergermarket", "rss": "https://www.mergermarket.com/rss"},
        {"name": "Private Equity News", "rss": "https://www.penews.com/feed"},
    ],

    # 6. CONSULTING, THINK TANKS & ADVISORY (INSURANCE-SPECIFIC)
    "consulting_advisory": [
        {"name": "McKinsey – Insurance", "rss": "https://www.mckinsey.com/industries/financial-services/our-insights/rss"},
        {"name": "BCG – Insurance", "rss": "https://www.bcg.com/rss"},
        {"name": "Bain – Financial Services", "rss": "https://www.bain.com/rss/"},
        {"name": "Deloitte – Insurance Insights", "rss": "https://www2.deloitte.com/us/en/feeds/insurance.xml"},
        {"name": "PwC – Insurance", "rss": "https://www.pwc.com/gx/en/industries/financial-services/insurance/rss.xml"},
        {"name": "Capgemini World Insurance Report", "rss": "https://www.capgemini.com/rss"},
    ],

    # 7. CYBER, DATA PRIVACY & OPERATIONAL RISK
    "cyber_risk": [
        {"name": "Dark Reading", "rss": "https://www.darkreading.com/rss.xml"},
        {"name": "The Record by Recorded Future", "rss": "https://therecord.media/feed"},
        {"name": "Bleeping Computer", "rss": "https://www.bleepingcomputer.com/feed/"},
        {"name": "CSO Online", "rss": "https://www.csoonline.com/feed/"},
        {"name": "ISACA Journal", "rss": "https://www.isaca.org/rss"},
    ],

    # 8. GENERAL BUSINESS (FILTERED, LOW NOISE)
    "general_business": [
        {"name": "Financial Times – Insurance", "rss": "https://www.ft.com/insurance?format=rss"},
        {"name": "Wall Street Journal – Risk & Insurance", "rss": "https://feeds.a.dj.com/rss/RiskandCompliance.xml"},
        {"name": "The Economist – Finance", "rss": "https://www.economist.com/finance-and-economics/rss.xml"},
        {"name": "CNBC – Finance", "rss": "https://www.cnbc.com/id/10001147/device/rss/rss.html"},
    ]
}

# SOURCE_WHITELIST = {
#    "industry_insurance": [
#         {"name": "Insurance Business Magazine", "rss": "https://www.insurancebusinessmag.com/us/rss/news/"},
#         {"name": "Digital Insurance", "rss": "https://www.dig-in.com/feed"},
#         {"name": "Insurance Journal", "rss": "https://www.insurancejournal.com/rss/news/"},
#         {"name": "PropertyCasualty360", "rss": "https://www.propertycasualty360.com/feed/"},
#         {"name": "Asia Insurance Review", "rss": "https://www.asiainsurancereview.com/rss"},
#     ],
#     "consulting_advisory": [
#         {"name": "McKinsey Insurance", "rss": "https://www.mckinsey.com/industries/financial-services/our-insights/rss"},
#         {"name": "Deloitte Insights", "rss": "https://www2.deloitte.com/us/en/insights/rss-feeds.html"},
#         {"name": "PwC Insights", "rss": "https://www.pwc.com/gx/en/feeds/insights.rss"},
#     ],
#     "cyber_risk": [
#         {"name": "Reuters Business", "rss": "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best"},
#         {"name": "Dark Reading", "rss": "https://www.darkreading.com/rss.xml"},
#         {"name": "Bleeping Computer", "rss": "https://www.bleepingcomputer.com/feed/"},
#         {"name": "The Record", "rss": "https://therecord.media/feed"},
#     ],
#     "technology": [
#         {"name": "TechCrunch Enterprise", "rss": "https://techcrunch.com/category/enterprise/feed/"},
#         {"name": "ZDNet", "rss": "https://www.zdnet.com/topic/security/rss.xml"},
#     ],
#     "general_business": [
#         {"name": "Financial Times", "rss": "https://www.ft.com/rss/home"},
#         {"name": "BBC Business", "rss": "http://feeds.bbci.co.uk/news/business/rss.xml"},
#         {"name": "CNBC", "rss": "https://www.cnbc.com/id/10001147/device/rss/rss.html"},
#     ]
# }


def get_generation_prompt(articles_json: str, today_date: str) -> str:
    """Generate the master prompt for newsletter content generation."""
    
    return f"""
Based on the following news articles from the last 24 hours, generate a CXO Insurance & BFSI Intelligence Brief.

TODAY'S DATE: {today_date}
COVERAGE WINDOW: Last 24 Hours

ARTICLES TO ANALYZE:
{articles_json}

---

Generate the newsletter with EXACTLY this structure:

## 1️⃣ EXECUTIVE SNAPSHOT (60-Second Read)

Provide 3-5 crisp bullets answering:
- What changed?
- Why it matters NOW
- Who should care (CEO / CIO / CRO / CHRO)

Write like a board pre-read, not commentary.

---

## 2️⃣ STRATEGIC THEMES EMERGING TODAY

Identify 3 dominant themes from today's signals.
Format each as:
**Theme Name:** One-line strategic insight explaining the shift or implication

---

## 3️⃣ CURATED INTELLIGENCE

For each significant item (max 10-15), use this structure:

**[Headline]**
*Source | Geography | Theme*

**Why this matters:**
- Strategic implication (2-3 lines)
- Risk or opportunity
- Time horizon: Now / Near / Long

Focus on IMPLICATION, not description.

---

## 4️⃣ COMPETITIVE & PEER SIGNALS

Cover in bullet format:
- Moves by insurers, MGAs, reinsurers
- Leadership appointments
- Capability build-outs
- Strategic pivots

---

## 5️⃣ TECHNOLOGY & AI RADAR

Highlight:
- New AI / GenAI use cases in insurance/BFSI
- Platforms gaining traction
- Signals of operating leverage or cost takeout

No vendor hype. Neutral tone.

---

## 6️⃣ RISK & THREAT WATCH

Summarize:
- Cyber incidents affecting financial services
- Regulatory or compliance risks
- Geopolitical or systemic threats

Frame in business exposure, not technical detail.

---

## 7️⃣ CXO ACTION CUES

- **WATCH:** Early indicators worth monitoring
- **PREPARE:** Likely next moves to plan for
- **ACT:** Immediate considerations

---

CRITICAL RULES:
1. Only include items a CXO would care about in the next board or exec meeting
2. No fluff, no marketing language
3. Consulting-grade, boardroom-ready tone
4. If fewer than 15 high-quality items exist, return fewer - do NOT dilute quality
"""

def get_quality_scoring_prompt(article: dict) -> str:
    """Prompt to score an article for CXO relevance."""
    return f"""
Score this article for CXO Insurance/BFSI relevance:

HEADLINE: {article.get('headline', '')}
SOURCE: {article.get('source', '')}
SUMMARY: {article.get('summary', '')}

Score on:
1. CXO Relevance: High / Medium / Low
2. Industry Impact: Local / Regional / Global
3. Novelty: Incremental / Meaningful / Disruptive
4. Theme: Which of these applies?
   - Regulation, Policy & Compliance
   - M&A, Partnerships & Strategic Moves
   - Technology & Operating Model Disruption
   - AI, Automation & Advanced Analytics
   - Cybersecurity & Risk Landscape
   - Market, Macro & Geopolitical Risk
   - Customer, Distribution & Experience
   - Talent, Workforce & Future of Work
   - Industry Thought Leadership

Return JSON format:
{{"include": true/false, "relevance": "High/Medium/Low", "impact": "Local/Regional/Global", "novelty": "Incremental/Meaningful/Disruptive", "theme": "Theme Name", "reason": "One line why"}}

Only return include=true for High relevance + Meaningful/Disruptive novelty.
"""
