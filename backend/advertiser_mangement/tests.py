from django.test import TestCase
from .models import Ad, Advertiser

class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
        # Advertiser.objects.create(name='advertiser3')
    
    def test_title(self):
        ins = Ad.objects.all()
        expected_object_name = f'{ins[1].title}'
        self.assertEquals(expected_object_name, 'title1')
