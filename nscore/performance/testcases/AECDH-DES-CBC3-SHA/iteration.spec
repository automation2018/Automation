$TestDescription|$ScriptName|$User|$OEF|$Wan|$HPM|%Url|$Ciphers|$KA_PCT|$NUM_KA
#
#CPS evaluation Testcase for ssl based NS requests
AECDH-DES-CBC3-SHA_CPS|scriptTiny|128|0 1 0|0|0|https|AECDH-DES-CBC3-SHA|G_KA_PCT ALL 0|G_NUM_KA ALL 1 1
#HPS evaluation Testcase for ssl based NS requests
AECDH-DES-CBC3-SHA_HPS|scriptTiny|128|0 1 0|0|0|https|AECDH-DES-CBC3-SHA|G_KA_PCT ALL 100|G_NUM_KA ALL 0 0
#Throughput evaluation Testcase for ssl based NS requests
AECDH-DES-CBC3-SHA_TPUT|script40K|128|0 1 0|0|0|https|AECDH-DES-CBC3-SHA|G_KA_PCT ALL 100|G_NUM_KA ALL 0 0
