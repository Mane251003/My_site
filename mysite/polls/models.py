from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    rate=models.FloatField()
    count=models.IntegerField(default=0)


    def update_rating(self, new_rating):
        self.rate=(self.rate*self.count+new_rating)/(self.count+1)
        self.count+=1
        self.save()


    def __str__(self):
        return f"{self.title} {self.rate}"
    

    
