import requests
from util.msgbox import *
from util.softExit import *

try:
    offsetsList = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()
except:
    msgbox('Ошибка', 'не удалось получить оффсеты', 0)
    pExit()

timestamp = offsetsList["timestamp"]
dwLocalPlayer = offsetsList["signatures"]["dwLocalPlayer"]
dwEntityList = offsetsList["signatures"]["dwEntityList"]
dwGlowObjectManager = offsetsList["signatures"]["dwGlowObjectManager"]
dwForceAttack = offsetsList["signatures"]["dwForceAttack"]
dwForceJump = offsetsList["signatures"]["dwForceJump"]
dwClientState = offsetsList["signatures"]["dwClientState"]
dwForceLeft = offsetsList["signatures"]["dwForceLeft"]
dwForceRight = offsetsList["signatures"]["dwForceRight"]
dwClientState_ViewAngles = offsetsList["signatures"]["dwClientState_ViewAngles"]


m_iTeamNum = offsetsList["netvars"]["m_iTeamNum"]
m_iHealth = offsetsList["netvars"]["m_iHealth"]
m_iGlowIndex = offsetsList["netvars"]["m_iGlowIndex"]
m_clrRender = offsetsList["netvars"]["m_clrRender"]
m_iDefaultFOV = offsetsList["netvars"]["m_iDefaultFOV"]
m_iCrosshairId = offsetsList["netvars"]["m_iCrosshairId"]
m_fFlags = offsetsList["netvars"]["m_fFlags"]
m_flFlashMaxAlpha = offsetsList["netvars"]["m_flFlashMaxAlpha"]
m_bIsScoped = offsetsList["netvars"]["m_bIsScoped"]
m_iItemDefinitionIndex = offsetsList["netvars"]["m_iItemDefinitionIndex"]
m_hActiveWeapon = offsetsList["netvars"]["m_hActiveWeapon"]


WEAPON_DEAGLE = 1
WEAPON_ELITE = 2
WEAPON_FIVESEVEN = 3
WEAPON_GLOCK = 4
WEAPON_AK47 = 7
WEAPON_AUG = 8
WEAPON_AWP = 9
WEAPON_FAMAS = 10
WEAPON_G3SG1 = 11
WEAPON_GALILAR = 13
WEAPON_M249 = 14
WEAPON_M4A1 = 16
WEAPON_MAC10 = 17
WEAPON_P90 = 19
WEAPON_MP5SD = 23
WEAPON_UMP45 = 24
WEAPON_XM1014 = 25
WEAPON_BIZON = 26
WEAPON_MAG7 = 27
WEAPON_NEGEV = 28
WEAPON_SAWEDOFF = 29
WEAPON_TEC9 = 30
WEAPON_TASER = 31
WEAPON_HKP2000 = 32
WEAPON_MP7 = 33
WEAPON_MP9 = 34
WEAPON_NOVA = 35
WEAPON_P250 = 36
WEAPON_SHIELD = 37
WEAPON_SCAR20 = 38
WEAPON_SG556 = 39
WEAPON_SSG08 = 40
WEAPON_KNIFEGG = 41
WEAPON_KNIFE = 42
WEAPON_FLASHBANG = 43
WEAPON_HEGRENADE = 44
WEAPON_SMOKEGRENADE = 45
WEAPON_MOLOTOV = 46
WEAPON_DECOY = 47
WEAPON_INCGRENADE = 48
WEAPON_C4 = 49
WEAPON_HEALTHSHOT = 57
WEAPON_KNIFE_T = 59
WEAPON_M4A1_SILENCER = 60
WEAPON_USP_SILENCER = 61
WEAPON_CZ75A = 63
WEAPON_REVOLVER = 64
WEAPON_TAGRENADE = 68
WEAPON_FISTS = 69
WEAPON_BREACHCHARGE = 70
WEAPON_TABLET = 72
WEAPON_MELEE = 74
WEAPON_AXE = 75
WEAPON_HAMMER = 76
WEAPON_SPANNER = 78
WEAPON_KNIFE_GHOST = 80
WEAPON_FIREBOMB = 81
WEAPON_DIVERSION = 82
WEAPON_FRAG_GRENADE = 83
WEAPON_SNOWBALL = 84
WEAPON_BUMPMINE = 85
WEAPON_BAYONET = 500
WEAPON_KNIFE_FLIP = 505
WEAPON_KNIFE_GUT = 506
WEAPON_KNIFE_KARAMBIT = 507
WEAPON_KNIFE_M9_BAYONET = 508
WEAPON_KNIFE_TACTICAL = 509
WEAPON_KNIFE_FALCHION = 512
WEAPON_KNIFE_SURVIVAL_BOWIE = 514
WEAPON_KNIFE_BUTTERFLY = 515
WEAPON_KNIFE_PUSH = 516
WEAPON_KNIFE_URSUS = 519
WEAPON_KNIFE_GYPSY_JACKKNIFE = 520
WEAPON_KNIFE_STILETTO = 522
WEAPON_KNIFE_WIDOWMAKER = 523
STUDDED_BLOODHOUND_GLOVES = 5027
T_GLOVES = 5028
CT_GLOVES = 5029
SPORTY_GLOVES = 5030
SLICK_GLOVES = 5031
LEATHER_HANDWRAPS = 5032
MOTORCYCLE_GLOVES = 5033
SPECIALIST_GLOVES = 5034
STUDDED_HYDRA_GLOVES = 5035