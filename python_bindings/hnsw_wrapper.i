%module hnsw_wrapper

%{
#define SWIG_FILE_WITH_INIT
#include "hnsw_wrapper.h"

%}

%include <stdint.i>
%include <std_vector.i>
%include <std_pair.i>
%include "hnsw_wrapper.h"
%include "../include/hnsw/detail/sparse_vector.hpp"

%template(vector_key_t) std::vector<py_key_t>;
%template(dense_vector_t) std::vector<py_elem_t>;
%template(sparse_elem_t) hnsw::detail::sparse_elem<py_elem_t>;
%template(sparse_vector_t) std::vector<hnsw::detail::sparse_elem<py_elem_t>>;
