#include "hnsw_wrapper.h"

pyhnsw_index::pyhnsw_index(std::uint_fast32_t random_seed, size_t max_links, size_t ef_construction)
    : hnsw_index(random_seed) {
    hnsw::index_options_t options;
    options.max_links = max_links;
    options.ef_construction = ef_construction;
    hnsw_index.options = options;
}

void pyhnsw_index::insert(const py_key_t &key, const py_vector_t &vector) { // TODO: vector&&?
    hnsw_index.insert(key, vector);
}

void pyhnsw_index::remove(const py_key_t &key) {
    hnsw_index.remove(key);
}

std::vector<py_key_t> pyhnsw_index::search(const py_vector_t &target, size_t nn, size_t ef) const {
    std::vector<py_key_t> result;

    auto hnsw_result = hnsw_index.search(target, nn, ef);

    result.reserve(hnsw_result.size());

    for (auto & search_result : hnsw_result) {
        result.push_back(search_result.key);
    }

    return result;
}

