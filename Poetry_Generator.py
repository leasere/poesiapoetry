# ===========  Poetry Generator/Generador de Poesía  =============
# Programa para generar poesía a partir de fragmentos preexistentes

estrofa = []

idioma = input("Castellano/English: ")
while ((idioma != "Castellano") and (idioma != "English") and (idioma != "castellano") and (idioma != "english")):
    print ("Por favor seleccione idioma/Please choose a language")
    idioma = input("Castellano/English: ")
else:
    if ((idioma == "Castellano") or (idioma == "castellano")):
        print ("\n Bienvenida al generador de poesía! \n")

        # primera linea
        # Idea Vilariño, "Ya no será"
        primera = int(input("Escribe un número del 1 al 10: "))
        if primera == 1:
            print ("Un caminito entre arbustos\n")
            primera = ("Un caminito entre arbustos\n")
        if primera == 2:
            print ("Si pudiera saber\n")   
            primera = ("Si pudiera saber\n")
        if primera == 3:
            print ("Esto que va que viene\n")   
            primera = ("Esto que va que viene\n")   
        if primera == 4:
            print ("No pensarás a veces\n")   
            primera = ("No pensarás a veces\n")   
        if primera == 5:
            print ("Con amor corroído desplazando\n")   
            primera = ("Con amor corroído desplazando\n")   
        if primera == 6:
            print ("Vamos andando vamos\n")   
            primera = ("Vamos andando vamos\n")   
        if primera == 7:
            print ("Mis manos\n")   
            primera = ("Mis manos\n") 
        if primera == 8:
            print ("Ya en desnudez total\n")
            primera = ("Ya en desnudez total\n")
        if primera == 9:
            print ("No sé qué hay en la tarde, en la luz, en el alma,\n")
            primera = ("No sé qué hay en la tarde, en la luz, en el alma,\n")
        if primera == 10:
            print ("Yo no te pido nada\n")
            primera = ("Yo no te pido nada\n")

        estrofa.append(primera)

                
        # segunda linea
        # Alejandra Pizarnik, "La extracción de la piedra de locura. Otros poemas"
        segunda = int(input("Escribe un número del 1 al 10: "))
        if segunda == 1:
            print ("Recibe este amor que te pido.\n")   
            segunda = ("Recibe este amor que te pido.\n")
        if segunda == 2:
            print ("en donde anida el miedo.\n")   
            segunda = ("en donde anida el miedo.\n")
        if segunda == 3:
            print ("su rostro rueda por mí\n")   
            segunda = ("su rostro rueda por mí\n")
        if segunda == 4:
            print ("las palabras del sueño de la infancia de la muerte\n")   
            segunda = ("las palabras del sueño de la infancia de la muerte\n")   
        if segunda == 5:
            print ("parte de la cara y las manos.\n")   
            segunda = ("parte de la cara y las manos.\n")   
        if segunda == 6:
            print ("Nadie viene. Esta sombra.\n")   
            segunda = ("Nadie viene. Esta sombra.\n")  
        if segunda == 7:
            print ("en mi tragedia del viento en el corazón.\n")  
            segunda =  ("en mi tragedia del viento en el corazón.\n")  
        if segunda == 8:
            print ("me vestirán con cenizas al alba,\n")
            segunda = ("me vestirán con cenizas al alba,\n")
        if segunda == 9:
            print ("para mi infancia.\n")
            segunda = ("para mi infancia.\n")
        if segunda == 10:
            print ("el sonido de la luz en una hora muerta,\n")
            segunda = ("el sonido de la luz en una hora muerta,\n")
        
        estrofa.append(segunda)

        # tercera linea
        # Alfonsina Storni, "Languidez"
        tercera = int(input("Escribe un número del 1 al 10: "))
        if tercera == 1:
            print ("curioseaban con sus ramas\n")   
            tercera = ("curioseaban con sus ramas\n")
        if tercera == 2:
            print ("los mundos son redondos y los cuerpos redondos,\n")   
            tercera = ("los mundos son redondos y los cuerpos redondos,\n")   
        if tercera == 3:
            print ("mirémonos sin miedo y a los ojos:\n")   
            tercera = ("mirémonos sin miedo y a los ojos:\n") 
        if tercera == 4:
            print ("échame sobre el alma gota a gota tu alma,\n")   
            tercera = ("échame sobre el alma gota a gota tu alma,\n")   
        if tercera == 5:
            print ("descansando los tristes ojos sobre la arena\n")   
            tercera = ("descansando los tristes ojos sobre la arena\n")  
        if tercera == 6:
            print ("Ahondo y tengo miedo:\n")   
            tercera = ("Ahondo y tengo miedo:\n")
        if tercera == 7:
            print ("recuerdos de mi infancia\n")   
            tercera = ("recuerdos de mi infancia\n")   
        if tercera == 8:
            print ("procure mirarse, ella que no siente\n")
            tercera = ("procure mirarse, ella que no siente\n")
        if tercera == 9:
            print ("y eras en mí como una espina brava.\n")
            tercera = ("y eras en mí como una espina brava.\n")
        if tercera == 10:
            print ("de amor me estoy muriendo,\n")
            tercera = ("de amor me estoy muriendo,\n")

        estrofa.append(tercera)

        # cuarta linea
        # Isabel Bono, "Me muero"
        cuarta = int(input("Escribe un número del 1 al 10: "))
        if cuarta == 1:
            print ("del falso arte de estar en el mundo\n")   
            cuarta = ("del falso arte de estar en el mundo\n") 
        if cuarta == 2:
            print ("miras donde señala la luz\n")   
            cuarta = ("miras donde señala la luz\n")   
        if cuarta == 3:
            print ("solo porque al abrir la ventana\n")   
            cuarta = ("solo porque al abrir la ventana\n")   
        if cuarta == 4:
            print ("el milagro aparece ante tus ojos\n")   
            cuarta = ("el milagro aparece ante tus ojos\n")  
        if cuarta == 5:
            print ("conocer cada minuto de su infancia\n")   
            cuarta = ("conocer cada minuto de su infancia\n")   
        if cuarta == 6:
            print ("cuerpos huecos a la velocidad de esta luz\n")   
            cuarta = ("cuerpos huecos a la velocidad de esta luz\n")  
        if cuarta == 7:
            print ("bajo la luz de la farola\n")   
            cuarta = ("bajo la luz de la farola\n")   
        if cuarta == 8:
            print ("esas mañanas en las que duele respirar, pero te gusta\n")
            cuarta = ("esas mañanas en las que duele respirar, pero te gusta\n")
        if cuarta == 9:
            print ("deseas que las cosas quietas cobren vida,\n")
            cuarta = ("deseas que las cosas quietas cobren vida,\n")
        if cuarta == 10:
            print ("vaciando el cielo\n")
            cuarta = ("vaciando el cielo\n")

        estrofa.append(cuarta)

        # quinta linea
        # Winétt de Rokha, "Fotografía en oscuro"
        quinta = int(input("Escribe un número del 1 al 10: "))
        if quinta == 1:
            print ("mujer eterna, abandonada y oscura\n")   
            quinta = ("mujer eterna, abandonada y oscura\n") 
        if quinta == 2:
            print ("besando el camino sin término.\n")   
            quinta = ("besando el camino sin término.\n")   
        if quinta == 3:
            print ("interna y cálida para el cuerpo cansado.\n")   
            quinta = ("interna y cálida para el cuerpo cansado.\n")   
        if quinta == 4:
            print ("la mujer contemporánea\n")   
            quinta = ("la mujer contemporánea\n")  
        if quinta == 5:
            print ("y me extiendo al amparo profundo\n")   
            quinta = ("y me extiendo al amparo profundo\n")   
        if quinta == 6:
            print ("Los pies y las manos\n")   
            quinta = ("Los pies y las manos\n")  
        if quinta == 7:
            print ("salvando este puente, sin olvidar el océano...\n")   
            quinta = ("salvando este puente, sin olvidar el océano...\n")   
        if quinta == 8:
            print ("prendida al dorso.\n")
            quinta = ("prendida al dorso.\n")
        if quinta == 9:
            print ("Tus gestos van a morir, helados,\n")
            quinta = ("Tus gestos van a morir, helados,\n")
        if quinta == 10:
            print ("mudos secretos de inmolación rebelde,\n")
            quinta = ("mudos secretos de inmolación rebelde,\n")

        estrofa.append(quinta)

        # sexta linea
        # Rosa Alcayaga, "La primera gota de sangre"
        sexta = int(input("Escribe un número del 1 al 10: "))
        if sexta == 1:
            print ("Repican campanas en el silencio repetido de la muerte oscura\n")   
            sexta = ("Repican campanas en el silencio repetido de la muerte oscura\n") 
        if sexta == 2:
            print ("Curiosa leyenda en Sodoma\n")   
            sexta = ("Curiosa leyenda en Sodoma\n")   
        if sexta == 3:
            print ("Por eso me lloro presente\n")   
            sexta = ("Por eso me lloro presente\n")   
        if sexta == 4:
            print ("Entre las casas de un enésimo sector en Playa Ancha\n")   
            sexta = ("Entre las casas de un enésimo sector en Playa Ancha\n")  
        if sexta == 5:
            print ("¡Qué más querí!\n")   
            sexta = ("¡Qué más querí!\n")   
        if sexta == 6:
            print ("Brota la sangre del puñal blasfemo\n")   
            sexta = ("Brota la sangre del puñal blasfemo\n")  
        if sexta == 7:
            print ("Entre la vida y la muerte un camino incierto\n")   
            sexta = ("Entre la vida y la muerte un camino incierto\n")   
        if sexta == 8:
            print ("De mi madre\n")
            sexta = ("De mi madre\n")
        if sexta == 9:
            print ("Es el único alimento\n")
            sexta = ("Es el único alimento\n")
        if sexta == 10:
            print ("Entre las rocas veo sangre tuya y mía\n")
            sexta = ("Entre las rocas veo sangre tuya y mía\n")

        estrofa.append(sexta)

        print (*estrofa)
        print ("\n Créditos: \n Primer verso: Idea Vilariño, 'Ya no será' \n Segundo verso: Alejandra Pizarnik, 'La extracción de la piedra de locura. Otros poemas' \n Tercer verso: Alfonsina Storni, 'Languidez' \n Cuarto verso: Isabel Bono, 'Me muero' \n Quinto verso: Winétt de Rokha, 'Fotografía en oscuro' \n Sexto verso: Rosa Alcayaga, 'La primera gota de sangre'")
        print ("\n Espero te haya divertido crear poesía! \n Si querés ayudar a que existan más proyectos como este podés invitarme a un cafecito acá https://cafecito.app/leasere \n Muchas gracias!")



 
                



    stanza = []


    if ((idioma == "English") or (idioma == "english")):
        print ("\n Welcome to the poetry generator! \n")

        # all verses are by Adrienne Rich

        # first line
        first = int(input("Choose a number between 1 and 10: "))
        if first == 1: 
            print ("I wake up in your bed. I know I have been dreaming.\n")
            first = ("I wake up in your bed. I know I have been dreaming.\n")
        if first == 2:
            print ("The world tells me I am its creature\n")   
            first = ("The world tells me I am its creature\n")   
        if first == 3:
            print ("Your silence today is a pond where drowned things live\n")   
            first = ("Your silence today is a pond where drowned things live\n")   
        if first == 4:
            print ("A thinking woman sleeps with monsters.\n")   
            first = ("A thinking woman sleeps with monsters.\n")  
        if first == 5:
            print ("Violently asleep in the old house.\n")   
            first = ("Violently asleep in the old house.\n")   
        if first == 6:
            print ("The freedom of the wholly mad\n")   
            first = ("The freedom of the wholly mad\n")  
        if first == 7:
            print ("A woman in the shape of a monster\n")   
            first = ("A woman in the shape of a monster\n")   
        if first == 8:
            print ("How calm, how inoffensive these words\n")
            first = ("How calm, how inoffensive these words\n")
        if first == 9:
            print ("Close to your body, in the\n")
            first = ("Close to your body, in the\n")
        if first == 10:
            print ("The women who first knew themselves\n")
            first = ("The women who first knew themselves\n")

        stanza.append(first)

        # second line
        second = int(input("Choose a number between 1 and 10: "))
        if second == 1: 
            print ("The city as object of love.\n")
            second = ("The city as object of love.\n")
        if second == 2:
            print ("Language cannot do everything—\n")   
            second = ("Language cannot do everything—\n")   
        if second == 3:
            print ("dress, go out, drink coffee,\n")   
            second = ("dress, go out, drink coffee,\n")   
        if second == 4:
            print ("and loaded the camera,\n")   
            second = ("and loaded the camera,\n")  
        if second == 5:
            print ("The beak that grips her, she becomes. And Nature,\n")   
            second = ("The beak that grips her, she becomes. And Nature,\n")   
        if second == 6:
            print ("The stone is still a stone,\n")   
            second = ("The stone is still a stone,\n")  
        if second == 7:
            print ("rotating in their midnight meadow:\n")   
            second = ("rotating in their midnight meadow:\n")   
        if second == 8:
            print ("I am raked by eyes  brushed by hands\n")
            second = ("I am raked by eyes  brushed by hands\n")
        if second == 9:
            print ("to kill is to cut off from pain\n")
            second = ("to kill is to cut off from pain\n")
        if second == 10:
            print ("a monster in the shape of a woman\n")
            second = ("a monster in the shape of a woman\n")

        stanza.append(second)

        # third line
        third = int(input("Choose a number between 1 and 10: "))
        if third == 1: 
            print ("from your unlived life\n")
            third = ("from your unlived life\n")
        if third == 2:
            print ("What winds are walking overhead, what zone\n")   
            third = ("What winds are walking overhead, what zone\n")   
        if third == 3:
            print ("a touch is enough to let us know\n")   
            third = ("a touch is enough to let us know\n")   
        if third == 4:
            print ("the skies are full of them\n")   
            third = ("the skies are full of them\n")  
        if third == 5:
            print ("Does the infant memorize the body of the mother\n")   
            third = ("Does the infant memorize the body of the mother\n")   
        if third == 6:
            print ("the midsummer night light rising from beneath\n")   
            third = ("the midsummer night light rising from beneath\n")  
        if third == 7:
            print ("It has ceased to hear itself, therefore\n")   
            third = ("It has ceased to hear itself, therefore\n")   
        if third == 8:
            print ("moony, inlet-warm, seabathed, I watched you sleep,\n")
            third = ("moony, inlet-warm, seabathed, I watched you sleep,\n")
        if third == 9:
            print ("If I thought of my words as changing minds,\n")
            third = ("If I thought of my words as changing minds,\n")
        if third == 10:
            print ("you've been at your desk for hours. I know what I dreamed:\n")
            third = ("you've been at your desk for hours. I know what I dreamed:\n")

        stanza.append(third)

        # fourth line
        fourth = int(input("Choose a number between 1 and 10: "))
        if fourth == 1: 
            print ("silence not absence\n")
            fourth = ("silence not absence\n")
        if fourth == 2:
            print ("as you stand looking at these\n")   
            fourth = ("as you stand looking at these\n")   
        if fourth == 3:
            print ("in it the length of a room\n")   
            fourth = ("in it the length of a room\n")   
        if fourth == 4:
            print ("water. All these phenomena\n")   
            fourth = ("water. All these phenomena\n")  
        if fourth == 5:
            print ("it asks itself\n")   
            fourth = ("it asks itself\n")   
        if fourth == 6:
            print ("we're not alone in the universe, even in sleep:\n")   
            fourth = ("we're not alone in the universe, even in sleep:\n")  
        if fourth == 7:
            print ("Menstrual blood\n")   
            fourth = ("Menstrual blood\n")   
        if fourth == 8:
            print ("the horizon—when I said «a cleft of light»\n")
            fourth = ("the horizon—when I said «a cleft of light»\n")
        if fourth == 9:
            print ("like death and childbirth.\n")
            fourth = ("like death and childbirth.\n")
        if fourth == 10:
            print ("If you go through\n")
            fourth = ("If you go through\n")

        stanza.append(fourth)

        # fifth line
        fifth = int(input("Choose a number between 1 and 10: "))
        if fifth == 1: 
            print ("among the Clocks and instruments\n")
            fifth = ("among the Clocks and instruments\n")
        if fifth == 2:
            print ("looking down the red rocks to where a soundless curl\n")   
            fifth = ("looking down the red rocks to where a soundless curl\n")   
        if fifth == 3:
            print ("But gentleness is active\n")   
            fifth = ("But gentleness is active\n")   
        if fifth == 4:
            print ("through gorges unexlored since dawn\n")   
            fifth = ("through gorges unexlored since dawn\n")  
        if fifth == 5:
            print ("The hammer-blows of time\n")   
            fifth = ("The hammer-blows of time\n")   
        if fifth == 6:
            print ("as if it were against us\n")   
            fifth = ("as if it were against us\n")  
        if fifth == 7:
            print ("This morning you left the bed\n")   
            fifth = ("This morning you left the bed\n")   
        if fifth == 8:
            print ("Their figures moving in the Sunday garden\n")
            fifth = ("Their figures moving in the Sunday garden\n")
        if fifth == 9:
            print ("How do I exist?\n")
            fifth = ("How do I exist?\n")
        if fifth == 10:
            print ("I leave the book upon a pillowed chair\n")
            fifth = ("I leave the book upon a pillowed chair\n")

        stanza.append(fifth)

        # sixth line
        sixth = int(input("Choose a number between 1 and 10: "))
        if sixth == 1: 
            print ("I would have loved to live in a world\n")
            sixth = ("I would have loved to live in a world\n")
        if sixth == 2:
            print ("whatever we do together is pure invention\n")   
            sixth = ("whatever we do together is pure invention\n")   
        if sixth == 3:
            print ("to take each other's lives in our hands, as bodies.\n")   
            sixth = ("to take each other's lives in our hands, as bodies.\n")   
        if sixth == 4:
            print ("I would tell the story\n")   
            sixth = ("I would tell the story\n")  
        if sixth == 5:
            print ("who fought with what she partly understood.\n")   
            sixth = ("who fought with what she partly understood.\n")   
        if sixth == 6:
            print ("Now, look again at the face\n")   
            sixth = ("Now, look again at the face\n")  
        if sixth == 7:
            print ("walking as I've walked before\n")   
            sixth = ("walking as I've walked before\n")   
        if sixth == 8:
            print ("to bring the essential vein to light\n")
            sixth = ("to bring the essential vein to light\n")
        if sixth == 9:
            print ("as women have done  or hiding\n")
            sixth = ("as women have done    or hiding\n")
        if sixth == 10:
            print ("in order to forget\n")
            sixth = ("in order to forget\n")

        stanza.append(sixth)

        print (*stanza)
        print ("\n All verses are by Adrienne Rich")
        # print ("\n I hope you had fun creating a poem! \n If you want to help create more projects like this one you can support me through this link: [paypal] \n Thanks a lot!")






# print ("bye")