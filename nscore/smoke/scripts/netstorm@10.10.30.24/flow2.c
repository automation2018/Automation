#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"

void flow2()
{
    ns_smtp_send ("smtp_session",
	"SMTP_SERVER=websrv.cavisson.com",
	"USER_ID=%type",
	"PASSWORD=%rr_type",
	"FROM_EMAIL=%name",
	"TO_EMAILS=niraj.panda@cavisson.com",
	"CC_EMAILS=arun.yadav@cavisson.com",
	"BCC_EMAILS=mani.krishna@cavisson.com",
	"SUBJECT=SMTP smoke test Mail",
	"BODY=Hello this is test mail for SMTP smoke testing",
	"HEADER=X-Priority:3",
	"MESSAGE_COUNT=1"
    );
}
