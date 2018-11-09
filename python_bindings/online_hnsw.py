import scipy.sparse as ss

from hnsw_wrapper import pyhnsw_index, dense_vector_t, sparse_elem_t, sparse_vector_t

class HNSW(pyhnsw_index):
    def __init__(self, random_seed=1, max_links=32, ef_construction=200, is_sparse=True):
        self.is_sparse = is_sparse
        pyhnsw_index.__init__(self, random_seed, max_links, ef_construction)

    def insert(self, key, vector):
        if self.is_sparse:
            vector = from_sparse(vector)
        else:
            vector = from_dense(vector)

        pyhnsw_index.insert(self, key, vector)

    def remove(self, key):
        pyhnsw_index.remove(self, key)

    def search(self, target, nn, ef_search=None):
        if ef_search is None:
            ef_search = nn + 100
        if self.is_sparse:
            target = from_sparse(target)
        else:
            target = from_dense(target)

        return list(pyhnsw_index.search(self, target, nn, ef_search))

def from_sparse(m):
    elems = []
    for i, v in zip(m.indices, m.data):
        elem = sparse_elem_t()
        elem.idx = int(i)
        elem.value = float(v)
        elems.append(elem)
    return sparse_vector_t(elems)

def from_dense(m):
    return dense_vector_t([float(x) for x in m])
