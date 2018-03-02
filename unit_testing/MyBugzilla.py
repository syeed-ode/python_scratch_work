import requests


class MyBugzilla:
    def __init__(self, account=None, server='https://bugzilla.mozilla.org'):
        self.account = account
        self.server = server
        self.session = requests.Session()
        self.val = "Hello"

    def __repr__(self):
        return str(self.val)

    def bug_link(self, bug_id):
        return '%s/show_bug.cgi?id=%s' % (self.server, bug_id)

    def get_new_bugs(self):
        call = self.server + '/rest/bug'
        params = {'assigned_to': self.account
                  , 'status': 'NEW'
                  , 'limit': 10}
        try:
            res = self.session.get(call, params=params).json()
            self.val = res
            print(res)
        except requests.exceptions.ConnectionError:
            # oh well
            res = {'bugs': []}

        def _add_link(bug):
            bug['link'] = self.bug_link(bug['id'])
            return bug

        for bug in res['bugs']:
            yield _add_link(bug)
