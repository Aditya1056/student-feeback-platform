from django.db import models
# from djangoratings.fields import RatingField

from account.models import (
    Faculty,
    Student,
)
from personal.models import Course

# Create your models here.

class Feedback(models.Model) :

    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    
    content = models.TextField(max_length=255, blank=False)
    # course_rating = RatingField(range=10)
    course_rating = models.CharField(max_length=255, choices=RATING_CHOICES, null=False)
    # course = models.CharField(max_length=255, null=False)
    course = models.ForeignKey(Course, blank=False, null=True, on_delete=models.SET_NULL)

    is_draft = models.BooleanField(default = False)


    upvotes = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL) # set_null or cascade ??????
    # since the student ID here would be an entry in the primary key for a feedback (if there is no id used)
    # then we cannot use NULL to populate ON DELETE,

    date_submitted = models.DateTimeField(verbose_name = "date_submitted", auto_now_add = True)

    def __str__(self) :
        if not self.student :
            return f"student deleted ({self.id})"
        return self.student.name + ", " + self.course.course_code


class Voting(models.Model) :
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL) # set_null or cascade ??????
    feedback = models.ForeignKey(Feedback, null=True, on_delete=models.SET_NULL)

    upvotable = models.BooleanField(default = True)
    downvotable = models.BooleanField(default = True)


    def __str__(self) :
        if not self.student or not self.feedback :
            return f"student or feedback deleted ({self.id})"
        return self.student.name + '_' + str(self.feedback.course) + '_' + str(self.feedback.id)


class FacultyVoting(models.Model) :
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL) # set_null or cascade ??????
    feedback = models.ForeignKey(Feedback, null=True, on_delete=models.SET_NULL)

    upvotable = models.BooleanField(default = True)
    downvotable = models.BooleanField(default = True)


    def __str__(self) :
        if not self.faculty or not self.feedback :
            return f"faculty or feedback deleted ({self.id})"
        return self.faculty.name + '_' + str(self.feedback.course) + '_' + str(self.feedback.id)

class TestModel(models.Model) :
    name = models.CharField(max_length=256)


    def __str__(self) :
        return self.name