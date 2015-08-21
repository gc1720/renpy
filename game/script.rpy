# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define y = Character('Yusuke', color="#c8ffc8")
define k = Character('Kuwabara',color="#ff00c8")
define b = Character('Byakko',color="#ff00ff")


image bg = "images/backg.jpg"
image bg2 ="images/bg2.jpg"
image bg3 ="images/castillo.jpg"
image bg4 ="images/Zona2.jpg"
image bg5 ="images/pelea1.jpg"
image yusuke = "images/yuskarender.png"
image kuwabara = "images/Kuwabara1.png"
image kuwa2 = "images/Kazuma12.png"
image kuwa3 = "images/kpelea.gif"
image kuwa4 = "images/Kazumapelea.png"
image kuwa 5 = "images/FullShotKuwabara.jpg"
image byakko = "images/Byakko.png"
image byakko2 = "images/byakko2.png"





# The game starts here.
# - El juego comienza aquí.
label start:
    
    play music "backmusic.mp3"
    scene bg
    with fade
    with Dissolve(.5)
    pause.5
    show yusuke
    
    y "Hola Soy Yusuke Urameshi."
    hide yusuke 
    scene bg
    with fade
    with Dissolve(.5)
    pause.5
    show kuwabara
    k "Yo soy Kuwabara"
    
    hide kuwabara
    
    
    stop music 
    play music "luchaT.mp3"
    menu:
        "ir a peleas.":
         jump peleas
        "no.":
         jump no
        
    label peleas: 
        
    scene bg2
    with fade
    show yusuke at left
    with move
    y "entraremos a ese torneo kuwabara"
    show kuwabara at right 
    k "iremos a ganar esas batallas urameshi"
    
    hide kuwabara
    hide yusuke
    
    scene bg3
    with fade
    
    show kuwa2 at left:
        ypos 250
    with move 
    k "ese lugar nos espera urameshi"
    k "estoy ansioso por vencer a esos tipos"
    
    show yusuke at right
    y "se que saldremos victoriosos de ahi"
    
    hide kuwa2
    hide yusuke
    
    scene black
    with fade
    show byakko at left
    with move
    b "asi que tu eres el payaso que viene a retarme"
    b "te destruire facilmente"
    
    show kuwa3 at center
    k "eso esta por verse"
    k "no podras conmigo"
    k "yo te hare pedazos"
    
    scene bg4 
    with fade
    with Dissolve(.5)
    pause.5
    show kuwa2 at left:
        ypos 250
    k"empieza tu destruccion"
    show byakko at right 
    b"no hables de mas!!"
    
    scene bg4
    with fade
    with Dissolve(.5)
    pause.5
    show byakko2 at left
    with move
    b"moriras por bocon"
    show kuwa3 at right
    with move
    k"..."
    
    scene black
    with fade
    with Dissolve(.5)
    pause.5
    show pelea1
    
    
    k"estas a punto de morir"
    hide pelea1
    show kuwa4
    k"muereeee"
    
    hide kuwa4
    
    show kuwa 5
    with pixellate
    
    k"te lo dije que ibas a morir"
    k"yo sabia que ganaria"
    
    label no:
        scene bg
        with fade
    with Dissolve(.5)
    pause.5
    
    y"FIN"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return
