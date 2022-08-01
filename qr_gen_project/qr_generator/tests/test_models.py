
# from unicodedata import category
# from django.test import TestCase
# from qr_generator.models import QRCollection, User, UserCollection, Category
# import datetime


# from django.core.files.uploadedfile import SimpleUploadedFile

# # newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')

# from django.core.files import File


# class QRCollectionTest(TestCase):
#     """Test Module for QRCollection Model"""
    
#     def test_creates_user(self):
#         self.user = User.objects.create_user("nico", "sharonarome", "sharonarome")
#         self.assertIsInstance(self.user, User)
#         self.assertEqual(self.user.email, "sharonarome")

#     def test_creates_superuser(self):
#         self.user = User.objects.create_superuser("nico", "sharonarome", "sharonarome")
#         self.assertIsInstance(self.user, User)
#         self.assertEqual(self.user.email, "sharonarome")

#     def test_raises_error_when_no_name(self):
#         self.assertRaises(
#             ValueError, User.objects.create_user,username="", email="sharonarome", password="sharonarome"
#             )

#         self.assertRaisesMessage(ValueError, "Username Must be given")


#     nick_user = User.objects.create_user("nico", "sharonarome", "sharonarome")
#     category = Category.objects.get(id=1)

#     def test_add_new_collection(self):

#         qr = QRCollection.objects.create(
#             qr_user = self.nick_user,
#             url_to_qr_code="https://github.com",
#             category = category,
#             time_created = datetime.datetime.now(),
#             qr_code = b"",
#             extra_info = "Extra"            
#         )