# Markdown formatting for newsletter
from datetime import datetime

def format_markdown(top_stories, trends, risks, now: datetime):
    md = f"""# CXO Morning Intel — {now.strftime('%Y-%m-%d')}

## Top 5 Stories\n"""
    for i, s in enumerate(top_stories, 1):
        md += f"- **Story {i}**: [{s['headline']}]({s['url']}) [Impact: {s['impact']}] [Virality: {s['virality']}] [Source: {s['source']}]\n  {s['summary']} CXO Actionable: [Review, Share] \n\n"
    md += "## Trends Radar\n"
    for t in trends:
        md += f"- {t}\n"
    md += "\n## Risks Alert\n"
    for r in risks:
        md += f"- {r}\n"
    md += "\n---\nSources: Reuters, Bloomberg, ET BFSI, CXOToday, CIO Dive, Insurance Times, Forbes Tech Council, KPMG, Accenture.\n"
    return md
