from django.db import models

class Departmentbranch(models.Model):
    branch = models.CharField(max_length=150)
    def __str__(self):
        return self.branch
   
    
#==================Many to one relationship=======================    
class Studentdata(models.Model):
    dept= models.ForeignKey(Departmentbranch,on_delete=models.CASCADE)
    name= models.CharField(max_length=150)
    city= models.CharField(max_length=150)
    marks=models.IntegerField()


#==================Many to Many relationship=======================   
class Lecturer(models.Model):
    depbranch= models.ManyToManyField(Departmentbranch)
    Lecturer_name= models.CharField(max_length=150)

    def __str__(self):
        return self.Lecturer_name
                        
    ret = ''
    def get_dept_values(self):
        global ret
        for depbranch in self.depbranch.all():
            self.ret = self.ret + depbranch.branch +"," + " "
        return self.ret


