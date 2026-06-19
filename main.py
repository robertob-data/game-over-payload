from ursina import *
import random
app = Ursina(title='Game Over Payload')

window.icon = 'GOPayload.ico'

#Fontes
fontOrbitron = '/fonts/Orbitron-VariableFont_wght.ttf'
fontTechMono = '/fonts\ShareTechMono-Regular.ttf'

# sons
click_sound = Audio('/sons/click/click.wav', autoplay=False, volume=0.1)
denied_sound = Audio('/sons/click/denied.mp3', autoplay=False, volume=0.3)
upgrade_sound = Audio('/sons/click/UpgradeSound.mp3', autoplay=False, volume=0.3)
music = Audio('/sons/musica/dark_ambient.mp3', loop=True, autoplay=True, volume=0.08)

# config inicial janela
window.size = (1366, 768)

# Escalas configuradas matematicamente
ESCALA_PARADO = (0.4, 0.2)
ESCALA_HOVER = (0.44, 0.22) 
ESCALA_CLICK = (0.32, 0.16)

#Upgrades valores
multiplier = 1.0

auto_Script_valor = 0
bot_scanner_valor = 0
social_enginer_valor = 0
spyware_valor = 0
root_kit_valor = 0
zero_day_exploit_valor = 0

#upgrade Custo
auto_script_custo = 50 #gera 1
bot_scanner_custo = 250 #gera 5
social_enginer_custo = 1000 # gera 25
spyware_custo = 5000 #gera 125
root_kit_custo = 25000 #gera 600
zero_day_exploit_custo = 125000 #gera 3k
    
#placar valores
contador = 999990
pontos = f'Dados : {contador:.2f}'
tempo = 0
dados_por_segundo = 0

# texturas mundiais
hack_button_texture = '/ui/button_hack.png'
dados_texture = '/icons/money.png'
dados_texture2 = '/icons/bandwidth_surge.png'
loja_texture = '/ui/resource_bar.png.png'

#texturas upgrade
auto_Script_texture = '/icons/script_kiddie.png'
bot_scanner_texture = '/icons/bot_scanner.png'
social_enginer_texture = '/icons/social_enginer.png'
spyware_texture = '/icons/Spyware.png'
root_kit_texture = '/icons/rootkit.png'
zero_day_exploit_texture = '/icons/zeroday.png'

# background
bg_texture = '/Background/background.png'
bg_texture2 = '/Background/background3.png'
bg = Entity(
    parent=camera.ui,
    model='quad',
    texture=bg_texture,
    scale=(2,1),
    z=10
)

#end game
end_texture = '/Background/endgame.png'
gameover = Entity(
    parent=camera.ui,
    model='quad',
    texture=end_texture,
    scale=(2,1),
    enabled=False,
    z=-20
)

# Botão hack
hack_button = Button(
    model='quad',
    texture=hack_button_texture,
    scale=ESCALA_PARADO,
    position=(0, 0),
    collider='box',
    z=1,
    parent=camera.ui,
    color=color.gray,
)

# UI dados (cash) texto
Dados = Text(
    pontos,
    parent=camera.ui,
    position=(-0.06,0.4),
    font = fontOrbitron
)
#Ui icone data (cash) texto
icone_dados = Entity(
    parent=camera.ui,
    model='quad',
    texture=dados_texture,
    scale=0.05,
    position=(-0.09, 0.39),
    color=color.gray
)

#Ui para loja
loja_layout = Entity(
    parent=camera.ui,
    model='quad',
    texture=loja_texture,
    scale=(1.1,0.5),
    position=(-0.49,-0.34),
    color = color.gray,
    z=9
)

#UI dos upgrades
#upgrade autoscript
auto_Script = Button(
    parent=camera.ui,
    model='quad',
    texture=auto_Script_texture,
    scale=(0.05,0.05),
    position=(-0.76,-0.23),
    color=color.gray   
)
auto_Script_text = Text(f''' Auto Script:
                        
    Possui: {auto_Script_valor}
        
    +1 Dados/s

    Custo: {auto_script_custo}''',
        font=fontTechMono,
        position=(-0.73,-0.21),
        scale=0.65)

#upgrade bot_scanner

bot_scanner = Button(
    parent=camera.ui,
    model='quad',
    texture=bot_scanner_texture,
    scale=(0.05,0.05),
    position =(-0.57,-0.23),
    color=color.gray
)
bot_scanner_text = Text(f''' Bot Scanner:
                        
    Possui: {bot_scanner_valor}
        
    +5 Dados/s

    Custo: {bot_scanner_custo}''',
        font=fontTechMono,
        position=(-0.54,-0.21),
        scale=0.65)


#upgrade social enginer
social_enginer = Button(
    parent=camera.ui,
    model='quad',
    texture=social_enginer_texture,
    scale=(0.05,0.05),
    position =(-0.38    ,-0.23),
    color=color.gray
)
social_enginer_text = Text(f''' Social Engineer:
                        
    Possui: {social_enginer_valor}
        
    +25 Dados/s

    Custo: {social_enginer_custo}''',
        font=fontTechMono,
        position=(-0.35 ,-0.21),
        scale=0.65)

