from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView,UpdateView, DeleteView

from .models import AdvUser
from .forms import  ChangeUserInfoForm, RegisterUserForm
from django.urls import reverse_lazy,reverse
from django.views.generic.base import TemplateView
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.signing import BadSignature
from .utilities import signer

from authapp.captcha_decorators import check_recaptcha


#-----------------------------------------------------------------------------------------------------------
class RcLoginView(LoginView):
    template_name = 'profile/login.html'

    """
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['modelsCadillac'] = SuperModelAuto.objects.filter(markAuto__title='Cadillac')
        context['modelsChevrolet'] = SuperModelAuto.objects.filter(markAuto__title='Chevrolet')
        context['modelsHummer'] = SuperModelAuto.objects.filter(markAuto__title='Hummer')
        context['modelsGMC'] = SuperModelAuto.objects.filter(markAuto__title='GMC')
        context['posts_co'] = Post.objects.all().count()
        context['super_posts_co'] = SuperPost.objects.all().count()
        return context 
    """
class RcLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'profile/logout.html'
        

@login_required
def profile(request):
    #--------обязательный блок-------------------------
    
    #--------------------------------------------------
    #context = {'posts_co':posts_co,'modelsCadillac':modelsCadillac,'modelsChevrolet':modelsChevrolet,
    #'modelsHummer':modelsHummer,'modelsGMC':modelsGMC,'super_posts_co':super_posts_co}
    return render(request, 'profile/profile.html',)
        
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'profile/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('profile')
    success_message = 'Личные данные пользователя изменены'
    
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class RcPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/password_change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Пароль пользователя изменен'

#@check_recaptcha
class RegisterView(CreateView):
    model = AdvUser
    form_class = RegisterUserForm
    template_name = 'profile/register_user.html'
 
    def form_valid(self, form):
        # проверка валидности reCAPTCHA
        if self.request.recaptcha_is_valid:
            form.save()
            return render(self.request, 'profile/register_done.html', self.get_context_data())
        return render(self.request, 'profile/register_user.html', self.get_context_data())


class RegisterDoneView(TemplateView):
    template_name = 'profile/register_done.html'

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'profile/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'profile/user_is_activated.html'
    else:
        template = 'profile/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'profile/delete_user.html'
    success_url = reverse_lazy('index')
    
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                                      'Пользователь удалён')
        return super().post(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

#------------------------------------------------------------
