/*-----------------------------------------------------------------------------
    Name: fetch0
    Generated By: netstorm
    Date of generation: 9/30/2011 10:12:47
    Flow details:
    Modification History:
-----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void fetch0()
{
    ns_web_url ("url_page1_html",
        "URL=http://127.0.0.1/custom/samples/autofetch/url_start.html",
    INLINE_URLS,
            "URL=http://127.0.0.1/custom/samples/autofetch/url_page1_embd1.html", END_INLINE,
            "URL=http://127.0.0.1/custom/samples/autofetch/url_page1_embd2.html", END_INLINE
    );

    ns_page_think_time(0.0);

    ns_web_url ("url_page2_html",
        "URL=http://127.0.0.1/custom/samples/autofetch/url_Index.html",
    INLINE_URLS,
            "URL=http://127.0.0.1/custom/samples/autofetch/url_page2_embd1.html", END_INLINE,
            "URL=http://127.0.0.1/custom/samples/autofetch/url_page2_embd2.html", END_INLINE
    );

    ns_page_think_time(0);
}
