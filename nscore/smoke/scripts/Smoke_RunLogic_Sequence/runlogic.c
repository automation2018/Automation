#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"


extern int init_script();
extern int exit_script();

typedef void FlowReturn;

// Note: Following extern declaration is used to find the list of used flows. Do not delete/edit it
// Start - List of used flows in the runlogic
extern FlowReturn LoginLogout();
extern FlowReturn PassengerDetail();
extern FlowReturn Reservation();
extern FlowReturn Tours();
// End - List of used flows in the runlogic
%per_value1
%per_value2

void runlogic()
{
    NSDL2_RUNLOGIC(NULL, NULL, "Executing init_script()");

    init_script();

    NSDL2_RUNLOGIC(NULL, NULL, "Executing sequence block - Block1");
    {
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - LoginLogout");
        LoginLogout();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - PassengerDetail");
        PassengerDetail();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Reservation");
        Reservation();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Tours");
        Tours();
    }

    NSDL2_RUNLOGIC(NULL, NULL, "Executing ns_exit_session()");
    ns_exit_session();
}
