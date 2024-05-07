from django.db import models

NUM_STAGES = 5
STAGES = range(1, NUM_STAGES + 1)


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(STAGES, STAGES),
        default=STAGES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else STAGES[0]

        if new_box in STAGES:
            self.box = new_box
            self.save()

        return self
