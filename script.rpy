# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# game/script.rpy

# ==============================
# Character Definitions
# ==============================
define e = Character("Elara", color="#66cc99")   # greenish
define m = Character("Merek", color="#6699ff")   # blueish
define r = Character("Rowan", color="#ffcc66")   # golden
define c = Character("Curator", color="#cc6666") # reddish


# ==============================
# Game Variables
# ==============================
init python:
    fear = 30
    guilt = 10
    hope = 50
    sacrifices = 0
    inventory = []
    max_fear = 100
    max_guilt = 100 
    max_hope = 100
    max_sacrifices = 5
    def adjust_stats(fear_change=0, guilt_change=0, hope_change=0, sacrifices_change=0):
        global fear, guilt, hope, sacrifices
        fear = min(max(fear + fear_change, 0), max_fear)
        guilt = min(max(guilt + guilt_change, 0), max_guilt)
        hope = min(max(hope + hope_change, 0), max_hope)
        sacrifices = min(max(sacrifices + sacrifices_change, 0), max_sacrifices)
    def show_stats():
        return "Fear: {} | Guilt: {} | Hope: {} | Sacrifices: {}".format(fear, guilt, hope, sacrifices)    
    def show_inventory():
        return "Inventory: " + ", ".join(inventory) if inventory else "Inventory: Empty"        
# ==============================
# Start of Game
# ==============================
label start:
    scene black
    with fade

    "The town sleeps under a shallow moon. You wake to the sound of distant bells — a call that tastes like iron."
    "You know one truth: sacrifices must be made. The question is, what will you trade for tomorrow?"
    "In the morning light, three figures seek you: Elara, the healer; Merek, the captain; and the child Rowan."   

    jump meet_elara


# ==============================
# Meet Elara
# ==============================
label meet_elara:
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "elara_normal.png" to the images 
    # directory.
    scene expression im.Scale("bg village_day.jpg", config.screen_width, config.screen_height)
    image elara normal = "elara_normal.png"
    show elara normal at top
    
    
    e "Thank you for coming. The land is sick, and so are we."
    e "I fear what we must do, but I also see hope. Will you help us decide?"
    hide elara
    with fade
    e "We all feel it. The harvest was thin. The river slowed. There is talk of an old bargain."
    e "If we offer something precious, the land may remember how to breathe again."

    menu:
        "Offer to assist gather rare herbs.":
            $ fear -= 5
            $ hope += 5
            "You promise to help. Elara nods, relief in her chest."
            $ inventory.append("Herb Satchel")
        "Suggest a council to decide.":
            $ fear += 5
            "You call for a council. Elara frowns — delay might be dangerous."
        "Volunteer someone else quietly.":
            $ guilt += 10
            $ fear -= 5
            "You hint at others. Elara's eyes sharpen; she sees the cost on your face."


# ==============================
# Meet Merek
# ==============================
    label meet_merek: 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "captain man.png.png" to the images 
    # directory.
    scene expression im.Scale("bg market.jpg", config.screen_width, config.screen_height)
    image merek normal = "captain man.png.png"
    show merek normal at top
    m "The dam is failing. If it breaks, the valley floods and the crops drown."
    m "We could give men and supplies to mend the dam — a sacrifice. It will cost lives."
    m "Convince them to stand down, or let them go and risk the harvest?"

    menu:
        "Rally volunteers to repair the dam.":
            $ sacrifices += 1
            $ guilt += 15
            $ hope -= 10
            "You speak of duty. Some step forward. The price is heavy."
        "Find non-lethal solutions.":
            $ hope += 10
            $ fear += 5
            "You and Merek fashion a weaker but safer solution."
            $ inventory.append("Makeshift Plans")
        "Refuse to ask for lives.":
            $ guilt -= 5
            $ hope -= 5
            "You refuse. Merek respects your stance, but the town mutters."
# ==============================
# Meet Rowan
# ==============================
label meet_rowan:
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "boy.jpg" to the images 
    # directory.
    scene expression im.Scale("bg house_night.jpg", config.screen_width, config.screen_height)
    image rowan normal = "boy.jpg"
    show rowan normal at top
    r "If we give them the lantern, will mother live?"
    "The lantern heals, but it is fragile and rare. To use it will consume something vital."

    menu:
        "Give the lantern to Rowan's mother.":
            $ sacrifices += 1
            $ guilt -= 5
            $ hope += 20
            "Hope flares in Rowan’s eyes — and a pang of loss pricks you."
        "Keep the lantern.":
            $ guilt += 20
            $ hope -= 10
            "You hide the lantern. Rowan cries."
        "Break the lantern.":
            $ sacrifices += 1
            $ guilt += 30
            $ hope -= 20
            "You smash the lantern. For a moment, everyone is equal in darkness."

    jump crossroads


# ==============================
# Crossroads
# ==============================
label crossroads:
    scene expression im.Scale("bg ritual_circle.jpg", config.screen_width, config.screen_height)
    c "A final offering. The valley will ask for a single thing in return for balance. Will you choose?"

    menu:
        "Offer yourself.":
            $ sacrifices += 1
            $ hope += 50
            $ guilt -= 10
            jump ending_self
        "Offer a loved one.":
            $ sacrifices += 2
            $ guilt += 50
            $ hope += 30
            jump ending_others
        "Refuse the bargain.":
            $ fear += 30
            $ hope -= 20
            jump ending_refuse


# ==============================
# Endings
# ==============================
label ending_self:
    "You step into the circle. Rivers remember their routes. Crops lift their heads."
    "Your name becomes a lantern passed at nights; stories say you gave everything and bought a future."
    return

label ending_others:
    "The town prospers, but silence follows where laughter once was."
    "You live, but each meal tastes like ash."
    return

label ending_refuse:
    "You refuse to feed the old machine. The valley suffers, but the bargain weakens."
    "Some die, but others rebuild with sweat and skill."
    return