#upgrade spyware
spyware = Button(
    parent=camera.ui,
    model='quad',
    texture=spyware_texture,
    scale=(0.05,0.05),
    position =(-0.76,-0.36),
    color=color.gray
)
spyware_text = Text(f''' SpyWare:
                        
    Possui: {spyware_valor}
        
    +125 Dados/s

    Custo: {spyware_custo}''',
        font=fontTechMono,
        position=(-0.74,-0.34),
        scale=0.65)

#upgrade rootkit
root_kit = Button(
    parent=camera.ui,
    model='quad',
    texture=root_kit_texture,
    scale=(0.05,0.05),
    position =(-0.57,-0.36),
    color=color.gray
)
root_kit_text = Text(f''' RootKit:
                        
    Possui: {root_kit_valor}
        
    +600 Dados/s

    Custo: {root_kit_custo}''',
        font=fontTechMono,
        position=(-0.54,-0.34),
        scale=0.60)

#upgrade zerodayexploit
zero_day_exploit1 = Button(
    parent=camera.ui,
    model='quad',
    texture=zero_day_exploit_texture,
    scale=(0.05,0.05),
    position =(-0.38,-0.36),
    color=color.gray
)
zero_day_exploit_text = Text(f''' Zero Day Exploit:
                        
    Possui: {zero_day_exploit_valor}
        
    +3000 Dados/s

    Custo: {zero_day_exploit_custo:,}''',
        font=fontTechMono,
        position=(-0.35,-0.34),
        scale=0.60)

#Dados por segundo
dadosS_icone = Entity(
    parent=camera.ui,
    model='quad',
    texture=dados_texture2,
    scale=0.03,
    position=(-0.08, 0.34),
    color=color.gray
)
dadosS = Text(f'{dados_por_segundo} Dados/s',
              font=fontOrbitron,
              position=(-0.06,0.35),
              scale=0.7)

#atualiza UI 
def atualizar_ui():
    Dados.text = f'Dados : {contador:.2f}'
    
    #upgrades
    #autoscript
    auto_Script_text.text = f''' Auto Script:
                        
    Possui: {auto_Script_valor:,}
        
    +1 Dados/s

    Custo: {auto_script_custo:,}'''
    
    #bot_scanner
    bot_scanner_text.text = f''' Bot Scanner:
                        
    Possui: {bot_scanner_valor:,}
        
    +5 Dados/s

    Custo: {bot_scanner_custo:,}'''
    
    #social enginer
    social_enginer_text.text = f''' Social Engineer:
                        
    Possui: {social_enginer_valor:,}
        
    +25 Dados/s

    Custo: {social_enginer_custo:,}'''
    
    #spyware
    spyware_text.text = f''' SpyWare:
                        
    Possui: {spyware_valor:,}
        
    +125 Dados/s

    Custo: {spyware_custo:,}'''
    
    #RootKit
    root_kit_text.text = f''' RootKit:
                        
    Possui: {root_kit_valor:,}
        
    +600 Dados/s

    Custo: {root_kit_custo:,}'''
    
    #zeroDayExploit
    zero_day_exploit_text.text = f''' Zero Day Exploit:
                        
    Possui: {zero_day_exploit_valor:,}
        
    +3000 Dados/s

    Custo: {zero_day_exploit_custo:,}'''
    
    dadosS.text = f'{dados_por_segundo} Dados/s'

#botao
# animação botão Hover
def hack_button_dentro():
    hack_button.color = color.white
# animaçao Botao over
def hack_button_fora():
    hack_button.animate_scale(ESCALA_PARADO, duration=0.1)
    hack_button.color = color.gray
# click Botao
def hack_button_click():
    global contador
    contador += 1

    # animação de click
    hack_button.scale = ESCALA_CLICK
    hack_button.animate_scale(ESCALA_PARADO, duration=0.1)
    
    #animaçao icone cash(dados)
    icone_dados.color = color.white
    icone_dados.animate_color(color.gray, duration=0.1)
    
    #chama o popup
    criar_popup()
    
    
    click_sound.play()
    atualizar_ui()
#cria popup quando clica +1
def criar_popup():
    pop_up = Text('+1',
              font=fontOrbitron,
              parent=camera.ui,
              position=(mouse.x + random.uniform(-0.01, 0.01), mouse.y + random.uniform(-0.01, 0.01)))
    pop_up.animate_y(pop_up.y + random.uniform(0.05,0.3), duration=0.7)
    
    destroy(pop_up, delay=0.9)

#funçao do upgrade auto_script
def auto_script_click():
    global auto_Script_valor, contador, dados_por_segundo, auto_script_custo, multiplier
    
    #upgrade auto script
    if contador >= auto_script_custo:
        auto_Script_valor += 1
        contador -= auto_script_custo
        auto_script_custo = int(auto_script_custo * 1.25)
        dados_por_segundo += 1
        
        multiplier += 0.01
        
        upgrade_sound.play()
    else:
        denied_sound.play()
        
    atualizar_ui()

