from django.views.generic import TemplateView, View, UpdateView, DeleteView, CreateView
from thuvienbk.models import Book, BookAuthor, PaymentMethod
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from web3 import Web3
import json
import collections
from thuvienbk.solidity_parser import symbolic, parser
# pprint de debug
from pprint import pprint



from django.shortcuts import get_object_or_404, render

from .forms import UserUpdateForm, ProfileUpdateForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['books_highly'] =  Book.objects.all()[:3]
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    


class HistoryPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/history.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HistoryPageView, self).get_context_data(*args, **kwargs)

        # Get user address
        user_address = PaymentMethod.objects.get(user_id= self.request.user.id).wallet_address

        # Implement web3
        # Connecting to web3 + Initiating web3
        url = 'https://rinkeby.infura.io/v3/95b9bf5b38fb4b9d939b3ae99cfa8386'
        web3 = Web3(Web3.HTTPProvider(url))

        # Contract address + abi
        contract_address = web3.toChecksumAddress("0x30d9072A565be8C25580e442C872aF6421b26cD8")
        abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"constant":true,"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getOrderHistory","outputs":[{"components":[{"internalType":"uint256","name":"token","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint8","name":"quantity","type":"uint8"},{"internalType":"uint256","name":"price_in_wei","type":"uint256"}],"internalType":"struct BookStoreInit.order[]","name":"","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"_from","type":"address"},{"internalType":"uint256","name":"_token","type":"uint256"},{"internalType":"uint8","name":"_quantity","type":"uint8"}],"name":"implementTransaction","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"incognitoAddress","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

        #Creating contract instance
        contract = web3.eth.contract(contract_address, abi=abi)

        # Request view orders list
        result = contract.functions.getOrderHistory(user_address).call()
        print("Order list: ")

        # print(result)

        data = {}
        count = 0
        for item in result:
            data[count] = (json.dumps(item))
            count += 1
            print(item)

        print(data)
        context['tx_list'] = data
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
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
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
    print(context)
    return render(request, 'pages/Audit-verHtml/audit.html', context)

################################ Phần của link ########################################

def f_write(f, name, value, Type):
    f.write(name)
    f.write('=')
    if Type=='str': 
        f.write("\"")
        f.write(str(value))
        f.write("\"")
    if Type=='dict' or Type=='number': 
        f.write(str(value))
    f.write('\n')
def runSC(admin, user_address ,ownerToOrderList, ownerToBalance, totalToken,book_isbn,book_quantity, book_price):
    # cần build msg
    
    asttree = parser.parse_file("thuvienbk/BookStore.sol")
    f = open("thuvienbk/renderToPython.py", 'w')
    f.write(open('thuvienbk/init.py').read())
    f_write(f, 'admin', admin, 'str')
    f_write(f, 'user_address', user_address, 'str')
    f_write(f, 'totalToken', totalToken, 'dict')
    print(totalToken)
    f.write("ownerToOrderList = collections.defaultdict(lambda : 0)\n")
    f_write(f,"ownerToOrderList[user_address]", ownerToOrderList[user_address], 'dict')
    f.write("ownerToOrderList[user_address]=convert(ownerToOrderList[user_address])\n")
    f.write("ownerToBalance= collections.defaultdict(lambda : 0)\n")
    f_write(f,"ownerToBalance[admin]", ownerToBalance[admin], 'number' )
    f_write(f,"ownerToBalance[user_address]", ownerToBalance[user_address], 'number' )
    f_write(f,"ownerToBalance['0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De']", ownerToBalance['0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De'], 'number' )
    f_write(f,"book_quantity", book_quantity, 'number' )
    f_write(f,"book_price", book_price, 'number' )
    f_write(f,"book_isbn", book_isbn, 'str' )
    f.write("msg = Msg(admin, user_address, book_price*book_quantity)\n")
    f.write("ownerToBalance['0x0000'] = msg.value\n")
    f.close()
    
    f = open("thuvienbk/renderToPython.py", 'a+')
    # change something with bugs
    dse = symbolic.SymbolicExecution(asttree,f )
    listFunc= dse.run()
    #import time ;time.sleep(1)
    f.close()
    
    
    import thuvienbk.renderToPython as renderToPython
    transaction = renderToPython.BookStore()
    init = (renderToPython.admin,
            
            (renderToPython.ownerToBalance[renderToPython.admin],  
            renderToPython.getSumToken(renderToPython.totalToken)), 
            
            renderToPython.user_address,
            (renderToPython.ownerToBalance[renderToPython.user_address]+renderToPython.msg.value,
            renderToPython.getSumToken(renderToPython.ownerToOrderList[renderToPython.user_address]) ))
    transaction.implementTransaction(user_address, book_isbn, book_quantity )
    final = (renderToPython.admin,
            
            (renderToPython.ownerToBalance[renderToPython.admin],  
            renderToPython.getSumToken(renderToPython.totalToken)), 
            
            renderToPython.user_address,
            (renderToPython.ownerToBalance[renderToPython.user_address],
            renderToPython.getSumToken(renderToPython.ownerToOrderList[renderToPython.user_address]) ))
    #f = open("thuvienbk/renderToPython.py", 'w')
    #f.close()
    return init, final



def audit_request(request):
    if request.method == 'POST':
        print("Im auditing...")
        
        
        # Get user info
        user_address = PaymentMethod.objects.get(user_id= request.user.id).wallet_address

        # Get book price
        book_price = Book.objects.get(ISBN=request.POST['isbn']).price
        book_isbn = str(Book.objects.get(ISBN=request.POST['isbn']).ISBN)
        book_quantity = 1
        

        # Implement web3
        # Connecting to web3 + Initiating web3
        url = 'https://rinkeby.infura.io/v3/95b9bf5b38fb4b9d939b3ae99cfa8386'
        web3 = Web3(Web3.HTTPProvider(url))

        # Contract address + abi
        contract_address = web3.toChecksumAddress("0x30d9072A565be8C25580e442C872aF6421b26cD8")
        abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"constant":true,"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getOrderHistory","outputs":[{"components":[{"internalType":"uint256","name":"token","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint8","name":"quantity","type":"uint8"},{"internalType":"uint256","name":"price_in_wei","type":"uint256"}],"internalType":"struct BookStoreInit.order[]","name":"","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"_from","type":"address"},{"internalType":"uint256","name":"_token","type":"uint256"},{"internalType":"uint8","name":"_quantity","type":"uint8"}],"name":"implementTransaction","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"incognitoAddress","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

        #Creating contract instance
        contract = web3.eth.contract(contract_address, abi=abi)

        # Admin address
        admin = contract.functions.owner().call()

        ownerToOrderList= collections.defaultdict(lambda : 0)
        ownerToOrderList[user_address] = contract.functions.getOrderHistory(user_address).call()
        
        ownerToBalance= collections.defaultdict(lambda : 0)

        ownerToBalance[admin] = web3.eth.getBalance(admin)
        ownerToBalance[user_address] =  web3.eth.getBalance(user_address)
        ownerToBalance['0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De']= web3.eth.getBalance('0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De')
        lst = Book.objects.all()
        in_stocks=  Book.objects.get(ISBN=request.POST['isbn']).in_stocks
        totalToken = {}
        
        for x in range(0, len(lst)):
            totalToken[str(lst[x].ISBN)] = lst[x].in_stocks
            #print(type(lst[x]))
        #totalToken = {book_isbn: 3, 'physics':12 , 'computer': 5}
        print(totalToken)
        SC = runSC(admin, user_address ,ownerToOrderList, ownerToBalance, totalToken , book_isbn, book_quantity, book_price*pow(10,18))
        data ={}
        data['audit_result'] = SC[1]
        print("Result neeeeeeeeeee: ")
        print(SC[0])
        print(SC[1])
        return JsonResponse(data)

################################ Hết phần của link ########################################


def audit_result(request):
    if request.method == 'POST':
        print("Im listening...")
        
        # data mẫu thôi, tự mà kéo data về bằng web3
        # data = {
        #     'name': 'Vitor',
        #     'location': 'Finland',
        #     'is_active': True,
        #     'count': 28
        # }

        # Get user info
        user_address = PaymentMethod.objects.get(user_id= request.user.id).wallet_address
        user_pkey = PaymentMethod.objects.get(user_id= request.user.id).private_key

        # Get book price
        book_price = Book.objects.get(ISBN=request.POST['isbn']).price
        book_isbn = Book.objects.get(ISBN=request.POST['isbn']).ISBN
        book_quantity = 1

        # Implement web3
        # Connecting to web3 + Initiating web3
        url = 'https://rinkeby.infura.io/v3/95b9bf5b38fb4b9d939b3ae99cfa8386'
        web3 = Web3(Web3.HTTPProvider(url))

        # Contract address + abi
        contract_address = web3.toChecksumAddress("0x30d9072A565be8C25580e442C872aF6421b26cD8")
        abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"constant":true,"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getOrderHistory","outputs":[{"components":[{"internalType":"uint256","name":"token","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint8","name":"quantity","type":"uint8"},{"internalType":"uint256","name":"price_in_wei","type":"uint256"}],"internalType":"struct BookStoreInit.order[]","name":"","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"_from","type":"address"},{"internalType":"uint256","name":"_token","type":"uint256"},{"internalType":"uint8","name":"_quantity","type":"uint8"}],"name":"implementTransaction","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"incognitoAddress","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

        #Creating contract instance
        contract = web3.eth.contract(contract_address, abi=abi)

        #Call a simple blockNumer getter
        #print(web3.eth.blockNumber)


        #Prepare Implement transaction
        nonce = web3.eth.getTransactionCount(user_address)
        tx = contract.functions.implementTransaction(user_address, book_isbn, book_quantity).buildTransaction({
            'from': user_address,
            'value': web3.toWei(book_price*book_quantity, "ether"),
            'nonce': nonce
        })

        signed_tx = web3.eth.account.signTransaction(tx, user_pkey)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print("Transaction receipt: ")
        print(tx_receipt)

        # Request view orders list
        # result = contract.functions.getOrderHistory(user_address).call()
        # print("Order list: ")
        # print(result)
        
        # Phải làm kiểu này để data có dạng json
        data = {}
        data['tx_hash'] = tx_receipt.transactionHash.hex()
        data['contract'] = tx_receipt.to
        data['block_number'] = tx_receipt.blockNumber
        data['gas'] = tx_receipt.gasUsed

        return JsonResponse(data)
    # else:
    #     return render(request, 'pages/Audit-verHtml/audit.html', context)


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
