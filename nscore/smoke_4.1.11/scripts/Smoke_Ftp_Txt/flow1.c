#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void flow1()
{
    ns_ftp_get("page1",
	"FTP_SERVER=10.10.30.38:1025",
        "USER_ID=netstorm",
        //"USER_ID={uname}",
        "PASSWORD=netstorm",
        //"PASSWORD={pass}",
        "PASSIVE=%type",
        "TYPE=%rr_type",
        "FILE=largetext.txt"
        %name
    );

    ns_ftp_put("page2",
       "FTP_SERVER=10.10.30.38:1025",
       "USER_ID=netstorm",
       "PASSWORD=netstorm",
       "PASSIVE=%type",
       "TYPE=%rr_type",
       "FILE=/home/netstorm/work/scripts/Smoke/Smoke/Smoke_Ftp_Txt/xyz.txt"
);
}
