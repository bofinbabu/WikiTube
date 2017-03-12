import wikipedia
import re
regex_parentheses = re.compile('\(.+?\)')

# Wikipedia logo
# https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/440px-Wikipedia-logo-v2.svg.png

# Set of stub articles
stubs = set()

# Images to avoid
img_blacklist = set(['Commons-logo.svg', 'Symbol_support_vote.svg'])


def get_wiki_page_by_title(title):
    return wikipedia.page(title)

def wiki_searck(keyword):
    return wikipedia.search(keyword)

def get_title(wiki_page):
    """ Return title of the wikipedia page object """
    return wiki_page.title

def get_summary(wiki_page):
    """ Return summary of wikipedia page object
        Removes parenthesised text
    """
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

def get_image_links(wiki_page):
    """ A list of Wikimedia images """
    images = wiki_page.images
    for img in images:
        if img.split('.')[1] is not 'wikimedia'or \
                        img.split('/')[4] is not 'commons' or \
                        img.split('/')[-1:] in img_blacklist:
            images.remove(img)
    return images

