import webbrowser


def openUrlArgsHandler(args):
    domain_ext = {'.com', '.de', '.net', '.tk', '.co.uk', '.org', '.info',
                  '.cn', '.nl', '.ru', '.eu', '.br', '.au', '.fr', '.it',
                  '.ar', '.pl', '.biz', '.ee', '.lt', '.lv', '.no', '.pro'}
    args_str = ''.join(args)
    for ext in domain_ext:
        if ext in args_str:
            return True
    return False

def googleSearchArgsHandler(args):
    args_lst = ''.join(args).strip().lower().split()
    if args_lst[0] == 'g' or args_lst[0] == 'google':
        return True
    return False

def openSpecialUrlArgsHandler(keyword):
    keyword_str = ''.join(keyword).strip().lower()
    keyword_lst = keyword_str.split()
    keyword_str_nospace = keyword_str.replace(' ', '')
    if keyword_lst[0] == 'g' or keyword_lst[0] == 'google':
        return 'URL_open.openSpec'
    if (keyword_str_nospace == 'utmoodle' or
        keyword_str_nospace == 'moodleut' or
        keyword_str_nospace == 'moodle'):
        return 'URL_open.openSpecUtmoodle'
    if keyword_str.split()[0] == 'imdb':
        return 'URL_open.openSpecImdb'
    if keyword_lst[0] == 'yt' or keyword_lst[0] == 'youtube':
        return 'URL_open.openSpecYoutube'

def openUrl(raw_url):
    url = ''
    raw_url_str = ''.join(raw_url)
    if not (raw_url_str.startswith('http://') or
            raw_url_str.startswith('https://')):
        url += 'http://'
    url += raw_url_str
    webbrowser.open_new_tab(url)

def googleSearch(raw_query):
    query_lst = ''.join(raw_query).split()
    query = ' '.join(query_lst[1:])
    webbrowser.open_new_tab('http://www.google.com/search?q=' + query)

def openSpecUtmoodle(*args):
    webbrowser.open_new_tab('https://moodle.ut.ee/login/index.php')

def openSpecImdb(query):
    query_str = ''.join(query).lower().replace('imdb', '').strip()
    if query_str:
        webbrowser.open_new_tab('http://www.imdb.com/find?ref_=nv_sr_fn&q=' + query_str.replace(' ', '+') + '&s=all')
    else:
        webbrowser.open_new_tab('http://www.imdb.com/')

def openSpecYoutube(query):
    query_lst = ''.join(query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + query)
    else:
        webbrowser.open_new_tab('https://www.youtube.com/')
