import hashlib
import random
import requests


HOST = 'localhost'
PORT = '19801'
PLATFORM = 'platform'

URL_SCHEMA = 'http://{HOST}:{PORT}/{PLATFORM}/'.format(
    HOST=HOST, PORT=PORT, PLATFORM=PLATFORM)
USERS = ['peter', 'elisabeth', 'annelies', 'hildegard', 'erwin']


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
        response = self.session.post(
            '{}{}'.format(URL_SCHEMA, parent_path),
            json={
                '@type': 'ftw.simplelayout.ContentPage',
                'title': title
                })
        self.publish(response)

    def create_text_block(self, parent_path, title, content):
        response = self.session.post(
            '{}{}'.format(URL_SCHEMA, parent_path),
            json={
                '@type': 'ftw.simplelayout.TextBlock',
                'title': title,
                'text': content
                })
        self.publish(response)

    def publish(self, response):
        if not response:
            return
        obj_url = response.json()['@id']
        action = '{}/@workflow/ipa_demo_web_workflow--TRANSITION--veroffentlichen--entwurf_veroffentlicht'.format(obj_url)
        self.session.post(action)


def construct_external_link(target, title):
    return '<a class="external-link" href="{}" target="_self" title="">{}</a>'.format(
        target, title)


def construct_internal_link(target, title):
    return '<a title="" href="{}{}" class="internal-link" target="_self">{}</a>'.format(
        URL_SCHEMA, target, title)


def get_lorem_ipsum_with_links():
    lorem_ipsum =  'Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Non minor, inquit, voluptas percipitur ex vilissimis rebus quam ex pretiosissimis. Mihi, inquam, qui te id ipsum rogavi? Ita cum ea volunt retinere, quae superiori conveniunt, in Aristonem incidunt; Ex rebus enim timiditas, non ex vocabulis nascitur. Id quaeris, inquam, in quo, utrum respondero, verses te huc atque necesse est. Quamquam id quidem, infinitum est in hac urbe; Duo Reges: constructio interrete. Quod autem satis est, eo quicquid accessit, nimium est; Ita multo sanguine profuso in laetitia et in victoria est {}. Egone quaeris, inquit, quid sentiam?'

    internal = [
        # Internal broken (404)
        'finanzgeschaefte',
        'stadtverwaltungsunterhaltsplaene',
        'amtsverhandlungen',
        'omnibus-planungsstelle',
        'gruener-als-motto',
        'antipattern-in-der-informatik']

    external = [
        # External status 301
        'http://www.2phasen.ch',
        'http://www.2-phasen.ch',
        'http://fuehrerausweise.ch/informationen/fak/',
        'http://www.ilv.ch',
        'http://home.gibm.ch/',
        'http://ict-berufsbildung.ch/',
        'http://berufsmaturbb.ch/index.php?id=2',
        'http://www.Lausinfo.ch',
        'http://www.epschaenzli.ch/',
        # External status 302
        'http://www.baselland-shop.ch',
        'http://www.wahlen.bl.ch/de/vote/list/2016/06/05',
        'http://www.wahlen.bl.ch/de/vote/list/2016/06/05',
        'http://www.igkg-beiderbasel.ch/index.php/bueroassistent-in',
        'http://www.statistik.bl.ch/web_portal/9_1',
        'http://www.statistik.bl.ch/web_portal/13_2',
        'http://www.statistik.bl.ch/web_portal/1_1_1',
        # External status 303
        'https://www.entwicklung.bs.ch/',
        'https://www.aue.bs.ch/',
        'http://www.umweltberichtbeiderbasel.ch/',
        'https://www.umweltberichtbeiderbasel.bs.ch/indikatoren/indikatoren-uebersicht.html',
        'https://www.blkb.ch/newhome',
        # External status 307
        'https://www.stiftung-mercator.ch/de/foerderung/',
        'http://www.energiepaket-bl.ch/',
        'https://www.lignumregionbasel.ch/agenda/anmeldeformular/',
        'http://www.baselland-tourismus.ch/',
        'http://elmar.swisstph.ch/',
        # External status 308
        'http://www.bricklive.ch',
        'http://www.swissmilk.ch',
        'http://www.bricklive.ch',
        'http://www.safeatwork.ch/startseite.html',
        # External status 404
        'https://www.lego.com/de-ch/404',
        'https://list25.com/404',
        'https://brettterpstra.com/2018/']

    internal_concat = [lorem_ipsum.format(construct_internal_link(
        link, hashlib.md5(link.encode()).hexdigest()))
        for link in internal]

    external_concat = [lorem_ipsum.format(construct_external_link(
        link, hashlib.md5(link.encode()).hexdigest()))
        for link in internal]

    internal_concat.extend(external_concat)
    return internal_concat


def create_text_blocks(user_sessions, sl_pages, text_content):
    titles = [
        'football', 'economics', 'income', 'insect', 'trainer', 'thanks',
        'sympathy', 'reception', 'video', 'error', 'owner', 'county',
        'audience', 'lab', 'library', 'warning', 'database', 'lady',
        'inspection', 'reputation', 'combination', 'hall', 'magazine',
        'vehicle', 'theory', 'height', 'membership', 'employment', 'weakness',
        'length', 'passenger', 'passion', 'chapter', 'relationship', 'context',
        'police', 'knowledge', 'version', 'committee', 'uplift', 'perfection']

    for index, text in enumerate(text_content):
        sl_page = random.choice(sl_pages)
        user_session = random.choice(user_sessions)
        user_session.create_text_block(sl_page, titles[index], text)


def create_sl_pages(user_sessions):
    titles = ['article', 'difference', 'drawing', 'internet', 'preparation',
              'unit', 'variety', 'worker']

    for title in titles:
        user_session = random.choice(user_sessions)
        user_session.create_sl_page('', title)

    return titles


def create_users():
    admin = UserSession('admin')
    for user in USERS:
        admin.create_manager(user)


if __name__ == '__main__':
    create_users()
    user_sessions = [UserSession(user) for user in USERS]

    sl_pages = create_sl_pages(user_sessions)
    text_content = get_lorem_ipsum_with_links()
    create_text_blocks(user_sessions, sl_pages, text_content)
