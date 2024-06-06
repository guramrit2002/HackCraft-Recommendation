from django.db import models
import uuid
# Create your models here.

class HackathonRecord(models.Model):
    _id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
    problem_statement = models.CharField(max_length=1000,null=True)
    tag = models.CharField(max_length=300,null=True)
    tech = models.CharField(max_length=300,null=True)

# import csv
# from root.models import HackathonRecord

# # Path to your CSV file
# csv_file_path = 'E:/Projects/hackathondata.csv'

# # Open the CSV file and read its contents
# with open(csv_file_path, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # Create a new HackathonRecord instance for each row
#         hackathon_record = HackathonRecord(
#             problem_statement=row['problem'],
#             tag=row['tag'],
#             tech=row['tech']
#         )
#         # Save the instance to the database
#         hackathon_record.save()
        