#uppgrade bot scanner
def bot_scanner_click():
    global contador, bot_scanner_custo, dados_por_segundo, multiplier, bot_scanner_valor
    
    if contador >= bot_scanner_custo:
        bot_scanner_valor += 1
        contador -= bot_scanner_custo
        bot_scanner_custo = int(bot_scanner_custo * 1.25)
        dados_por_segundo += 5
        
        multiplier += 0.01
        
        
        upgrade_sound.play()
    else:
        denied_sound.play()
        
    atualizar_ui()
    
#upgrade social enginer
def social_enginer_click():
    global contador, social_enginer_custo, dados_por_segundo, multiplier, social_enginer_valor
    
    if contador >= social_enginer_custo:
        social_enginer_valor += 1
        contador -= social_enginer_custo
        social_enginer_custo = int(social_enginer_custo * 1.25)
        dados_por_segundo += 25
        
        multiplier += 0.01
        
        upgrade_sound.play()
    else:
        denied_sound.play()
    
    atualizar_ui()
    
#upgrade spyware
def spyware_click():
    global contador, spyware_custo, dados_por_segundo, multiplier, spyware_valor
    
    if contador >= spyware_custo:
        spyware_valor += 1
        contador -= spyware_custo
        spyware_custo = int(spyware_custo * 1.25)
        dados_por_segundo += 125
        
        multiplier += 0.01
        
        upgrade_sound.play()
    else:
        denied_sound.play()
    
    atualizar_ui()
    
#upgrade rootkit
def root_kit_click():
    global contador, root_kit_custo, dados_por_segundo, multiplier, root_kit_valor
    
    if contador >= root_kit_custo:
        root_kit_valor += 1
        contador -= root_kit_custo
        root_kit_custo = int(root_kit_custo * 1.25)
        dados_por_segundo += 600
        
        multiplier += 0.01
        
        upgrade_sound.play()
    else:
        denied_sound.play()
    
    atualizar_ui()
    
#upgrade zero day exploit
def zero_day_exploit_click():
    global contador, zero_day_exploit_custo, dados_por_segundo, multiplier, zero_day_exploit_valor
    
    if contador >= zero_day_exploit_custo:
        zero_day_exploit_valor += 1
        contador -= zero_day_exploit_custo
        zero_day_exploit_custo = int(zero_day_exploit_custo * 1.25)
        dados_por_segundo += 3000
        
        multiplier += 0.01
        
        upgrade_sound.play()
    else:
        denied_sound.play()
    
    atualizar_ui()

#end game
def reset_game():
    global contador, dados_por_segundo, multiplier
    global auto_Script_valor, bot_scanner_valor, social_enginer_valor, spyware_valor, root_kit_valor, zero_day_exploit_valor
    global auto_script_custo, bot_scanner_custo, social_enginer_custo, spyware_custo, root_kit_custo, zero_day_exploit_custo
    
    contador = 0 # ou 0
    dados_por_segundo = 0
    multiplier = 1.0
    auto_Script_valor = bot_scanner_valor = social_enginer_valor = spyware_valor = root_kit_valor = zero_day_exploit_valor = 0
    
    # Reseta os custos para o valor inicial
    auto_script_custo = 50
    bot_scanner_custo = 250
    social_enginer_custo = 1000
    spyware_custo = 5000
    root_kit_custo = 25000
    zero_day_exploit_custo = 125000
    atualizar_ui()

def input(key):
    if gameover.enabled:
        if key == 'enter':
            #reset do jogo
            gameover.animate('alpha', 0, duration=0.5, curve=curve.linear)
            invoke(reset_do_fim, delay=0.5)
        elif key == 'escape':
            application.quit()

def reset_do_fim():
    reset_game()
    gameover.enabled = False
    hack_button.enabled = True
    atualizar_ui()

#atualizado 60x por segundo
def update():
    global tempo, contador, auto_Script_valor, multiplier, bot_scanner_valor, social_enginer_valor, spyware_valor, root_kit_valor, zero_day_exploit_valor


    if contador >= 1000000 and not gameover.enabled:
        gameover.enabled = True
        hack_button.enabled = False
        
        gameover.alpha = 0
        gameover.animate('alpha', 1, duration=1.5, curve=curve.linear)
        
    #adiciona dados/s dos upgrades
    #autoscript
    tempo = tempo + time.dt
    
    if tempo >= 1:
        ganho = (auto_Script_valor * 1 + bot_scanner_valor * 5 + social_enginer_valor * 25 + spyware_valor * 125 + root_kit_valor * 600 + zero_day_exploit_valor * 3000) * multiplier
        contador += ganho
        tempo = 0
        atualizar_ui()

# eventos hackButton
hack_button.on_click = hack_button_click
hack_button.on_mouse_enter = hack_button_dentro
hack_button.on_mouse_exit = hack_button_fora

#eventos loja
auto_Script.on_click = auto_script_click
bot_scanner.on_click = bot_scanner_click
social_enginer.on_click = social_enginer_click
spyware.on_click = spyware_click
root_kit.on_click = root_kit_click
zero_day_exploit1.on_click = zero_day_exploit_click

app.run()