import hashlib
import os

def get_file_hash(filename):
    """Compute the hash of a file using SHA1"""
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def merkle_tree(files):
    """Compute the top hash of a Merkle hash tree for a list of files"""
    hashes = [get_file_hash(file) for file in files]
    while len(hashes) > 1:
        hashes = [hashlib.sha1(hashes[i].encode('utf-8') + hashes[i+1].encode('utf-8')).hexdigest() for i in range(0, len(hashes), 2)]
    return hashes[0]

# Example usage
files = ['L1.txt', 'L2.txt', 'L3.txt', 'L4.txt']
top_hash = merkle_tree(files)
print('Top hash:', top_hash)

# Modify one of the files and compute the top hash again
os.system('echo "Modified content" >> L1.txt')
new_top_hash = merkle_tree(files)
print('New top hash:', new_top_hash)