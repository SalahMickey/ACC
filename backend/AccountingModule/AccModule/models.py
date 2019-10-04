from django.db import models
import datetime
# Create your models here.
class company(models.Model):
    name = models.CharField()
    
class Accounts_Types(models.Model):
    name = models.CharField(max_length=250)

class COA(models.Model):
    code = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=200)
    lvl = models.IntegerField(default=1)
    parent = models.ForeignKey('self',null=True, related_name='father', on_delete=models.PROTECT)
    part2code = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('Accounts_Types', on_delete=models.PROTECT)
    credit = models.DecimalField(max_digits=20, decimal_places=10,null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=10,null=True)
    def __str__(self):
        return self.name

class FiscalYear(models.Model):
    name = models.CharField(max_length=64)
    date_fr = models.DateField()
    date_to = models.DateField()


class Period(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT)

class journal(models.Model):
    description = models.CharField(max_length=50)
    date = models.DateTimeField()

class journalEntry(models.Model):
    journal_id = models.ForeignKey(journal, on_delete=models.PROTECT)
    account = models.ForeignKey(COA, on_delete=models.PROTECT)
    credit = models.DecimalField(max_digits=19, decimal_places=6)
    debit = models.DecimalField(max_digits=19, decimal_places=6)
