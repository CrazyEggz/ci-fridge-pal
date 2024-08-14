from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Item, Category, Unit


class DashboardTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test_user", password="test1234!!")

    def test_page_redirects_if_not_logged_in(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_username_is_present_on_page(self):
        self.assertTrue(self.client.login(
            username="test_user", password="test1234!!"))

        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, "test_user")


class AddItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test_user", password="test1234!!")

    def test_page_redirects_if_not_logged_in(self):
        url = reverse('add-item')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_username_is_present_on_page(self):
        self.assertTrue(self.client.login(
            username="test_user", password="test1234!!"))

        response = self.client.get(reverse('add-item'))
        self.assertContains(response, "test_user")


class EditItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test_user", password="test1234!!")
        self.item = Item.objects.create(
            name='Garden Peas',
            quantity=5,
            expiry_date=date.today() + timedelta(days=7),
            location=0,
            user=user)

    def test_page_redirects_if_not_logged_in(self):
        url = reverse('edit-item', args=[self.item.pk])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_username_is_present_on_page(self):
        self.assertTrue(self.client.login(
            username="test_user", password="test1234!!"))

        response = self.client.get(reverse('edit-item', args=[self.item.pk]))
        self.assertContains(response, "test_user")


class DeleteItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test_user", password="test1234!!")
        self.item = Item.objects.create(
            name='Garden Peas',
            quantity=5,
            expiry_date=date.today() + timedelta(days=7),
            location=0,
            user=user)

    def test_page_redirects_if_not_logged_in(self):
        url = reverse('delete-item', args=[self.item.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_username_is_present_on_page(self):
        self.assertTrue(self.client.login(
            username="test_user", password="test1234!!"))

        response = self.client.post(
            reverse('delete-item', args=[self.item.pk]))
        self.assertRedirects(response, reverse('dashboard'))
