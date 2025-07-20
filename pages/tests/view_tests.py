import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from pages.models import (
    PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage,
    AboutPageHero, OurMission, NewArrivals, OurMaterials,
    BestSelling, LaunchedProducts,
)

@pytest.mark.django_db
def test_privacy_policy_view_no_pdf(client):
    url = reverse('privacy_policy')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['privacy_policy'] is None
    assert response.context['pdf_url'] is None

@pytest.mark.django_db
def test_returns_policy_view_no_pdf(client):
    url = reverse('returns_policy')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['returns_policy'] is None
    assert response.context['pdf_url'] is None

@pytest.mark.django_db
def test_faqs_view(client):
    FAQ1 = FAQs.objects.create(question='Q1', answer='A1')
    FAQ2 = FAQs.objects.create(question='Q2', answer='A2')

    url = reverse('faqs_view')
    response = client.get(url)
    assert response.status_code == 200
    faqs = response.context['faqs']
    assert len(faqs) == 2
    assert FAQ1 in faqs and FAQ2 in faqs

@pytest.mark.django_db
def test_contact_view_get(client):
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200
    assert 'contact_form' in response.context
    assert response.context['on_contact'] is True

@pytest.mark.django_db
def test_contact_view_post_valid(client):
    data = {
        'full_name': 'Test User',
        'email': 'test@example.com',
        'message': 'Hello!',
    }
    url = reverse('contact')
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == url

    messages = list(get_messages(response.wsgi_request))
    assert any("Your message has been sent successfully!" in str(m) for m in messages)

    assert ContactMessage.objects.filter(email='test@example.com').exists()

@pytest.mark.django_db
def test_contact_view_post_invalid(client):
    data = {
        'full_name': '',
        'email': 'invalid',
        'message': '',
    }
    url = reverse('contact')
    response = client.post(url, data)
    assert response.status_code == 200
    form = response.context['contact_form']
    assert form.errors

@pytest.mark.django_db
def test_about_view(client):
    hero = AboutPageHero.objects.create(overlay_title='Hero', hero_image='test.jpg')
    mission = OurMission.objects.create(our_mission_title='Mission', our_mission_description='Desc')
    materials = OurMaterials.objects.create(our_materials_title='Materials', our_materials_description='Desc')
    best_selling = BestSelling.objects.create(best_selling_title='Best Seller', best_description='Desc', best_image='best.jpg')

    for i in range(5):
        NewArrivals.objects.create(new_name=f'New {i}', launched_date='2023-01-0' + str(i+1), new_image='new.jpg')
        LaunchedProducts.objects.create(launched_name=f'Launched {i}', launched_date='2023-01-0' + str(i+1), launched_image='launch.jpg')

    url = reverse('about_view')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['hero'] == hero
    assert context['mission'] == mission
    assert context['materials'] == materials
