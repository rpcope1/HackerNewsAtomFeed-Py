#---------------------------------------
#   Hacker News Atom Feed Generator
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   A simple Atom feed server for Hacker
#   News data written by Robert P. Cope
#
#   Homepage: https://github.com/rpcope1/HackerNewsAtomFeed-Py


__author__ = 'Robert P. Cope'
__license__ = 'LGPL v3'

from HackerNewsAPI import HackerNewsAPI
import SimpleHTTPServer
import SocketServer
import pyatom
import sys
import os
import threading
import datetime
import time
import logging

feed_logger = logging.getLogger(__name__)
if not feed_logger.handlers:
    ch = logging.StreamHandler()
    feed_logger.addHandler(ch)
    feed_logger.setLevel(logging.INFO)



FS_SEPARATOR = "\\" if os.name in ["nt", "os2"] else "/"

FEED_RELATIVE_DIR = 'feed'
FEED_FULL_DIR = FS_SEPARATOR.join([os.path.dirname(os.path.realpath(__file__)), FEED_RELATIVE_DIR])
FEED_FILE = 'feed.xml'

HACKERNEWS_ITEM_URL_TEMPLATE = 'https://news.ycombinator.com/item?id={id}'


def main(hostname='localhost', port=8000, refresh_min=15):
    #Set up to serve out of this directory.
    feed_logger.info('Initializing Hacker News Atom Feed Server')
    if not os.path.isdir(FEED_FULL_DIR):
        os.mkdir(FEED_FULL_DIR)
    api = HackerNewsAPI()
    url = 'http://{host}:{port}'.format(host=hostname, port=port)
    feed_url = '{url}/{feed_file}'.format(url=url, feed_file=FEED_FILE)
    feed_logger.info('Location: {}'.format(feed_url))
    feed = pyatom.AtomFeed(title='Hacker News',
                           subtitle='An example Hacker News Atom Feed',
                           url=url,
                           feed_url=feed_url)
    httpd_handler = HackerNewsAtomHandler
    feed_logger.info('Starting socket server...')
    httpd = SocketServer.TCPServer((hostname, port), httpd_handler)
    update_feed(feed, api)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    while True:
        time.sleep(refresh_min*60)
        update_feed(feed, api)


class HackerNewsAtomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return "/".join([FEED_FULL_DIR, path])


def update_feed(feed, api):
    feed_logger.info('Updating feed. NOTE: This could take a while...')
    feed.entries = []
    stories = api.get_top_stories()
    num_stories = len(stories)
    for i, item_num in enumerate(stories):
        feed_logger.info('Getting story {} of {} and updating feed.'.format(i, num_stories))
        story = api.get_item(item_num)
        feed.add(title=story.title,
                 id=story.id,
                 content=story.text if hasattr(story, 'text') else "",
                 content_type='plain',
                 url=story.url if story.url else HACKERNEWS_ITEM_URL_TEMPLATE.format(id=story.id),
                 author=story.by,
                 updated=datetime.datetime.fromtimestamp(int(story.time)))
    feed_data = feed.to_string().encode('utf8')
    feed_file_full_path = FS_SEPARATOR.join([FEED_FULL_DIR, FEED_FILE])
    feed_logger.info('Writing feed to file: {}'.format(feed_file_full_path))
    with open(feed_file_full_path, 'w') as f:
        f.write(feed_data)
    feed_logger.info('Feed update complete.')


if __name__ == "__main__":
    main(*sys.argv[1:])

