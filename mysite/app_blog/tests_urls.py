from django.test import TestCase
from django.urls import reverse, resolve
from app_blog.views import HomePageView, ArticleDetail


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_view(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        url = reverse(
            'article-detail',
            args=('2026', '10', '02', 'test-article'),
        )
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleDetail)

