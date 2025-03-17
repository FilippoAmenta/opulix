from datetime import date, timedelta

from django.db.models import Sum
from django.contrib import admin
from django.utils.html import format_html
from django.utils.timezone import now
from django.template.loader import render_to_string

from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

from unfold.admin import ModelAdmin
from unfold.components import BaseComponent, register_component

from apps.expenses.models import (
    ExpenseCategory,
    ExpenseTag,
    Expense
)

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(TreeNodeModelAdmin, ModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    form = TreeNodeForm

    list_display = [
        'label',
        'color_display',
        'budget'
    ]
    list_editable = [
        'budget'
    ]
    search_fields = [
        'label',
    ]
    def color_display(self, obj):
        return format_html('<div style="width: 15px; height: 15px; background-color: {};" />',obj.color)
    color_display.short_description = "Color"

    list_before_template = "expenses/expense-category/list_before.html"

@register_component
class DriverActiveComponent(BaseComponent):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["children"] = render_to_string("helpers/kpi.html",
            {
                "total": 10,
                "progress": None,
                "percentage": None,
            },
        )
        return context


@admin.register(ExpenseTag)
class ExpenseTagAdmin(ModelAdmin):
    list_display = [
        'label',
        'archived',
    ]
    list_filter = [
        'archived'
    ]
    search_fields = [
        'label',
    ]

@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    list_display = [
        'date',
        'category',
        '_tags',
        'amount'
    ]

    def _tags(self, obj):
        return ", ".join(tag.label for tag in obj.tags.all()) 
    _tags.short_description = 'Tags'

    autocomplete_fields = [
        'category',
        'tags'
    ]

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request)
        today = now().date()

        this_month = today.month
        this_year = today.year

        if this_month == 1:
            last_month = 12
            last_year = this_year - 1
        else:
            last_month = this_month - 1
            last_year = this_year

        this_month_queryset = queryset.filter(date__year=this_year, date__month=this_month)
        last_month_queryset = queryset.filter(date__year=last_year, date__month=last_month)

        this_month_total = this_month_queryset.aggregate(total=Sum('amount'))['total'] or 0
        last_month_total = last_month_queryset.aggregate(total=Sum('amount'))['total'] or 0

        extra_context = extra_context or {}
        extra_context['this_month_total'] = this_month_total
        extra_context['last_month_total'] = last_month_total

        return super().changelist_view(request, extra_context=extra_context)


