import requests
from util.msgbox import *
from enum import IntEnum


try:
    offsetsList = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()
except:
    msgbox('Ошибка', 'не удалось получить оффсеты', 0)
    raise SystemExit

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
dwClientState_State = offsetsList["signatures"]["dwClientState_State"]

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
m_bUseCustomAutoExposureMin = offsetsList["netvars"]["m_bUseCustomAutoExposureMin"]
m_bUseCustomAutoExposureMax = offsetsList["netvars"]["m_bUseCustomAutoExposureMax"]
m_flCustomAutoExposureMin = offsetsList["netvars"]["m_flCustomAutoExposureMin"]
m_flCustomAutoExposureMax = offsetsList["netvars"]["m_flCustomAutoExposureMax"]
m_bSpotted = offsetsList["netvars"]["m_bSpotted"]
m_iObserverMode = offsetsList["netvars"]["m_iObserverMode"]
m_iFOV = offsetsList["netvars"]["m_iFOV"]
m_bDormant = offsetsList["signatures"]["m_bDormant"]
m_vecOrigin = offsetsList["netvars"]["m_vecOrigin"]


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


class ClassId(IntEnum):
    CAI_BaseNPC = 0,
    CAK47 = 1,
    CBaseAnimating = 2,
    CBaseAnimatingOverlay = 3,
    CBaseAttributableItem = 4,
    CBaseButton = 5,
    CBaseCombatCharacter = 6,
    CBaseCombatWeapon = 7,
    CBaseCSGrenade = 8,
    CBaseCSGrenadeProjectile = 9,
    CBaseDoor = 10,
    CBaseEntity = 11,
    CBaseFlex = 12,
    CBaseGrenade = 13,
    CBaseParticleEntity = 14,
    CBasePlayer = 15,
    CBasePropDoor = 16,
    CBaseTeamObjectiveResource = 17,
    CBaseTempEntity = 18,
    CBaseToggle = 19,
    CBaseTrigger = 20,
    CBaseViewModel = 21,
    CBaseVPhysicsTrigger = 22,
    CBaseWeaponWorldModel = 23,
    CBeam = 24,
    CBeamSpotlight = 25,
    CBoneFollower = 26,
    CBRC4Target = 27,
    CBreachCharge = 28,
    CBreachChargeProjectile = 29,
    CBreakableProp = 30,
    CBreakableSurface = 31,
    CBumpMine = 32,
    CBumpMineProjectile = 33,
    CC4 = 34,
    CCascadeLight = 35,
    CChicken = 36,
    CColorCorrection = 37,
    CColorCorrectionVolume = 38,
    CCSGameRulesProxy = 39,
    CCSPlayer = 40,
    CCSPlayerResource = 41,
    CCSRagdoll = 42,
    CCSTeam = 43,
    CDangerZone = 44,
    CDangerZoneController = 45,
    CDEagle = 46,
    CDecoyGrenade = 47,
    CDecoyProjectile = 48,
    CDrone = 49,
    CDronegun = 50,
    CDynamicLight = 51,
    CDynamicProp = 52,
    CEconEntity = 53,
    CEconWearable = 54,
    CEmbers = 55,
    CEntityDissolve = 56,
    CEntityFlame = 57,
    CEntityFreezing = 58,
    CEntityParticleTrail = 59,
    CEnvAmbientLight = 60,
    CEnvDetailController = 61,
    CEnvDOFController = 62,
    CEnvGasCanister = 63,
    CEnvParticleScript = 64,
    CEnvProjectedTexture = 65,
    CEnvQuadraticBeam = 66,
    CEnvScreenEffect = 67,
    CEnvScreenOverlay = 68,
    CEnvTonemapController = 69,
    CEnvWind = 70,
    CFEPlayerDecal = 71,
    CFireCrackerBlast = 72,
    CFireSmoke = 73,
    CFireTrail = 74,
    CFish = 75,
    CFists = 76,
    CFlashbang = 77,
    CFogController = 78,
    CFootstepControl = 79,
    CFunc_Dust = 80,
    CFunc_LOD = 81,
    CFuncAreaPortalWindow = 82,
    CFuncBrush = 83,
    CFuncConveyor = 84,
    CFuncLadder = 85,
    CFuncMonitor = 86,
    CFuncMoveLinear = 87,
    CFuncOccluder = 88,
    CFuncReflectiveGlass = 89,
    CFuncRotating = 90,
    CFuncSmokeVolume = 91,
    CFuncTrackTrain = 92,
    CGameRulesProxy = 93,
    CGrassBurn = 94,
    CHandleTest = 95,
    CHEGrenade = 96,
    CHostage = 97,
    CHostageCarriableProp = 98,
    CIncendiaryGrenade = 99,
    CInferno = 100,
    CInfoLadderDismount = 101,
    CInfoMapRegion = 102,
    CInfoOverlayAccessor = 103,
    CItem_Healthshot = 104,
    CItemCash = 105,
    CItemDogtags = 106,
    CKnife = 107,
    CKnifeGG = 108,
    CLightGlow = 109,
    CMapVetoPickController = 110,
    CMaterialModifyControl = 111,
    CMelee = 112,
    CMolotovGrenade = 113,
    CMolotovProjectile = 114,
    CMovieDisplay = 115,
    CParadropChopper = 116,
    CParticleFire = 117,
    CParticlePerformanceMonitor = 118,
    CParticleSystem = 119,
    CPhysBox = 120,
    CPhysBoxMultiplayer = 121,
    CPhysicsProp = 122,
    CPhysicsPropMultiplayer = 123,
    CPhysMagnet = 124,
    CPhysPropAmmoBox = 125,
    CPhysPropLootCrate = 126,
    CPhysPropRadarJammer = 127,
    CPhysPropWeaponUpgrade = 128,
    CPlantedC4 = 129,
    CPlasma = 130,
    CPlayerPing = 131,
    CPlayerResource = 132,
    CPointCamera = 133,
    CPointCommentaryNode = 134,
    CPointWorldText = 135,
    CPoseController = 136,
    CPostProcessController = 137,
    CPrecipitation = 138,
    CPrecipitationBlocker = 139,
    CPredictedViewModel = 140,
    CProp_Hallucination = 141,
    CPropCounter = 142,
    CPropDoorRotating = 143,
    CPropJeep = 144,
    CPropVehicleDriveable = 145,
    CRagdollManager = 146,
    CRagdollProp = 147,
    CRagdollPropAttached = 148,
    CRopeKeyframe = 149,
    CSCAR17 = 150,
    CSceneEntity = 151,
    CSensorGrenade = 152,
    CSensorGrenadeProjectile = 153,
    CShadowControl = 154,
    CSlideshowDisplay = 155,
    CSmokeGrenade = 156,
    CSmokeGrenadeProjectile = 157,
    CSmokeStack = 158,
    CSnowball = 159,
    CSnowballPile = 160,
    CSnowballProjectile = 161,
    CSpatialEntity = 162,
    CSpotlightEnd = 163,
    CSprite = 164,
    CSpriteOriented = 165,
    CSpriteTrail = 166,
    CStatueProp = 167,
    CSteamJet = 168,
    CSun = 169,
    CSunlightShadowControl = 170,
    CSurvivalSpawnChopper = 171,
    CTablet = 172,
    CTeam = 173,
    CTeamplayRoundBasedRulesProxy = 174,
    CTEArmorRicochet = 175,
    CTEBaseBeam = 176,
    CTEBeamEntPoint = 177,
    CTEBeamEnts = 178,
    CTEBeamFollow = 179,
    CTEBeamLaser = 180,
    CTEBeamPoints = 181,
    CTEBeamRing = 182,
    CTEBeamRingPoint = 183,
    CTEBeamSpline = 184,
    CTEBloodSprite = 185,
    CTEBloodStream = 186,
    CTEBreakModel = 187,
    CTEBSPDecal = 188,
    CTEBubbles = 189,
    CTEBubbleTrail = 190,
    CTEClientProjectile = 191,
    CTEDecal = 192,
    CTEDust = 193,
    CTEDynamicLight = 194,
    CTEEffectDispatch = 195,
    CTEEnergySplash = 196,
    CTEExplosion = 197,
    CTEFireBullets = 198,
    CTEFizz = 199,
    CTEFootprintDecal = 200,
    CTEFoundryHelpers = 201,
    CTEGaussExplosion = 202,
    CTEGlowSprite = 203,
    CTEImpact = 204,
    CTEKillPlayerAttachments = 205,
    CTELargeFunnel = 206,
    CTEMetalSparks = 207,
    CTEMuzzleFlash = 208,
    CTEParticleSystem = 209,
    CTEPhysicsProp = 210,
    CTEPlantBomb = 211,
    CTEPlayerAnimEvent = 212,
    CTEPlayerDecal = 213,
    CTEProjectedDecal = 214,
    CTERadioIcon = 215,
    CTEShatterSurface = 216,
    CTEShowLine = 217,
    CTesla = 218,
    CTESmoke = 219,
    CTESparks = 220,
    CTESprite = 221,
    CTESpriteSpray = 222,
    CTest_ProxyToggle_Networkable = 223,
    CTestTraceline = 224,
    CTEWorldDecal = 225,
    CTriggerPlayerMovement = 226,
    CTriggerSoundOperator = 227,
    CVGuiScreen = 228,
    CVoteController = 229,
    CWaterBullet = 230,
    CWaterLODControl = 231,
    CWeaponAug = 232,
    CWeaponAWP = 233,
    CWeaponBaseItem = 234,
    CWeaponBizon = 235,
    CWeaponCSBase = 236,
    CWeaponCSBaseGun = 237,
    CWeaponCycler = 238,
    CWeaponElite = 239,
    CWeaponFamas = 240,
    CWeaponFiveSeven = 241,
    CWeaponG3SG1 = 242,
    CWeaponGalil = 243,
    CWeaponGalilAR = 244,
    CWeaponGlock = 245,
    CWeaponHKP2000 = 246,
    CWeaponM249 = 247,
    CWeaponM3 = 248,
    CWeaponM4A1 = 249,
    CWeaponMAC10 = 250,
    CWeaponMag7 = 251,
    CWeaponMP5Navy = 252,
    CWeaponMP7 = 253,
    CWeaponMP9 = 254,
    CWeaponNegev = 255,
    CWeaponNOVA = 256,
    CWeaponP228 = 257,
    CWeaponP250 = 258,
    CWeaponP90 = 259,
    CWeaponSawedoff = 260,
    CWeaponSCAR20 = 261,
    CWeaponScout = 262,
    CWeaponSG550 = 263,
    CWeaponSG552 = 264,
    CWeaponSG556 = 265,
    CWeaponShield = 266,
    CWeaponSSG08 = 267,
    CWeaponTaser = 268,
    CWeaponTec9 = 269,
    CWeaponTMP = 270,
    CWeaponUMP45 = 271,
    CWeaponUSP = 272,
    CWeaponXM1014 = 273,
    CWeaponZoneRepulsor = 274,
    CWorld = 275,
    CWorldVguiText = 276,
    DustTrail = 277,
    MovieExplosion = 278,
    ParticleSmokeGrenade = 279,
    RocketTrail = 280,
    SmokeTrail = 281,
    SporeExplosion = 282,
    SporeTrail = 283,


