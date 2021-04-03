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
    arg = data + ' ' + seed
    hash1 = hashlib.sha256(arg.encode('utf-8'))
    arg = hash1.hexdigest()
    hash1_int = int(hash1.hexdigest(), 16)
    ticket = hash1_int % n
    while ticket in forbidden:
        hash1 = hashlib.sha256(arg.encode('utf-8'))
        arg = hash1.hexdigest()
        hash1_int = int(hash1.hexdigest(), 16)
        ticket = hash1_int % n
        #print("tick : {}".format (data))

    forbidden += [ticket]
    return ticket
 
if __name__ == '__main__':
    print("=== WELCOME TO TICKETS RANDOMIZER ===")
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print("\nn={} file={} param={}\n".format (namespace.numbilets,namespace.file,namespace.parameter) )
    f = open(str(namespace.file), encoding='utf-8')
    taken = []
    for line in f:
    	print("{:35s}\t{}".format (line.strip()+':', 1+ticket_rand(int(namespace.numbilets), line, namespace.parameter, taken)))
    #print(taken)
    
    # benchmarks =====================================================================

    print("\n=== BENCHMARKS(deltas of distribution 100k records) ===\n")

    a = [0]*int(namespace.numbilets)
    s_linear = 0
    s_quadro = 0

    for y in range(100000):
    	i = ticket_rand(int(namespace.numbilets), str(y), namespace.parameter, [])
    	a[i] += 1
    for i in range(int(namespace.numbilets)):
    	delta = abs(100*((a[i] / 100000.0)- (1.0/int(namespace.numbilets))))
    	print("delta[ticket{}] {:10.3f}%".format (i, delta))
    	s_linear += delta 
    	s_quadro += delta ** 2

    avg_delta = s_linear / int(namespace.numbilets)
    dispersion = s_quadro / int(namespace.numbilets)
    print("\navg delta:     {:10.3f}%".format (avg_delta))
    print("dispersion:    {:10.3f}%".format (dispersion))
        
