from django.test import TestCase
from django.contrib.auth import get_user_model
from requests.api import post
from .models import Information
from django.urls import reverse
User = get_user_model(
)
class Snickers(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username = 'ramzan',
            email = 'ramzanxam@gmail.com',
            password = 'secret'
        )
# Create your tests here.
        self.post = Information.objects.create(
            url = 'https://habr.com/ru/post/593695/',
            title = 'Кто же вы, мистер Рамзан?',
            teg = 'twitterджек дорсипараг агравалсоциальные сетигенеральный директортвиттер',
            body = 'Кстати, одним из кураторов проекта Bluesky от Twitter в 2019 году был обозначен Агравал',
            user = self.user,
            info = 'Дата основания 21 февраля 2005',
            hab = 'Блог компании NeoflexGit',
            time = '4 октября 2018 в 11:39',
            image = 'https://habrastorage.org/r/w1560/webt/pm/lu/an/pmluanwspkx7wwuwnebnzv6b0um.png',
            vote ='+10',
            bookmarks = '99',
            user_content_karma = '421.5',
            user_content_rate = '7.5'
        )
    def test_post_str(self):
        self.assertEqual(str(self.post), self.post.title)
    def test_post_content(self):
        self.assertEqual(f'{self.post.url}', 'https://habr.com/ru/post/593695/')
        self.assertEqual(f'{self.post.title}', 'Кто же вы, мистер Рамзан?')
        self.assertEqual(f'{self.post.teg}', 'twitterджек дорсипараг агравалсоциальные сетигенеральный директортвиттер')
        self.assertEqual(f'{self.post.body}', 'Кстати, одним из кураторов проекта Bluesky от Twitter в 2019 году был обозначен Агравал')
        self.assertEqual(f'{self.post.user}', 'ramzan')
        self.assertEqual(f'{self.post.info}', 'Дата основания 21 февраля 2005')
        self.assertEqual(f'{self.post.hab}', 'Блог компании NeoflexGit')
        self.assertEqual(f'{self.post.time}', '4 октября 2018 в 11:39')
        self.assertEqual(f'{self.post.image}', 'https://habrastorage.org/r/w1560/webt/pm/lu/an/pmluanwspkx7wwuwnebnzv6b0um.png')
        self.assertEqual(f'{self.post.vote}', '+10')
        self.assertEqual(f'{self.post.bookmarks}', '99')
        self.assertEqual(f'{self.post.user_content_karma}', '421.5')
        self.assertEqual(f'{self.post.user_content_rate}', '7.5')
    def test_post_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Подписаться')
