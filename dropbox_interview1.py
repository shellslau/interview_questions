"""

- /foo
    - /images
      - /foo.png
    - /temp
      - /baz
        - /that.foo
    - /bar.png
    - /file.tmp
    - /other.temp
    - /blah.txt
    
def find_duplicates(path)
find_duplicates('foo')

[images, temp, bar.png, file.tmp, other.temp, blah.txt]


[
   ['/foo/bar.png', '/foo/images/foo.png'],
   ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/baz/that.foo']
]


def list_dir(path: str) -> List[str]:
    Returns a non-recursive list of entries (files and folders) with relative
    paths in this directory only. Basically the same functionality as doing “ls”
    or “dir” in a shell 
    pass 

def is_dir(path: str) -> bool:
    pass

def join_path(path: str, subpath: str) -> str:
    platform independent
    pass


file = File('/foo/bar.txt')
file.read(1000)  # reads 1000 bytes from the file. returns None when EOF reached
file.size # returns the size

class Hash
    def update(self, input_string):
        pass
        
    def digest(self):
        pass
        
h = Hash()
h.update('foo')
h.update('bar')
hashval = h.digest()

h = Hash()
h.update('foobar')
hashval = h.digest()


"""
def make_file_list(path):
    files = list_dir(path)
    filenames = []
    for file in files:
        if not is_dir(file):
            filenames.append(join_path(path, file))
        else:
            files = files + make_file_list(file)
    return filenames
    
def make_size_dict(path):
    files = make_file_list(path)
    sizes = {}
    for filename in files:
        file = File(filename)
        if sizes[file.size]:
            sizes[file.size].append(file)
        else:
            sizes[file.size] = [file]
    return sizes

def make_hashval(filename):
    file = File(filename)
    h = Hash()
    val = file.read(1000)
    while val:
        h.update(val)
        val = file.read(1000)
    return h.digest()
    
def find_duplicate(path):
    size_dict = make_size_dict(path)
    dups = []
    for size in size_dict:
        if len(size_dict[size]) > 1:
            hashes = {}
            for filename in size_dict[size]:
                hash = make_hash_val(filename)
                if hashes[hash]:
                    hashes[hash].append(filename)
                else:
                    hashes[hash] = [filename]
            for hash in hashes:
                if len(hashes[hash]) > 1:
                    dups.append(hashes[hash])
    return dups
            