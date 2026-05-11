from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError  
from groups.models import Group, GroupMember
from django.contrib import messages

class CreateGroupView(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group
    template_name = 'groups/group_form.html'

class SingleGroupView(generic.DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

class ListGroupView(generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'

class JoinGroupView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
       
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            
            messages.warning(self.request, 'UPLINK_ERROR: Already a member of this sector!')
        else:
            
            messages.success(self.request, 'UPLINK_SUCCESS: Access granted to group.')
        
        return super().get(request, *args, **kwargs)
    
class LeaveGroupView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            
            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except GroupMember.DoesNotExist:
           
            messages.warning(self.request, 'SESSION_ERROR: No active membership found.')
        else:
            membership.delete()
        
            messages.success(self.request, 'SESSION_TERMINATED: You have left the sector.')

        return super().get(request, *args, **kwargs)