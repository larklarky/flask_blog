from bs4 import BeautifulSoup

VALID_TAGS = ['strong', 'em', 'p', 'ul', 'li', 'br', 'b', 'i', 'span', 'strike', 'ol', 'u' ]

def sanitize_html(value):

    soup = BeautifulSoup(value)

    for tag in soup.findAll(True):
        if tag.name not in VALID_TAGS:
            tag.hidden = True

    return soup.renderContents().decode('utf-8')