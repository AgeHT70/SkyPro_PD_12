
with open("UII.csv") as file:
    data = file.read()

from_csv = data.split('\n')
for i in range(8):
    print(f"{i}: {from_csv[i]}")
# for i in range(5, len(data)):
#     print(data[i].strip().split(';'))
# insert = 'insert into t031 ('

# NSYST,

# NSYST_T001,
# FAM, IMJ, OTCH
# D_ROJD, M_ROJD, Y_ROJD
# PSP_S, PSP_N, VYDAN, D_PSP, M_PSP, Y_PSP

# SLUGBA,
# UIN
# N_PROT
# D_SOVER, M_SOVER, Y_SOVER
# PR_VID1, PR_VID2
# ORG_RESH
# Y_RESH	M_RESH	D_RESH
# KODRAI1_RESH
#
# MERA_NAK, RAZ_NAK
# DOP_STATJ
# NAIM
# DOLJN
# RESP
# KRAJ
# RAJON
# KW_PUNKT
# ULICA
# N_DOM
# KORPUS
# KW
# AREA
# POS_IN_GOROD
# MICK_RN
# DOP_ATR
# DISKVA
# AREST
# LISHEN
# KAT_ORG
# ORGNAME
# RESP_UR
# KRAJ_UR
# RAJON_UR
# KW_PUNKT_UR
# ULICA_UR
# N_DOM_UR
# KORPUS_UR
# KW_UR
# AREA_UR
# POS_IN_GOROD_UR
# MICK_RN_UR
# DOP_ATR_UR
# RESP_RASP
# KRAJ_RASP
# RAJON_RASP
# KW_PUNKT_RASP
# ULICA_RASP
# N_DOM_RASP
# KORPUS_RASP
# KW_RASP
# AREA_RASP
# POS_IN_GOROD_RASP
# MICK_RN_RASP
# DOP_ATR_RASP
# DT_REG
# DT_IZM
# KODRAI
# KODRAI1
# KODRAI1_KOD
# KODREG
# SH_POLZ
# SH_POLZ1
# DOSTUP
# IBD_ARX
# CN_DELARX
# GENOTIP
# GRAJDAN
# Y_OPLAT
# M_OPLAT
# D_OPLAT
# KATEG
# VID_DOC
# N_POST
# UPD_ARX
# NOMER
# REGION
# MODEL
# DT_REG_RESH
# NET_RESH
# Y_ZAKON
# M_ZAKON
# D_ZAKON
# Y_IZJAT
# M_IZJAT
# D_IZJAT
# N_BLANK
# MESTO_SOVER
# N_UDOST
# RESP_SOVER
# KRAJ_SOVER
# RAJON_SOVER
# KW_PUNKT_SOVER
# POS_IN_GOROD_SOVER
# MICK_RN_SOVER
# ULICA_SOVER
# N_DOM_SOVER
# KORPUS_SOVER
# KW_SOVER
# AREA_SOVER
# DOP_ATR_SOVER
# FABULA
# SLUGBA_SOST
# SOTR_SOST
# SFERA
# ZAKON
# KOL_IZ
# Y_VVOD
# M_VVOD
# D_VVOD
# Y_VOZ
# M_VOZ
# D_VOZ
# POVOD
# RABOT
# OKATO
# KBK
# Y_FSSP
# M_FSSP
# D_FSSP
# RAZ_FSSP
# DP_ST
# P1