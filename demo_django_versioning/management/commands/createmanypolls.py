import timeit

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from simple_history.utils import bulk_create_with_history

from demo_django_versioning.models import Question, Choice


class Command(BaseCommand):
    help = 'Creates a bunch of polls so we can check the history'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating questions and choices via loop'))
        for i in range(0, 1001):
            question = Question.objects.create(
                question_text=f"Loop cext for {i}",
                pub_date=timezone.now(),
            )
            for x in range(0, 6):
                Choice.objects.create(
                    question=question,
                    choice_text=f"Choice {i} - {x}"
                )
                question.question_text = f"{question.question_text}, has {x} choices."
                question.save()

        self.stdout.write(self.style.SUCCESS('Creating questions via bulk insert.'))
        data = [
            Question(
                question_text=f'Bulk question {1000 + x}', pub_date=timezone.now()
            ) for x in range(1000000)
        ]
        start = timeit.default_timer()
        bulk_create_with_history(data, Question, batch_size=1000)
        stop = timeit.default_timer()
        self.stdout.write(self.style.SUCCESS(f'Done. Bulk creation took: {stop-start}'))
