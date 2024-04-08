from django.db import models
from django.utils.translation import gettext as _

from django.utils import timezone

# Specify the default value for the new non-nullable field
default_value = timezone.now

class School(models.Model):
    
    school_name = models.CharField(_("school_name"), max_length=255)
    First_Name = models.CharField(_("First Name"), max_length=150)
    Last_Name = models.CharField(_("Last Name"), max_length=150)
    Year_Level = models.CharField(_("Year Level"), max_length=50)
    Class = models.CharField(_("Class"), max_length=50)
    Subject = models.CharField(_("Subject"), max_length=50)
    Answers = models.CharField(_("Answers"), max_length=255)
    Correct_Answers =  models.CharField(_("Correct Answers"), max_length=255)
    Question_Number = models.CharField(_("Question Number"), max_length=255)
    Subject_Contents = models.CharField(_("Subject Contents"), max_length=255)
    Assessment_Areas = models.CharField(_("Assessment Areas"), max_length=255)
    sydney_correct_count_percentage = models.CharField(_("sydney_correct_count_percentage"), max_length=255)
    sydney_average_score = models.CharField(_("sydney_average_score"), max_length=255)
    sydney_participants = models.CharField(_("sydney_participants"), max_length=255)
    student_score  = models.CharField(_("student_score"), max_length=255)
    student_total_assessed  = models.CharField(_("student_total_assessed"), max_length=255)
    student_area_assessed_score  = models.CharField(_("student_area_assessed_score"), max_length=255)
    total_area_assessed_score  = models.CharField(_("total_area_assessed_score"), max_length=255)
    participant  = models.CharField(_("participant"), max_length=255)
    correct_answer_percentage_per_class  = models.CharField(_("correct_answer_percentage_per_class"), max_length=255)
    average_score  = models.CharField(_("average_score"), max_length=255)
    school_percentile  = models.CharField(_("school_percentile"), max_length=255)
    sydney_percentile  = models.CharField(_("sydney_percentile"), max_length=255)
    strength_status = models.CharField(_("strength_status"), max_length=255)
    high_distinct_count = models.CharField(_("high_distinct_count"), max_length=255)
    distinct_count = models.CharField(_("distinct_count"), max_length=255)
    credit_count = models.CharField(_("credit_count"), max_length=255)
    participant_count = models.CharField(_("participant_count"), max_length=255)
    award = models.CharField(_("award"), max_length=255)