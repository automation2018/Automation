/*-----------------------------------------------------------------------------
    Name: CookieClient
    Generated By: netstorm
    Date of generation: 07/19/2012 11:29:15
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void CookieClient()
{
    ns_web_url ("CookieMacys_html",
        "URL=http://127.0.0.1/Cookie_Smoke/CookieMacys.html"
    );

    ns_page_think_time(0);

}
