
class custmer(models.Model):
   name = models.CharField(max_length=120)
   logo = models.ImageField(upload_to='customers', default='no_picture.jpg')

## imply that each customer is resprented by name

def __str__(self):
    return str(self.name)