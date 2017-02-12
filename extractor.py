import wikipedia
import re
regex_parentheses = re.compile('\(.+?\)')


stubs = set()

def get_title(wiki_page):
    """ Return title of the wikipedia page object """
    return wiki_page.title

def get_summary(wiki_page):
    """ Return summary of wikipedia page object"""
    summary = wiki_page.summary
    if len(summary.split()) < 150:
        stubs.add(wiki_page.pageid)
        return None
    summary = regex_parentheses.sub('', summary)
    summary = summary.replace('\n', ' ')
    return summary

def get_topics(wiki_page):
    """ Return preprocessed list of topics from the current page """
    topics = wiki_page.links
    for topic in topics:
        if 'List of' in topic:
            topics.remove(topic)
    return topics
