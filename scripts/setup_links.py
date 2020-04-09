import requests


HOST = 'localhost'
PORT = '8080'
PLATFORM = 'platform'

URL_SCHEMA = 'http://{HOST}:{PORT}/{PLATFORM}/'.format(
    HOST=HOST, PORT=PORT, PLATFORM=PLATFORM)


class UserSession():
    def __init__(self, user):
        self.session = requests.Session()
        self.session.auth = (user, user)
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'})

    def get(self, url):
        return self.session.get(URL_SCHEMA + url)

    def create_manager(self, user):
        return self.session.post(
            '{}{}'.format(URL_SCHEMA, '@users'),
            json={
                'email': '{}@example.com'.format(user),
                'fullname': user.capitalize(),
                'password': user,
                'roles': ['Manager'],
                'username': user
                })

    def create_sl_page(self, parent_path, title):
        return self.session.post(
            '{}{}'.format(URL_SCHEMA, parent_path),
            json={
                '@type': 'ftw.simplelayout.ContentPage',
                'title': title
                })

    def create_text_block(self, parent_path, title, content):
        return self.session.post(
            '{}{}'.format(URL_SCHEMA, parent_path),
            json={
                '@type': 'ftw.simplelayout.TextBlock',
                'title': title,
                'text': content
                })


def construct_external_link(target, title):
    return '<a class="external-link" href="{}" target="_self" title="">{}</a>'.format(
        target, title)


def construct_internal_link(target, title):
    return '<a title="" href="{}{}" class="internal-link" target="_self">{}</a>'.format(
        URL_SCHEMA, target, title)


admin = UserSession('admin')
peter = UserSession('peter')

# Create an SL page
# print(peter.create_sl_page('', 'About'))

# Create users
# admin.create_manager('peter')
