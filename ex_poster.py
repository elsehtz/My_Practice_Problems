user_agent = "image uploader"
default_message = "Image $current of $total"

import logging
import os
from os.path import abspath, isabs, isdir, isfile, join
import random
import string
import sys
import mimetypes
import urllib.request
import http.client
import time
import re
import requests

# Receive data through API
# GET http:
# https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=12726f0dbcdab529193f10e791dd

response = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=12726f0dbcdab529193f10e791dd")
print(response)
data = response.json()
print(data)
# Send data through API
# POST site:
# https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=12726f0dbcdab529193f10e791dd


def post_file():
    with open('report.xls', 'r', encoding='utf-8') as f:
        r = requests.post('http://httpbin.org/post', files={'report.xls': f})

# Generate a random string
def random_string (length):
    pass

# Regex module
text_to_search = r'''
abcdefghijklmnopqrstuvwxyz 
swhat at
408.967.71184
9208 983 3043
abc
'''

sentence = r'Start a sentence and bring it to an end'

pattern = re.compile(r'\D\d\d\d\W\d\d\d\W\d\d\d\d\D')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Encode data
def encode_multipart_data (data, files):
    
    boundary = random_string(30)

    def get_content_type (filename):
        return mimetypes.guess_type (filename)[0] or 'application/octet-stream'

    def encode_field (field_name):
        return ('--' + boundary,
                'Content-Disposition: form-data; name="%s"' % field_name,
                '', str (data [field_name]))

    def encode_file (field_name):
        filename = files [field_name]
        return ('--' + boundary,
                'Content-Disposition: form-data; name="%s"; filename="%s"' % (field_name, filename),
                'Content-Type: %s' % get_content_type(filename),
                '', open (filename, 'rb').read ())

    lines = []
    for name in data:
        lines.extend (encode_field (name))
    for name in files:
        lines.extend (encode_file (name))
    lines.extend (('--%s--' % boundary, ''))
    body = '\r\n'.join (lines)

    headers = {'content-type': 'multipart/form-data; boundary=' + boundary,
               'content-length': str (len (body))}

    return body, headers

def send_post (url, data, files):
    req = urllib.request(url)
    connection = http.client.HTTPConnection (req.get_host ())
    connection.request ('POST', req.get_selector (),
                        *encode_multipart_data (data, files))
    response = connection.getresponse ()
    logging.debug ('response = %s', response.read ())
    logging.debug ('Code: %s %s', response.status, response.reason)

def make_upload_file (server, thread, delay = 15, message = None,
                      username = None, email = None, password = None):

    delay = max (int (delay or '0'), 15)

    def upload_file (path, current, total):
        assert isabs (path)
        assert isfile (path)

        logging.debug ('Uploading %r to %r', path, server)
        message_template = string.Template (message or default_message)

        data = {'MAX_FILE_SIZE': '3145728',
                'sub': '',
                'mode': 'regist',
                'com': message_template.safe_substitute (current = current, total = total),
                'resto': thread,
                'name': username or '',
                'email': email or '',
                'pwd': password or random_string (20),}
        files = {'upfile': path}

        send_post(server, data, files)

        logging.info('Uploaded %r', path)
        rand_delay = random.randint (delay, delay + 5)
        logging.debug('Sleeping for %.2f seconds------------------------------\n\n', rand_delay)
        time.sleep(rand_delay)

    return upload_file

def upload_directory (path, upload_file):
    assert isabs(path)
    assert isdir(path)

    matching_filenames = []
    file_matcher = re.compile(r'\.(?:jpe?g|gif|png)$', re.IGNORECASE)

    for dirpath, dirnames, filenames in os.walk (path):
        for name in filenames:
            file_path = join(dirpath, name)
            logging.debug('Testing file_path %r', file_path)
            if file_matcher.search (file_path):
                matching_filenames.append(file_path)
            else:
                logging.info('Ignoring non-image file %r', path)

    total_count = len (matching_filenames)
    for index, file_path in enumerate (matching_filenames):
        upload_file(file_path, index + 1, total_count)

def run_upload (options, paths):
    upload_file = make_upload_file(**options)

    for arg in paths:
        path = abspath(arg)
        if isdir (path):
            upload_directory(path, upload_file)
        elif isfile (path):
            upload_file(path)
        else:
            logging.error('No such path: %r' % path)

    logging.info('Done!')