#include <hnsw/distance.hpp>
#include <hnsw/index.hpp>

#include <string>
#include <vector>

// TODO: parameters
using py_key_t = size_t;
using py_elem_t = float;
using py_dist_t = hnsw::cosine_distance_t;

using py_index_t = hnsw::hnsw_index<py_key_t, std::vector<py_elem_t>, py_dist_t>;

class pyhnsw_index {
public:
    pyhnsw_index(std::uint_fast32_t random_seed, size_t max_links, size_t ef_construction);

    void insert(const py_key_t &key, const std::vector<py_elem_t> &vector);
    void remove(const py_key_t &key);
    std::vector<py_key_t> search(const std::vector<py_elem_t> &target, size_t nn, size_t ef) const;

private:
    py_index_t hnsw_index;
};
