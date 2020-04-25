from hashlib import sha256

"""
Merkle Tree implementation in Python by J.P. Florez
"""
import hashlib
# Merkle tree class 
class MerkleTree(object):
    def __init__(self):
        pass
    # markle tree create method taking a list and a hash function
    def createMerkleTree(self, list, hash):
        if not list:
            raise ValueError(
            'Missing List'
        )

        if(len(list) == 1):
            return list

        tempList = []
        if( len(list) % 2 != 0):
            list.append(list[len(list)-1])
            
        for leaf in xrange(0, len(list), 2):
            currentHash = hash(list[leaf] + list[leaf+1])
            tempList.append(currentHash.hexdigest())

        return self.createMerkleTree(tempList, hash)
        
    

    
if __name__ == '__main__':
    print 'find hashes'

    import uuid
    hashes = []

    for x in xrange(0,10):
        hashes.append(str(uuid.uuid4().hex))

    # hashes.append("Hello")
    # hashes.append("Hola")

    print 'hashes {0}'.format(hashes)
    print 'finished creating hashes'
    cls = MerkleTree()
    mk = cls.createMerkleTree(hashes, hashlib.sha256)
    print 'finding merkle tree root \n'

    print 'merkle tree root is {0}'.format(mk)