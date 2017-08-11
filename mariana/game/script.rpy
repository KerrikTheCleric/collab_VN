# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sylvie")

init:
    image sylvie normal = "sylvie2_normal.png"
    image sylvie giggle = "sylvie2_giggle.png"
    image sylvie smile = "sylvie2_smile.png"
    image sylvie surprised = "sylvie2_surprised.png"
    
    image bg duomo_di_milano = "duomo_di_milano.jpg"
    image bg black = "black.jpg"
    
    default knew = False


# The game starts here.

label start:
    
    scene bg black
    
    show sylvie normal at left
    
    s "Hi. My name is Sylvie and I'm stolen from the example game!"
    
    show sylvie giggle at center with fade
    
    s "For purely budgetary concerns, of course. Shoestring budgets are tight these days."
    
    scene bg duomo_di_milano
    
    show sylvie normal 
    
    s "Hey, did you know that the design for Anor Londo was stolen from the Duomo di Milano in Italy?"
    s "Here, let me move aside so you can see this improperly scaled image."
    
    show sylvie smile at right with pixellate
    
    s "That tickled!"
    
    show sylvie normal
    
    s "So, did you know that? Be honest."
    
    menu:

        "I did not, good to know.":
            
            $ knew = False


        "Well, duh.":
            
            $ knew = True

            
    if knew: 
        
        show sylvie surprised
        
        s "You knew?"
        
        show sylvie normal
        
        s "From Soft really are a bunch of hacks."
    
        
    else:
    
        show sylvie giggle
    
        s "And knowing is half the battle!"
        
        show sylvie normal
        
    "I think that's enough. This wasn't that bad to set up. The real thing will probably end me."


    return
