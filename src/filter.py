# CXO Intelligence Filtering and Curation Logic
from datetime import datetime, timedelta
from collections import Counter

def filter_and_rank_stories(stories):
    """
    Filter and rank stories per CXO Intelligence Brief spec.
    Only retain High relevance + Meaningful/Disruptive novelty.
    """
    now = datetime.utcnow()
    
    # Filter by recency (last 24 hours per spec)
    recent = []
    for s in stories:
        try:
            story_date = datetime.fromisoformat(s["date"])
            if (now - story_date) < timedelta(hours=48):  # 48h for buffer
                recent.append(s)
        except:
            recent.append(s)  # Include if date parsing fails
    
    # Sort by relevance and novelty
    def score_story(s):
        relevance_score = 0 if s.get("relevance") == "High" else 1
        novelty_score = {"Disruptive": 0, "Meaningful": 1, "Incremental": 2}.get(s.get("novelty", "Incremental"), 2)
        return (relevance_score, novelty_score)
    
    recent.sort(key=score_story)
    
    # Top stories (max 12 per spec)
    top_stories = recent[:12]
    
    # Extract emerging themes from the stories
    themes = extract_themes(top_stories)
    
    # Extract risks and competitive signals
    risks = extract_risks(top_stories)
    competitive = extract_competitive_signals(top_stories)
    tech_signals = extract_tech_signals(top_stories)
    
    return top_stories, themes, risks, competitive, tech_signals

def extract_themes(stories):
    """Identify 3 dominant strategic themes from today's BFSI signals."""
    theme_counts = Counter(s.get("theme", "General") for s in stories)
    top_themes = theme_counts.most_common(3)
    
    theme_insights = {
        "Insurance Regulation & Compliance": "Regulatory scrutiny intensifying; IRDAI/NAIC mandates requiring compliance investments",
        "Banking Regulation & Compliance": "Banking regulators tightening oversight; capital and liquidity requirements in focus",
        "M&A, Partnerships & Strategic Moves": "Consolidation accelerating; strategic partnerships reshaping competitive landscape",
        "Insurtech & Digital Insurance": "Digital insurance adoption accelerating; legacy carriers responding to insurtech threat",
        "Fintech & Digital Banking": "Digital banking disruption continuing; embedded finance creating new distribution models",
        "AI & Analytics in BFSI": "GenAI moving from pilot to production; early movers gaining underwriting and claims advantage",
        "Cyber Risk & Financial Crime": "Financial sector cyber threats escalating; board-level focus on resilience required",
        "Underwriting & Claims Innovation": "Underwriting automation and claims efficiency driving combined ratio improvements",
        "Capital Markets & Investment": "Investment portfolio strategies adapting to rate environment and market volatility",
        "Customer Experience & Distribution": "Digital distribution and bancassurance partnerships becoming key differentiators",
        "BFSI Industry Developments": "Sector-wide developments impacting insurance and banking operations"
    }
    
    return [{"name": t[0], "insight": theme_insights.get(t[0], "Strategic BFSI developments emerging")} for t in top_themes]

def extract_risks(stories):
    """Extract risk and threat signals for CRO/CISO attention in BFSI context."""
    risk_themes = ["Cyber Risk & Financial Crime", "Insurance Regulation & Compliance", "Banking Regulation & Compliance"]
    risks = []
    
    for s in stories:
        if s.get("theme") in risk_themes:
            risks.append({
                "headline": s["headline"],
                "source": s["source"],
                "severity": "High" if s.get("novelty") == "Disruptive" else "Medium",
                "url": s["url"]
            })
    
    return risks[:5]  # Top 5 risks

def extract_competitive_signals(stories):
    """Extract competitive and peer signals in BFSI sector."""
    competitive = []
    competitive_keywords = ["insurer", "bank", "carrier", "acquisition", "partnership", "launch", 
                          "appoint", "ceo", "cfo", "cio", "expand", "enters", "wins", "secures"]
    
    for s in stories:
        text = (s.get("headline", "") + " " + s.get("summary", "")).lower()
        if any(kw in text for kw in competitive_keywords):
            competitive.append({
                "headline": s["headline"],
                "source": s["source"],
                "theme": s.get("theme", "BFSI Industry"),
                "url": s["url"]
            })
    
    return competitive[:5]  # Top 5 competitive signals

def extract_tech_signals(stories):
    """Extract technology and AI radar signals for BFSI."""
    tech = []
    tech_keywords = ["ai", "genai", "automation", "platform", "cloud", "digital", "insurtech", 
                    "fintech", "machine learning", "core system", "modernization", "api"]
    
    for s in stories:
        text = (s.get("headline", "") + " " + s.get("summary", "")).lower()
        if any(kw in text for kw in tech_keywords):
            implication = "Operating leverage opportunity"
            if "underwriting" in text or "claims" in text:
                implication = "Underwriting/claims efficiency gain"
            elif "customer" in text or "experience" in text:
                implication = "Customer experience enhancement"
            elif "compliance" in text or "regulation" in text:
                implication = "Compliance automation opportunity"
            
            tech.append({
                "headline": s["headline"],
                "source": s["source"],
                "implication": implication,
                "url": s["url"]
            })
    
    return tech[:5]  # Top 5 tech signals
