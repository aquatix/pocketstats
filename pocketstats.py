import pocket
from pocket import Pocket
import datetime

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


def unix_to_string(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


try:
    import settings
except ImportError:
    print('Copy settings_example.py to settings.py and set the configuration to your own preferences')
    sys.exit(1)

consumer_key = settings.consumer_key
access_token = settings.access_token

pocket_instance = pocket.Pocket(consumer_key, access_token)

#items = pocket_instance.get(state='unread')
#print 'Number of items: ' + str(len(items[0]['list']))
#items = pocket_instance.get(state='archive')
#print 'Number of items: ' + str(len(items[0]['list']))
#sys.exit()

#items = pocket_instance.get()
items = pocket_instance.get(count=10)
#print items[0]['status']
print 'Number of items: ' + str(len(items[0]['list']))

for item_id in items[0]['list']:
    #print item_id
    item = items[0]['list'][item_id]
    print item
    #print safe_unicode(item['status']) + ' '+ safe_unicode(item['item_id']) + ' ' + safe_unicode(item['resolved_id']) + ' ' + safe_unicode(item['given_title'])
    print safe_unicode(item['status']) + ' ' + safe_unicode(item['item_id']) + ' ' + safe_unicode(item['resolved_id']) + ' ' + unix_to_string(item['time_added']) + ' ' + unix_to_string(item['time_updated'])
    #datetime.datetime.fromtimestamp(int(item['time_updated'])).strftime('%Y-%m-%d %H:%M:%S')
    #print safe_unicode(item['given_title'])
    print safe_unicode(item['resolved_url'])
    #print safe_unicode(item['resolved_title'])

#items = pocket_instance.get(state='unread')
#print items[0]['status']
#print len(items[0]['list'])