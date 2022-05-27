"""Tests for the Patient model."""

def test_create_person():
    from inflammation.models import Person

    name = 'Alice'
    p = Person(name=name)

    assert p.name == name


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Alice'
    p = Doctor(name=name)

    assert p.name == name
