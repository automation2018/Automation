$K_TNAME|$K_NUM_USERS|$K_RAMP_UP_TIME|$K_DURATION|$K_RAMP_DOWN_TIME|$K_SCRIPT|$K_SVR_HOST|$K_RR_MODE|$K_REPORTING|$K_SESSION_PACING|$K_O_THINK_TIME|$K_THINK_TIME|$K_NEW_USER|$K_TRACING|$K_HIERARICHAL_VIEW|$K_HTTP_HEADER

##G_SEND_NS_TX_HTTP_HEADER

# with two groups,mode 0 and header
SMOKE-051-001|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|ALL 0 cavisson

# with one group,mode 1 and no header
SMOKE-051-002|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|G1 1

# with two groups,mode 1 and header 
SMOKE-051-003|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|ALL 1 cavisson

# with two two groups,mode 1,header and transaction name
SMOKE-051-004|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|ALL 1 cavisson astar

# with one group,mode 2 
SMOKE-051-005|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|G1 2

# with two groups,mode 2 and header
SMOKE-051-006|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|ALL 2 cavisson

# with two groups,mode 2,header and transaction name
SMOKE-051-007|1|ALL IMMEDIATELY|SESSIONS 2|ALL IMMEDIATELY|hpd_header|127.0.0.1 10.10.30.96 -|1|ALL 1|ALL 1 0 2000|ALL 1|ALL ALL 3 10 50|ALL 1|ALL 0 0 0 0|default|ALL 2 cavisson astar

#END_ITERATION


