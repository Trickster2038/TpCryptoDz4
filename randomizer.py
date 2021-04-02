print("=== WELCOME TO RANDOMIZER ===")
# python randomizer.py -n 3 -f list.txt -p 33
import sys
import argparse
import sha3
import hashlib
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--numbilets')
    parser.add_argument ('-f', '--file')
    parser.add_argument ('-p', '--parameter')
    return parser

def ticket_rand(n, data, seed, forbidden):
    hash1 = sha3.keccak_256()
    arg = data + ' ' + seed
    hash1.update(arg.encode('utf-8'))
    hash1.update(hash1.hexdigest().encode('utf-8'))
    hash1.update(hash1.hexdigest().encode('utf-8'))
    hash1_int = int(hash1.hexdigest(), 16)
    ticket = hash1_int % n
    return ticket
 
def ticket_rand2(n, data, seed, forbidden):
    #hash1 = sha3.keccak_256()
    arg = data + ' ' + seed
    hash1 = hashlib.sha256(arg.encode('utf-8'))
    arg = hash1.hexdigest()
    hash1_int = int(hash1.hexdigest(), 16)
    ticket = hash1_int % n
    # hash1 = hashlib.md5(arg.encode('utf-8'))
    # hash2 = hashlib.md5(hash1.hexdigest().encode('utf-8'))
    # hash3 = hashlib.md5(hash2.hexdigest().encode('utf-8'))
    #for i in range(1):
    while ticket in forbidden:
        hash1 = hashlib.sha256(arg.encode('utf-8'))
        arg = hash1.hexdigest()
        hash1_int = int(hash1.hexdigest(), 16)
        ticket = hash1_int % n
        print("tick : {}".format (data))

    forbidden += [ticket]
    #ticket = hash1_int % n
    return ticket
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print("n= {}".format (namespace.numbilets) )
    print("file= {}".format (namespace.file) )
    print("param= {}\n\n".format (namespace.parameter) )
    f = open(str(namespace.file), encoding='utf-8')
    taken = []
    for line in f:
    	print("{} : {}".format (line.strip(), 1+ticket_rand2(int(namespace.numbilets), line, namespace.parameter, taken)))
    	# line.encode('utf-8')
    print(taken)
    
    # benchmarks =====================================================================

    a = [0]*int(namespace.numbilets)
    s_linear = [0]*int(namespace.numbilets)
    s_quadro = [0]*int(namespace.numbilets)

    for y in range(100000):
    	i = ticket_rand2(int(namespace.numbilets), str(y), namespace.parameter, [])
    	#print(i)
    	a[i] += 1
    	#print(ticket_rand2(int(namespace.numbilets), str(y), namespace.parameter, []))
    for i in range(int(namespace.numbilets)):
    	print("delta[ticket{}] {:10.3f}%".format (i, 100*((a[i] / 100000.0)- (1.0/int(namespace.numbilets)))))
    	s_linear[i] = (100*((a[i] / 100000.0)- (1.0/int(namespace.numbilets)))) 
    	s_quadro[i] = (100*((a[i] / 100000.0)- (1.0/int(namespace.numbilets)))) ** 2

    avg_delta = s_linear[i] / int(namespace.numbilets)
    dispersion = s_quadro[i] / int(namespace.numbilets)
    print("avg delta {:10.3f}%".format (avg_delta))
    print("dispersion {:10.3f}%".format (dispersion))
        
