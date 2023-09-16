#variable definitions

#characters
define a = Character("Azari", image="azari", color="#dedede")
define a2 = Character("Azari", color="#dedede") #no side image
define l = Character("Layne", image="layne", color="#dedede")
define al = Character("Alexandre", color="#dedede")
define q = Character("???")

# NVL characters are used for the phone texting
define a_nvl = Character("Azari", kind=nvl, callback=Phone_SendSound)
define l_nvl = Character("Layne", kind=nvl, callback=Phone_ReceiveSound)
define al_nvl = Character("Alexandre", kind=nvl, callback=Phone_ReceiveSound)
define ai_nvl = Character("Aika", kind=nvl, callback=Phone_ReceiveSound)
define c_nvl = Character("Chaayan", kind=nvl, callback=Phone_ReceiveSound)
define d_nvl = Character("Daniel", kind=nvl, callback=Phone_ReceiveSound)
define e_nvl = Character("Eve", kind=nvl, callback=Phone_ReceiveSound)

#configurations
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#ADJUST THESE
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.7

#images
image black = "black.jpg"
image white = "white.jpg"
image a_bed = "azari_bedroom.png"
image a_bed_night = "azari_bedroom_night.png"
image a_bed_night_blur = "azari_bedroom_night_blur.png"
image bridge = "bridge_bg_day.png"
image bridge_night = "bridge_bg_night.png"
image bridge_night_blur = "bridge_bg_night_blur.png"
image forest = "Forest_BG.png"
image forest_rain = "Forest_BG_Rain.png"
image wrong_forest = "wrong_forest.png"
image reunion = "Reunion_CG.png"
image lockscreen_morning = "Azari_Phone_Lockscreen.png"
image lockscreen_night = "Azari_Phone_Lockscreen_Night.png"
image layne_notif_lockscreen = "Layne_Phone_Lockscreen_Notif.png"
image village = "village_bg.png"
image village_blur = "village_bg_blur.png"
image village_empty = "village_empty.png"
image village_rain = "village_bg_rain.png"
image villager_A_death = "village_azari_death_dream"
image royal_A_death = "royal_azari_death_dream"

#sprites (zoom 0.5 them !)

#village sprites
image villager_L:
    "Village_L.png"
    zoom 0.5
image villager_A:
    "Village_A.png"
    zoom 0.5


#azari sprites - day
image side azari neutral:
    "A_neutral.png"
    zoom 0.4
    xpos 0.05

image side azari awkward:
    "A_Awk.png"
    zoom 0.4
    xpos 0.05
image side azari awk smile:
    "A_Awk_Smile.png"
    zoom 0.4
    xpos 0.05
image side azari awk smile closed:
    "A_Awk_Smile_Closed.png"
    zoom 0.4
    xpos 0.05
image side azari blush excited:
    "A_Blush_Excited.png"
    zoom 0.4
    xpos 0.05
image side azari blush ss:
    "A_Blush_SlightSmile.png"
    zoom 0.4
    xpos 0.05
image side azari concern:
    "A_Concern.png"
    zoom 0.4
    xpos 0.05
image side azari confused:
    "A_Confused.png"
    zoom 0.4
    xpos 0.05
image side azari embarass:
    "A_Embarass.png"
    zoom 0.4
    xpos 0.05
image side azari embarass open:
    "A_Embarass_Open.png"
    zoom 0.4
    xpos 0.05
image side azari excited:
    "A_Excite.png"
    zoom 0.4
    xpos 0.05
image side azari neutral:
    "A_Neutral.png"
    zoom 0.4
    xpos 0.05
image side azari neutral closed:
    "A_Neutral_Closed.png"
    zoom 0.4
    xpos 0.05
image side azari neutral open:
    "A_Neutral_Open.png"
    zoom 0.4
    xpos 0.05
image side azari pain smile:
    "A_Pain_Smile.png"
    zoom 0.4
    xpos 0.05
image side azari shock open:
    "A_Shock_Open.png"
    zoom 0.4
    xpos 0.05
image side azari ss:
    "A_SlightSmile.png"
    zoom 0.4
    xpos 0.05
image side azari ss open:
    "A_SlightSmile_Open.png"
    zoom 0.4
    xpos 0.05
image side azari wink:
    "A_Wink.png"
    zoom 0.4
    xpos 0.05

#azari sprites - night
image side azari awk n:
    "A_Awk_N.png"
    zoom 0.4
    xpos 0.05
image side azari awk smile n:
    "A_Awk_Smile_N.png"
    zoom 0.4
    xpos 0.05
image side azari awk smile closed n:
    "A_Awk_Smile_Closed_N.png"
    zoom 0.4
    xpos 0.05
image side azari blush excited n:
    "A_Blush_Excited_N.png"
    zoom 0.4
    xpos 0.05
image side azari blush ss n:
    "A_Blush_SlightSmile_N.png"
    zoom 0.4
    xpos 0.05
image side azari concern n:
    "A_Concern_N.png"
    zoom 0.4
    xpos 0.05
image side azari confused n:
    "A_Confused_N.png"
    zoom 0.4
    xpos 0.05
image side azari embarass n:
    "A_Embarass_N.png"
    zoom 0.4
    xpos 0.05
image side azari embarass open n:
    "A_Embarass_Open_N.png"
    zoom 0.4
    xpos 0.05
image side azari excite n:
    "A_Excite_N.png"
    zoom 0.4
    xpos 0.05
image side azari neutral n:
    "A_Neutral_N.png"
    zoom 0.4
    xpos 0.05
image side azari neutral closed n:
    "A_Neutral_Closed_N.png"
    zoom 0.4
    xpos 0.05
image side azari neutral open n:
    "A_Neutral_Open_N.png"
    zoom 0.4
    xpos 0.05
image side azari pain smile n:
    "A_Pain_Smile_N.png"
    zoom 0.4
    xpos 0.05
image side azari shock open n:
    "A_Shock_Open_N.png"
    zoom 0.4
    xpos 0.05
image side azari ss n:
    "A_SlightSmile_N.png"
    zoom 0.4
    xpos 0.05
image side azari ss open n:
    "A_SlightSmile_Open_N.png"
    zoom 0.4
    xpos 0.05
image side azari wink n:
    "A_Wink_N.png"
    zoom 0.4
    xpos 0.05


#layne sprites - day
image l_awk:
    "L_Awk.png"
    zoom 0.5
image l_awk_smile:
    "L_Awk_Smile.png"
    zoom 0.5
image l_awk_smile_closed:
    "L_Awk_Smile_Close.png"
    zoom 0.5
image l_blush_smile:
    "L_Blush_Smile.png"
    zoom 0.5
image l_concern:
    "L_Concern.png"
    zoom 0.5
image l_confused:
    "L_Confused.png"
    zoom 0.5
image l_embarass_awk:
    "L_Embarass_Awk.png"
    zoom 0.5
image l_embarass_lookaway:
    "L_Embarass_LookAway.png"
    zoom 0.5
image l_excite:
    "L_Excite.png"
    zoom 0.5
image l_neutral:
    "L_Neutral.png"
    zoom 0.5
image l_neutral_open:
    "L_Neutral_Open.png"
    zoom 0.5
image l_pain_smile:
    "L_Pain_Smile.png"
    zoom 0.5
image l_shock:
    "L_Shock.png"
    zoom 0.5
image l_shock_blush:
    "L_Shock_Blush.png"
    zoom 0.5
image l_shock_blush_open:
    "L_Shock_Blush_Open.png"
    zoom 0.5
image l_shock_open:
    "L_Shock_Open.png"
    zoom 0.5
image l_slightsmile:
    "L_SlightSmile.png"
    zoom 0.5
image l_slightsmile_open:
    "L_SlightSmile_Open.png"
    zoom 0.5

#layne sprites - night
image l_awk_n:
    "L_Awk_N.png"
    zoom 0.5
image l_awk_smile_n:
    "L_Awk_Smile_N.png"
    zoom 0.5
image l_awk_smile_closed_n:
    "L_Awk_Smile_Closed_N.png"
    zoom 0.5
image l_blush_smile_n:
    "L_Blush_Smile_N.png"
    zoom 0.5
image l_concern_n:
    "L_Concern_N.png"
    zoom 0.5
image l_confused_n:
    "L_Confused_N.png"
    zoom 0.5
image l_embarass_awk_n:
    "L_Embarass_Awk_N.png"
    zoom 0.5
image l_embarass_lookaway_n:
    "L_Embarass_LookAway_N.png"
    zoom 0.5
image l_excite_n:
    "L_Excite_N.png"
    zoom 0.5
image l_neutral_n:
    "L_Neutral_N.png"
    zoom 0.5
image l_neutral_open_n:
    "L_Neutral_Open_N.png"
    zoom 0.5
image l_pain_smile_n:
    "L_Pain_Smile_N.png"
    zoom 0.5
image l_shock_n:
    "L_Shock_N.png"
    zoom 0.5
image l_shock_blush_n:
    "L_Shock_Blush_N.png"
    zoom 0.5
image l_shock_blush_open_n:
    "L_Shock_Blush_Open_N.png"
    zoom 0.5
image l_shock_open_n:
    "L_Shock_Open_N.png"
    zoom 0.5
image l_slightsmile_n:
    "L_SlightSmile_N.png"
    zoom 0.5
image l_slightsmile_open_n:
    "L_SlightSmile_Open_N.png"
    zoom 0.5

#VARIABLES
default layne_affection = 0


