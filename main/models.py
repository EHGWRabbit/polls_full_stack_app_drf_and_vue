from django.db import models
from django.db import IntegrityError 


class Problem(models.Model):
    title = models.CharField(max_length=250)
    no_solved_tasks = models.IntegerField()
    votes = models.IntegerField(default=0)
    global_ecology = models.IntegerField(default=1)
    global_economic = models.IntegerField(default=1)
    global_poor = models.IntegerField(default=1)
    global_food = models.IntegerField(default=1)

    def __str__(self):
        return self.title 

class Cry(models.Model):
    ip_address = models.CharField(max_length=20, default='None', unique=True)
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, related_name='problem')

    def save(self, commit=True, *args, **kwargs):
        if commit:
            try:
                self.problem.cry += 1
                self.problem.save()
                super(Cry, self).save(*args, **kwargs)
            except IntegrityError:
                self.problem.cry -= 1
                self.problem.save()
                raise IntegrityError 
        else:
            raise IntegrityError
    

    def __str__(self):
        return self.problem.title
