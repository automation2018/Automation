/*-----------------------------------------------------------------------------
    Name: vuser
    Generated By: netstorm
    Date of generation: 7/27/2011 11:5:55
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void vuser()
{
    ns_web_url ("class2K_html",
        "URL=http://127.0.0.1/file_set/dir00000/class2K.html",
    );
    ns_page_think_time(0);

    ns_web_url ("class2K_html_1",
        "URL=http://127.0.0.1/file_set/dir00000/class2K.html?{Pagename}",
      "BODY={Pagename}"   
 );
    ns_page_think_time(0);
}
