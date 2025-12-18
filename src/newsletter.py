import datetime
import pytz
from .sources import scan_all_sources
from .filter import filter_and_rank_stories
from .format import format_markdown

IST = pytz.timezone('Asia/Kolkata')

# Entrypoint for newsletter generation

def generate_newsletter():
    now = datetime.datetime.now(IST)
    stories = scan_all_sources()
    top_stories, trends, risks = filter_and_rank_stories(stories)
    markdown = format_markdown(top_stories, trends, risks, now)
    return markdown
