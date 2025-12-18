# CXO Morning Intel Agent

A modular Python app to scan top news sources, filter for high-impact CXO-relevant stories, and output a markdown newsletter. Designed for containerization and web hosting.

## Structure
- `src/` - Core logic modules
- `main.py` - Entrypoint
- `requirements.txt` - Dependencies
- `Dockerfile` - Containerization

## Features
- Scheduled scan (7 AM IST)
- Source plugins (Reuters, Bloomberg, etc.)
- Topic and impact filtering
- Markdown output as per spec
- Ready for web deployment
