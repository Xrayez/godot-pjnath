#include "pjnath_wrap.h"

PJNATH::PJNATH() {
    
}

PJNATH::~PJNATH() {
    
}

void PJNATH::initialize() {
    pj_init();
    pjlib_util_init();
    pjnath_init();
}

void PJNATH::_bind_methods() {

    ClassDB::bind_method(D_METHOD("initialize"), &PJNATH::initialize);
}
