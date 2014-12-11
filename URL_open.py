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
    if main_kw == "ekss":
        return "URL_open.openSpecEKSS"
    if main_kw == 'õs':
        return 'URL_open.openÕs'
    if main_kw == "wolfram" or main_kw == "alpha" or main_kw == "wolframalpha" or main_kw == "wa":
        return "URL_open.openSpecWA"
    if main_kw.startswith("trans") or main_kw.startswith("tõlg") or main_kw.startswith("dict"):
        return "URL_open.openDictionary"
    if main_kw == "wiki" or main_kw == "wikipedia" or main_kw == "w":
        return "URL_open.openWikiEn"
    if main_kw == "viki" or main_kw == "vikipeedia" or main_kw == "v":
        return "URL_open.openWikiEst"


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

def openSpecEKSS(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://www.eki.ee/dict/ekss/index.cgi?Q=' + query + "&F=M")
    else:
        webbrowser.open_new_tab('http://www.eki.ee/dict/ekss/')

def openÕs(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://www.eki.ee/dict/qs/index.cgi?Q=' + query + '&F=M')
    else:
        webbrowser.open_new_tab('http://www.eki.ee/dict/qs/')

def openSpecWA(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://www.wolframalpha.com/input/?i=' + query)
    else:
        webbrowser.open_new_tab('http://www.wolframalpha.com/')

def openDictionary(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = ' '.join(query_lst[1:])
        (webbrowser.open_new_tab('http://dictionary.sensagent.com/' +
                                 " ".join(query_lst[3:]) + "/" + query_lst[1] + "-" + query_lst[2]))
    else:
        webbrowser.open_new_tab('http://www.sensagent.com/')

def openWikiEn(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://en.wikipedia.org/w/index.php?search=' + query)
    else:
        webbrowser.open_new_tab('http://en.wikipedia.org/wiki/Main_Page')

def openWikiEst(raw_query):
    query_lst = ''.join(raw_query).strip().lower().split()
    if len(query_lst) > 1:
        query = '+'.join(query_lst[1:])
        webbrowser.open_new_tab('http://et.wikipedia.org/w/index.php?search=' + query)
    else:
        webbrowser.open_new_tab('http://et.wikipedia.org/wiki/Esileht')
