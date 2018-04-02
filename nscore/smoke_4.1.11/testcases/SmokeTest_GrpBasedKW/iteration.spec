$TestDescription|$KeyValue1|$KeyValue2|%URL|$SESSIONS|$Script1|$User1|$Check_Monitor1|$Check_Monitor2

# G_MAX_URL_RETRIES
# NS retries in case of SSL_HANDSHAKE, PARTIAL HEADER, CONFAIL

# configure hpd for ssl handshake fail
# add SSL_CLIENT_AUTHENTICATION 1 in hpd.conf and restart
#SMOKE-020-001|G_MAX_URL_RETRIES G1  0|SHOW_INITIATED 1|https://127.0.0.1/url_retry_ssl_fail.html|SESSIONS 1|hpd_tours_url_retry|1|#|#

# configure url such that response will be partial header
# send HEADER=Range: bytes=0-0 along with request
#SMOKE-020-002|G_MAX_URL_RETRIES G1  3|SHOW_INITIATED 1|https://127.0.0.1/url_retry_request_write_fail.html","HEADER=Range: bytes=0-0|SESSIONS 1|hpd_tours_url_retry|1|#|#

# connection fail url 
#SMOKE-020-003|G_MAX_URL_RETRIES G1 5|SHOW_INITIATED 1|http://10.10.30.96:8134/url_retry_confail.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
#SMOKE-020-004|G_MAX_URL_RETRIES ALL 5|SHOW_INITIATED 1|https://127.0.0.1/url_retry_ssl_fail.html|SESSIONS 1|hpd_tours_url_retry|1|#|#


# G_DISABLE_*_HEADER : accept, host, reuseaddr, ua, connection, use recorded host in host header, accept-encoding, all
SMOKE-020-005|G_DISABLE_ACCEPT_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-006|G_DISABLE_ACCEPT_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-007|G_DISABLE_HOST_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-008|G_DISABLE_HOST_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#

# Validation pending
SMOKE-020-009|G_DISABLE_REUSEADDR G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-010|G_DISABLE_REUSEADDR G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#

SMOKE-020-011|G_DISABLE_UA_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-012|G_DISABLE_UA_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-013|G_DISABLE_CONNECTION_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-014|G_DISABLE_CONNECTION_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-015|G_USE_RECORDED_HOST_IN_HOST_HDR G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-016|G_USE_RECORDED_HOST_IN_HOST_HDR G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-017|G_DISABLE_ACCEPT_ENC_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-018|G_DISABLE_ACCEPT_ENC_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-019|G_DISABLE_ALL_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-020|G_DISABLE_ALL_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-021|G_DISABLE_KA_HEADER G1 0|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#
SMOKE-020-022|G_DISABLE_KA_HEADER G1 1|#|http://127.0.0.1/tours/index.html|SESSIONS 1|hpd_tours_url_retry|1|#|#

# G_CONTINUE_ON_PAGE_ERROR <group> <page> <mode>
SMOKE-020-023|G_CONTINUE_ON_PAGE_ERROR G2 index 0|SGRP G2 NA Internet 0 hpd_tours_cont_on_err 1|http://127.0.0.1/tours/index11.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-024|G_CONTINUE_ON_PAGE_ERROR G1 index 1|SGRP G2 NA Internet 0 hpd_tours_cont_no_err 1|http://127.0.0.1/tours/index11.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-025|G_CONTINUE_ON_PAGE_ERROR G2 index 1|SGRP G2 NA Internet 0 hpd_tours_cont_on_err 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-026|G_CONTINUE_ON_PAGE_ERROR ALL ALL 1|SGRP G2 NA Internet 0 hpd_tours_cont_on_err 1|http://127.0.0.1/tours/indexxx.html|SESSIONS 2|hpd_tours_url_retry|1|#|#

# G_IDLE_MSECS <group> <time in miliseconds>
# SVC_TIME 2 50000
SMOKE-020-027|G_IDLE_MSECS ALL 30000|SGRP G2 NA Internet 0 hpd_tours_idle_msec 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-028|G_IDLE_MSECS G2 70000|SGRP G2 NA Internet 0 hpd_tours_idle_msec 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-029|G_IDLE_MSECS G2 50000|SGRP G2 NA Internet 0 hpd_tours_idle_msec 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#

