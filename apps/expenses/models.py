from django.db import models
from colorfield.fields import ColorField
from treenode.models import TreeNodeModel
from djmoney.models.fields import MoneyField

class ExpenseCategory(TreeNodeModel):
    label = models.CharField(max_length=63)
    color = ColorField()
    budget = MoneyField(max_digits=6, decimal_places=2, default_currency='EUR', null=True, blank=True)
    code = models.CharField(max_length=63, unique=True, blank=True, null=True)

    treenode_display_field = "label"
    
    external_id = models.CharField(max_length=63, blank=True, null=True)
    
    def __str__(self):
        return str(self.label)
    
    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Expense category'
        verbose_name_plural = 'Expense categories'


class ExpenseTag(models.Model):
    label = models.CharField(max_length=63, unique=True)
    archived = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.label)
    
    class Meta():
        verbose_name = 'Expense tag'
        verbose_name_plural = 'Expense tags'

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT, related_name='expenses')
    tags = models.ManyToManyField(ExpenseTag, blank=True, related_name='expenses')
    amount = MoneyField(max_digits=6, decimal_places=2, default_currency='EUR')

    def __str__(self):
        return str(self.category)
    
    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'