/*-----------------------------------------------------------------------------
    Name: authc
    Generated By: netstorm
    Date of generation: 7/13/2011 1:11:28
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"


void authc()
{
    ns_web_url ("authc",
        "URL=http://127.0.0.1/tours/index.html",
        "METHOD=POST",
    );

    ns_page_think_time(((double )ns_get_pg_think_time())/1000.0);

}