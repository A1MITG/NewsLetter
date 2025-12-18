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

# CXO-Trusted Source Whitelist
SOURCE_WHITELIST = {
    "industry_insurance": [
        {"name": "Insurance Business Magazine", "rss": "https://www.insurancebusinessmag.com/us/rss/news/"},
        {"name": "Digital Insurance", "rss": "https://www.dig-in.com/feed"},
        {"name": "Insurance Journal", "rss": "https://www.insurancejournal.com/rss/news/"},
        {"name": "PropertyCasualty360", "rss": "https://www.propertycasualty360.com/feed/"},
        {"name": "Asia Insurance Review", "rss": "https://www.asiainsurancereview.com/rss"},
    ],
    "consulting_advisory": [
        {"name": "McKinsey Insurance", "rss": "https://www.mckinsey.com/industries/financial-services/our-insights/rss"},
        {"name": "Deloitte Insights", "rss": "https://www2.deloitte.com/us/en/insights/rss-feeds.html"},
        {"name": "PwC Insights", "rss": "https://www.pwc.com/gx/en/feeds/insights.rss"},
    ],
    "cyber_risk": [
        {"name": "Reuters Business", "rss": "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best"},
        {"name": "Dark Reading", "rss": "https://www.darkreading.com/rss.xml"},
        {"name": "Bleeping Computer", "rss": "https://www.bleepingcomputer.com/feed/"},
        {"name": "The Record", "rss": "https://therecord.media/feed"},
    ],
    "technology": [
        {"name": "TechCrunch Enterprise", "rss": "https://techcrunch.com/category/enterprise/feed/"},
        {"name": "ZDNet", "rss": "https://www.zdnet.com/topic/security/rss.xml"},
    ],
    "general_business": [
        {"name": "Financial Times", "rss": "https://www.ft.com/rss/home"},
        {"name": "BBC Business", "rss": "http://feeds.bbci.co.uk/news/business/rss.xml"},
        {"name": "CNBC", "rss": "https://www.cnbc.com/id/10001147/device/rss/rss.html"},
    ]
}

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

For each significant item (max 10-12), use this structure:

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
4. If fewer than 10 high-quality items exist, return fewer - do NOT dilute quality
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
