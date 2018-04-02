/*-----------------------------------------------------------------------------
    Name: flow
    Recorded By: netstorm
    Date of recording: 08/11/2014 02:15:47
    Flow details:
    Build details: 4.0.0 (build# 9)
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void flow()
{

    ns_start_transaction("index");
    ns_web_url ("index_html",
  "URL=http://10.10.30.13:85/tours/ index.html}",
       // "URL=http://127.0.0.1/tours/index.html",
      //  "URL=https:// www.jcpenney.com/",
        //"PageLoadWaitTime=100",
        //"HEADER=Accept-Language:en-us",
        INLINE_URLS,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/login.gif", "HEADER=Accept-Language:en-us", END_INLINE
    );
    
    ns_end_transaction("index", NS_AUTO_STATUS);
    ns_page_think_time(1.5);

return;
/*
    ns_start_transaction("index_RV");
    ns_web_url ("index_html_RV",
        "URL=http://127.0.0.1/tours/index.html",
        "HEADER=Accept-Language:en-us",
        INLINE_URLS,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language:en-us", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/login.gif", "HEADER=Accept-Language:en-us", END_INLINE
    );

    ns_end_transaction("index_RV", NS_AUTO_STATUS);
    ns_page_think_time(3.0);
return; */
/*    
    ns_start_transaction("login");
    ns_web_url ("login",
        //"URL=http://127.0.0.1/&cgi-bin/login?&userSession=75893.0884568651DQADHfApHDHfcDtccpfAttcf&username=&password=&login.x=55&login.y=14&login=Login&JSFormSubmit=off",
        //"URL=http://127.0.0.1/cgi-bin/login?userSession=75893.0884568651DQADHfApHDHfcDtccpfAttcf&username=netstorm&password=netstorm&login.x=63&login.y=22&login=Login&JSFormSubmit=off",
        "URL=https://www.jcpenney.com/g/men/N-bwo3y?pageType=X2H2",
        "PageLoadWaitTime=100",
        "HEADER=Accept-Language:en-us",
        INLINE_URLS,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours{/Merc10-dev/images/flights.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/home.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/signoff.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/vep/images/velocigen.gif", "HEADER=Accept-Language:en-us", END_INLINE
    );
    ns_end_transaction_as("login", NS_AUTO_STATUS, "loginpage");
    ns_page_think_time(1.5);
    
    ns_start_transaction("welcome");
    ns_web_url ("welcome",
        //"URL=http://127.0.0.1/cgi-bin/welcome",
        "URL=https://www.jcpenney.com/g/mens-shirts/N-bwo3yD1nohp5?cm_re=DEPT-MENS-_-S2-VN-2-_-Shirts&cm_re=S1-_-CAT-_-ZoneA-_-1",
        "PageLoadWaitTime=100",
        "HEADER=Accept-Language:en-us",
        INLINE_URLS,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/vep/images/velocigen.gif", "HEADER=Accept-Language:en-us", END_INLINE,
            //"URL=http://127.0.0.1/tours/Merc10-dev/images/login.gif", "HEADER=Accept-Language:en-us", END_INLINE
    );
    ns_end_transaction("welcome", NS_AUTO_STATUS);
*/
}
