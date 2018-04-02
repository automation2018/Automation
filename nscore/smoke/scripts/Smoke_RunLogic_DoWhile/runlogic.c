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
extern FlowReturn FlowWhile();
// End - List of used flows in the runlogic


void runlogic()
{
    NSDL2_RUNLOGIC(NULL, NULL, "Executing init_script()");

    init_script();

    NSDL2_RUNLOGIC(NULL, NULL, "Executing dowhile block - DoWhile. NS Variable = var_dowhile");
    {

        NSDL2_RUNLOGIC(NULL, NULL, "NS Variable value for block - DoWhile = %d", ns_get_int_val("var_dowhile"));
        do
        {

            NSDL2_RUNLOGIC(NULL, NULL, "Executing sequence block - Seq");
            {
                NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - LoginLogout");
                LoginLogout();
                NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - FlowWhile");
                FlowWhile();
            }
        } while(ns_get_int_val("var_dowhile"));
    }

    NSDL2_RUNLOGIC(NULL, NULL, "Executing ns_exit_session()");
    ns_exit_session();
}
