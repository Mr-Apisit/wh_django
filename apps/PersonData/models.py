from django.db import models



class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateField('date pubblish')
    
    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(verbose_name="this correct",default=False)
    
    