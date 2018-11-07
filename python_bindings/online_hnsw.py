from hnsw_wrapper import pyhnsw_index, vector_key, vector_elem

class HNSW(pyhnsw_index):
    def __init__(self, random_seed=1, max_links=32, ef_construction=200):
        pyhnsw_index.__init__(self, random_seed, max_links, ef_construction)

    def insert(self, key, vector):
        pyhnsw_index.insert(self, key, vector_elem(vector))

    def remove(self, key):
        pyhnsw_index.remove(self, key)

    def search(self, target, nn, ef_search=None):
        if ef_search is None:
            ef_search = nn + 100

        return list(pyhnsw_index.search(self, vector_elem(target), nn, ef_search))

