/*-----------------------------------------------------------------------------
    Name: MainUrlAuth
    Generated By: netstorm
    Date of generation: 02/26/2012 11:12:39
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void MainUrlAuth()
{
    ns_web_url ("ntlm_html",
        "URL=http://127.0.0.1/Ntlm/ntlm.html",
        "HTTPAuthUserName=%Username",
        "HTTPAuthPassword=%Password"

);
 
   ns_web_url ("index_html",
        "URL=http://127.0.0.1/Ntlm/flower.html", 
        "HTTPAuthUserName={Usrname}",
        "HTTPAuthPassword={Passwd}",

);

         ns_page_think_time(0);
   ns_web_url ("ntlm_html1",
        "URL=http://127.0.0.1/Ntlm/ntlm_New.html",
        "HTTPAuthUserName={Usrname}",
        "HTTPAuthPassword={Passwd}",
    
);

}
