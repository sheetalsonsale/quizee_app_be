from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
  uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now_add=True)
  class Meta:
    abstract = True
  

class Category(BaseModel):
  
  category_name = models.CharField(max_length=10)
  def __str__(self):
        return self.category_name 

class Question(BaseModel):
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Category')
  question = models.CharField(max_length=100)
  marks = models.IntegerField(default=5)
  def __str__(self):
        return self.question 

class Answer(BaseModel):
  Question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='Question')
  Answer = models.CharField(max_length=100)
  is_correct = models.BooleanField(default=False)
  def __str__(self):
        return self.Answer 

 