"""
Insurance-Only CXO Intelligence Brief
Big-4 Standard | Chief-of-Staff Vetted | Continuum Labs
"""

import datetime
import pytz
from .sources import scan_all_sources
from .filter import filter_and_rank_stories

IST = pytz.timezone('Asia/Kolkata')

# Insurance-specific keywords for strict filtering (must have at least one)
INSURANCE_KEYWORDS = [
    'insurance', 'insurer', 'reinsurance', 'reinsurer', 'underwriting', 'underwriter',
    'policyholder', 'premium', 'actuarial', 'actuary', 'loss ratio', 'combined ratio',
    'solvency', 'p&c', 'property casualty', 'life insurance', 'health insurance',
    'annuity', 'mga', 'tpa', 'captive', 'insurtech', 'irdai', 'naic',
    'eiopa', 'lloyd', 'cat bond', 'catastrophe bond', 'reserving', 'pricing model',
    'policy admin', 'carrier', 'bancassurance', 'risk transfer', 'cedant',
    'retrocession', 'excess of loss', 'quota share', 'treaty', 'facultative'
]

# Exclude keywords - non-insurance content that should never appear
EXCLUDE_KEYWORDS = [
    # Retail/Consumer (not insurance)
    'ftc', 'federal trade commission', 'retailer', 'retail store', 'grocery', 'instacart',
    'doordash', 'uber eats', 'amazon prime', 'subscription service', 'e-commerce',
    'consumer complaint', 'refund customers', 'deceptive subscription',
    
    # Banking/Payments (not insurance)
    'payment gateway', 'lending platform', 'loan origination', 'mortgage lender', 
    'credit card issuer', 'neobank', 'capital markets', 'trading platform', 'hedge fund',
    'cryptocurrency', 'bitcoin', 'blockchain wallet',
    
    # Generic cyber/security (not insurer-specific)
    'fbi', 'nhs breach', 'retail breach', 'government it', 'public sector breach',
    'hospital it', 'school district', 'municipality', 'city government',
    
    # Marketing/PR noise
    'award winner', 'thought leadership', 'webinar', 'podcast episode', 'sponsored content',
    
    # Healthcare providers (not insurers)
    'hospital system', 'health system', 'medical center', 'clinic network'
]

# Strong insurance signals - if present, article is definitely insurance-related
STRONG_INSURANCE_SIGNALS = [
    'insurance carrier', 'insurance company', 'life insurer', 'p&c insurer',
    'health insurer', 'reinsurer', 'lloyd', 'underwriting', 'actuarial',
    'cat bond', 'solvency', 'irdai', 'naic', 'eiopa', 'insurance regulator',
    'mga', 'managing general agent', 'insurtech', 'claims processing',
    'policy administration', 'loss ratio', 'combined ratio', 'premium volume'
]


def is_insurance_relevant(story):
    """Strict filter: Only include insurance-specific content."""
    headline = story.get('headline', '').lower()
    summary = story.get('summary', '').lower()
    text = headline + ' ' + summary
    source = story.get('source', '').lower()
    category = story.get('category', '').lower()
    
    # HARD EXCLUDE: If contains any exclude keyword, reject immediately
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return False
    
    # Check for strong insurance signals (high confidence)
    has_strong_signal = any(kw in text for kw in STRONG_INSURANCE_SIGNALS)
    
    # Check for basic insurance keywords
    has_insurance_keyword = any(kw in text for kw in INSURANCE_KEYWORDS)
    
    # Source-based validation
    is_insurance_source = category in ['insurance', 'reinsurance', 'insurtech', 'benefits']
    is_native_source = story.get('bfsi_native', False)
    
    # Decision logic:
    # 1. Strong signal = include
    if has_strong_signal:
        return True
    
    # 2. Insurance keyword + insurance-native source = include
    if has_insurance_keyword and is_native_source:
        return True
    
    # 3. Insurance keyword + insurance category = include
    if has_insurance_keyword and is_insurance_source:
        return True
    
    # 4. Generic "claims" or "fraud" without insurance context = exclude
    # These words appear in non-insurance contexts (FTC claims, retail fraud, etc.)
    ambiguous_words = ['claims', 'fraud', 'broker', 'pricing', 'distribution']
    if any(w in text for w in ambiguous_words) and not has_insurance_keyword:
        return False
    
    # 5. Insurance keyword from non-native source = include only if headline is insurance-focused
    if has_insurance_keyword and any(kw in headline for kw in INSURANCE_KEYWORDS):
        return True
    
    return False