def class_id_c4(classID):
    return classID == ClassId.CC4 or classID == ClassId.CPlantedC4



def class_id_gun(classID): ###########################Ultimate shitcode
    if (classID == ClassId.CAK47 or classID == ClassId.CSCAR17 or classID == ClassId.CWeaponAug
    or classID == ClassId.CWeaponBizon or classID == ClassId.CWeaponElite or classID == ClassId.CWeaponFamas
    or classID == ClassId.CWeaponFiveSeven or classID == ClassId.CDEagle or classID == ClassId.CWeaponM249
    or classID == ClassId.CWeaponG3SG1 or classID == ClassId.CWeaponGalil or classID == ClassId.CWeaponGalilAR
    or classID == ClassId.CWeaponGlock or classID == ClassId.CWeaponHKP2000  or classID == ClassId.CWeaponM3
    or classID == ClassId.CWeaponM4A1 or classID == ClassId.CWeaponMAC10 or classID == ClassId.CWeaponMag7
    or classID == ClassId.CWeaponMP5Navy or classID == ClassId.CWeaponMP7 or classID == ClassId.CWeaponMP9
    or classID == ClassId.CWeaponNegev or classID == ClassId.CWeaponNOVA or classID == ClassId.CWeaponP228
    or classID == ClassId.CWeaponP250 or classID == ClassId.CWeaponP90 or classID == ClassId.CWeaponSawedoff
    or classID == ClassId.CWeaponSCAR20 or classID == ClassId.CWeaponScout or classID == ClassId.CWeaponSG550
    or classID == ClassId.CWeaponSG552 or classID == ClassId.CWeaponSG556 or classID == ClassId.CWeaponShield
    or classID == ClassId.CWeaponSSG08 or classID == ClassId.CWeaponTaser or classID == ClassId.CWeaponUSP
    or classID == ClassId.CWeaponTec9 or classID == ClassId.CWeaponTMP or classID == ClassId.CWeaponUMP45
    or classID == ClassId.CWeaponXM1014 or classID == ClassId.CWeaponAWP):
        return True
    else:
        return False

def class_id_grenade(classID):#######################Ultimate shitcode
    if (classID == ClassId.CDecoyGrenade or classID == ClassId.CDecoyProjectile
    or classID == ClassId.CMolotovProjectile or classID == ClassId.CMolotovGrenade
    or classID == ClassId.CHEGrenade or classID == ClassId.CIncendiaryGrenade 
    or classID == ClassId.CSmokeGrenade or classID == ClassId.ParticleSmokeGrenade
    or classID == ClassId.CSmokeGrenadeProjectile or classID == ClassId.CFlashbang):
        return True
    else:
        return False