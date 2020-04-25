# Merkle-Tree-Implementation-using-Python
Merkle Tree Implementation using Python

Merkle tree implementation using Python and hashlib library

The project is comprised of a MerkleTree object, containing a createMerkleTree method

```
class MerkleTree(object):
    def __init__(self):
        pass
```
Initialize constructor for MerkleTree object
```
    # markle tree create method taking a list and a hash function
    def createMerkleTree(self, list, hash):
        if not list:
            raise ValueError(
            'Missing List'
            )

        if(len(list) == 1):
            return list
```
Since this is a recursive implementation, once we have one node (root) we will return the list.

```
        tempList = []
```
Initialize temp list to store new leaves

```
        if( len(list) % 2 != 0):
            list.append(list[len(list)-1])
```
If list is odd, append tail to list
```
        for leaf in xrange(0, len(list), 2):
            currentHash = hash(list[leaf] + list[leaf+1])
            tempList.append(currentHash.hexdigest())

        return self.createMerkleTree(tempList, hash)
 ```

A simple test using uuid to generate random hashes and create a list:

```
import uuid
    hashes = []

    for x in xrange(0,10):
        hashes.append(str(uuid.uuid4().hex))

    print 'hashes {0}'.format(hashes)
    print 'finished creating hashes'
    cls = MerkleTree()
    mk = cls.createMerkleTree(hashes, hashlib.sha256)
    print 'finding merkle tree root \n'

    print 'merkle tree root is {0}'.format(mk)
```