def categorize_story(story):
    """Categorize story into thematic sections."""
    headline = story.get('headline', '').lower()
    summary = story.get('summary', '').lower()
    text = headline + ' ' + summary
    category = story.get('category', '')
    
    # Technology & AI
    if any(kw in text for kw in ['ai', 'genai', 'machine learning', 'automation', 'platform', 'digital', 'technology', 'cloud', 'data']):
        if any(kw in text for kw in INSURANCE_KEYWORDS):
            return 'tech_ai'
    
    # Risk, Regulation & Trust
    if any(kw in text for kw in ['regulation', 'regulatory', 'compliance', 'solvency', 'capital', 'cyber', 'breach', 'irdai', 'naic', 'eiopa', 'fca', 'reserve', 'risk']):
        return 'risk_regulation'
    
    # Partner & Vendor Signals
    if any(kw in text for kw in ['partner', 'vendor', 'platform', 'consolidat', 'acquire', 'merger', 'deal']):
        return 'partner_vendor'
    
    # Default: Strategic Insurance Developments
    return 'strategic'


def generate_newsletter_html():
    now = datetime.datetime.now(IST)
    stories = scan_all_sources()
    top_stories, themes, risks, competitive, tech_signals = filter_and_rank_stories(stories)
    date_str = now.strftime('%A, %d %B %Y')
    time_str = now.strftime('%H:%M') + " IST"
    
    # Apply strict insurance filter
    insurance_stories = [s for s in top_stories if is_insurance_relevant(s)]
    
    # Categorize stories
    strategic = []
    tech_ai = []
    risk_regulation = []
    partner_vendor = []
    
    for story in insurance_stories:
        cat = categorize_story(story)
        # Adjusted limits for each category to allow more articles
        if cat == 'tech_ai' and len(tech_ai) < 4:
            tech_ai.append(story)
        elif cat == 'risk_regulation' and len(risk_regulation) < 4:
            risk_regulation.append(story)
        elif cat == 'partner_vendor' and len(partner_vendor) < 4:
            partner_vendor.append(story)
        elif len(strategic) < 8:
            strategic.append(story)
    
    # Generate executive pulse
    executive_pulse = generate_executive_pulse(insurance_stories)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance CXO Intelligence Brief — {date_str}</title>
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap' rel='stylesheet'>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; 
            background: #0f172a; 
            color: #1e293b; 
            min-height: 100vh; 
            padding: 40px 20px;
            line-height: 1.6;
        }}
        
        .container {{ max-width: 800px; margin: 0 auto; }}
        
        /* Header */
        .header {{
            background: linear-gradient(135deg, #0c1929 0%, #1a365d 100%);
            border-radius: 12px 12px 0 0;
            padding: 40px 48px;
            color: #fff;
            position: relative;
        }}
        .header::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6, #3b82f6);
        }}
        
        .logo-row {{
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 20px;
        }}
        .logo {{
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 800;
            color: #fff;
        }}
        .brand {{
            font-size: 1em;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        
        .header-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.9em;
            font-weight: 600;
            margin-bottom: 6px;
        }}
        .header-subtitle {{
            color: #94a3b8;
            font-size: 0.9em;
            margin-bottom: 16px;
        }}
        .header-meta {{
            display: flex;
            gap: 20px;
            font-size: 0.85em;
            color: #cbd5e1;
        }}
        
        /* Main */
        .main {{ background: #fff; }}
        
        /* Executive Pulse */
        .pulse {{
            background: linear-gradient(135deg, #1e3a5f, #0f2744);
            padding: 28px 48px;
            border-bottom: 2px solid #3b82f6;
        }}
        .pulse-label {{
            display: inline-block;
            background: rgba(251, 191, 36, 0.15);
            color: #fbbf24;
            font-size: 0.65em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            padding: 5px 12px;
            border-radius: 4px;
            margin-bottom: 12px;
        }}
        .pulse-text {{
            font-size: 1.15em;
            color: #f1f5f9;
            font-weight: 500;
            line-height: 1.5;
        }}
        
        /* Section */
        .section {{
            padding: 32px 48px;
            border-bottom: 1px solid #e2e8f0;
        }}
        .section:last-child {{ border-bottom: none; }}
        .section-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }}
        .section-icon {{
            font-size: 1.1em;
        }}
        .section-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.15em;
            color: #1e293b;
            font-weight: 600;
        }}
        
        /* Article List */
        .article-list {{
            list-style: none;
        }}
        .article-item {{
            padding: 16px 0;
            border-bottom: 1px solid #f1f5f9;
        }}
        .article-item:last-child {{
            border-bottom: none;
            padding-bottom: 0;
        }}
        .article-headline {{
            font-size: 1em;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 6px;
            line-height: 1.4;
        }}
        .article-headline a {{
            color: inherit;
            text-decoration: none;
        }}
        .article-headline a:hover {{
            color: #3b82f6;
        }}
        .article-meta {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8em;
            color: #64748b;
            margin-bottom: 8px;
        }}
        .article-source {{
            background: #f1f5f9;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 500;
        }}
        .article-summary {{
            font-size: 0.9em;
            color: #475569;
            line-height: 1.5;
        }}
        .article-link {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            color: #3b82f6;
            font-size: 0.85em;
            font-weight: 600;
            text-decoration: none;
            margin-top: 8px;
        }}
        .article-link:hover {{
            text-decoration: underline;
        }}
        
        /* Empty State */
        .empty {{
            color: #94a3b8;
            font-style: italic;
            font-size: 0.9em;
            padding: 12px 0;
        }}
        
        /* Footer */
        .footer {{
            background: #f8fafc;
            padding: 28px 48px;
            border-radius: 0 0 12px 12px;
        }}
        .footer-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
        }}
        .footer-logo {{
            width: 28px;
            height: 28px;
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 800;
            color: #fff;
        }}
        .footer-name {{
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #475569;
            font-size: 0.85em;
        }}
        .footer-text {{
            font-size: 0.75em;
            color: #94a3b8;
            line-height: 1.6;
        }}
        
        @media (max-width: 768px) {{
            .header, .pulse, .section, .footer {{
                padding-left: 24px;
                padding-right: 24px;
            }}
            .header-title {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="logo-row">
                <div class="logo">CL</div>
                <span class="brand">Continuum Labs</span>
            </div>
            <h1 class="header-title">Insurance Intelligence Brief</h1>
            <div class="header-meta">
                <span>📅 {date_str}</span>
                <span>🕐 {time_str}</span>
                <span>📊 Last 24 Hours</span>
            </div>
        </header>
        
        <main class="main">
            <!-- Executive Pulse -->
            <div class="pulse">
                <div class="pulse-label">⚡ Executive Pulse</div>
                <p class="pulse-text">{executive_pulse}</p>
            </div>
            
            <!-- Strategic Insurance Developments -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">📊</span>
                    <h2 class="section-title">Strategic Insurance Developments</h2>
                </div>
                <ul class="article-list">
"""
    
    for s in strategic[:8]:
        html += generate_article_item(s)
    
    if not strategic:
        html += '<li class="empty">No material strategic developments in the last 24 hours.</li>'
    
    html += """
                </ul>
            </div>
            
            <!-- Technology & AI (Insurance-Only) -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">🤖</span>
                    <h2 class="section-title">Technology & AI (Insurance-Only)</h2>
                </div>
                <ul class="article-list">
"""
    
    for s in tech_ai[:4]:
        html += generate_article_item(s)
    
    if not tech_ai:
        html += '<li class="empty">No material insurance technology developments in the last 24 hours.</li>'
    
    html += """
                </ul>
            </div>
            
            <!-- Risk, Regulation & Trust -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">⚖️</span>
                    <h2 class="section-title">Risk, Regulation & Trust</h2>
                </div>
                <ul class="article-list">
"""
    
    for s in risk_regulation[:4]:
        html += generate_article_item(s)
    
    if not risk_regulation:
        html += '<li class="empty">No material regulatory or risk developments in the last 24 hours.</li>'
    
    html += """
                </ul>
            </div>
"""
    
    # Partner & Vendor Signals (optional)
    if partner_vendor:
        html += """
            <!-- Partner & Vendor Signals -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">🤝</span>
                    <h2 class="section-title">Partner & Vendor Signals</h2>
                </div>
                <ul class="article-list">
"""
        for s in partner_vendor[:4]:
            html += generate_article_item(s)
        html += """
                </ul>
            </div>
"""
    
    html += f"""
        </main>
        
        <footer class="footer">
            <div class="footer-brand">
                <div class="footer-logo">CL</div>
                <span class="footer-name">Continuum Labs</span>
            </div>
            <p class="footer-text">
                Insurance-only intelligence for CXO decision-makers. Board-ready, no-clutter, actionable.<br>
                © {now.year} Continuum Labs. Classification: Internal Use Only.
            </p>
        </footer>
    </div>
</body>
</html>
"""
    return html


def generate_executive_pulse(stories):
    """Generate one-line executive pulse."""
    if not stories:
        return "No material insurance developments in the last 24 hours."
    
    # Find most impactful story
    top = stories[0]
    headline = top.get('headline', '')
    
    # Create sharp, decision-oriented pulse
    if 'acquire' in headline.lower() or 'merger' in headline.lower() or 'm&a' in headline.lower():
        return f"Sector consolidation signal: {headline[:90]} — strategic positioning review warranted."
    elif 'regul' in headline.lower() or 'irdai' in headline.lower() or 'naic' in headline.lower():
        return f"Regulatory shift detected: {headline[:90]} — compliance and capital teams to assess."
    elif 'cyber' in headline.lower() or 'breach' in headline.lower():
        return f"Risk event: {headline[:90]} — CISO and CRO briefing recommended."
    elif 'ai' in headline.lower() or 'technology' in headline.lower() or 'digital' in headline.lower():
        return f"Technology signal: {headline[:90]} — operating model implications to evaluate."
    elif 'cat bond' in headline.lower() or 'reinsurance' in headline.lower():
        return f"Capital markets movement: {headline[:90]} — CFO and reinsurance teams to monitor."
    else:
        return f"{headline[:100]} — CXO attention warranted."


def generate_article_item(story):
    """Generate HTML for a single article item."""
    headline = story.get('headline', 'No headline')
    source = story.get('source', 'Source')
    url = story.get('url', '#')
    summary = story.get('summary', '')
    
    # Clean and truncate summary
    summary = summary.replace('The post', '').replace('appeared first on', '').replace('[…]', '').strip()
    if len(summary) > 180:
        summary = summary[:180].rsplit(' ', 1)[0] + '...'
    
    # Determine insurance function impacted
    text = (headline + ' ' + summary).lower()
    functions = []
    if any(kw in text for kw in ['underwriting', 'underwriter', 'risk selection']):
        functions.append('Underwriting')
    if any(kw in text for kw in ['claims', 'claim', 'loss']):
        functions.append('Claims')
    if any(kw in text for kw in ['actuarial', 'actuary', 'reserve', 'pricing']):
        functions.append('Actuarial')
    if any(kw in text for kw in ['technology', 'platform', 'digital', 'ai', 'it']):
        functions.append('IT')
    if any(kw in text for kw in ['distribution', 'agent', 'broker', 'channel']):
        functions.append('Distribution')
    if any(kw in text for kw in ['compliance', 'regulation', 'solvency', 'capital']):
        functions.append('Risk/Compliance')
    
    function_str = ' · '.join(functions[:2]) if functions else ''
    
    html = f"""
                    <li class="article-item">
                        <h3 class="article-headline"><a href="{url}" target="_blank">{headline}</a></h3>
                        <div class="article-meta">
                            <span class="article-source">{source}</span>
"""
    if function_str:
        html += f'<span>→ {function_str}</span>'
    
    html += f"""
                        </div>
                        <p class="article-summary">{summary}</p>
                        <a href="{url}" target="_blank" class="article-link">Read →</a>
                    </li>
"""
    return html
