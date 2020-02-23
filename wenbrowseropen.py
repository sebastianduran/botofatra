import webbrowser
firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open_new_tab('http://www.csestack.org')

