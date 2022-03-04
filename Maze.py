from email.policy import default
from util.getGameAddres import *
from util.getOffsets import *
from util.softExit import*
from util.getActiveWin import *

import re
from threading import Thread
import dearpygui.dearpygui as dpg
import random, string
import time, keyboard, random
from win32api import GetKeyState
import ini
import subprocess
from pathvalidate import validate_filename


# aim

def TriggerBot():
    TriggerBot_Status = dpg.get_value(triggerbot_)
    
    while TriggerBot_Status:
        TriggerBot_Delay = dpg.get_value(triggerbot_del)
        Knife_Check = dpg.get_value(aim_knifec)
        Scope_Check = dpg.get_value(aim_scopec)
        Jump_Check = dpg.get_value(aim_jumpc)

        lPlayer = pm.read_int(client + dwLocalPlayer)

        if lPlayer and gameIsActive():
            entityID = pm.read_int(lPlayer + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entityID - 1) * 0x10)

            if entity and entityID > 0 and entityID <= 32:
                mTeam = pm.read_int(lPlayer + m_iTeamNum)
                eTeam = pm.read_int(entity + m_iTeamNum)
                
                weapon = pm.read_int(lPlayer + m_hActiveWeapon)
                weapon_entity = pm.read_int(client + dwEntityList + ((weapon & 0xFFF) - 1) * 0x10)

                on_ground = pm.read_int(lPlayer + m_fFlags)
                weapon_id = int(pm.read_short(weapon_entity + m_iItemDefinitionIndex))

                snipers = [WEAPON_AWP, WEAPON_SSG08, WEAPON_SCAR20, WEAPON_G3SG1]
                knifes_idk = [WEAPON_KNIFE, WEAPON_KNIFE_T, WEAPON_MELEE]

                if weapon_id in snipers:scoped = pm.read_int(lPlayer + m_bIsScoped)
                else:scoped = 1

                if not Scope_Check:scoped = 1
                if not Jump_Check:on_ground = 257
                if not Knife_Check:weapon_id = WEAPON_AK47

                if eTeam != mTeam and scoped == 1 and weapon_id not in knifes_idk:
                    if on_ground == 257 or on_ground == 263:
                        time.sleep(TriggerBot_Delay)
                        pm.write_int(client + dwForceAttack, 6)    
            
        time.sleep(0.01)

def TriggerBot_thread():
    Thread(target=TriggerBot).start()

# end aim


# visuals
def conver_col_to_int(col):
    col[0] = int(col[0])
    col[1] = int(col[1])
    col[2] = int(col[2])
    return col

def Chams():
    while dpg.get_value(chams_):
        Chams_Color = conver_col_to_int(dpg.get_value(chams_col))
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            mTeam = pm.read_int(lPlayer + m_iTeamNum)

            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if (entity):
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if (eTeam != mTeam):
                        pm.write_int(entity +  m_clrRender, Chams_Color[0])
                        pm.write_int(entity +  m_clrRender + 0x1, Chams_Color[1])
                        pm.write_int(entity +  m_clrRender + 0x2, Chams_Color[2])
                        pm.write_int(entity +  m_clrRender + 0x3, 1)
    
        time.sleep(0.2)

    
def chams_reset():
    lPlayer = pm.read_int(client + dwLocalPlayer)

    if lPlayer:
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                pm.write_int(entity +  m_clrRender, 255)
                pm.write_int(entity +  m_clrRender + 0x1, 255)
                pm.write_int(entity +  m_clrRender + 0x2, 255)

def Chams_thread():
    Chams_Status = dpg.get_value(chams_)
    if Chams_Status:
            Thread(target=Chams).start()
    else:
        chams_reset()

def GlowESP():
    GlowESP_Line = 0.7
    while dpg.get_value(glow_):
        GlowESP_Color = conver_col_to_int(dpg.get_value(glow_col))
        lPlayer = pm.read_int(client + dwLocalPlayer)
        
        if lPlayer:
            glowManager = pm.read_int(client + dwGlowObjectManager)
            mTeam = pm.read_int(lPlayer + m_iTeamNum)

            for i in range(1, 31):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if eTeam != mTeam:
                        entityGlow = pm.read_int(entity + m_iGlowIndex)

                        pm.write_float(glowManager + entityGlow * 0x38 + 0x8, (GlowESP_Color[0] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0xC, (GlowESP_Color[1] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x10, (GlowESP_Color[2] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x14, GlowESP_Line)

                        pm.write_bool(glowManager + entityGlow * 0x38 + 0x28, True)

        time.sleep(0.01)

def GlowESP_thread():
    Thread(target=GlowESP).start()

def GlobalWH():
    pm = pymem.Pymem("csgo.exe")

    client = pymem.process.module_from_name(pm.process_handle,"client.dll")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)

    address = client.lpBaseOfDll + re.search(rb"\x83\xF8.\x8B\x45\x08\x0F",clientModule).start() + 2
    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)

    pm.close_process()


#visuals end

#misc

def BHop():
    while dpg.get_value(bhop_):
        bhop_mode_ = dpg.get_value(bhop_mode)

        force_jump = client + dwForceJump
        player = pm.read_int(client + dwLocalPlayer)
        on_ground = pm.read_int(player + m_fFlags)

        if bhop_mode_ == 'rage':
            if keyboard.is_pressed('space'): 
                if player and on_ground == 257 or on_ground == 263:
                    pm.write_int(force_jump, 6)

        if bhop_mode_ == 'legit':
            if keyboard.is_pressed('space'): 
                if player and on_ground == 257 or on_ground == 263:
                    a = random.randint(0,5)
                    time.sleep(a/100)
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)

        time.sleep(0.02)

def bhop_thread():
    try:Thread(target=BHop).start()
    except:pass

def AutoPistol():
    while dpg.get_value(auto_pistol_):
        if GetKeyState(1) == -127 or GetKeyState(1) == -128:

            lPlayer = pm.read_int(client + dwLocalPlayer)

            if lPlayer and gameIsActive():
                pm.write_int(client + dwForceAttack, 6)

        time.sleep(0.02)

def AutoPistol_thread():
    try:Thread(target=AutoPistol).start()
    except:pass

def NoFlash():
    NoFlash_Status = dpg.get_value(NoFlash_)

    while NoFlash_Status:
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if lPlayer:
            pm.write_float(lPlayer + m_flFlashMaxAlpha, 0.0)

        time.sleep(0.01)
    if not NoFlash_Status:
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if lPlayer:
            pm.write_float(lPlayer + m_flFlashMaxAlpha, 255.0)

def NoFlash_thread():
    try:Thread(target=AutoPistol).start()
    except:pass

def ShowMoney():
    pm = pymem.Pymem("csgo.exe")

    client = pymem.process.module_from_name(pm.process_handle,"client.dll")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)

    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()
    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)

    pm.close_process()
'''
def AutoStrafer(y_angle, oldviewangle):
    lPlayer = pm.read_int(client + dwLocalPlayer)
    on_ground = pm.read_uint(lPlayer + m_fFlags)
    print(y_angle, oldviewangle)
    if lPlayer and (on_ground == 256 or on_ground == 262):
        if y_angle > oldviewangle:
            pm.write_int(client + dwForceLeft, 6)

        elif y_angle < oldviewangle:
            pm.write_int(client + dwForceRight, 6)

        else:
            pm.write_int(client + dwForceRight, 6)
    return y_angle

def AutoStrafer_():
    oldviewangle = 0.0
    while dpg.get_value(auto_strafer_):
        y_angle = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
        y_angle = AutoStrafer(y_angle, oldviewangle)
        oldviewangle = y_angle

def AutoStrafer_thread():
    Thread(target=AutoStrafer_).start()
'''

def PlayerFov():
    while dpg.get_value(fov):
        PlayerFov_Value = dpg.get_value(fov_val)
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            pm.write_int(lPlayer + m_iDefaultFOV, PlayerFov_Value)

        time.sleep(0.05)

    if not dpg.get_value(fov):
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            pm.write_int(lPlayer + m_iDefaultFOV, 90)

def PlayerFov_thread():
    Thread(target=PlayerFov).start()

# end misc

'''
# config

def create_config_dir():
    if not os.path.isdir(path):
        os.mkdir(path)

def create_config():
    try:
        if not os.path.isfile(path + '/' + validate_filename(dpg.get_value(filnam))):
            with open(path + '/' + validate_filename(dpg.get_value(filnam)), 'w+', encoding='utf-8') as f:
                # yeah
                f.write('[legit]')
                f.write('triggerbot = ' + str(dpg.get_value(triggerbot_)))
                f.write('trigerbot_delay = ' + str(dpg.get_value(triggerbot_del)))
                f.write('aim_check_knife = ' + str(dpg.get_value(aim_knifec)))
                f.write('aim_check_scope = ' + str(dpg.get_value(aim_scopec)))
                f.write('aim_check_jump = ' + str(dpg.get_value(aim_jumpc)))

                f.write('[visuals]')
                f.write('glow = ' + str(dpg.get_value(glow_)))
                f.write('glow_color = ' + str(dpg.get_value(glow_col)))
                f.write('chams = ' + str(dpg.get_value(chams_)))
                f.write('chams_color = ' + str(dpg.get_value(chams_col)))
                f.write('global_wh = ' + str(dpg.get_value(global_wh)))
                f.write('fov = ' + str(dpg.get_value(fov)))
                f.write('fov_value = ' + str(dpg.get_value(fov_val)))

                f.write('[misc]')
                f.write('bhop = ' + str(dpg.get_value(bhop_)))
                f.write('bhop_mode' + str(dpg.get_value(bhop_mode)))
                f.write('auto_pistol = ' + str(dpg.get_value(auto_pistol_)))
                f.write('no_flash = ' + str(dpg.get_value(NoFlash_)))
                f.write('show_money = ' + str(dpg.get_value(ShowMoney_)))
        else:
            msgbox('Error', 'file allready exists', 0)
    except Exception as ex:
        msgbox('Error', 'failed to create config: ' + str(ex), 0)

def load_config():
    pass


def save_config():
    pass

# end config
'''


# gui
title = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

dpg.create_context()
dpg.create_viewport(title = title, resizable = True, width = 600, height = 350)
dpg.setup_dearpygui()

with dpg.window() as window:
    dpg.add_text('Maze X [by hkon aka hiikion]')
    with dpg.tab_bar():

        with dpg.tab(label='legit'):

            with dpg.group(horizontal=True):
                triggerbot_ = dpg.add_checkbox(label='triggerbot', callback=TriggerBot_thread)
                triggerbot_del = dpg.add_slider_float(label='triggerbot delay', max_value=0.220, width=200, default_value=0.170, min_value=0.0)

            dpg.add_text('')
            dpg.add_text('flags:')
            aim_knifec = dpg.add_checkbox(label='knife check')
            aim_jumpc = dpg.add_checkbox(label='jump check')
            aim_scopec = dpg.add_checkbox(label='scope check')

            
            
        with dpg.tab(label='visuals'):

            with dpg.group(horizontal=True):
                chams_ = dpg.add_checkbox(label='chams', callback=Chams_thread)
                chams_col = dpg.add_color_edit(no_alpha=True, no_inputs=True, no_tooltip=True)

            with dpg.group(horizontal=True):
                glow_ = dpg.add_checkbox(label='glow', callback=GlowESP_thread)
                glow_col = dpg.add_color_edit(no_alpha=True, no_inputs=True, no_tooltip=True)

            global_wh = dpg.add_checkbox(label='global wh', callback=GlobalWH)

            with dpg.group(horizontal=True):
                fov = dpg.add_checkbox(label='fov changer', callback=PlayerFov_thread)
                fov_val = dpg.add_slider_int(label='triggerbot delay', max_value=179, min_value=1, width=200, default_value=90)

            
        with dpg.tab(label='misc'):
            
            with dpg.group(horizontal=True):
                bhop_ = dpg.add_checkbox(label='bhop', callback=bhop_thread)
                bhop_mode = dpg.add_combo(['legit', 'rage'], default_value='legit', width=100)
            
            #auto_strafer_ = dpg.add_checkbox(label='auto strafer', callback=AutoStrafer_thread)

            auto_pistol_ = dpg.add_checkbox(label='auto pistol', callback=AutoPistol_thread)

            NoFlash_ = dpg.add_checkbox(label='no flash', callback=NoFlash_thread)

            ShowMoney_ = dpg.add_checkbox(label='show money', callback=ShowMoney)


with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll): #(53, 0, 85) #(56, 0, 99) #(40, 93, 0)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 5, category=dpg.mvThemeCat_Core)
        '''
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (53, 0, 85), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (53, 0, 85), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (56, 0, 99), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (56, 0, 99), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (53, 0, 85), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (40, 93, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (40, 93, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (40, 93, 0), category=dpg.mvThemeCat_Core)
        '''


dpg.bind_theme(global_theme)


dpg.set_primary_window(window, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
# end gui

