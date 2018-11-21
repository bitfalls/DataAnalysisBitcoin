#from blockchain import statistics
import blockchain
from collections import Counter, OrderedDict
from datetime import datetime
#print(statistics.get().blocks_size)

#print(blockchain.statistics.get().blocks_size)
#print(blockchain.blockexplorer.get_address('1FCUQUYRCjxSfkNk5XnKx1xfNYvdZScrGt').total_received)
#print(blockchain.blockexplorer.get_tx('6c62072cd17410c6b17a36de9119bef59d38044647e3908d5da720d24b063840'))
#print(blockchain.blockexplorer.get_address('1FCUQUYRCjxSfkNk5XnKx1xfNYvdZScrGt').total_sent)
#est = blockchain.blockexplorer.get_address('1FCUQUYRCjxSfkNk5XnKx1xfNYvdZScrGt')
#tt = test.transactions

def validation(addr_list, labeled_list):
    return 0



def label(labeled_list):
    for i in labeled_list:
        address = blockchain.blockexplorer.get_address(i)
        final_bal = address.final_balance/100000000
        trans = address.n_tx
        total_rec = address.total_received/100000000
        total_sent = address.total_sent/100000000
        print(final_bal/trans, total_rec/trans, trans, total_rec)

addr = '1EEqRvnS7XqMoXDcaGL7bLS3hzZi1qUZm1'
#tt = blockchain.blockexplorer.get_tx('6c62072cd17410c6b17a36de9119bef59d38044647e3908d5da720d24b063840')

def get_addresses(addr):
    main_address = blockchain.blockexplorer.get_address(addr)

    balance = main_address.final_balance
    
    output_addrs={}
    input_addrs={}
    tran_id = []
    time = []
    amt_spent = []
    amt_got = []
    
    sum_in = 0
    sum_out = 0
    imp_trans = []
    
    
    
    already_labeled = []
    
    for i in main_address.transactions:
        temp_list = []
        tran_id.append(i.hash)
        time.append(datetime.utcfromtimestamp(int(i.time)).strftime('%Y-%m-%d %H:%M:%S'))
        for j in i.inputs:
            temp_list.append(j.address)
        if (len(temp_list) > 1) & (addr in temp_list):
            temp_list.remove(addr)
            already_labeled.extend(temp_list)
        elif addr in temp_list:
            for x in i.outputs:
                if x.address not in output_addrs.keys():
                    output_addrs[x.address] = []
                output_addrs[x.address].append(x.value)
        else:
            for j in i.inputs:
                if j.address not in input_addrs.keys():
                    input_addrs[j.address] = []
                input_addrs[j.address].append(j.value)
                
    already_labeled = list(set(already_labeled))     
            
    for i in already_labeled:
        if i in input_addrs.keys():
            input_addrs.pop(i, None)
        if i in output_addrs.keys():
            output_addrs.pop(i, None)
    
        
    freq_addrs_in = sorted(input_addrs, key=lambda k: len(input_addrs[k]), reverse=True)
    freq_addrs_out = sorted(output_addrs, key=lambda k: len(output_addrs[k]), reverse=True)
    
    amt_addrs_in = {key: sum(input_addrs[key]) for key in input_addrs}
    amt_addrs_in = sorted(amt_addrs_in, key=lambda x: amt_addrs_in[x], reverse=True)
    amt_addrs_out = {key: sum(output_addrs[key]) for key in output_addrs}
    amt_addrs_out = sorted(amt_addrs_out, key=lambda x: amt_addrs_out[x], reverse=True)
    
    try:
        freq_addrs_in.remove(addr)
        amt_addrs_in.remove(addr)
        freq_addrs_out.remove(addr)
        amt_addrs_out.remove(addr)
    except:
        1
    final_list = {}
    for i in freq_addrs_out, amt_addrs_out, freq_addrs_in, amt_addrs_in:
    #    try:
    #        for j in i[0:10]:
    #            final_list.append(j)
    #    except:
    #        for j in i:
    #            final_list.append(j)
        for j in i:
            if j not in final_list.keys():
                final_list[j]=0
            final_list[j]= final_list[j]+1

    final_list = sorted(final_list.items(), key=lambda kv: kv[1], reverse=True)
    
    return final_list, already_labeled
#final_list = (Counter(final_list)).most_common
#print(final_list)

#for i in len(final_list):
#    print(i, blockchain.blockexplorer.get_address(i).total_received, blockchain.blockexplorer.get_address(i).n_tx, blockchain.blockexplorer.get_address(i).final_balance)
#label(already_labeled)

final_list, already_labeled = get_addresses(addr) 
    
#validation(final_list, already_labeled)
