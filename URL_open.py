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

def openSpecialUrlArgsHandler(keyword):
    keyword_str = ''.join(keyword).strip().lower()
    keyword_lst = keyword_str.split()
    keyword_str_nospace = keyword_str.replace(' ', '')
    main_kw = keyword_lst[0]
    if main_kw == 'g' or main_kw == 'google':
        return 'URL_open.openSpecGoogle'
    if main_kw == 'yt' or main_kw == 'youtube':
        return 'URL_open.openSpecYoutube'
    if main_kw == 'imdb' or main_kw == 'movie':
        return 'URL_open.openSpecImdb'
    if main_kw == 'lf' or main_kw == 'lastfm' or main_kw == 'music':
        return 'URL_open.openSpecLastfm'
    if (keyword_str_nospace == 'utmoodle' or
        keyword_str_nospace == 'moodleut' or
        keyword_str_nospace == 'moodle'):
        return 'URL_open.openSpecUtmoodle'

def openUrl(raw_url):
    url = ''
    raw_url_str = ''.join(raw_url)
    if not (raw_url_str.startswith('http://') or
            raw_url_str.startswith('https://')):
        url += 'http://'
    url += raw_url_str
    webbrowser.open_new_tab(url)

def openSpecGoogle(raw_query):
    query_lst = ''.join(raw_query).split()
    query = ' '.join(query_lst[1:])
    webbrowser.open_new_tab('http://www.google.com/search?q=' + query)

def openSpecUtmoodle(*args):
    webbrowser.open_new_tab('https://moodle.ut.ee/login/index.php')

def openSpecImdb(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://www.imdb.com/find?ref_=nv_sr_fn&q=' + query + '&s=all')
    else:
        webbrowser.open_new_tab('http://www.imdb.com/')

def openSpecYoutube(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + query)
    else:
        webbrowser.open_new_tab('https://www.youtube.com/')

def openSpecLastfm(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://www.last.fm/search?q=' + query + '&type=all')
    else:
        webbrowser.open_new_tab('http://www.last.fm/')
