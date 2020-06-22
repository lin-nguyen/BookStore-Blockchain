from django.views.generic import TemplateView, View, UpdateView, DeleteView, CreateView
from thuvienbk.models import Book, BookAuthor, PaymentMethod, BookImage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


from django.shortcuts import get_object_or_404, render

from .forms import UserUpdateForm, ProfileUpdateForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['books_highly'] =  Book.objects.all()[:4]
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class HistoryPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/history.html'

class BookStoreView(TemplateView):
    template_name = 'pages/book/book_list.html'
    book_list = Book.objects.all()        
    def get_context_data(self, **kwargs):
        context = super(BookStoreView, self).get_context_data(**kwargs)
        context['books_highly'] =  Book.objects.all()[:4]
        context['books'] =  Book.objects.all()
        return context
        
class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'pages/profile.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'pages/profile.html', context)

@login_required
def audit_page_view(request, isbn):
    context = {
        'book': Book.objects.get(ISBN=isbn)
    }
    return render(request, 'pages/Audit-verHtml/audit.html', context)


class PurchasePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/auditSmartContract/src/MainPage.js'


class UserPaymentMethod(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'transaction_method/user_methods.html')


class PaymentMethodCreate(LoginRequiredMixin, CreateView):
    model = PaymentMethod
    template_name = 'transaction_method/method_create.html'
    fields = ['wallet_address', 'private_key']

    success_url = '/' + 'payment_methods'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PaymentMethodUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PaymentMethod
    template_name = 'transaction_method/method_update.html'
    fields = ['wallet_address', 'private_key']

    success_url = '/' + 'payment_methods'

    def test_func(self):
        method = self.get_object()
        if self.request.user == method.user:
            return True
        return False

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PaymentMethodDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PaymentMethod
    template_name = 'transaction_method/method_delete.html'
    success_url = '/' + 'payment_methods'

    def test_func(self):
        method = self.get_object()
        if self.request.user == method.user:
            return True
        return False

# class HotPageView(generic.ListView):
#     template_name = 'pages/hot.html'
#     context_object_name = 'book_list'
#
#     def get_queryset(self):
#         return Sach.objects.filter(dang_hot=True).order_by('id')
#
#
# class OldBookPageView(generic.ListView):
#     template_name = 'pages/old_book.html'
#     context_object_name = 'book_list'
#
#     def get_queryset(self):
#         return Sach.objects.all().order_by('id')
#
#
# class NewBookPageView(generic.ListView):
#     template_name = 'pages/new_book.html'
#     context_object_name = 'the_loai'
#
#     def get_queryset(self):
#         return TheLoaiSach.objects.all()
#
#
# def them_sach(request):
#     sach = Sach(Sach.objects.latest('id').id+1, ten_sach=request.POST["ten_sach"], tac_gia=request.POST["tac_gia"], nam_xuat_ban=request.POST["nam_xuat_ban"], gia_ban=request.POST["gia_ban"],  the_loai=TheLoaiSach.objects.filter(id=request.POST["the_loai"]).first(), so_luong_ton_kho = request.POST['so_luong'])
#     sach.save();
#
#     return HttpResponseRedirect('/old_book')
#
#
# def cap_nhat_so_luong(request):
#     sach=Sach.objects.filter(id=request.POST["sach_id"]).first()
#     sach.so_luong_ton_kho = request.POST["sl"]
#     sach.save();
#     return HttpResponseRedirect('/old_book')
#
#
# def cap_nhat_hot(request):
#     sach=Sach.objects.filter(id=request.POST["sach_id"]).first()
#     sach.dang_hot = request.POST["hot"]
#     sach.save();
#     return HttpResponseRedirect('/old_book')
