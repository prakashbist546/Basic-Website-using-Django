from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    JOB = 'Job'
    INTERN = 'Intern'
    VACANCY_TYPE_CHOICES = (
        (JOB, 'Job'),
        (INTERN, 'Intern'),
    )
    type = models.CharField(
        max_length=10,
        choices=VACANCY_TYPE_CHOICES,
        default=JOB,
    )
    slug = models.CharField(max_length=50, default=title)
    summary = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snip(self):
        return self.summary[:40]+'...'

    def monthname(self):
        n = int(self.date.month)
        months = (
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        )
        return months[n-1]













