#ifndef PJNATH_H
#define PJNATH_H

#include "core/reference.h"

#include "pjlib.h"
#include "pjlib-util.h"
#include "pjnath.h"

class PJNATH : public Reference  {
    GDCLASS(PJNATH, Reference);

private:
    pj_status_t status;

public:

PJNATH();
~PJNATH();

public:
    void initialize();

protected:
    static void _bind_methods();
};

#endif
