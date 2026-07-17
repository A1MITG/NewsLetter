# Markdown formatting for newsletter - CXO Executive Brief Format
from datetime import datetime

def format_markdown(top_stories, themes, risks, competitive, tech_signals, now: datetime):
    """Generate Big-4 consulting-grade CXO Intelligence Brief."""
    
    date_str = now.strftime('%d %B %Y')
    date_str = now.strftime('%d %B %Y')
    weekday = now.strftime('%A')

    md = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# CXO DAILY INSURANCE INTELLIGENCE BRIEF
## (Chief-of-Staff Vetted | Big-4 Standard)

**{weekday}, {date_str}** | Coverage: Last 24 Hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ **One-Line Executive Take (Most Important)**

"""
    # Section 1: One-Line Executive Take
    if top_stories:
        # Find the most important story and generate a one-line take
        main_story = top_stories[0]
        take = main_story.get('executive_take') or main_story.get('summary', main_story.get('headline', 'No material CXO-level developments in the last 24 hours.'))
        # Enforce 25 words max, no adjectives/hype
        take = ' '.join(take.split()[:25])
        md += f"{take}\n"
    else:
        md += "No material CXO-level developments in the last 24 hours.\n"

    md += """

2️⃣ **Executive Snapshot (≤120 words)**
"""
    # Section 2: Executive Snapshot
    if top_stories:
        for s in top_stories[:4]:
            signal = s.get('signal', s.get('headline', ''))
            implication = s.get('implication', s.get('summary', ''))
            impacted = s.get('impacted', s.get('cxo', 'CXO'))
            md += f"- {signal} → {implication} → {impacted}\n"
    else:
        md += "- No material CXO-level developments in the last 24 hours.\n"

    md += """

3️⃣ **Key Developments by Lens**

A. **Business & Strategy**
"""
    # Section 3A: Business & Strategy
    for s in top_stories:
        if s.get('lens') == 'Business & Strategy':
            md += f"- {s.get('headline','')}\n  - Why: {s.get('why','')}\n  - Second-order: {s.get('second_order','')}\n  Source: {s.get('source','')} ([link]({s.get('url','')}))\n"

    md += """
B. **Regulation, Policy & Compliance**
"""
    for s in top_stories:
        if s.get('lens') == 'Regulation, Policy & Compliance':
            md += f"- {s.get('headline','')}\n  - Jurisdiction: {s.get('jurisdiction','')}\n  - Nature: {s.get('nature','')}\n  - Risk: {s.get('risk','')}\n  - Horizon: {s.get('horizon','')}\n  Source: {s.get('source','')} ([link]({s.get('url','')}))\n"

    md += """
C. **Technology, Data & AI**
"""
    for s in top_stories:
        if s.get('lens') == 'Technology, Data & AI':
            md += f"- {s.get('headline','')}\n  - Function: {s.get('function','')}\n  - Reality: {s.get('reality','')}\n  Source: {s.get('source','')} ([link]({s.get('url','')}))\n"

    md += """
D. **M&A, Partnerships & Capital Moves**
"""
    for s in top_stories:
        if s.get('lens') == 'M&A, Partnerships & Capital Moves':
            md += f"- {s.get('headline','')}\n  - Buyer/Seller/Partner: {s.get('party','')}\n  - Rationale: {s.get('rationale','')}\n  - Competitive: {s.get('competitive','')}\n  Source: {s.get('source','')} ([link]({s.get('url','')}))\n"

    md += """
E. **Employee Benefits & Health (If Material)**
"""
    for s in top_stories:
        if s.get('lens') == 'Employee Benefits & Health':
            md += f"- {s.get('headline','')}\n  - Focus: {s.get('focus','')}\n  Source: {s.get('source','')} ([link]({s.get('url','')}))\n"

    md += """

4️⃣ **Risk & Opportunity Register (Tabular – Mandatory)**

| Signal | Category | Impact | Likelihood | Primary CXO |
|--------|----------|--------|------------|-------------|
"""
    # Section 4: Risk & Opportunity Register
    if risks:
        for r in risks[:5]:
            md += f"| {r.get('signal','')} | {r.get('category','')} | {r.get('impact','')} | {r.get('likelihood','')} | {r.get('cxo','')} |\n"
    else:
        md += "| No material risks or opportunities | | | | |\n"

    md += """

5️⃣ **CXO Action Brief (Decision-Oriented)**
"""
    # Section 5: CXO Action Brief
    if top_stories:
        for s in top_stories:
            if s.get('action'):
                md += f"- {s['action']}\n"
    else:
        md += "- No immediate actions required.\n"

    md += """

6️⃣ **Source Traceability (Clean & Minimal)**
"""
    # Section 6: Source Traceability
    if top_stories:
        for s in top_stories:
            md += f"- {s.get('source','')} ([link]({s.get('url','')}))\n"
    else:
        md += "- No sources.\n"

    md += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_© {now.year} CXO Intelligence Unit | Confidential_

"""
    return md
    return md
