from django.db import models

# Create your models here.

 
class ZettelThread(models.Model):
  fid = models.CharField(max_length=200)
  title = models.CharField(max_length=300)
  zettel_type = models.CharField(max_length=100, default="default")
  
  metadata = models.ManyToManyField('self')
  zettels = models.ManyToManyField('Zettel')

  def __str__(self):
    return self.fid + ": " + self.title

class Zettel(models.Model):
  zid = models.PositiveIntegerField()
  full_id = models.CharField(max_length=204)

  title = models.CharField(max_length=300)
  content = models.TextField()
  thread = models.ForeignKey(ZettelThread, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.full_id