label start:
    stop music

    # first dream sequence
    scene black
    $ renpy.pause(1.5, hard=True)
    play music "audio/storm.mp3" loop volume 0.2
    scene forest_rain
    with fade


    a neutral "{i} Huh…? Where am I…?"
    a "{i} A forest? How did I…"
    a shock open "{i} And it’s raining?!"
    a confused "{i} But…I’m completely dry?"

    show villager_A with Dissolve(1.0):
        yoffset 70
        xoffset 300

    "Someone speedwalks by in front of me, completely unperturbed by my presence."
    a "{i} Who is…?"
    a neutral "{i} Ah."
    a "{i} A dream, maybe? That would explain why I’m completely dry."
    a "{i} Never been aware of a dream before though. Does that make this a lucid dream?"

    hide villager_A with Dissolve(1.0)

    a "{i} Who would’ve thought, all that time I spent trying to lucid dream in high school and it finally happens when I don’t even try–-"

    q "AAAAAA!"

    a shock open "Huh?!"
    "I snap back towards the scream, only to witness that same person slip on the mud and fall off the nearby ledge."
    "Running over to try and help, I try to stop by the ledge to look down at the damage, but the loose mud underneath my feet causes me to twist my ankle, and I tumble after."

    a "Wh-AAAAAA!"

    scene black

    "My stomach drops at the fall, and I shut my eyes tightly at the growing pit in my stomach."

    play sound "audio/thud.mp3" volume 0.7

    "A resounding thud, and all the wind is knocked out of my chest."

    stop music

    "For a moment, I feel nothing, and then everything."

    play sound "audio/heartbeat_tense.mp3" loop volume 0.2

    "Pain blooms all over my body, and I can barely breathe."

    a2 "{i} Shit…is the other person okay?"

    "I strain my neck, pain shooting through my muscles, to gaze to my left. And then my right."
    "But no one’s there."

    a2 "{i} What…?"
    "I can feel myself fading quickly, but before I completely succumb, one thing stands out and unsettles me down to my core."



    scene villager_A_death with vpunch

    "A small woven basket near my arm, the scattered red sage mingling with the color of my blood."

    stop sound

    scene a_bed
    "I wake with a start, feeling phantom pains in my chest and breathing heavy." with vpunch
    "Sweat clings to my shirt, and my lungs burn for a few moments before fading away."

    a concern "{i} That was…weird."
    "Weird is an understatement, but with my mind still racing, it’s the only word that comes to my mind."
    a "{i}I haven’t had a dream that felt so real in forever. Have I {b}ever{/b} had a dream that vivid before?"
    "I clutch my chest, willing myself to breathe deeply and slowly."
    "It takes a few minutes, but my heart rate no longer beats wildly in my ears, and I exhale loudly."
    a neutral "{i} …Did my alarm go off?"
    "I grab my phone from under my pillow."

    show lockscreen_morning at truecenter with Dissolve(0.5)


    a "{i} 6:57…it’s only a few minutes until my alarm goes off. I might as well just get up now."
    "Despite thinking that, the weight of my tiredness seems to win out, and I find myself laying in bed for those few minutes."
    a neutral closed "{i} …I don’t actually have to be awake until 7. I can stay here for a few minutes."

    hide lockscreen_morning with Dissolve(1.0)

    "My thoughts drift back to that strange dream from earlier."
    a "{i} Where did that person go? They fell off that cliff too, but it seemed like they disappeared."
    a neutral "{i} And I ended up with their basket somehow. There’s no way it just {b}fell{/b} onto my arm."
    a "{i} It’s almost as if…I became them."
    "I shudder at the thought."
    a "{i} Creepy."
    "A yawn escapes me."
    a concern "{i} Of course I had to have a weird dream right before a morning shift."
    a "{i} Hopefully I can stay awake until it’s over."

    play sound "audio/alarm_sound.mp3" volume 0.7

    "The sound of my alarm finally blares, snapping me out of my thoughts. Begrudgingly, I peel myself out of bed, and get ready for work."
    a neutral "{i} On the bright side, working the opening shift means I don’t have to worry about making breakfast myself."
    a "{i} Thank god the cafe is free for employees. Maybe I can check out the bestsellers that arrived last week while I eat."

    play sound "audio/text.mp3" volume 0.7

    "A quick message comes into my work group chat from my boss."

    #phone messaging system
    nvl_narrator "Autumn's Legacy Employees"
    al_nvl "Good morning everyone!"
    al_nvl "I just spoke to the author of Hisato and they agreed to come in next month for a book signing at the shop!"
    al_nvl "I know quite a few of you here enjoyed that novel, and I was told that they would be willing to give out signatures to the employee’s for free as thanks!"
    al_nvl "Let me know if you are interested by the end of today and I’ll give them a quick headcount of how many people to expect :)"
    ai_nvl "uhhh….DUH ABSOLUTELY that’s like my favorite book >:DDD"
    c_nvl "It’s wonderful to have them here. I would love to get a signature from them as well."
    d_nvl "Hmm I guess it sounds fun. Why not?"
    e_nvl "Ohhh me please!!!!!"

    "I chuckle a bit at the speed of the responses, then head over to type my own."

    a_nvl "would love to cash in on that signature opportunity as well >:)"

    nvl clear

    "I set my phone down after sending the message, finishing up the rest of my routine, before heading out the door."

    scene bridge with Dissolve(2.0)

    "My lethargy from this morning fades away the moment I step outside and feel the slight chill in the air."
    "Despite the good news from today, I can’t help but feel my mind reaching back towards the nightmare from earlier."
    a concern"{i} Normally I just dream about customers accidentally knocking over the book displays or spilling their drinks in the cafe and demanding refunds."
    a "{i} Hopefully it’s not a bad omen for today…Surely it isn’t, with the book signing success and all."

    show l_neutral with Dissolve(2.0):
        yoffset 70
        xoffset 400

    a neutral "{i} The premise of it was strange though. That seemed like an entirely different time period."
    a "{i} There has been a new craze with historical fiction at the store lately… Maybe it’s been imprinted in my mind?"
    a neutral closed "{i} God, I hope not. I’ve had enough of history from high school."

    hide l_neutral with Dissolve(2.0)

    a "{i} …"
    a shock open "{i} …Wait a minute–!"
    "I spin around in place and immediately rush towards the silver ponytail bounding away from me, muttering quick apologies and “excuse me’s” to the people I push past."
    a "{i} It can’t be…"
    "Stretching my arm out, I lean forward and cling onto the forearm of the person I’ve been chasing."

    scene reunion with vpunch
    with Dissolve(1.0)

    "I open my mouth to force some words out, any words out, but as soon as he turns around and I’m face to face with him, I freeze up, the words get caught in my throat."
    "He seems to react similarly, but before any of us can break the tension, a bright light seems to overtake my vision, and I shut my eyes at the sight."

    play sound "audio/bell.mp3" volume 0.5
    scene white
    $ renpy.pause(1.0, hard=True)
    scene black with Dissolve(2.0)

    #act 1
    scene village_blur with Dissolve(2.0)

    "I squint my eyes, trying to adjust to the bright lights around me."

    scene black with Dissolve(2.0)
    scene village_blur with Dissolve(1.0)
    scene black with Dissolve(1.0)
    scene village with Dissolve(1.0)

    "Looking at the scenery in front of me, I whip my head around in confusion, taking in the sights that are {i}clearly not where I originally was.{/i}"
    "Yet, my blood runs cold because of the familiarity of the place. Although I wasn’t in this exact place, it’s not hard to recognise this atmosphere."
    a shock open "{i}This is the place from my dream."
    a confused "{i} But how? Why? I was on the bridge a couple minutes ago, how did I suddenly get here?"
    a "{i} And where even is ‘here’?"
    a "{i} Am I still dreaming somehow?"

    q "...Azari?"

    show l_shock with Dissolve(1.0):
        yoffset 70
        xoffset 400

    "A small voice breaks my train of thought, and I finally make eye contact with the man in front of me."
    "A man so familiar, yet so unrecognizable at the same time."

    a neutral open "...Layne."
    a pain smile "{i} It’s been a while."

    hide l_shock

    show l_awk:
        yoffset 70
        xoffset 400

    "A beat passes."
    a neutral "{i} What do I even say? ‘Do you know where we are?’ ‘What was that light from before?’"
    a "{i} ‘How have you been?’ ‘What have you been up to since high school?’"
    a pain smile "{i} ’Why did you stop talking to me?’"
    a neutral closed"{i} Of all the times, of all the {b}people{/b} I could run into, of course it had to be in the most complicated situation possible."

    hide l_awk

    show l_awk_smile:
        yoffset 70
        xoffset 400

    l "Uh…you wouldn’t happen to know what’s going on, would you?"

    a concern "{i} He looks uncomfortable. Is it because he’s forced to talk to me again, or just because of the situation?"
    a neutral open "Just as confused as you are Layne."

    hide l_awk_smile

    show l_awk_smile_closed:
        yoffset 70
        xoffset 400

    l "Hah…I figured…"

    hide l_awk_smile_closed

    show l_awk:
        yoffset 70
        xoffset 400

    a "{i} He’s not bringing up what happened back then. Am I the only one affected by it?"
    a concern "{i} Am I the only one who cared…?"
    a neutral closed "{i} Well, I guess if he had it his way, we would never talk to each other again. It worked out in his favor for 6 years."
    "I let out an annoyed exhale, then gaze back at Layne."
    a neutral open"Look, I have a lot to say to you, but right now we have a few bigger problems at hand. We’ll figure this issue out first, and then we’re talking. I’m not letting you get out of that, got it?"

    hide l_awk

    show l_shock:
        yoffset 70
        xoffset 400

    "Layne looks at me blankly before flushing and nodding."

    hide l_shock

    show l_shock_blush_open:
        yoffset 70
        xoffset 400

    l "Yeah…that sounds good to me."

    hide l_shock_blush_open

    show l_shock_blush:
        yoffset 70
        xoffset 400

    "At his confirmation, I take another look around at our surroundings, hoping the need for investigation will defer my desire to interrogate Layne on the spot."
    a neutral closed "{i} As much as I want to grill him about everything, this probably isn’t the best time or place to do it."

    hide l_shock_blush

    show l_neutral:
        yoffset 70
        xoffset 400

    "A couple people roam the path–some on a simple stroll, some sitting by the path, while others elect to stand and talk amongst themselves."
    "On its own, there’s nothing out of the ordinary, but looking at each of the passersby closely…"
    a confused "I can’t make out anyone’s face."
    "I had assumed that my post-dream haziness was the reason I couldn’t remember any faces from my dream, but standing in front of all of these people now, not a single face is clear enough to identify."
    a neutral open"It’s just like in my dream…"

    hide l_neutral

    show l_confused:
        yoffset 70
        xoffset 400

    l "Your dream?"

    a "Oh, I mean…"
    a awkward"{i} God, how do I explain this without sounding insane?"
    a neutral closed"{i} Whatever, it’s not as if the situation we’re in isn’t crazy on its own."
    a "It was…weird."

    hide l_confused

    show l_shock:
        yoffset 70
        xoffset 400
    a "I had a dream today about being in a place just like this, and even then, I couldn’t make out anyone’s face."
    "My cheeks heat up slightly at the topic."
    a embarass open "I mean, it’s certainly strange that we ended up here somehow and that it matches my dream, but I don’t mean to imply that we were transported into my dream or something."
    a "This situation is unreal but even I know that it’s ridiculous–-"

    l "I had a dream about this place too."

    hide l_shock
    show l_neutral:
        yoffset 70
        xoffset 400

    a "Huh?"
    "He had a dream too…?"
    a neutral open"Did you also fall off a cliff?"

    hide l_neutral
    show l_shock:
        yoffset 70
        xoffset 400

    l "I…"

    hide l_shock
    show l_pain_smile:
        yoffset 70
        xoffset 400

    l "...No, I didn’t. But I found someone who did."
    l "I just remember running around and panicking looking for someone, and then finding them at the bottom of a cliff."

    a concern "I…think I experienced the opposite side of that. Or well, kind of?"

    hide l_pain_smile
    show l_confused:
        yoffset 70
        xoffset 400

    l "What do you mean ‘kind of’?"

    a neutral open "It’s like…I started out as me, and witnessed someone fall off a cliff."
    a concern "But then when I went to go help, I fell and then somehow…shifted into the person I witnessed fall."

    hide l_confused
    show l_neutral:
        yoffset 70
        xoffset 400
    "Layne hums in acknowledgement, his gaze focusing arbitrarily on the ground in front of him."

    l "Was there a storm in your dream?"

    "I nod."

    a "{i} So we had two sides of the same dream."
    a "{i} But why? Why us? Why now?"

    l "It was raining in my dream too. It’s not raining now though. So we don’t know for sure if the accident is about to happen later today, or if it’s already happened today."

    a neutral open "And how are we supposed to know if we're even {i}close{/i} to the accident? We could be weeks away from it altogether."

    hide l_neutral
    show l_awk_smile:
        yoffset 70
        xoffset 400

    l "That’s…also true. Regardless, I guess the only thing we can do at this point is try to investigate and see if it brings us any closer to figuring out what’s going on."

    a neutral closed "Haah...I suppose any new information here would be helpful."

    hide l_awk_smile
    show l_neutral:
        yoffset 70
        xoffset 400

    l "We should probably try asking someone about the people in our dreams, but more generally instead of asking about the accident."
    l "If the accident hasn’t happened yet, we’d probably look a little crazy…"

    a neutral open"And if the accident DID happen, we’d just look insensitive."

    hide l_neutral
    show l_awk_smile:
        yoffset 70
        xoffset 400

    l "Yeah…"

    hide l_awk_smile
    show l_neutral:
        yoffset 70
        xoffset 400
    l "Let’s just ask someone about where to find them. We can just….say we’re old friends visiting or something."

    hide l_neutral with Dissolve(1.0)

    "Use your mouse to explore the area and find objects you can interact with!"

    play music "audio/Bloom_Onycs.mp3" fadein 1.0 loop volume 0.08

    #first dream variables
    $ village_outfit = False
    $ village_azari_known = False
    $ village_azari_true_location = False
    $ village_azari_false_location = False
    $ village_layne_location = False
    $ first_dream_success = False



    label first_dream:
        if village_azari_known == False:
            call screen village_imagemap
        elif village_layne_location == False:
            call screen village_imagemap
        elif village_outfit == False:
            call screen village_imagemap
        else:
            jump post_village_imagemap

    screen village_imagemap():
        imagemap:
            ground "village_bg.png"
            idle "village_bg.png"
            hover "village_bg_hover.png"
            hotspot(946, 632, 148, 283) action Jump("village_stroll")
            hotspot(626, 748, 86, 42) action Jump("village_sit")
            hotspot(1202, 557, 107, 133) action Jump("village_house")
            hotspot(1422, 708, 121, 114) action Jump("laundry")

    label village_stroll:
        scene village

        if village_outfit == False:
            a neutral open "Excuse me, could I ask you a few questions?"
            "The person in front of us stops and turns, their expression warping from a gentle smile to confusion to disgust."
            q "I'm not interested, sorry."

            "They immediately turn away and speed off, leaving Layne and myself none-the-wiser."

            show l_awk with Dissolve(1.0):
                yoffset 70
                xoffset 400
            a confused "What the hell was their problem?"

            hide l_awk
            show l_awk_smile:
                yoffset 70
                xoffset 400

            l "Maybe they thought we were scammers? It’s not like we really look like we belong here."
            "I look down at my outfit, then at Layne’s."
            "Although our styles seem a lot less novel in comparison to other styles, my face heats up as I’m suddenly aware of how crazy I must seem in comparison to the others."
            a embarass open "...Let’s go find more appropriate outfits then."

            hide l_awk_smile with Dissolve(1.0)
            jump first_dream
        elif village_azari_known == False:
            show l_slightsmile with Dissolve(1.0):
                yoffset 70
                xoffset 400
            a neutral open "Excuse me, could I ask you a few questions?"
            "The person in front of us stops and turns, their expression warping from a gentle smile to slight confusion"

            q "What do you need?"

            "Although significantly less hostile than our previous encounter, there is still a distinct sense of distance between us."

            a "{i} I gotta get them to trust us."
            a neutral closed "{i} Deep breath in, customer service voice on."
            a ss open "We’re looking for some people and we were wondering if you could help us find them."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "We’re trying to meet up with some friends, but we don’t know the area too well."

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Layne adds, putting on an air of friendly confidence."

            a pain smile "{i} He’s always been a people person. Guess that hasn’t changed since back then."
            "The person seems to relax a bit looking at his (seemingly) genuine smile, and offer a small smile of their own in return."
            "Seeing how easily he can deceive them sends knots into my stomach."
            a concern"{i} …He must’ve done the same with me back then. How could I never notice?"
            q "Oh! Not to worry, the village is quite small so we should be able to help find who you’re looking for. Who were you trying to find?"

            "I pause, glancing nervously at Layne."

            hide l_slightsmile
            show l_concern:
                yoffset 70
                xoffset 400
            "His face scrunches up in concern for a split second, before returning back to his cool demeanour."

            hide l_concern
            show l_slightsmile:
                yoffset 70
                xoffset 400

            a neutral "{i} I don’t know that person’s name, and by the looks of Layne’s face, he doesn’t seem to either. How do I go about describing them without seeming too suspicious?"

            menu:
                 "I’m looking for a woman with a blue-ish ponytail.":
                     a "She’s around my height?"

                     q "Oh, you’re looking for–"

                     "To my surprise, their voice cuts out, as if someone had muted a video."

                     hide l_slightsmile
                     show l_confused:
                         yoffset 70
                         xoffset 400
                     "I stare at Layne in confusion, but he also seems just as lost as I do."

                     hide l_confused
                     show l_neutral:
                         yoffset 70
                         xoffset 400
                     "The person seem to look at us, waiting for confirmation. With no other option, I just nod in agreement."

                     a "Yes, that’s the one. Do you know where she is?"

                     q "I saw her about a half hour ago heading towards the forest to gather some red sage for her husband."
                     q "Not sure if she’s still there, but red sage is hard to come by these days, so I’d wager she’ll be there for a while."

                     "They point towards the edge of town towards the nearby forest."

                     a ss open"Ah, I see. Thank you so much!"

                     "With a smile, I wave them off, mentally making note of the direction to head in my mind."

                     hide l_neutral
                     show l_slightsmile_open:
                         yoffset 70
                         xoffset 400

                     l "I’m glad that worked out well. If we need to find her, then we’ll head towards the forest. For now, I think we should try to ask for more information."

                     hide l_slightsmile_open with Dissolve(1.0)

                     $ village_azari_true_location = True
                     $ village_azari_known = True
                     jump first_dream
                 "I'm looking for a woman who carries a basket with her":
                     "I motion with my hands."
                     a "It’s about this big, stained green in some areas?"

                     q "A basket? Well a lot of us carry a basket with us, and the grass stains a lot of our belongings green, so that’s not too much to go off of."

                     "I feel my face drop."
                     a concern "{i} Was that description not enough?"

                     q "If she’s carrying a basket, she might be going to gather some herbs or fruits. Most of the herbs we gather are over behind the village’s inn, while the fruits are over down south."

                     a ss open "Ah, I see. Thank you so much!"
                     "I wave them goodbye and they continue off down the path."

                     l "Do you know what the woman was trying to get?"

                     a confused "Huh?"

                     l "The woman in your dream. Was she trying to get herbs or fruits?"

                     "I try to focus back on the details in my dream."
                     a neutral "She was trying to get…"

                     menu:
                         "...fruits.":
                             a "...fruits, I think."
                             a "{i} There was definitely something red in her basket. Berries, maybe?"

                             hide l_neutral
                             show l_slightsmile_open:
                                 yoffset 70
                                 xoffset 400

                             l "Got it. If we need to find her, then we’ll head south. For now, I think we should try to ask for more information."

                             hide l_slightsmile_open with Dissolve(1.0)

                             $ village_azari_known = True
                             $ village_azari_false_location = True
                             jump first_dream
                         "...herbs.":
                             a "Herbs. She had red sage in her basket, I remember that."
                             a "{i} It’s hard to get that image out of my head really."

                             hide l_neutral
                             show l_slightsmile_open:
                                 yoffset 70
                                 xoffset 400

                             l "Got it. If we need to find her, then we’ll head behind the inn. For now, I think we should try to ask for more information."

                             hide l_slightsmile_open with Dissolve(1.0)

                             $ village_azari_true_location = True
                             $ village_azari_known = True

                             jump first_dream
                 "I'm looking for someone who went near the cliff.":

                     show l_neutral with Dissolve(1.0):
                         yoffset 70
                         xoffset 400
                     a "There’s a particularly steep cliff somewhere in the forest. Does anyone usually go there?"
                     "The person looks at me in shock, practically offended by the question."

                     hide l_neutral
                     show l_awk:
                         yoffset 70
                         xoffset 400

                     q "No one in the village is stupid enough to go by a cliff, are you kidding?"

                     "I cringe at the hostility in their tone. Layne looks just as flustered."
                     a embarass "{i} Okay, so clearly that was a stupid question,, but was that {b}really{/b} necessary?"
                     "Seemingly sensing the awkwardness of their outburst, the person suddenly avoids eye contact with me."

                     q "{i}Ahem{/i}, what I meant to say is that there isn’t anyone who really fits that description, but there's a couple forests with cliffs that you can try out. Sorry."

                     "With a quick bow of their head, they scurry off, eager to awkward tension."

                     a confused "What was wrong that time?"

                     hide l_awk
                     show l_awk_smile:
                         yoffset 70
                         xoffset 400

                     l "Um, well..."
                     l "Maybe the incident...has already happened? They seemed a little on edge."

                     "I feel my heart sink at his words."
                     a concern "{i} Yeah, that would make the most sense. So then it was all for nothing?"
                     a "{i} Then what are we supposed to do here?"

                     hide l_awk_smile
                     show l_pain_smile:
                         yoffset 70
                         xoffset 400
                     "Layne rests a hand on my arm, offering me a comforting smile."

                     l "...Well, we still don't know for sure. There’s more people we can ask for information to find out. Let’s go."

                     hide l_pain_smile with Dissolve(1.0)

                     $ village_azari_known = True
                     $ village_azari_false_location = True
                     jump first_dream
        else:

            show l_slightsmile_open with Dissolve(1.0):
                yoffset 70
                xoffset 400
            l "Excuse me, could I ask you a few questions?"

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Like before, the person in front of us stops at the sound of Layne’s voice and turns around, confusion written on their face."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "I’m sorry to bother you on your walk. We’re looking for someone and we were wondering if you could help us find them? We don’t really know the area too well."

            q "Oh! Yeah, who were you trying to find?"

            l "His name is–"

            "But like with the group from before, Layne’s voice cuts out upon saying the name."
            a confused "{i} Layne knows his name?"
            a "{i} Was he just pretending to be confused before?"
            "I try to push down that uncomfortable feeling bubbling in my throat."
            a concern "{i} How many things will he hide from me?"

            q "Last I saw him he was waving his wife off from his house. I don’t think he would’ve left, not unless his wife had already returned home, and especially not if he was expecting you two to visit."
            q "His house is down the path. It’s the 3rd house on the right, but you can easily identify it by the Adonis flowers planted in front."

            hide l_slightsmile_open
            show l_pain_smile:
                yoffset 70
                xoffset 400

            l "Adonis flowers…"

            hide l_pain smile
            show l_slightsmile:
                yoffset 70
                xoffset 400
            l "Got it. Thank you so much for your help."

            q "No problem!"

            $ village_layne_location = True

            stop music fadeout 1.0

            play music "audio/storm.mp3" loop volume 0.2

            scene village_rain with Dissolve(2.0)

            hide l_slightsmile
            show l_shock_n with Dissolve(1.0):
                yoffset 70
                xoffset 400

            "A clap of thunder resounds over us."
            "I turn to Layne, fear written all over my face."
            l "Rain."

            q "Looks like a storm is coming in. You might want to hurry heading over to — house!"

            a shock open n "Wait!"
            "I cringe at my volume, but look at the villager in earnest."
            a awk smile n "Does his wife have blue hair by any chance?"

            q "Uh, yeah, she does. Why do you ask?"

            a awk n "{i} Well, fuck. I didn't think this far ahead."
            a awk smile n "Ah, well, you know, I just..."

            hide l_shock_n
            show l_slightsmile_n:
                yoffset 70
                xoffset 400

            l "Haha, we just thought we might have seen her earlier, but we weren't completely sure. ---- has always gushed about his wife, but we've never been able to put a face to the name before."

            "They look slightly unconvinced, but luckily for us, they don’t question it."

            a concern n "{i} Layne’s gotten…too good at lying over these past years."

            q "That certainly sounds like —."

            "Another clap of thunder, much closer this time, followed by a light drizzle of rain, patters on the ground all around us."

            q "Well, I hope you can find them before the storm gets worse!"

            "The villager waves us goodbye and rushes off in the opposite direction, eager to avoid the storm soon approaching."

            jump post_village_imagemap

    label village_sit:
        scene village

        if village_outfit == False:
            a neutral open"Excuse me, could I ask you a few questions?"
            "The pair in front of us stops and looks up, their expressions warping from boisterous smiles to confusion to fear."
            q "Um, we’re not interested, sorry!"

            "They immediately pack up their things and speed off, making occasional glances back towards us, hints of discomfort shining in their eyes."

            show l_awk with Dissolve(1.0):
                yoffset 70
                xoffset 400

            a concern "Come on, I'm not {b} that {/b} scary, am I?"

            hide l_awk
            show l_shock:
                yoffset 70
                xoffset 400

            l "No, not at all!"
            "I stare in shock, before chuckling a little to myself."
            a pain smile "{i} I meant it as a joke, but seeing him vehemently deny it reminds me of high school."

            hide l_shock
            show l_awk_smile:
                yoffset 70
                xoffset 400

            l "Just…Maybe they thought we were scammers? It’s not like we really look like we belong here."

            "I look down at my outfit, then at Layne’s."
            "Although our styles seem a lot less novel in comparison to other styles, my face heats up as I’m suddenly aware of how crazy I must seem in comparison to the others."
            a embarass open"...Let’s go find more appropriate outfits then."
            jump first_dream
        elif village_azari_known == False:
            show l_slightsmile with Dissolve(1.0):
                yoffset 70
                xoffset 400
            a neutral open "Excuse me, could I ask you a few questions?"
            "The pair in front of us stop and look up, their expression warping from boisterous smiles to slight confusion."

            q "Oh, um, hello! What do you need?"

            "Although significantly less hostile than our previous encounter, there is still a distinct sense of uneasiness from the two."

            a "{i} I gotta get them to trust us."
            a neutral closed "{i} Deep breath in, customer service voice on."
            a ss open "We’re looking for some people and we were wondering if you could help us find them."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "We’re trying to meet up with some friends, but we don’t know the area too well."

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Layne adds, putting on an air of friendly confidence."

            a pain smile "{i} He’s always been a people person. Guess that hasn’t changed since back then."
            "The pair seem to relax a bit looking at his (seemingly) genuine smile, and offer small smiles of their own in return."
            "Seeing how easily he can deceive them sends knots into my stomach."
            a concern "{i} …He must’ve done the same with me back then. How could I never notice?"
            q "Oh! Not to worry, the village is quite small so we should be able to help find who you’re looking for. Who were you trying to find?"

            hide l_slightsmile
            show l_concern:
                yoffset 70
                xoffset 400

            "I pause, glancing nervously at Layne."
            "His face scrunches up in concern for a split second, before returning back to his cool demeanour."
            hide l_concern
            show l_slightsmile:
                yoffset 70
                xoffset 400

            a neutral"{i} I don’t know that person’s name, and by the looks of Layne’s face, he doesn’t seem to either. How do I go about describing them without seeming too suspicious?"

            menu:
                 "I’m looking for a woman with a blue-ish ponytail.":
                     a "She’s around my height?"

                     q "Oh, you’re looking for–"

                     "To my surprise, their voice cuts out, as if someone had muted a video."

                     hide l_slightsmile
                     show l_confused:
                         yoffset 70
                         xoffset 400
                     "I stare at Layne in confusion, but he also seems just as lost as I do."

                     hide l_confused
                     show l_neutral:
                         yoffset 70
                         xoffset 400
                     "The duo seems to look at us, waiting for confirmation. With no other option, I just nod in agreement."

                     a "Yes, that’s the one. Do you know where she is?"

                     q "Hmm, I think I saw her about a half hour ago? She was heading towards the forest to gather some red sage for her husband."
                     q "Not sure if she’s still there, but I remember my aunt saying red sage is hard to come by these days, so she’ll probably still be there."

                     "They point towards the edge of town towards the nearby forest."

                     a ss open "Ah, I see. Thank you so much!"

                     "With a smile, I wave them off, mentally making note of the direction to head in my mind."

                     hide l_neutral
                     show l_slightsmile_open:
                         yoffset 70
                         xoffset 400

                     l "I’m glad that worked out well. If we need to find her, then we’ll head towards the forest. For now, I think we should try to ask for more information."

                     hide l_slightsmile_open with Dissolve(1.0)

                     $ village_azari_true_location = True
                     $ village_azari_known = True
                     jump first_dream
                 "I'm looking for a woman who carries a basket with her":
                     "I motion with my hands."
                     a "It’s about this big, stained green in some areas?"

                     q "A...basket? Well a lot of people carry baskets with them, and the grass stains a lot of our belongings green, so that’s not too much to go off of."

                     "I feel my face drop."
                     a concern "{i} Was that description not enough?"

                     q "Oh, but if she’s carrying a basket, she might be going to gather some herbs or fruits? Most of the herbs we gather are over behind the village’s inn, while the fruits are over down south."

                     a ss open "Ah, I see. Thank you so much!"
                     "I wave them goodbye and they continue their jovial conversation."

                     l "Do you know what the woman was trying to get?"

                     a "Huh?"

                     l "The woman in your dream. Was she trying to get herbs or fruits?"

                     "I try to focus back on the details in my dream."
                     a neutral "She was trying to get…"

                     menu:
                         "...fruits.":
                             a "...fruits, I think."
                             a "{i} There was definitely something red in her basket. Berries, maybe?"

                             hide l_neutral
                             show l_slightsmile_open:
                                 yoffset 70
                                 xoffset 400

                             l "Got it. If we need to find her, then we’ll head south. For now, I think we should try to ask for more information."

                             hide l_slightsmile_open with Dissolve(1.0)

                             $ village_azari_known = True
                             $ village_azari_false_location = True
                             jump first_dream
                         "...herbs.":
                             a "Herbs. She had red sage in her basket, I remember that."
                             a "{i} It’s hard to get that image out of my head really."

                             hide l_neutral
                             show l_slightsmile_open:
                                  yoffset 70
                                  xoffset 400

                             l "Got it. If we need to find her, then we’ll head behind the inn. For now, I think we should try to ask for more information."

                             hide l_slightsmile_open with Dissolve(1.0)

                             $ village_azari_true_location = True
                             $ village_azari_known = True

                             jump first_dream
                 "I'm looking for someone who went near the cliff.":

                     show l_neutral with Dissolve(1.0):
                         yoffset 70
                         xoffset 400
                     a "There’s a particularly steep cliff somewhere in the forest. Does anyone usually go there?"
                     "The pair looks at each other in shock, practically offended by the question."

                     hide l_neutral
                     show l_awk:
                         yoffset 70
                         xoffset 400

                     q "No one in the village is stupid enough to go by a cliff, are you kidding?"

                     "I cringe at the hostility in their tone. Layne looks just as flustered."
                     a embarass "{i} Okay, so clearly that was a stupid question,, but was that {b}really{/b} necessary?"
                     "Seemingly sensing the awkwardness of their outburst, the villager gently slaps the other person's arm."

                     q "{i}Ahem{/i}, what I meant to say is that there isn’t anyone who really fits that description, but there's a couple forests with cliffs that you can try out. Sorry."

                     "With a quick bow of their head, the conversation ends, the awkward tension still spilling in the air."
                     "Layne and I thank them regardless, and walk away, leaving them back to their conversation that seems much less jovial than before."

                     a confused "What was wrong that time?"

                     hide l_awk
                     show l_awk_smile:
                         yoffset 70
                         xoffset 400

                     l "Um, well..."
                     l "Maybe the incident...has already happened? They seemed a little on edge."

                     "I feel my heart sink at his words."
                     a concern "{i} Yeah, that would make the most sense. So then it was all for nothing?"
                     a "{i} Then what are we supposed to do here?"
                     "Layne rests a hand on my arm, offering me a comforting smile."

                     hide l_awk_smile
                     show l_pain_smile:
                         yoffset 70
                         xoffset 400

                     l "...Well, we still don't know for sure. There’s more people we can ask for information to find out. Let’s go."
                     $ village_azari_known = True
                     $ village_azari_false_location = True
                     jump first_dream
        else:

            show l_slightsmile_open with Dissolve(1.0):
                yoffset 70
                xoffset 400
            l "Excuse me, could I ask you a few questions?"

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Like before, the two sitting in front of us stop their conversation at the sound of Layne’s voice and look up at us, confusion written on their face."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "I’m sorry to bother you. We’re looking for someone and we were wondering if you could help us find them? We don’t really know the area too well."

            q "Oh! Yeah, who were you trying to find?"

            l "His name is–"

            "But like with the other conversation from before, Layne’s voice cuts out upon saying the name."
            a confused "{i} Layne knows his name?"
            a "{i} Was he just pretending to be confused before?"
            "I try to push down that uncomfortable feeling bubbling in my throat."
            a concern "{i} How many things will he hide from me?"

            q "Well...Last I saw him he was waving his wife off from his house. I don’t think he would’ve left, not unless his wife had already returned home, and especially not if he was expecting you two to visit."
            q "His house is down the path. It’s the 3rd house on the right, but you can easily identify it by the Adonis flowers planted in front."

            hide l_slightsmile_open
            show l_pain_smile:
                yoffset 70
                xoffset 400

            l "Adonis flowers…"

            hide l_pain_smile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "Got it. Thank you so much for your help."

            q "No problem!"

            $ village_layne_location = True

            stop music fadeout 1.0

            play music "audio/storm.mp3" loop volume 0.2

            scene village_rain with Dissolve(2.0)
            hide l_slightsmile_open
            show l_shock_n with Dissolve(1.0):
                yoffset 70
                xoffset 400

            "A clap of thunder resounds over us."
            "I turn to Layne, fear written all over my face."
            l "Rain."

            q "Looks like a storm is coming in. You might want to hurry heading over to — house!"

            a shock open n "Wait!"
            "I cringe at my volume, but look at the villagers in earnest."
            a awk smile n "Does his wife have blue hair by any chance?"

            q "Uh, yeah, she does. Why do you ask?"

            a awk n "{i} Well, fuck. I didn't think this far ahead."
            a awk smile n "Ah, well, you know, I just..."

            hide l_shock_n
            show l_slightsmile_n:
                yoffset 70
                xoffset 400

            l "Haha, we just thought we might have seen her earlier, but we weren't completely sure. ---- has always gushed about his wife, but we've never been able to put a face to the name before."

            "They look slightly unconvinced, but luckily for us, they don’t question it."

            a concern n "{i} Layne’s gotten…too good at lying over these past years."

            q "That certainly sounds like —. Always talking about his wife."

            "Another clap of thunder, much closer this time, followed by a light drizzle of rain, patters on the ground all around us."

            q "Well, I hope you can find them before the storm hits!"

            "The pair gets up quickly and rushes off in the opposite direction, eager to avoid the storm soon approaching."

            jump post_village_imagemap

    label village_house:
        scene village

        if village_outfit == False:
            a neutral open"Excuse me, could I ask you a few questions?"
            "The pair in front of us stop their conversation and look down from the railing, their expressions warping from happy smiles to confusion to concern."
            q "Um, we’re not interested, sorry!"

            "They immediately whip around and shut the door, the slam echoing through the air."

            show l_awk with Dissolve(1.0):
                yoffset 70
                xoffset 400
            a confused "Come on, I'm wasn't {b} that {/b} rude, was I?"

            hide l_awk
            show l_shock:
                yoffset 70
                xoffset 400

            l "No, not at all!"
            "I stare in shock, before chuckling a little to myself."
            a pain smile "{i} I meant it as a joke, but seeing him vehemently deny it reminds me of high school."

            hide l_shock
            show l_awk_smile:
                yoffset 70
                xoffset 400

            l "Just…Maybe they thought we were scammers? It’s not like we really look like we belong here."

            "I look down at my outfit, then at Layne’s."
            "Although our styles seem a lot less novel in comparison to other styles, my face heats up as I’m suddenly aware of how crazy I must seem in comparison to the others."
            a embarass open"...Let’s go find more appropriate outfits then."
            jump first_dream
        elif village_azari_known == False:

            show l_slightsmile with Dissolve(1.0):
                yoffset 70
                xoffset 400
            a neutral open "Excuse me, could I ask you a few questions?"
            "The pair in front of us stop and look down, their expression warping from boisterous smiles to slight confusion."

            q "Oh, welcome! You two look like you're new here. What do you need?"

            "Although seemingly friendly, I can still detect a distinct sense of wariness from the two."

            a "{i} I gotta get them to trust us."
            a neutral closed "{i} Deep breath in, customer service voice on."
            a ss open "We’re looking for some people and we were wondering if you could help us find them."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "We’re trying to meet up with some friends, but we don’t know the area too well."

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Layne adds, putting on an air of friendly confidence."

            a pain smile "{i} He’s always been a people person. Guess that hasn’t changed since back then."
            "The pair seem to relax a bit looking at his (seemingly) genuine smile, and offer small smiles of their own in return."
            "Seeing how easily he can deceive them sends knots into my stomach."
            a concern "{i} …He must’ve done the same with me back then. How could I never notice?"
            q "Well, good news then, the village is quite small so we should be able to help find who you’re looking for. Who were you trying to find?"

            "I pause, glancing nervously at Layne."

            hide l_slightsmile
            show l_concern:
                yoffset 70
                xoffset 400
            "His face scrunches up in concern for a split second, before returning back to his cool demeanour."

            hide l_concern
            show l_slightsmile:
                yoffset 70
                xoffset 400
            a neutral "{i} I don’t know that person’s name, and by the looks of Layne’s face, he doesn’t seem to either. How do I go about describing them without seeming too suspicious?"

            menu:
                 "I’m looking for a woman with a blue-ish ponytail.":
                     a "She’s around my height?"

                     q "Oh, you’re looking for–"

                     "To my surprise, their voice cuts out, as if someone had muted a video."

                     hide l_slightsmile
                     show l_confused:
                         yoffset 70
                         xoffset 400

                     "I stare at Layne in confusion, but he also seems just as lost as I do."

                     hide l_confused
                     show l_neutral:
                         yoffset 70
                         xoffset 400

                     "The duo seems to look at us, waiting for confirmation. With no other option, I just nod in agreement."

                     a "Yes, that’s the one. Do you know where she is?"

                     q "Hmm, I think I saw her about a half hour ago? She was heading towards the forest to gather some red sage for her husband."
                     q "Not sure if she’s still there, but I remember my aunt saying red sage is hard to come by these days, so she’ll probably still be there."

                     "They point towards the edge of town towards the nearby forest."

                     a ss open "Ah, I see. Thank you so much!"

                     "With a smile, I wave them off, mentally making note of the direction to head in my mind."

                     hide l_neutral
                     show l_slightsmile_open:
                         yoffset 70
                         xoffset 400

                     l "I’m glad that worked out well. If we need to find her, then we’ll head towards the forest. For now, I think we should try to ask for more information."

                     hide l_slightsmile_open with Dissolve(1.0)

                     $ village_azari_true_location = True
                     $ village_azari_known = True
                     jump first_dream
                 "I'm looking for a woman who carries a basket with her":
                     "I motion with my hands."
                     a "It’s about this big, stained green in some areas?"

                     q "A...basket? Well a lot of people carry baskets with them, and the grass stains a lot of our belongings green, so that’s not too much to go off of."

                     "I feel my face drop."
                     a concern "{i} Was that description not enough?"

                     q "Oh, but if she’s carrying a basket, she might be going to gather some herbs or fruits? Most of the herbs we gather are over behind the village’s inn, while the fruits are over down south."

                     a ss open "Ah, I see. Thank you so much!"
                     "I wave them goodbye and they continue their jovial conversation."

                     l "Do you know what the woman was trying to get?"

                     a confused "Huh?"

                     l "The woman in your dream. Was she trying to get herbs or fruits?"

                     "I try to focus back on the details in my dream."
                     a neutral "She was trying to get…"

                     menu:
                         "...fruits.":
                             a "...fruits, I think."
                             a "{i} There was definitely something red in her basket. Berries, maybe?"

                             l "Got it. If we need to find her, then we’ll head south. For now, I think we should try to ask for more information."

                             hide l_slightsmile with Dissolve(1.0)
                             hide l_slightsmile_open with Dissolve(1.0)


                             $ village_azari_known = True
                             $ village_azari_false_location = True
                             jump first_dream
                         "...herbs.":
                             a "Herbs. She had red sage in her basket, I remember that."
                             a "{i} It’s hard to get that image out of my head really."


                             l "Got it. If we need to find her, then we’ll head behind the inn. For now, I think we should try to ask for more information."

                             hide l_slightsmile_open with Dissolve(1.0)

                             $ village_azari_true_location = True
                             $ village_azari_known = True
                             jump first_dream
                 "I'm looking for someone who went near the cliff.":

                     show l_neutral with Dissolve(1.0):
                         yoffset 70
                         xoffset 400
                     a "There’s a particularly steep cliff somewhere in the forest. Does anyone usually go there?"
                     "The pair looks at each other in shock, practically offended by the question."

                     hide l_neutral
                     show l_awk:
                         yoffset 70
                         xoffset 400

                     q "No one in the village is stupid enough to go by a cliff, are you kidding?"

                     "I cringe at the hostility in their tone. Layne looks just as flustered."
                     a embarass "{i} Okay, so clearly that was a stupid question,, but was that {b}really{/b} necessary?"
                     "Seemingly sensing the awkwardness of their outburst, the villager gently slaps the other person's arm."

                     q "{i}Ahem{/i}, what I meant to say is that there isn’t anyone who really fits that description, but there's a couple forests with cliffs that you can try out. Sorry."

                     "With a quick bow of their head, the conversation ends, the awkward tension still spilling in the air."
                     "Layne and I thank them regardless, and walk away, leaving them back to their conversation that seems much less jovial than before."

                     a confused "What was wrong that time?"

                     hide l_awk
                     show l_awk_smile:
                         yoffset 70
                         xoffset 400

                     l "Um, well..."
                     l "Maybe the incident...has already happened? They seemed a little on edge."

                     "I feel my heart sink at his words."
                     a concern "{i} Yeah, that would make the most sense. So then it was all for nothing?"
                     a "{i} Then what are we supposed to do here?"

                     hide l_awk_smile
                     show l_pain_smile:
                         yoffset 70
                         xoffset 400
                     "Layne rests a hand on my arm, offering me a comforting smile."

                     l "...Well, we still don't know for sure. There’s more people we can ask for information to find out. Let’s go."

                     hide l_pain_smile with Dissolve(1.0)

                     $ village_azari_known = True
                     $ village_azari_false_location = True
                     jump first_dream
        else:
            show l_slightsmile_open with Dissolve(1.0):
                yoffset 70
                xoffset 400
            l "Excuse me, could I ask you a few questions?"

            hide l_slightsmile_open
            show l_slightsmile:
                yoffset 70
                xoffset 400

            "Like before, the two sitting in front of us stop their conversation at the sound of Layne’s voice and look up at us, confusion written on their face."

            hide l_slightsmile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "I’m sorry to bother you on your walk. We’re looking for someone and we were wondering if you could help us find them? We don’t really know the area too well."

            q "Oh! Yeah, who were you trying to find?"

            l "His name is–"

            "But like with the other conversation from before, Layne’s voice cuts out upon saying the name."
            a confused "{i} Layne knows his name?"
            a "{i} Was he just pretending to be confused before?"
            "I try to push down that uncomfortable feeling bubbling in my throat."
            a concern "{i} How many things will he hide from me?"

            q "Well...Last I saw him he was waving his wife off from his house. I don’t think he would’ve left, not unless his wife had already returned home, and especially not if he was expecting you two to visit."
            q "His house is down the path. It’s the 3rd house on the right, but you can easily identify it by the Adonis flowers planted in front."

            hide l_slightsmile_open
            show l_pain_smile:
                yoffset 70
                xoffset 400

            l "Adonis flowers…"

            hide l_pain_smile
            show l_slightsmile_open:
                yoffset 70
                xoffset 400

            l "Got it. Thank you so much for your help."

            q "No problem!"

            $ village_layne_location = True

            stop music fadeout 1.0

            play music "audio/storm.mp3" loop volume 0.2

            scene village_rain with Dissolve(2.0)

            hide l_slightsmile_open
            show l_shock_n with Dissolve(1.0):
                yoffset 70
                xoffset 400

            "A clap of thunder resounds over us."
            "I turn to Layne, fear written all over my face."
            l "Rain."

            q "Looks like a storm is coming in. You might want to hurry heading over to — house!"

            a shock open n "Wait!"
            "I cringe at my volume, but look at the villagers in earnest."
            a awk smile n "Does his wife have blue hair by any chance?"

            q "Uh, yeah, she does. Why do you ask?"

            a awk n "{i} Well, fuck. I didn't think this far ahead."
            a awk smile n "Ah, well, you know, I just..."

            hide l_shock_n
            show l_slightsmile_open_n:
                yoffset 70
                xoffset 400

            l "Haha, we just thought we might have seen her earlier, but we weren't completely sure. ---- has always gushed about his wife, but we've never been able to put a face to the name before."

            "They look slightly unconvinced, but luckily for us, they don’t question it."

            a concern n "{i} Layne’s gotten…too good at lying over these past years."

            q "That certainly sounds like —. Always talking about his wife."

            "Another clap of thunder, much closer this time, followed by a light drizzle of rain, patters on the ground all around us."

            q "Well, I hope you can find them before the storm hits!"

            "The pair gets up quickly and rushes inside, eager to avoid the storm soon approaching."

            jump post_village_imagemap

    label laundry:
        scene village

        show l_neutral with Dissolve(1.0):
            yoffset 70
            xoffset 400

        "I glance at the basket of laundry outside of one of the houses, and walk towards it."
        "Layne trails behind me, obviously confused by my actions, but I pay him no mind and begin rummaging through the basket."

        hide l_neutral
        show l_shock:
            yoffset 70
            xoffset 400

        l "Wh–WAIT, what are you {i}doing{/i}?"

        a neutral "Getting us more appropriate outfits. Now shut up and put this on."
        "I toss a cloak in his direction and grab another one for myself."
        a "{i} Not the most ideal, but it’s the best we can do."

        "Layne stares at me shellshocked, various noises of confusion escaping his throat, before he finally sighs and puts the cloak on, glancing nervously around."

        a pain smile "If it really makes you feel that bad, we'll return it after we figure out what's going on."

        hide l_shock
        show l_pain_smile:
            yoffset 70
            xoffset 400

        l "I...yes, thank you."

        hide l_pain_smile
        show l_concern:
            yoffset 70
            xoffset 400

        "With that resolved (kind of, Layne's still looking around worried that someone saw him) I look back around the town for more information."

        $ village_outfit = True

        hide l_concern with Dissolve(1.0)

        jump first_dream
    label post_village_imagemap:

        hide l_slightsmile_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        l "The storm is about to start…This really might be the day we have to look out for."

        a neutral closed n "{i}Knowing{/i} that doesn’t help us at all, Layne. How are we supposed to stop this?"


        l "Well…"

        "Layne trails off, equally as panicked about what to do."

        a concern n "{i} Is he really unsure, or is this an act too?"
        "I rub my temples in frustration."
        a neutral closed n "{i} God, I shouldn't doubt him when we have more important things to worry about. I'm the one that told him to wait until after everything to clear things up."
        a pain smile n "...Sorry. I was overwhelmed, but that wasn’t fair of me to snap at you for that."

        hide l_concern_n
        show l_shock_blush_open_n:
            yoffset 70
            xoffset 400

        l "Oh-er-well-it’s okay! You don’t have to apologize for that."

        hide l_shock_blush_open_n
        show l_embarass_lookaway_n:
            yoffset 70
            xoffset 400

        a"{i} Same old Layne, never able to stand up for himself. I really need to fix that."
        a concern n "{i}…If we can even talk normally after this situation. What if he just avoids me again?"
        "I shake my head, willing myself not to dwell on that, instead trying to think about all of the information I have on hand."

        hide l_embarass_lookaway_n
        show l_neutral_n:
            yoffset 70
            xoffset 400

        a neutral n "{i} We know the woman I’m looking for should be near a cliff, and we know where the man Layne is looking for should be."
        a "{i} If we’re just at the beginning of the storm, we should have enough time to find one of them."
        "As if to solidify my plans, the droplets of rain start to increase in speed."

        hide l_neutral_n
        show l_shock_n:
            yoffset 70
            xoffset 400
        a "Layne, you go find the man from your dreams. I’ll go find the woman from my dreams. If we both tell them what happens, maybe we can intercept this."

        hide l_shock_n
        show l_shock_open_n:
            yoffset 70
            xoffset 400

        l "No!"

        hide l_shock_open_n
        show l_shock_n:
            yoffset 70
            xoffset 400

        a confused n "His sharp tone of voice cuts through the air suddenly."

        hide l_shock_n
        show l_embarass_lookaway_n:
            yoffset 70
            xoffset 400

        l "Or, well–sorry I didn’t mean to be that loud–I just–"

        hide l_embarass_lookaway_n
        show l_embarass_awk_n:
            yoffset 70
            xoffset 400

        l "I don’t think we should split up. Either of us could just as easily get caught up in the rain and get hurt."

        hide l_embarass_awk_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        l "Especially with your dream at the end…"
        l "I know it’s smartest to cover all bases, but I don’t want to risk it."
        l "{size=-10}Not with you."

        a concern n "{i}…I can’t say he doesn’t have a point. It’s not as if I’m not worried about what will happen if I go alone."
        a "{i} But is my fear worth it? What if that woman dies again?"

        menu:
            "Find the man from Layne’s dream first.":
                a neutral closed n "...Alright. We’ll go try to find the one from your dream then. If we warn him earlier on, maybe he’ll be able to find that woman quicker than we could."

                hide l_concern_n
                show l_neutral_n:
                    yoffset 70
                    xoffset 400

                l "You have a point. Then, let’s go."

                "The two of us walk towards the door, our steps heavy, yet careful from the growing slipperiness of the ground around us."
                "With three sharp knocks on the door, Layne lets his hand fall. A distant “coming!” rings out from inside, and we huddled together under the makeshift portico."
                "Suddenly faced inches away from Layne, I feel myself grow self-conscious at our distance."
                "Layne, on the other hand, simply stared straight forward, unperturbed by our sudden closeness."
                a embarass n "{i} Could this guy come to the door any quicker?"
                "The seconds seemed to stretch on forever, until finally the door swung open."

                hide l_neutral_n with Dissolve(1.0)

                show l_neutral_n with Dissolve(1.0):
                    yoffset 70
                    xoffset 100

                show villager_L with Dissolve(1.0):
                    yoffset 70
                    xoffset 700


                q "It’s about time you’re back, glad you didn’t–Oh!"

                "The man starts but immediately cuts himself off upon making eye contact with us."
                "…Or at least, what I assume is eye contact given that his face is similarly blurred like the rest of the villagers."

                q "I’m sorry, I thought you were someone else. Who might you two be?"

                hide l_neutral_n
                show l_slightsmile_open_n:
                    yoffset 70
                    xoffset 100

                l "Hi, we’re sorry to bother you, but we’re friends of some of the people in this village."
                l "We just wanted to let you know that a lot of people haven’t seen your wife in a while and we were planning to go check up on her with the storm and all. Would you mind coming with us?"

                "Just as before, Layne smoothly talks his way through, not even a hint of insincerity in his tone."
                "I can’t help but feel a pit form in my stomach."
                "The man pauses for a bit, skeptical of our intentions. It doesn’t take long for his apparent worry towards his wife to outweigh the suspicion he has towards us."

                q "Yeah…! Yeah. Let’s go."

                hide l_slightsmile_open_n
                show l_neutral_n:
                    yoffset 70
                    xoffset 100

                hide villager_L with Dissolve(0.5)
                show villager_L with Dissolve(0.5):
                    yoffset 70
                    xoffset 700
                "He quickly grabs something I don’t immediately recognise and holds it over the three of our heads, to protect us from the oncoming rain."
                "…Well, protecting us as best as it can."
                "The covering (which I quickly realise is an umbrella) seems to be a relatively big piece of animal skin, but it’s nowhere near big enough to comfortably fit all of us under."

                hide l_neutral_n with Dissolve(0.5)
                show l_neutral_n with Dissolve(0.5):
                    yoffset 70
                    xoffset 50
                "Layne seems to take notice of this and stands more off to the side, leaving the man and I to be more shielded from the rain as we speed-walk towards the forest as best as we can."


                menu:
                    "Do nothing":
                        a "{i} Sorry Layne, we don’t really have the time to waste on trying to figure out how to be most comfortable here."

                    "Pull Layne closer to the umbrella":
                        a "{i} Trying to switch spots with him probably would delay us more than we need."

                        hide l_neutral_n
                        show l_confused_n:
                            yoffset 70
                            xoffset 50
                        "I tug on his sleeve gently to alert him, then pull him closer by the sleeve."

                        hide l_confused_n with Dissolve(0.5)
                        show l_slightsmile_n with Dissolve(0.5):
                            yoffset 70
                            xoffset 100

                        "It doesn’t end up being by much, and Layne’s right shoulder ends up being mostly out of the umbrella anyways, but Layne shoots me a smile at the sentiment."

                        hide l_slightsmile_n
                        show l_neutral_n:
                            yoffset 70
                            xoffset 100
                        $ layne_affection += 1


                if village_azari_true_location:
                    "As we walk, we pass by and walk behind the inn."
                    jump after_village_investigation

                else:

                    "As we walk, we pass by and walk behind the inn."
                    a confused n "{i}The inn? The forest behind here had herbs if I remember correctly..."
                    "Bile seems to rise in my throat at the realization."
                    a concern n "{i} Thank god we asked him to go with us then."
                    jump after_village_investigation

                label after_village_investigation:
                    "The rain seems to pour down harder and harder with each step, getting increasingly harder and harder to see."

                    scene forest_rain with Dissolve(2.0)

                    show l_neutral_n with Dissolve(1.0):
                        yoffset 70
                        xoffset 100
                    show villager_L with Dissolve(1.0):
                        yoffset 70
                        xoffset 700

                    play sound "audio/walking.mp3" volume 0.5

                    "The smell of wet earth and mud floods my senses, and I catch myself slipping a couple times. Layne and the man follow similar fates."
                    "Every once in a while, the man opens his mouth to shout something. Probably her name, but the sound is lost on me."
                    a neutral open n "Can you hear me?"

                    hide l_neutral_n
                    show l_neutral_open_n:
                        yoffset 70
                        xoffset 100

                    l "Hello?"

                    "Layne and I both try to help, but ten minutes turn to twenty, and then thirty."
                    "The uncomfortable feeling in my stomach tightens all the way to my throat. My limbs feel heavy and each step seems to thunder over the pouring rain."
                    "Eventually we get to a familiar path. One that I saw in my dreams."


                    "I rip myself away from the group and run towards the ledge I feel off once before. My chest begins to throb as I inch closer and closer to the ledge."

                    scene black with Dissolve(0.3)
                    "Just as I’m about to look over, my vision turns dark as a weight settles onto my eyes."

                    a "Huh–?"

                    l "Don’t look."

                    "Layne’s voice fills my ears, strained and coarse. Another set of footsteps pad up towards us, before making a sudden stop."
                    "The silence that follows is almost deafening."
                    a "{i} No…it can’t be."

                    play sound "audio/running.mp3" volume 0.5

                    "Heavy, hurried footsteps pass by us, the soft earth squelching under each step."

                    jump village_azari_death

                    label village_azari_death:
                        "I reach up my hands to push away Layne’s to see what’s going on–to confirm my fears, but his hands remain steadfast over my eyes."

                        a concern n "Layne, let go."

                        "My voice trembles."

                        l "...No. You don’t need to see this twice."

                        a "{b} Layne."

                        "His hands falter in strength for a moment."
                        "A moment is all I need."

                        scene villager_A_death with hpunch
                        scene black with Dissolve(0.5)

                        "My breath catches in my throat at the sight, and I immediately shut my eyes again."
                        a "{i} Fuck."
                        "Even in that split second, the image ingrains itself into my mind."
                        "There she lays in a pool of her own blood unmoving, the man clutching her in his arms."
                        "That damn basket near her arm, the red sage spilling out into her blood."

                        play music "audio/storm.mp3" loop volume 0.2
                        scene forest_rain with Dissolve(3.0)


                        show l_pain_smile_n with Dissolve(1.0):
                            yoffset 30
                            xoffset 100
                            zoom 1.5

                        "I catch sight of Layne’s face. His pained expression probably mirrors my own."
                        a concern n "{i}What could we have done differently? How could we have saved her?"
                        "Hundreds of different choices flood my brain. I only feel worse."
                        "Layne rests a hand on my shoulder for comfort. Whether it’s meant for him or me, I’m not sure,  but as we gaze at each other, it’s clear that it’s not helping either of us."
                        "The loud wails of a grieving man are the only sounds echoing through."

                        play sound "audio/bell.mp3" volume 0.5

                        stop music

                        scene white with Dissolve(1.0)
                        scene black with Dissolve(3.0)
                        scene bridge_night_blur with Dissolve(1.0)

                        "…"
                        "I find myself back on the bridge."

                        scene bridge_night with Dissolve(1.0)
                        play music "audio/Memories_Sappheiros.mp3" fadein 1.0 loop volume 0.08

                        "Alone. The sun has set over me."
                        a pain smile n "{i} Ah…I never made it to work, did I?"
                        "My limbs feel lethargic. The dull warmth on my shoulder from where Layne’s hand once rested fades away–too quickly for my liking."
                        a concern n "{i} Layne…where is he?"
                        "I chuckle bitterly to myself."
                        a pain smile n "{i} Looks like nothing’s going right today."
                        "My lungs feel like lead in my chest as guilt eats me up from the inside out. I grip onto the railings, my legs no longer supporting my weight."
                        "I don’t know how long I sat there for."

                        l "Azari!"

                        show l_shock_n with Dissolve(0.5):
                            yoffset 30
                            xoffset 100
                            zoom 1.5
                        l "Thank god you’re still here. I half thought I dreamt up that whole scenario again."



                        "He kneels down next to me, placing a hand on my shoulder again, much like how he did when…"

                        a "{i} When we saw…"

                        hide l_shock_n
                        show l_concern_n:
                            yoffset 30
                            xoffset 100
                            zoom 1.5

                        l "..."

                        a "Wh–!"

                        #layne + azari hug cg v.1 (azari eyes wide, not hugging back)

                        "Warm arms wrap around my form. I try to turn my head to look towards Layne, but his face is buried into my shoulder."

                        l "Sorry for doing this without asking. If you don’t like it, I’ll stop, it’s just…"
                        l "This was the first thing I thought of to do to comfort you. I know that was an awful experience."

                        "A small part of me flames up in response to that. It screams that I should push him away and demand for answers. About how he's so calm, why he came back, why he’s still here."
                        "Why he still cares after leaving me without a word all those years ago."

                        #layne + azari hug cg v.2 (azari eyes closed, hugging back)

                        "Instead, I reach up to hug him back, releasing a heavy sigh and a few sniffles. Layne only rubs my back in response, muttering “It’s okay” over and over again softly under his breath."
                        "Eventually I pull away, feeling my cheeks heat up in embarrassment."
                        a embarass n "I…Ahem, thank you. I, uh, think it’s time to talk now. About everything."

                        jump out_village_explanation


            "Find the woman from my dream first.":
                a neutral n "...Alright. We’ll go try to find the woman from my dream then. We know which way we’re supposed to go, so it’s simpler to try to find her on our own."

                l "You have a point. Then, let’s go."

                if village_azari_false_location:
                    "The two of us head south, our steps heavy, yet careful from the growing slipperiness of the ground around us."

                    scene wrong_forest with Dissolve(1.0)

                    show l_concern with Dissolve(0.5):
                        yoffset 70
                        xoffset 400

                    "Eventually, we reach a forest clearing that upon looking at, is distinctly off."

                    a neutral "{i} There’s a lot more greenery here than I remember in my dream. It almost feels as if it's a different season."
                    a "{i} Are we in the wrong place? Or does it change if we go deeper in?"

                    menu:
                        "Turn back":
                            a concern"I don’t think this is the right place."

                            l "It doesn’t look the same in your memories either, huh? Do you think we need to go deeper though?"

                            a neutral "No, I don’t have a good feeling about this. We need to go back."

                            play sound "audio/walking.mp3" volume 0.5

                            jump saving_village_azari

                        "Go deeper in":
                            hide l_concern with Dissolve(0.5)
                            show l_concern with Dissolve(0.5):
                                zoom 1.5
                                yoffset 70
                                xoffset 100
                            "The rain seems to pour down harder and harder with each step, getting increasingly harder and harder to see."
                            "The smell of wet earth and mud floods my senses, and I catch myself slipping a couple times. Layne follows a similar fate, so we end up holding onto each other’s arms for stability."

                            a neutral open "Hello? Can you hear me?"

                            l "Is anybody out there?"

                            "Layne and I both try to help, but ten minutes turn to twenty, and then thirty."
                            "The more we traverse, the less familiar the path gets."
                            "Dread sets down in my stomach and all the way to my throat. My limbs feel heavy and each step seems to thunder over the pouring rain."

                            a concern "...I think we went the wrong way."

                            l "...I think so too."

                            "The two of us immediately rush back, praying that we still have time to make it. My legs burn from our pace, but that feels like a dull ache compared to the fear set in my heart."

                            scene forest_rain with Dissolve(1.0)
                            show l_concern_n with Dissolve(0.5):
                                yoffset 70
                                xoffset 400
                            "Eventually we get to a familiar path. One that I saw in my dreams."
                            "Layne seems to recognise it too, coming to a sudden stop."
                            "Distant, yet distinct sobs echo through the air. I freeze in place."

                            a  "{i} No…"

                            "I rip myself away from him and run towards the ledge I fell off once before. My chest begins to throb as I step closer and closer to the ledge, the cries getting louder and louder."

                            scene black with Dissolve(0.3)
                            "Just as I’m about to look over, my vision turns dark as a weight settles onto my eyes."

                            a shock open n "Huh–?"

                            l "Don’t look."

                            "Layne’s voice fills my ears, strained and riddled with fear. Despite being right next to me, I can barely hear him over the pouring rain and painful weeping."

                            a concern n "{i} No…it can’t be."

                            jump village_azari_death
                else:
                    jump saving_village_azari

    label saving_village_azari:
        scene black with Dissolve(1.0)
        scene forest with Dissolve(1.0)

        a neutral open n "Hello? Can you hear me?"

        hide l_concern_n
        show l_neutral_open_n:
            yoffset 70
            xoffset 400

        l "Is anybody out there?"

        "The rain seems to pour down harder and harder with each step, getting increasingly harder and harder to see."
        "The smell of wet earth and mud floods my senses, and I catch myself slipping a couple times. Layne follows a similar fate, so we end up holding onto each other’s arms for stability."

        hide l_neutral_open_n
        show l_shock_n:
            yoffset 70
            xoffset 400

        q "Is there someone there?"

        a shock open n "!!"
        a "Stay where you are!"

        "Layne and I rush over in the direction of her voice. I can hear my heart beat wildly in my chest."

        a concern n "{i} Please don’t move. Please be safe."

        hide l_shock_n with Dissolve(1.0)

        show villager_A with Dissolve(1.0):
            zoom 0.75
            yoffset 70
            xoffset 700


        show l_concern_n with Dissolve(1.0):
            zoom 1.5
            yoffset 70
            xoffset -100


        a "{i} !!"
        a "{i} There she is!"
        a "Hey!"

        "She turns around with an arm over her forehead to see Layne and us barreling towards her and instinctively begins to move toward us."
        "The ground beneath her feet seems to cave in."

        a shock open n "{i} No!"

        q "Huh–?!"

        hide l_concern_n
        show l_shock_n:
            zoom 1.5
            yoffset 70
            xoffset -100

        a "{i} No, no, no, she can’t die here!"

        hide l_shock_n with Dissolve(1.0)
        hide villager_A with Dissolve(0.5)
        show villager_A with Dissolve(0.5):
            zoom 1.5
            yoffset 70
            xoffset -275

        "I use every bit of strength I have left to pump my legs forward as fast as I can."
        "I reach out a hand, trying to grab an arm or anything."
        "My fingertips brush against her forearm."
        a "{i} Please…!"
        "I stretch out my arm as far as I possibly can."
        "And I manage to grab her forearm and pull her up, but the momentum still has me barreling forward."
        a concern n "{i} Shit."

        scene black with Dissolve(0.5)

        "I shut my eyes, bracing for impact."
        a neutral closed n "{i} Is this really how I’m going to die?"
        "But an arm wraps around my waist and roots me in place, knocking the air out of my lungs."

        scene forest_rain with hpunch

        "My eyes snap open from the force. I gasp for breath, expecting to be met with the ground, but I am greeted by a tree and the end of the ledge beneath my feet."
        "Suddenly aware of the arm at my waist, I whip my head around."

        show l_shock_n with Dissolve(0.5):
            zoom 1.5
            yoffset 70
            xoffset 100

        show villager_A with Dissolve(1.0):
            yoffset 70
            xoffset 700

        q "Are you okay?"

        hide l_shock_n
        show l_pain_smile_n:
            zoom 1.5
            yoffset 70
            xoffset 100

        "I merely stare at Layne. His face melts into pure relief."

        a shock open n "I’m…yeah I’m fine. Thanks Layne."

        show villager_A:
            yoffset 70
            xoffset 700
            linear 0.090 xoffset 710
            linear 0.090 xoffset 690
            linear 0.090 xoffset 700

        hide l_pain_smile_n with Dissolve(1.0)
        show l_pain_smile_n with Dissolve(1.0):
            yoffset 70
            xoffset 100
        "I pull myself back up with Layne’s help and take deep breaths, hoping to soothe the hammering of my heart."

        a concern n "Are you okay?"

        "The woman looks at me shocked, almost as if she forgot that {i}she{/i} was the one originally in danger."

        q "“I’m perfectly okay, thanks to you! Thank you…uh…?"

        "She trails off, looking expectantly at me."
        a confused n "{i}…? "
        a neutral n "{i} Oh."
        a "Oh, I’m—"

        q "—, are you there?!"

        "A sharp, concern-filled voice cuts through the air, followed by the heavy thud of boots splashing through the mud puddles."

        hide l_pain_smile_n with Dissolve(0.5)
        hide villager_A with Dissolve(0.5)

        show l_shock_n with Dissolve(0.2):
            yoffset 70
            xoffset -100

        show villager_A with Dissolve(0.2):
            yoffset 70
            xoffset 300

        show villager_L with Dissolve(0.2):
            yoffset 70
            xoffset 850

        "A figure soon emerges from among the dense forestry. They seem to spot our group, only pausing momentarily before barrelling over."
        "The cane in his hand is thrown to the side when he arrives, falling off the ledge where I once was. It doesn’t seem to bother him as he goes to envelope the woman in his arms."

        q "Thank God you’re okay…You weren’t back after so long, I feared the worst."

        q "I’m okay, don’t worry. These people were just accompanying me on my way back."

        "The woman looks over his shoulder to glance at the two of us, pressing an index finger to her lips in secrecy. Layne and I look at each other with a knowing glance."

        hide l_shock_n
        show l_awk_smile_n:
            yoffset 70
            xoffset -100

        a awk smile n "{i} Looks like she doesn’t want him to know…"

        stop music fadeout 2.0
        "The storm begins to die down. Rain still falls from the sky, but it’s no longer intense or filled with heavy winds."

        a pain smile n"{i} How convenient."
        "Finally, as if just aware of our presence, the man quickly turns to us, bowing his head down."

        q "I’m sorry for completely disregarding you both there, I was just…"

        hide l_awk_smile_n
        show l_neutral_n:
            yoffset 70
            xoffset -100

        q "...No matter. Thank you for accompanying her during this storm. If you need to warm up, you’re more than welcome to stop by our house and I’ll prepare something for you two."

        hide villager_A
        show villager_A:
            yoffset 70
            xoffset 300
            linear 0.090 xoffset 305
            linear 0.090 xoffset 295
            linear 0.090 xoffset 300
        q "{i}I’ll{/i} prepare something. You need to rest, it’s already bad enough you ran all the way out here on your own, and barely covered at that!"

        "The man brings his hand up behind his neck in embarrassment at his wife’s scolding tone."
        "They bicker (well, more like she lectures him about straining himself in the cold for a little bit longer) before turning to us once again."

        q "He is right though, you two should dry off at our house. You’re not from around here, are you? You can head out once the storm has passed, and after warming up."

        hide l_neutral_n
        show l_awk_n:
            yoffset 70
            xoffset -100

        "Unsure of how to respond, I glance at Layne. He seems to be apprehensive about the idea and fidgets with his necklace for a while."

        "A necklace that is painfully familiar to me."

        a pain smile n "{i}That necklace...he still has it."

        "After long deliberation, he turns to the couple."

        hide l_awk_n
        show l_slightsmile_n:
            yoffset 70
            xoffset -100

        l "Thank you for the offer, but we’ll have to be going now. The rain seems to be dying down anyways, so we should be fine."

        "He puts on a polite smile and a respectful tone, but I can tell that he’s trying to place distance between himself and the couple. The woman appears to notice it too."

        "Her posture falls a bit at the rejection, but she doesn’t push it. Her smile quickly returns to her tone."

        q "Alright, we won’t get in your way then. If you do end up needing anything, our house is close to the end of town. You can stop by anytime."

        q "...Thank you for everything."

        "The woman brightly smiles at us. Her husband also smiles, albeit a little awkwardly, and they both wave before turning away and walking off, the slight chatter fading out as they get further and further away."

        hide villager_A with Dissolve(0.5)
        hide villager_L with Dissolve(0.5)

        "I can’t help but smile back at the sight."

        hide l_slightsmile_n with Dissolve(1.0)
        show l_concern_n with Dissolve(0.5):
            yoffset 70
            xoffset 400
            linear 0.090 xoffset 405
            linear 0.090 xoffset 395
            linear 0.090 xoffset 400

        l "Haah..."



        "A loud sigh escapes from Layne and I see a fast movement out of the corner of my eye."
        "I whip my head around to my left to determine the source, only to see Layne squatting on the ground, his palms resting on the sides of his head."

        a concern n "You okay?"

        "Layne only glares at me in response."

        hide l_concern_n
        show l_pain_smile_n:
            yoffset 70
            xoffset 400

        l "You cannot seriously be asking me that."

        a awk smile n "…"

        l "…"

        hide l_pain_smile_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        "Another loud sigh escapes him, and he buries his face into his knees."
        "My heart twinges a little. I crouch down to Layne’s level and pat his back, filled with the need to comfort him."

        a ss open n "C’mon, was that too much exercise for you? Thought you would’ve gotten better with that over the years."

        "I try to joke, but my voice falters a bit. My hands still shake from the incident, and my chest burns."

        a concern n "{i} I could’ve…"

        "A small snort cuts me out of my thoughts."

        hide l_concern_n
        show l_awk_smile_closed_n:
            yoffset 70
            xoffset 400

        l "Bakery work isn’t exactly intensive. You really think I would go out of my way to exercise? I’d die before I’d make it to 10 minutes."

        a ss open n "Well, that’s still a whole 5 minutes longer than in high school. Maybe you have improved."

        "Layne lets out an unimpressed groan, and I let out a small laugh at his annoyance."

        a pain smile n "{i} …Yeah. This is how it should’ve been."

        hide l_awk_smile_closed_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        l "{size=-10} Please don’t ever do something like that again."

        a confused n "What’d you say?"

        hide l_concern_n
        show l_neutral_n:
            yoffset 70
            xoffset 400

        "Layne’s head snaps up and he intensely looks me in the eyes."

        hide l_neutral_n
        show l_neutral_open_n:
            yoffset 70
            xoffset 400

        l "I said–"

        play sound "audio/bell.mp3" volume 0.5

        scene white
        $ renpy.pause(1.5, hard=True)

        scene black with Dissolve(1.0)

        scene bridge_night_blur with Dissolve(1.0)

        a neutral closed n "{i}This…really has to stop happening."
        "I let my eyes adjust to my surroundings, the afterimages spotting through my vision, tingling my eyes."

        scene bridge_night with Dissolve(1.0)

        "To my surprise, I find myself back on the bridge, the cool evening air breezing past me."

        play music "audio/Bloom_Onycs.mp3" fadein 1.0 loop volume 0.08

        a shock open n "{i} Wait…evening–?"

        "I fish out my phone from my pocket and check the time."

        show lockscreen_night at truecenter with Dissolve(1.0)

        a "{i}7:24?! There’s no way I was actually gone that long."
        a "{i}And I missed work too…Alexandre’s going to be pissed about that."

        hide lockscreen_night with Dissolve(1.0)

        "I bury my head in my hands, groaning at the thought."

        a concern n "{i} God, I hope he doesn’t make me reorganize the classic literature shelf again…"

        "The bridge around me is silent, save for the gentle waves rippling on the side."
        "…Almost too silent."
        "I look around, realizing I’m the only one on the bridge."

        a confused n "{i} Where’s Layne?"
        "My hand reaches towards my pocket once more to grab my phone."

        a pain smile n "{i} But…it’s not like I can contact him anyways. He changed numbers."

        a "{i}And even if I could, what would I say? ‘Hey, remember how we just got teleported into that one village place and saved someone from dying? Crazy right?’ What if this never actually even happened?"

        "I shake my head in place."

        a concern n "{i}You’re spiraling again. Focus on what you know first."

        a neutral n "{i} You were heading into work before you saw Layne, and then you somehow transported into that one village place."

        a concern n "{i} …Maybe I need to take less hours at work."

        q "Azari!"

        "I snap my head over towards the voice."

        show l_concern_n with Dissolve (0.3):
            zoom 0.75
            yoffset 70
            xoffset 200

        l "Thank god you’re still here. I half thought I dreamt up that whole scenario again."

        a shock open n "Layne…"

        "I can barely make a sound."

        "He quickly makes his way over to me, huffing and puffing as he finally settles next to me."

        hide l_concern_n with Dissolve(0.3)
        show l_concern_n with Dissolve (0.3):
            zoom 1.5
            yoffset 70
            xoffset 100

        a "What, did you run all the way here?"

        hide l_concern_n
        show l_embarass_awk_n:
            zoom 1.5
            yoffset 70
            xoffset 100

        l "What….do you….think?"

        "He grabs onto the railing for extra support, before looking up at me, his face still flushed from the impromptu exercise."

        hide l_embarass_awk_n
        show l_concern_n:
            zoom 1.5
            yoffset 70
            xoffset 100

        l "I was worried that you’d be gone if I took too long"
        l "I guess that didn’t matter much since I still took forever running here and you haven’t left."

        a confused n "{i} Had it really been that long?"

        jump out_village_explanation


    label out_village_explanation:
        "Despite taking that initiative, I don’t even know where to start."
        hide l_concern_n with Dissolve(0.5)
        show l_awk_n with Dissolve(0.5):
            yoffset 70
            xoffset 400

        a awk n "{i}Talk about what? The weird time travel thing?"
        a "{i}Or about us?"

        "The thought of {i}us{/i} makes me feel too complicated."

        a neutral n "I guess…that was real right?"

        hide l_awk_n
        show l_confused_n:
            yoffset 70
            xoffset 400

        "Layne looks at me a little startled, a flash of confusion in his eyes momentarily, before they light up again in recognition."

        l "The village thing? Unless we both had a joint hallucination, I think it was."

        a neutral n "But…how?"

        hide l_confused_n
        show l_embarass_lookaway_n:
            yoffset 70
            xoffset 400

        l "That…I don’t know yet. This hasn’t ever happened to me before."

        hide l_embarass_lookaway_n
        show l_neutral_n:
            yoffset 70
            xoffset 400
        l "We seemed to transport when we made eye contact, but I don’t know what made that meeting special. I mean, we’re making eye contact now and we’re still on this bridge."

        a "...You said you had a dream too. Was that this morning?"

        l "Yeah?"

        a "Maybe that’s the connection then."

        hide l_neutral_n
        show l_confused_n:
            yoffset 70
            xoffset 400

        l "But that doesn’t make sense? If that’s the case, then why hasn’t this happened before–"

        hide l_confused_n
        show l_shock_open_n:
            yoffset 70
            xoffset 400

        l "...Oh."

        a confused n "Before? What do you mean before? We didn’t have those dreams before?"

        hide l_shock_open_n
        show l_awk_smile_n:
            yoffset 70
            xoffset 400

        a "Or…"

        "The gears start turning in my head."

        a neutral n "{i} I {/i} didn’t have the dream before. But you did, didn’t you?"

        show l_awk_smile_n:
            yoffset 70
            xoffset 400
            #sprite hpunch
            linear 0.090 xoffset 410 #move left 20 pixel in 0.2 seconds
            linear 0.090 xoffset 390 #move right 20 pixel in 0.2 seconds
            linear 0.090 xoffset 400 #move right 20 pixel in 0.2 seconds


        "Layne cringes and remains silent, but the silence is all I need for confirmation."

        a neutral closed n "...Fine. We’ll leave it at that then. But there was another thing that bothered me."
        a neutral n "Their names. How did you know them? They were cut out when anyone said them."

        hide l_awk_smile_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        l "I…didn’t know them. I just said random names and hoped for the best."

        "He reaches for the ring on his necklace–the same one that matches mine, and rubs the inside of it."

        a pain smile n "{i}A lie."
        a concern n "{i}But why would he lie? What is so bad about me knowing their names?"
        "I stare at him, unconvinced. He doesn’t elaborate any further."
        a "{i} How are we supposed to have a conversation if he just keeps hiding things from me?"
        a neutral n "Layne, we can’t get anywhere if you keep lying to me."

        l "...I’m sorry Azari."
        l "You’re right, I did lie. I knew their names from the first time I had that dream. But…I can’t tell you their names."

        a "But {i}why?{/i} Why can’t you tell me?"

        l "Because–"

        hide l_concern_n
        show l_shock_n:
            yoffset 70
            xoffset 400

        stop music fadeout 1.0
        play sound "audio/alarm_sound.mp3" volume 0.7

        "Both Layne and I shoot up in shock at the sound. I reach into my pocket to check my phone."

        #show lockscreen_alexandre_call at left with Dissolve(0.5)
        #move layne sprite to right

        a shock open n "Shit."

        hide l_shock_n
        show l_concern_n:
            yoffset 70
            xoffset 400

        l "What is it?"

        a concern n "It’s my boss. Probably going to ask why I didn’t come into work today."

        #hide lockscreen_alexandre_call with Dissolve(1.0)

        hide l_concern_n with Dissolve(1.0)

        "I turn around and reluctantly answer the call, slight dread settling into my stomach."

        a pain smile n "Hey Alexandre…"

        al "Azari! I’m so sorry for calling you so late. Chaayan just called–they have a family emergency and have to leave town in two days."
        al "Would it be possible for you to work Thursday instead of tomorrow?"

        a shock open n "Oh! Um, yeah, that’s no problem at all."

        a awk smile n "{i}I’m surprised Alexandre didn’t start out the call with a lecture…"

        al "Great, thank you so much! Sorry to spring this on you, especially after the rough customer you had to deal with today."

        al "I’m really glad you were here to handle that so well. Aika wanted me to thank you as well for the help."

        a confused n "{i}Huh???"
        a "{i} Today?? I didn’t come in today?"
        a "It, uh, was no problem, don’t worry about it."

        al "Glad to hear it. I’ll see you in a couple days then!"

        play sound "audio/end_call.mp3" volume 0.2

        "The call shuts off with a small ‘beep’, leaving me completely flabbergasted."

        a "What the…"

        show l_confused_n with Dissolve(1.0):
            yoffset 70
            xoffset 400

        l "What’s wrong?"

        a "Turns out I was at work today somehow."

        hide l_confused_n
        show l_awk_smile_n:
            yoffset 70
            xoffset 400

        l "You too, huh? When I got back here, I got an email from one of my employees with questions from today’s meeting."

        hide l_awk_smile_n
        show l_neutral_n:
            yoffset 70
            xoffset 400
        l "So going into the past doesn’t affect what we do here then…"

        a confused n "Hold on there. What do you mean {i}‘the past’?{/i} How did you know we weren’t just, I don’t know, transported to a different universe altogether?"

        l "Well…"

        hide l_neutral_n
        show l_blush_smile_n:
            yoffset 70
            xoffset 400

        "Layne pauses for a second, before chuckling slightly to himself."

        a awk n "What are {i}you{/i} laughing at?"

        l "Nothing! Nothing."

        l "It’s just…you {i}still{/i} hate history, don’t you?"

        a confused n "{i}...What?"
        a "I mean, yeah, but what does that have to do with anything?"

        hide l_blush_smile_n
        show l_slightsmile_open_n:
            yoffset 70
            xoffset 400

        l "We had several units about the middle ages all throughout high school. I’m more surprised you don’t remember it to be honest, especially with how often Mrs. Carter shoved it down our throats."

        a neutral open n "No fucking way you expect anyone to remember high school history class, let alone {i}me{/i} of all people."

        hide l_slightsmile_open_n
        show l_blush_smile_n:
            yoffset 70
            xoffset 400

        l "Hey, I just thought maybe you had decided to be more {i}intellectually stimulated{/i} over the years, my bad."

        a shock open n "You–!"

        "Layne only laughs at my indignation, which has me soften instantly."
        "Despite all my tension from earlier, I can’t help but feel comfortable in his presence. Almost as if the past 6 years without him didn’t exist."

        a pain smile n "{i} Will this all be over once tonight is over? Am I just going to have to go back to my everyday life without Layne?"

        hide l_blush_smile_n
        show l_slightsmile_n:
            yoffset 70
            xoffset 400

        "The conversation dies down as we stare wordlessly out at the purplish blue sky."

        a "...Hey Layne?"

        l "Yeah?"

        a "This isn’t the first time you’ve had a dream like this, right?"

        hide l_slightsmile_n
        show l_shock_n:
            yoffset 70
            xoffset 400

        "Layne’s eyes widen a little at the sudden topic shift, but recovers instantly."

        hide l_shock_n
        show l_pain_smile_n:
            yoffset 70
            xoffset 400

        l "...No, it wasn’t."

        a "Well…"
        a neutral closed n "If that's the case, then it’s likely that this isn’t going to be the {i}only{/i} dream we have then, right?"

        hide l_pain_smile_n
        show l_confused_n:
            yoffset 70
            xoffset 400

        l "I…guess so? We have no way of knowing."

        a neutral n"Right."
        a "So…"

        hide l_confused_n
        show l_shock_n:
            yoffset 70
            xoffset 400

        a "We should probably stay in contact, right? Just in case we get another weird dream?"
        a "I mean like, we’re only guessing that eye contact is the key, but what if it’s not? It would be rough if we were transported alone."

        hide l_shock_n
        show l_neutral_n:
            yoffset 70
            xoffset 400

        "Layne doesn’t immediately speak up, sending nerves into my veins."
        "I feel myself rambling on to try to fill in the empty space."

        a awk smile n "‘Cause like, this way, we can maybe figure out a plan of action before we go transport?"

        a "If we can figure out the key points of these dreams then that might make our objective clearer."
        a awk n "...If we have more dreams, that is."

        "I steel myself to not falter under Layne’s gaze. His expression mixes between several emotions that I can’t make out, but the hesitancy is clear on his face."

        a concern n "{i}Does he really not want anything to do with me after all?"
        a neutral closed n "{i}That's a stupid question, of course he doesn't. He wouldn't ghost you for 6 years if that wasn't the case."
        a concern n "{i} But...just maybe...?"

        hide l_neutral_n
        show l_awk_n:
            yoffset 70
            xoffset 400

        "After a small sigh, his gaze leaves mine and he looks back out into the sky."

        hide l_awk_n
        show l_awk_smile_closed_n:
            yoffset 70
            xoffset 400

        l "Okay. That’s probably smart."

        hide l_awk_smile_closed_n
        show l_awk_smile_n:
            yoffset 70
            xoffset 400

        "It takes everything in me to not let my relief show on my face."

        hide l_awk_smile_n
        show l_neutral_n:
            yoffset 70
            xoffset 400
        "I reach into my pocket and grab my phone, opening up my contacts to add his number. Layne takes it and swiftly adds in his number before handing it back to me."
        "I wait expectantly for him to pull out his phone to do the same, but he doesn’t move afterwards."

        a confused n "{i}Does he just want me to text him to get my number?"

        "I type out a quick message."

        #layne + azari first message

        nvl_narrator "Layne"
        a_nvl "hey it’s azari"

        "A quick buzz to my left tells us both that Layne received the message, but Layne still pulls out his phone for extra confirmation. "
        "I instinctively look over."

        show layne_notif_lockscreen at truecenter with Dissolve(1.0)

        l "Yup, got it."

        hide layne_notif_lockscreen with Dissolve(1.0)

        "He shuts off his phone, but the image still lingers in my head."

        a shock open n "{i}The contact name. It’s the same as it was in high school."
        a concern n "{i}But if he had my number all this time, why did he never contact me? Why did he keep it if he didn’t want to talk to me anymore?"
        "A heavy feeling floods into my core as questions spin around my head."

        hide l_neutral_n
        show l_awk_smile_n:
            yoffset 70
            xoffset 400

        l "I should probably start heading back now. I have to prepare new pastries for tomorrow morning."

        a awk n"Huh? Oh, yeah, you should probably go do that."
        a awk smile n "See you later? Maybe?"

        hide l_awk_smile_n
        show l_pain_smile_n:
            yoffset 70
            xoffset 400

        l "...Yeah, maybe."

        hide l_pain_smile_n with Dissolve(1.0)

        "Layne waves and walks in the opposite direction, leaving me alone on the bridge."
        "The sight of his back receding further into the night sends my heart into disarray."

        scene black with Dissolve(1.0)
        scene a_bed_night with Dissolve(1.0)

        a neutral closed n "{i}What a day…"

        "I collapse onto my bed immediately after entering inside, exhaustion flooding over me."

        a "{i}I don’t even understand how this happened. One minute I was on the bridge, the next I was in that old village."
        a awk n "{i}With Layne at that…"
        a "{i}And now I’m back in contact with him. It all feels so surreal."

        "I take a deep breath."

        a neutral closed n "{i}I’m so tired."
        a neutral n "{i}Thank God I don’t have work tomorrow."

        scene a_bed_night_blur with Dissolve(1.0)
        "I feel my eyelids droop over."
        a neutral closed n "{i}I’ll think about this…tomorrow…after some rest…"

        scene black with Dissolve(1.0)
        $ renpy.pause(1.0, hard=True)
        $ flash = Fade(.25, 0, .75, color="#fff")

        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene black with flash

        #scene wine with flash

        q "Glory to the empire!"

        play sound "audio/bell.mp3" volume 0.5

        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/breaking_glass.mp3" volume 0.3
        $ renpy.pause(2.0, hard=True)




        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene royal_A_death with flash
        play sound "audio/bell.mp3" volume 0.5
        scene black with flash
        play sound "audio/bell.mp3" volume 0.5
        scene royal_A_death with flash
        $ renpy.pause(1.0, hard=True)

        q "{i}The Emperor is dead!"

        $ renpy.pause(2.0, hard=True)

        play sound "audio/bell.mp3" volume 0.5
        scene black with Dissolve(2.0)

        #end of demo

        "Thank you so much for playing the demo of Memento Mori!"
        "Please leave a review below if you’ve enjoyed, or if  you have any comments on the characters/gameplay/plot!"
        "If you’d like to follow the development of this game or ask questions about anything, you can find updates and information {a=https://cosmicwishstudios.tumblr.com}here! {/a}"
        "Thank you again for playing!"
    return
