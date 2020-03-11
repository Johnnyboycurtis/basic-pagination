from django.test import TestCase
from pagination import views
from django.shortcuts import reverse


class ViewsTestCase(TestCase):
    def test_something_simple(self):
        self.assertEqual(1,1)

    def test_about(self):
        response = self.client.get(reverse("about"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pagination/about.html')

