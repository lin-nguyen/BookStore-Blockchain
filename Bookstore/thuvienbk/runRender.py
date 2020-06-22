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
    from solidity_parser import symbolic, parser
    import collections
    asttree = parser.parse_file("BookStore.sol")
    f = open("renderToPython.py", 'w')
    f.write(open('init.py').read())
    f_write(f, 'admin', admin, 'str')
    f_write(f, 'user_address', user_address, 'str')
    f_write(f, 'totalToken', totalToken, 'dict')
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
    f = open("renderToPython.py", 'a+')
    dse = symbolic.SymbolicExecution(asttree,f )
    listFunc= dse.run()
    f.close()

    import renderToPython
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

    return init, final
    
################### write in function  ####################
def audit_result(): 
    
    import collections
    admin = "0xAAAA"
    user_address = "0xBBBB"
    book_isbn = 'mathematic'
    balance = 0
    book_quantity =1
    book_price = 0.2
    ownerToOrderList= collections.defaultdict(lambda : 0)
    ownerToOrderList[user_address] = [('mathematic', 0, 2, 0.1),('computer', 0, 4, 0.2) ]

    ownerToBalance= collections.defaultdict(lambda : 0)
    ownerToBalance[admin] = 100
    ownerToBalance[user_address] =20

    totalToken = {'mathematic': 3, 'physics':12 , 'computer': 5}

    result = runSC(admin, user_address ,ownerToOrderList, ownerToBalance, totalToken , book_isbn, book_quantity, book_price)
    print(result[0])
    print(result[1])
audit_result()