from .models import Protocol
from django.views import generic


class ProtocolList(generic.ListView):
    model = Protocol
    paginate_by = 20
    context_object_name = 'protocol_list'
    queryset = Protocol.objects.order_by('-date')


class ProtocolDetail(generic.DetailView):
    model = Protocol


class AddProtocol(generic.edit.CreateView):
    model = Protocol
    fields = "__all__"
