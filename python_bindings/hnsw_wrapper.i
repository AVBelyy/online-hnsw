%module hnsw_wrapper

%{
#define SWIG_FILE_WITH_INIT
#include "hnsw_wrapper.h"

%}

%include <stdint.i>
%include <std_vector.i>
%include "hnsw_wrapper.h"

namespace std {
    %template(vector_key) vector<py_key_t>;
    %template(vector_elem) vector<py_elem_t>;
}

