from django.db import models
from users.models import User

class Category(models.Model):
    """
    A model representing a category that a 3D printable model can belong to.

    Fields:
        name (models.CharField): The name of the category.
        print_models (models.ManyToManyField): The 3D printable models that belong to this category.
    """
    name = models.CharField(max_length=50)

class PrintModel(models.Model):
    """
    A model representing a 3D printable model available for purchase on the service.

    Fields:
        name (models.CharField): The name of the printable model.
        description (models.TextField): A description of the printable model.
        price (models.DecimalField): The price of the printable model.
        download_file (models.FileField): The file containing the 3D model.
        owner (models.ForeignKey): The user who owns the printable model.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    download_file = models.FileField(upload_to='3D_models')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='print_models')


class SampleImage(models.Model):
    """
    A model representing an image of a 3D printable model.

    Fields:
        print_model (models.ForeignKey): The printable model the image belongs to.
        image (models.ImageField): The image file.
    """
    print_model = models.ForeignKey(PrintModel, on_delete=models.CASCADE, related_name='sample_images')
    image = models.ImageField(upload_to='sample_images')


class DownloadableFile(models.Model):
    """
    A model representing a file that can be downloaded for a 3D printable model.

    Fields:
        print_model (models.ForeignKey): The printable model the file belongs to.
        file (models.FileField): The file.
    """
    print_model = models.ForeignKey(PrintModel, on_delete=models.CASCADE, related_name='downloadable_files')
    file = models.FileField(upload_to='downloadable_files')


class Tag(models.Model):
    """
    A model representing a tag that can be associated with a 3D printable model.

    Fields:
        name (models.CharField): The name of the tag.
    """
    name = models.CharField(max_length=50)


class PrintModelTag(models.Model):
    """
    A model representing the relationship between a 3D print


    Regenerate response
    """
    print_model = models.ForeignKey(PrintModel, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='print_models')

class Order(models.Model):
    """
    A model representing an order made by a user on the 3D printing service.

    Fields:
        user (models.ForeignKey): The user who made the order.
        print_models (models.ManyToManyField): The 3D printable models included in the order.
        total_price (models.DecimalField): The total price of the order.
        order_date (models.DateTimeField): The date and time the order was made.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    print_models = models.ManyToManyField(PrintModel, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    """
    A model representing a review made by a user for a 3D printable model.

    Fields:
        print_model (models.ForeignKey): The 3D printable model being reviewed.
        user (models.ForeignKey): The user who made the review.
        rating (models.PositiveSmallIntegerField): The rating given by the user (out of 5).
        text (models.TextField): The review text.
    """
    print_model = models.ForeignKey(PrintModel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()


class Payment(models.Model):
    """
    A model representing a payment made for an order on the 3D printing service.

    Fields:
        order (models.OneToOneField): The order being paid for.
        payment_method (models.CharField): The payment method used.
        credit_card_number (models.CharField): The credit card number used (optional).
    """
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=50)
    credit_card_number = models.CharField(max_length=20, blank=True)