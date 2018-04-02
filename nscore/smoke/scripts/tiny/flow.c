/*-----------------------------------------------------------------------------
    Name: flow
    Generated By: netstorm
    Date of generation: 06/19/2012 01:35:43
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void flow()
{
    ns_start_transaction("VFabricDefault");
    ns_web_url ("index",
        "URL=http://127.0.0.1/index.jsp"
    );
    ns_end_transaction("VFabricDefault",NS_AUTO_STATUS);
  
    ns_start_transaction("VFabricSimpleServlet");
    ns_web_url ("simple_servlet",
        "URL=http://127.0.0.1/SimpleServlet/simple-servlet"
    );
    ns_end_transaction("VFabricSimpleServlet",NS_AUTO_STATUS);
    
    ns_start_transaction("VFabricHelloJSP");
    ns_web_url ("sample_jsp",
       "URL=http://127.0.0.1/sample/hello.jsp" 
    );
    ns_end_transaction("VFabricHelloJSP",NS_AUTO_STATUS);
    
    ns_start_transaction("VFabricHelloServlet");
    ns_web_url ("sample_servlet",     
       "URL=http://127.0.0.1/sample/hello"        
    ); 
    ns_end_transaction("VFabricHelloServlet",NS_AUTO_STATUS);
    
    ns_page_think_time(0);

}
