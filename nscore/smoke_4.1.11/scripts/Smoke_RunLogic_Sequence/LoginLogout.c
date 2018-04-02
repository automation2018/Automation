/*-----------------------------------------------------------------------------
    Name: LoginLogout
    Recorded By: netstorm
    Date of recording: 7/14/2011 0:14:6
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"


void LoginLogout()
{
    ns_start_transaction("TxnLoginLogout");
    ns_web_url ("index_html",
        "URL=http://127.0.0.1/tours/index.html",
        "HEADER=Accept-Language: en-US",
        INLINE_URLS,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/login.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language: en-US", END_INLINE
    );

    ns_page_think_time(0.031);

    ns_web_url ("login",
        "URL=http://127.0.0.1/cgi-bin/login?userSession=75893.0884568651DQADHfApHDHfcDtccpfAttcf&username=saurabh&password=cavisson&JSFormSubmit=off&login.x=46&login.y=8",
        "HEADER=Accept-Language: en-US",
        INLINE_URLS,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/flights.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/home.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/flights.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/home.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/signoff.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/vep/images/velocigen.gif", "HEADER=Accept-Language: en-US", END_INLINE
    );

    ns_page_think_time(0.032);

    ns_web_url ("welcome",
        "URL=http://127.0.0.1/cgi-bin/welcome",
        "HEADER=Accept-Language: en-US",
        INLINE_URLS,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/sun_swede.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/login.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/images/banner_merctur.jpg", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/vep/images/velocigen.gif", "HEADER=Accept-Language: en-US", END_INLINE,
            "URL=http://127.0.0.1/tours/Merc10-dev/images/banner_animated.gif", "HEADER=Accept-Language: en-US", END_INLINE
    );

    ns_page_think_time(0.016);
    ns_end_transaction("TxnLoginLogout", NS_AUTO_STATUS);
}
