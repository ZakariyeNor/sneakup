import pytest
from datetime import date, timedelta
from pages.models import (
    PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage,
    OurMission, OurMaterials,
)
@pytest.mark.django_db
def test_privacy_policy_model():
    policy = PrivacyPolicy.objects.create(
        title="Test Privacy",
        content="This is the privacy content.",
    )
    assert str(policy).startswith('Uploaded Test Privacy on')
    assert policy.title == "Test Privacy"

@pytest.mark.django_db
def test_returns_policy_model():
    policy = ReturnsPolicy.objects.create(
        title="Test Returns",
    )
    assert str(policy).startswith('Updated Test Returns on')
    assert policy.title == "Test Returns"

@pytest.mark.django_db
def test_faqs_model():
    faq = FAQs.objects.create(
        question="What is this?",
        answer="This is a test FAQ.",
    )
    assert str(faq).startswith('FAQ:')
    assert faq.question == "What is this?"

@pytest.mark.django_db
def test_contact_message_model():
    contact = ContactMessage.objects.create(
        full_name="Jane Doe",
        email="jane@example.com",
        message="Hello there!",
    )
    assert str(contact).startswith('From: Jane Doe | on')
    assert contact.email == "jane@example.com"

@pytest.mark.django_db
def test_our_mission_model():
    mission = OurMission.objects.create(
        our_mission_title="Our Mission Test",
        our_mission_description="We strive to test everything."
    )
    assert str(mission) == "Our Mission Test"

@pytest.mark.django_db
def test_our_materials_model():
    materials = OurMaterials.objects.create(
        our_materials_title="Materials Title",
        our_materials_description="Detailed materials description."
    )
    assert str(materials) == "Materials Title"
