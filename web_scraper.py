#$ python3 -m venv venv
#$ . ./venv/bin/activate
#$ pip install requests BeautifulSoup4

from requests import get
from requests.exceptions import RequestsException
from conextlib import closing
from bs4 import BeautifulSoup4


def scrape_content(url):
    """
    Get the content at `url` by making HTTP GET request.
    If response kind of HTML/XML; return txt content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
    '''
    # only if you want to have it loop and try again
    finally:
        pass
    '''
def is_good_response(resp):
    """
    Returns True if response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

"""
New plan: instead of web scraping, SQL injection for their database
to take their indexed data rather than scrape it
"""

"""
Thought:
How would you categorize something like Oeros to cookies or pantry? Sourpatch? Halo top?
Can't do anything with machine learning until I know what data I have to work with
Minimum information and defualts that I can use along with resources to find that information
"""
def main():
    url_name="https://stilltasty.com/"
    


if __name__ == "__main__":
    main()
