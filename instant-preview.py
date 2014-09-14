import sublime, sublime_plugin
import urllib
import urllib.request
import os

class InstantPreview(sublime_plugin.EventListener):

    def on_modified(self, view):
        self.refresh_view(view)

    def refresh_view(self, view):
        body = view.substr(sublime.Region(0, view.size()))
        filename = view.file_name()
        data = filename + '----------' + body
        data = data.encode('utf-8')
        if os.environ['PREVIEW_PORT']:
            port = os.environ['PREVIEW_PORT']
        else:
            port = '8090'
        req = urllib.request.Request(url='http://localhost:' + port, data=data, method='PUT')
        f = urllib.request.urlopen(req)
