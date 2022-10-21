from django.shortcuts import get_object_or_404
from todolist.models import Tasks
from django.views.generic import DetailView


class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Tasks
    context_object_name = 'todo_task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset