from util.getGameAddres import *
from util.getOffsets import *
from util.softExit import*
from util.getActiveWin import *
'''
import tool.glow_esp as glow_esp
import tool.glow_esp_hp as glow_esp_hp
import tool.chams as chams
import tool.player_fov as player_fov
import tool.trigger_bot as trigger_bot
import tool.global_wh as global_wh
'''
import re
from threading import Thread
import dearpygui.dearpygui as dpg
import random, string
import time, keyboard, random
from win32api import GetKeyState

# aim

def TriggerBot():
    TriggerBot_Status = dpg.get_value(triggerbot_)
    
    while TriggerBot_Status:
        TriggerBot_Delay = dpg.get_value(triggerbot_del)
        Knife_Check = dpg.get_value(triggerbot_knifec)
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if lPlayer and gameIsActive():
            entityID = pm.read_int(lPlayer + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entityID - 1) * 0x10)

            if entity and entityID > 0 and entityID <= 32:
                mTeam = pm.read_int(lPlayer + m_iTeamNum)
                eTeam = pm.read_int(entity + m_iTeamNum)

                snipers = [WEAPON_AWP, WEAPON_SSG08, WEAPON_SCAR20, WEAPON_G3SG1]
                weapon = pm.read_int(lPlayer + m_hActiveWeapon)
                weapon_entity = pm.read_int(client + dwEntityList + ((weapon & 0xFFF) - 1) * 0x10)

                on_ground = pm.read_int(lPlayer + m_fFlags)
                weapon_id = str(pm.read_short(weapon_entity + m_iItemDefinitionIndex))


                scoped = pm.read_int(lPlayer + m_bIsScoped)

                if eTeam != mTeam and scoped == 1 and weapon_id != WEAPON_KNIFE and on_ground == 257 or on_ground == 263:
                    time.sleep(TriggerBot_Delay / 100)
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
    address = client + re.search(rb"\x83\xF8.\x8B\x45\x08\x0F",client).start() + 2
    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)


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
    address = client + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',client).start()
    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)


# end misc





# gui
title = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

dpg.create_context()
dpg.create_viewport(title = title, resizable = False, width = 700, height = 500)
dpg.setup_dearpygui()

with dpg.window() as window:
    dpg.add_text('Maze X [by hkon aka hiikion]')
    with dpg.tab_bar():
        with dpg.tab(label='aim'):
            triggerbot_ = dpg.add_checkbox(label='triggerbot', callback=TriggerBot_thread)
            dpg.add_same_line()
            triggerbot_del = dpg.add_slider_int(label='triggerbot delay', max_value=150, width=200)
            dpg.add_text('')
            dpg.add_text('flags:')
            triggerbot_knifec = dpg.add_checkbox(label='knife check')
            triggerbot_jumpc = dpg.add_checkbox(label='jump check')
            triggerbot_scopec = dpg.add_checkbox(label='scope check')
            
            
        with dpg.tab(label='visuals'):
            chams_ = dpg.add_checkbox(label='chams', callback=Chams_thread)
            dpg.add_same_line()
            chams_col = dpg.add_color_edit(no_alpha=True, no_inputs=True, no_tooltip=True)

            glow_ = dpg.add_checkbox(label='glow', callback=GlowESP_thread)
            dpg.add_same_line()
            glow_col = dpg.add_color_edit(no_alpha=True, no_inputs=True, no_tooltip=True)

            global_wh = dpg.add_checkbox(label='global wh', callback=GlobalWH)

            
        with dpg.tab(label='misc'):
            bhop_ = dpg.add_checkbox(label='bhop', callback=bhop_thread)
            dpg.add_same_line()
            bhop_mode = dpg.add_combo(['legit', 'rage'], default_value='legit')

            auto_pistol_ = dpg.add_checkbox(label='auto pistol', callback=AutoPistol_thread)

            NoFlash_ = dpg.add_checkbox(label='no flash', callback=NoFlash_thread)

            ShowMoney_ = dpg.add_checkbox(label='show money', callback=ShowMoney)





dpg.set_primary_window(window, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
# end gui