# G_MAX_CON_PER_VUSER <group> 0 V1 V2 V3 V4 V5
SMOKE-020-030|G_MAX_CON_PER_VUSER G2 0 1 1 1 1 1|SGRP G2 NA Internet 0 hpd_tours_max_conn 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-031|G_MAX_CON_PER_VUSER G2 0 3 3 3 3 3|SGRP G2 NA Internet 0 hpd_tours_max_conn 1|http://127.0.0.1/tours/index.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-032|G_MAX_CON_PER_VUSER ALL 0 5 5 5 5 5|SGRP G2 NA Internet 0 hpd_tours_max_conn 2|http://127.0.0.1/tours/index.html|SESSIONS 3|hpd_tours_url_retry|1|#|#

###Virtual User Tracing - G_VUSER_TRACE <group> <mode>
SMOKE-020-033|G_VUSER_TRACE G1 0|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|CHECK_MONITOR NS virtualTrace1 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G2|CHECK_MONITOR NS virtualTrace2 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G1
SMOKE-020-034|G_VUSER_TRACE ALL 0|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|CHECK_MONITOR NS virtualTrace1 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G2|CHECK_MONITOR NS virtualTrace2 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G1
SMOKE-020-035|G_VUSER_TRACE G1 1|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|CHECK_MONITOR NS virtualTrace1 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G2|CHECK_MONITOR NS virtualTrace2 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G1
SMOKE-020-036|G_VUSER_TRACE ALL 1|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|CHECK_MONITOR NS virtualTrace1 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G2|CHECK_MONITOR NS virtualTrace2 3 Duration0 2 NA NA NA /opt/cavisson/monitors/custom/virtual_user_trace -g G1
SMOKE-020-037|G_VUSER_TRACE G1 2|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|#|#
SMOKE-020-038|G_VUSER_TRACE ALL 2|SGRP G2 NA Internet 0 hpd_tours 5|//|SESSIONS 10|hpd_tours2|5|#|#

#### G_ERR_CODE_OK - G_ERR_CODE_OK <<group> <mode> {either 0 or 1}
#If given '1' , then we set url status Success for all HTTP response code in 1xx, 2xx and 3xx group.
#If given '0', then we set url status success for error codes 200, 304, 301, 302. Also 401 is treated as success. All other HTTP status codes are treated as error.
SMOKE-020-039|G_ERR_CODE_OK G1 0|SGRP G2 NA Internet 0 hpd_tours_url_retry 1|http://127.0.0.1/101_test.html|SESSIONS 2|hpd_tours_url_retry|1|#|#
SMOKE-020-040|G_ERR_CODE_OK ALL 1|SGRP G2 NA Internet 0 hpd_tours_url_retry 1|http://127.0.0.1/101_test.html|SESSIONS 2|hpd_tours_url_retry|1|#|#


#####G_AVG_SSL_REUSE - G_AVG_SSL_REUSE <group> <percentage>
SMOKE-020-041|G_AVG_SSL_REUSE ALL 0|SGRP G2 NA Internet 0 hpd_tours_https 1|//|SESSIONS 2|hpd_tours_https|1|#|#
SMOKE-020-042|G_AVG_SSL_REUSE G1 0|SGRP G2 NA Internet 0 hpd_tours_https 1|//|SESSIONS 2|hpd_tours_https|1|#|#
SMOKE-020-043|G_AVG_SSL_REUSE G1 100|SGRP G2 NA Internet 0 hpd_tours_https 1|//|SESSIONS 2|hpd_tours_https|1|#|#
SMOKE-020-044|G_AVG_SSL_REUSE ALL 100|SGRP G2 NA Internet 0 hpd_tours_https 1|//|SESSIONS 2|hpd_tours_https|1|#|#

# DNS TIMEOUT:
#     1. DNS_SVC_TIME
#     2. G_DNS_TIMEOUT

# Added in performance suite
# G_CIPHER_LIST <group> <cipher> [multiple ciphers separated by : ]


# G_IGNORE_HASH_IN_URL
# G_PAGE_RELOAD
# G_CLICK_AWAY
