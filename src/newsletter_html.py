"""
CXO Insurance & BFSI Intelligence Brief - HTML Generator
Production-Ready Newsletter Output v1.0
"""

import datetime
import pytz
from .sources import scan_all_sources
from .filter import filter_and_rank_stories

IST = pytz.timezone('Asia/Kolkata')

def generate_newsletter_html():
    now = datetime.datetime.now(IST)
    stories = scan_all_sources()
    top_stories, themes, risks, competitive, tech_signals = filter_and_rank_stories(stories)
    date_str = now.strftime('%A, %d %B %Y')
    time_str = now.strftime('%H:%M') + " IST"
    
    # Generate executive snapshot bullets
    exec_bullets = generate_executive_snapshot(top_stories, themes)
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daily Insurance & BFSI CXO Intelligence Brief — {date_str}</title>
        <link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap' rel='stylesheet'>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #0f172a; color: #1e293b; min-height: 100vh; padding: 32px 16px; }}
            .wrapper {{ max-width: 900px; margin: 0 auto; }}
            
            /* Header */
            .header {{ background: linear-gradient(135deg, #1e3a5f 0%, #0d2847 100%); border-radius: 12px 12px 0 0; padding: 40px 48px; color: #fff; position: relative; border-bottom: 3px solid #3b82f6; }}
            .brand {{ font-size: 0.75em; text-transform: uppercase; letter-spacing: 4px; color: #60a5fa; margin-bottom: 12px; font-weight: 600; }}
            .title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 2.2em; font-weight: 700; margin-bottom: 4px; line-height: 1.2; }}
            .subtitle {{ font-size: 1em; color: #94a3b8; font-weight: 400; }}
            .meta-row {{ display: flex; gap: 24px; margin-top: 20px; font-size: 0.85em; color: #94a3b8; }}
            .meta-row span {{ display: flex; align-items: center; gap: 6px; }}
            .download-bar {{ margin-top: 20px; }}
            .download-bar a {{ background: #3b82f6; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-size: 0.9em; font-weight: 600; transition: all 0.2s; }}
            .download-bar a:hover {{ background: #2563eb; }}
            
            /* Content */
            .content {{ background: #fff; padding: 40px 48px; border-radius: 0 0 12px 12px; }}
            
            /* Section Numbers */
            .section {{ margin-bottom: 36px; }}
            .section-header {{ display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 2px solid #e2e8f0; }}
            .section-num {{ background: #1e3a5f; color: #fff; font-size: 0.75em; font-weight: 700; padding: 6px 10px; border-radius: 4px; }}
            .section-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 1.3em; color: #1e293b; font-weight: 600; }}
            
            /* Executive Snapshot */
            .exec-snapshot {{ background: #f8fafc; border-left: 4px solid #3b82f6; padding: 24px; border-radius: 0 8px 8px 0; margin-bottom: 32px; }}
            .exec-snapshot h3 {{ font-size: 0.7em; text-transform: uppercase; letter-spacing: 2px; color: #3b82f6; margin-bottom: 16px; font-weight: 700; }}
            .exec-snapshot ul {{ list-style: none; }}
            .exec-snapshot li {{ padding: 8px 0; font-size: 0.95em; color: #334155; line-height: 1.6; display: flex; align-items: flex-start; gap: 10px; }}
            .exec-snapshot li::before {{ content: '→'; color: #3b82f6; font-weight: 700; flex-shrink: 0; }}
            .exec-snapshot .cxo-tag {{ background: #dbeafe; color: #1e40af; font-size: 0.7em; padding: 2px 8px; border-radius: 4px; font-weight: 600; margin-left: 8px; }}
            
            /* Strategic Themes */
            .themes-grid {{ display: grid; gap: 16px; }}
            .theme-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; }}
            .theme-name {{ font-weight: 700; color: #1e3a5f; margin-bottom: 6px; }}
            .theme-insight {{ font-size: 0.9em; color: #64748b; line-height: 1.5; }}
            
            /* Curated Intelligence */
            .intel-item {{ border-bottom: 1px solid #e2e8f0; padding: 20px 0; }}
            .intel-item:last-child {{ border-bottom: none; }}
            .intel-meta {{ display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }}
            .intel-tag {{ font-size: 0.7em; padding: 3px 10px; border-radius: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
            .tag-source {{ background: #e0e7ff; color: #3730a3; }}
            .tag-theme {{ background: #fef3c7; color: #92400e; }}
            .tag-impact {{ background: #dcfce7; color: #166534; }}
            .intel-headline {{ font-size: 1.1em; font-weight: 600; color: #1e293b; margin-bottom: 10px; line-height: 1.4; }}
            .intel-headline a {{ color: #1e293b; text-decoration: none; transition: color 0.2s; }}
            .intel-headline a:hover {{ color: #3b82f6; }}
            .intel-summary {{ font-size: 0.9em; color: #64748b; line-height: 1.6; margin-bottom: 12px; }}
            .intel-why {{ background: #fffbeb; border-left: 3px solid #f59e0b; padding: 12px 16px; border-radius: 0 6px 6px 0; margin-bottom: 12px; }}
            .intel-why strong {{ font-size: 0.75em; text-transform: uppercase; color: #b45309; display: block; margin-bottom: 4px; }}
            .intel-why p {{ font-size: 0.9em; color: #78350f; line-height: 1.5; }}
            .intel-horizon {{ display: inline-block; font-size: 0.75em; padding: 3px 10px; border-radius: 4px; font-weight: 600; }}
            .horizon-now {{ background: #fecaca; color: #991b1b; }}
            .horizon-near {{ background: #fed7aa; color: #9a3412; }}
            .horizon-long {{ background: #d9f99d; color: #3f6212; }}
            .intel-link {{ display: inline-flex; align-items: center; gap: 4px; color: #3b82f6; font-size: 0.85em; font-weight: 600; text-decoration: none; margin-top: 8px; }}
            .intel-link:hover {{ text-decoration: underline; }}
            
            /* Signals Grid */
            .signals-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
            @media (max-width: 700px) {{ .signals-grid {{ grid-template-columns: 1fr; }} }}
            .signal-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; }}
            .signal-card h4 {{ font-size: 0.75em; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
            .signal-card.cyber h4 {{ color: #dc2626; }}
            .signal-card.tech h4 {{ color: #7c3aed; }}
            .signal-card.competitive h4 {{ color: #0891b2; }}
            .signal-card.risk h4 {{ color: #ea580c; }}
            .signal-list {{ list-style: none; }}
            .signal-list li {{ padding: 10px 0; border-bottom: 1px solid #e2e8f0; font-size: 0.9em; }}
            .signal-list li:last-child {{ border-bottom: none; }}
            .signal-list a {{ color: #1e293b; text-decoration: none; }}
            .signal-list a:hover {{ color: #3b82f6; }}
            .signal-source {{ font-size: 0.75em; color: #94a3b8; }}
            
            /* Action Cues */
            .action-cues {{ background: linear-gradient(135deg, #1e3a5f 0%, #0d2847 100%); border-radius: 8px; padding: 28px; color: #fff; }}
            .action-cues h3 {{ font-size: 0.75em; text-transform: uppercase; letter-spacing: 2px; color: #60a5fa; margin-bottom: 20px; }}
            .action-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
            @media (max-width: 700px) {{ .action-grid {{ grid-template-columns: 1fr; }} }}
            .action-item {{ }}
            .action-label {{ font-size: 0.7em; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; font-weight: 700; }}
            .action-label.watch {{ color: #fbbf24; }}
            .action-label.prepare {{ color: #fb923c; }}
            .action-label.act {{ color: #f87171; }}
            .action-text {{ font-size: 0.9em; color: #cbd5e1; line-height: 1.5; }}
            
            /* Footer */
            .footer {{ margin-top: 32px; padding: 24px; text-align: center; color: #64748b; font-size: 0.8em; }}
            .footer-brand {{ color: #3b82f6; font-weight: 700; margin-bottom: 8px; }}
            .footer-sources {{ margin-bottom: 12px; line-height: 1.6; }}
            .footer-disclaimer {{ color: #94a3b8; font-size: 0.85em; }}
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="header">
                <div class="brand">Continuum Intelligence</div>
                <div class="title">Daily Insurance & BFSI CXO Intelligence Brief</div>
                <div class="subtitle">Strategic insights for executive decision-makers</div>
                <div class="meta-row">
                    <span>📅 {date_str}</span>
                    <span>🕐 {time_str}</span>
                    <span>📊 Coverage: Last 24 Hours</span>
                </div>
                <div class="download-bar">
                    <a href='/newsletter/word'>↓ Download Executive Brief</a>
                </div>
            </div>
            
            <div class="content">
                <!-- 1. Executive Snapshot -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">01</span>
                        <span class="section-title">Executive Snapshot</span>
                    </div>
                    <div class="exec-snapshot">
                        <h3>60-Second Read</h3>
                        <ul>
    """
    
    # Add executive bullets
    for bullet in exec_bullets:
        cxo_tag = f'<span class="cxo-tag">{bullet["cxo"]}</span>' if bullet.get("cxo") else ""
        html += f'<li>{bullet["text"]}{cxo_tag}</li>\n'
    
    html += """
                        </ul>
                    </div>
                </div>
                
                <!-- 2. Strategic Themes -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">02</span>
                        <span class="section-title">Strategic Themes Emerging Today</span>
                    </div>
                    <div class="themes-grid">
    """
    
    # Add themes
    for theme in themes:
        html += f'''
                        <div class="theme-card">
                            <div class="theme-name">{theme["name"]}</div>
                            <div class="theme-insight">{theme["insight"]}</div>
                        </div>
        '''
    
    html += """
                    </div>
                </div>
                
                <!-- 3. Curated Intelligence -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">03</span>
                        <span class="section-title">Curated Intelligence</span>
                    </div>
    """
    
    # Add curated stories
    for i, s in enumerate(top_stories[:10], 1):
        horizon = "Now" if s.get("novelty") == "Disruptive" else ("Near" if s.get("novelty") == "Meaningful" else "Long")
        horizon_class = {"Now": "horizon-now", "Near": "horizon-near", "Long": "horizon-long"}.get(horizon, "horizon-near")
        
        html += f'''
                    <div class="intel-item">
                        <div class="intel-meta">
                            <span class="intel-tag tag-source">{s.get("source", "Source")}</span>
                            <span class="intel-tag tag-theme">{s.get("theme", "General")[:20]}</span>
                            <span class="intel-tag tag-impact">{s.get("impact", "Regional")}</span>
                        </div>
                        <div class="intel-headline"><a href="{s["url"]}" target="_blank" rel="noopener">{s["headline"]}</a></div>
                        <div class="intel-why">
                            <strong>Why This Matters</strong>
                            <p>{s.get("summary", "Strategic development requiring executive attention.")}</p>
                        </div>
                        <span class="intel-horizon {horizon_class}">Time Horizon: {horizon}</span>
                        <a href="{s["url"]}" target="_blank" rel="noopener" class="intel-link">Read Full Article →</a>
                    </div>
        '''
    
    html += """
                </div>
                
                <!-- 4 & 5. Signals Grid -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">04</span>
                        <span class="section-title">Competitive & Technology Signals</span>
                    </div>
                    <div class="signals-grid">
                        <div class="signal-card competitive">
                            <h4>🏢 Competitive & Peer Signals</h4>
                            <ul class="signal-list">
    """
    
    # Add competitive signals
    for sig in competitive[:4]:
        html += f'''
                                <li>
                                    <a href="{sig["url"]}" target="_blank">{sig["headline"][:80]}...</a>
                                    <div class="signal-source">{sig["source"]}</div>
                                </li>
        '''
    
    if not competitive:
        html += '<li>No significant competitive signals in the last 24 hours</li>'
    
    html += """
                            </ul>
                        </div>
                        <div class="signal-card tech">
                            <h4>🤖 Technology & AI Radar</h4>
                            <ul class="signal-list">
    """
    
    # Add tech signals
    for sig in tech_signals[:4]:
        html += f'''
                                <li>
                                    <a href="{sig["url"]}" target="_blank">{sig["headline"][:80]}...</a>
                                    <div class="signal-source">{sig["source"]} · {sig.get("implication", "")}</div>
                                </li>
        '''
    
    if not tech_signals:
        html += '<li>No significant technology signals in the last 24 hours</li>'
    
    html += """
                            </ul>
                        </div>
                    </div>
                </div>
                
                <!-- 6. Risk Watch -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">05</span>
                        <span class="section-title">Risk & Threat Watch</span>
                    </div>
                    <div class="signals-grid">
                        <div class="signal-card risk" style="grid-column: 1 / -1;">
                            <h4>⚠️ Risk Alerts for CRO/CISO Attention</h4>
                            <ul class="signal-list">
    """
    
    # Add risk signals
    for sig in risks[:5]:
        severity_style = 'color: #dc2626; font-weight: 600;' if sig.get("severity") == "High" else ''
        html += f'''
                                <li style="{severity_style}">
                                    <a href="{sig["url"]}" target="_blank">{sig["headline"]}</a>
                                    <div class="signal-source">{sig["source"]} · Severity: {sig.get("severity", "Medium")}</div>
                                </li>
        '''
    
    if not risks:
        html += '<li>No critical risk alerts in the last 24 hours</li>'
    
    html += """
                            </ul>
                        </div>
                    </div>
                </div>
                
                <!-- 7. CXO Action Cues -->
                <div class="section">
                    <div class="section-header">
                        <span class="section-num">06</span>
                        <span class="section-title">CXO Action Cues</span>
                    </div>
                    <div class="action-cues">
                        <h3>Strategic Action Framework</h3>
                        <div class="action-grid">
                            <div class="action-item">
                                <div class="action-label watch">👁️ Watch</div>
                                <div class="action-text">Early indicators of regulatory shifts and competitive moves worth monitoring over the next 30 days</div>
                            </div>
                            <div class="action-item">
                                <div class="action-label prepare">📋 Prepare</div>
                                <div class="action-text">Technology investments and capability builds that peers are executing; assess relevance to your strategy</div>
                            </div>
                            <div class="action-item">
                                <div class="action-label act">⚡ Act</div>
                                <div class="action-text">Immediate review of cyber risk posture and compliance readiness based on today's threat signals</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <div class="footer-brand">CONTINUUM INTELLIGENCE</div>
                <div class="footer-sources">Sources: Insurance Journal · Digital Insurance · Reuters · Dark Reading · TechCrunch · BBC Business · CNBC · Financial Times</div>
                <div class="footer-disclaimer">This intelligence brief is prepared for executive decision-makers. Information derived from sources believed reliable but not guaranteed. © 2025 Continuum. All rights reserved.</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html


def generate_executive_snapshot(stories, themes):
    """Generate 3-5 crisp executive bullets."""
    bullets = []
    
    # What changed - based on top stories
    if stories:
        top_theme = themes[0]["name"] if themes else "Industry developments"
        bullets.append({
            "text": f"<strong>Key Signal:</strong> {top_theme} dominating today's intelligence with {len(stories)} high-priority items",
            "cxo": "CEO"
        })
    
    # Risk signal
    risk_stories = [s for s in stories if "Cyber" in s.get("theme", "") or "Risk" in s.get("theme", "")]
    if risk_stories:
        bullets.append({
            "text": f"<strong>Risk Alert:</strong> {len(risk_stories)} cybersecurity/risk developments requiring board-level visibility",
            "cxo": "CRO/CISO"
        })
    
    # Technology signal
    tech_stories = [s for s in stories if "AI" in s.get("theme", "") or "Technology" in s.get("theme", "")]
    if tech_stories:
        bullets.append({
            "text": f"<strong>Tech Radar:</strong> {len(tech_stories)} AI/technology developments with strategic implications",
            "cxo": "CIO/CDO"
        })
    
    # Regulatory signal
    reg_stories = [s for s in stories if "Regulation" in s.get("theme", "")]
    if reg_stories:
        bullets.append({
            "text": f"<strong>Compliance Watch:</strong> {len(reg_stories)} regulatory developments requiring legal/compliance review",
            "cxo": "CLO/CCO"
        })
    
    # Default if no specific signals
    if not bullets:
        bullets.append({
            "text": "<strong>Market Scan:</strong> Limited high-priority signals in the last 24 hours; routine monitoring continues",
            "cxo": "All CXOs"
        })
    
    return bullets[:5]
