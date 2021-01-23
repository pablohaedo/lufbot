import telegram

messageList = {
    "/start" : {
        "messages" : ['Menú principal.'],
        "keyboard" : [
            ['PASOS DE UNA VENTA',
            'PLANES'],
            ['COMO COMPRAR',
            'COMO REGISTRARSE'],
            ['SEGUIMIENTO',
            "LISTA DE PRECIOS"],
            ['DESAFIO 5D',
            'MARATON 10 DIAS'],
            ['HLOK',
            'CAPACITACION']
            ]
    },
    "LISTA DE PRECIOS" : {
        "messages" : ['ARGENTINA','URUGUAY','CHILE'], 
        "keyboard" : [['LISTA ARGENTINA'],['LISTA URUGUAY'],['LISTA CHILE']]
    },
    "LISTA ARGENTINA": {
        "messages" : ["""PUBLICO
CLIENTES PREFERENTES 25%
ASOCIADO X DESCUENTOS"""], 
        "keyboard" : [['ARG PUBLICO'],['ARG PREFERENTES 25'],['ARG ASOCIADOS']]
    },
    "ARG PUBLICO" : {
        "messages" : ['IMG:listado/arg/publico/1.jpg','IMG:listado/arg/publico/2.jpg','IMG:listado/arg/publico/3.jpg','IMG:listado/arg/publico/4.png']
    },
    "ARG PREFERENTES 25" : {
        "messages" : ['IMG:listado/arg/preferentes/1.jpg','IMG:listado/arg/preferentes/2.png','IMG:listado/arg/preferentes/3.png']
    },
    "ARG ASOCIADOS" : {
        "messages" : ['IMG:listado/arg/asociados/nocategorizado.jpg','IMG:listado/arg/asociados/monotributista.jpg']
    },
    "LISTA CHILE": {
        "messages" : ["""PUBLICO
CLIENTES PREFERENTES 25%
ASOCIADO X DESCUENTOS"""], 
        "keyboard" : [['CHI PUBLICO'],['CHI 25'],['CHI ASOCIADOS']]
    },
    "CHI PUBLICO" : {
        "messages" : ['IMG:listado/chi/publico/1.jpg','IMG:listado/chi/publico/2.jpg','IMG:listado/chi/publico/3.jpg']
    },
    "CHI PREFERENTES 25" : {
        "messages" : ['IMG:listado/chi/preferentes/1.jpg','IMG:listado/chi/preferentes/2.jpg','IMG:listado/chi/preferentes/3.jpg']
    },
    "CHI ASOCIADOS": {
        "messages" : ['IMG:listado/chi/asociados/1.jpg','IMG:listado/chi/asociados/2.jpg']
    },
    "LISTA URUGUAY": {
        "messages" : ["""PUBLICO
ASOCIADO X DESCUENTOS"""], 
        "keyboard" : [['URU PUBLICO'],['URU ASOCIADOS']]
    },
    "URU PUBLICO" : {
        "messages" : ['IMG:listado/uru/publico/1.jpg']
    },
    "URU ASOCIADOS" : {
        "messages" : ['IMG:listado/uru/asociados/1.jpg']
    },
    "PLANES" : {
        "messages" : ['ARGENTINA','URUGUAY','CHILE'], 
        "keyboard" : [['PLANES ARGENTINA'],['PLANES URUGUAY'], ['PLANES CHILE']]
    },
    'PLANES ARGENTINA': {
        "messages" : ['Programas SIN ALTA (precio público)', 'Programas CON ALTA'],
        "keyboard": [['ARG SIN ALTA'],['ARG CON ALTA']]
    },
    'ARG SIN ALTA': {
        "messages": ['IMG:planes/arg/sin/1.jpg','IMG:planes/arg/sin/2.jpg','IMG:planes/arg/sin/3.jpg']
    },
    'ARG CON ALTA': {
        "messages": ['IMG:planes/arg/con/1.jpg','IMG:planes/arg/con/2.jpg','IMG:planes/arg/con/3.jpg']
    },
    'PLANES CHILE': {
        "messages" : ['Programas SIN ALTA (precio público)', 'Programas CON ALTA'],
        "keyboard": [['CHI SIN ALTA'],['CHI CON ALTA']]
    },
    'CHI SIN ALTA': {
        "messages": ['IMG:planes/chi/sin/1.jpg','IMG:planes/chi/sin/2.jpg','IMG:planes/chi/sin/3.jpg']
    },
    'CHI CON ALTA': {
        "messages": ['IMG:planes/chi/con/1.jpg','IMG:planes/chi/con/2.jpg','IMG:planes/chi/con/3.jpg']
    },
    'PLANES URUGUAY': {
        "messages" : ['Programas SIN ALTA (precio público)', 'Programas CON ALTA'],
        "keyboard": [['URU SIN ALTA'],['URU CON ALTA']]
    },
    'URU SIN ALTA': {
        "messages": ['IMG:planes/uru/sin/1.jpg','IMG:planes/uru/sin/2.jpg','IMG:planes/uru/sin/3.jpg']
    },
    'URU CON ALTA': {
        "messages": ['IMG:planes/uru/con/1.jpg','IMG:planes/uru/con/2.jpg','IMG:planes/uru/con/3.jpg']
    },

    "PASOS DE UNA VENTA" : {
        "messages" : ['PREGUNTAS','METODO DESAYUNO','PRODUCTOS','OBJECIONES'],
        "keyboard" : [['PREGUNTAS'],['METODO DESAYUNO'],['PRODUCTOS'],['OBJECIONES']]
    },
    "PREGUNTAS" : {
        "messages" : ['''Contame un poco más de vos y así sé que puedo recomendarte:\n 
    ¿Que objetivo físico te gustaría lograr?\n
    ¿Cuanto mides y pesas actualmente?\n
    ¿Cuanta agua tomas al día?\n
    ¿Cuantas comidas haces a lo largo del día?\n
    ¿Haces deporte?\n
    ¿Trabajas en algo que requiera esfuerzo físico?''']
    },
    "METODO DESAYUNO" : {
        "messages" : ['''Perfecto. Te cuento un poco, en tu caso te recomiendo el “Programa de Desayuno Equilibrado” que consiste en sustituir tu desayuno por Batidos Nutricionales de Herbalife! Que además de ser muuuy ricos😋 te van a aportar a nivel nutricional todo lo que tu cuerpo necesita. Muy importante!!! No vas a sentir que estás a dieta porque haces varias comidas a lo largo del día, con lo cual nunca vas a tener sensación de hambre😉🙌! \n
    Por mi parte tendrás seguimiento cada vez que lo necesites, cualquier duda que tengas, planes de alimentación y entrenamiento en el caso que lo necesites y quieras.''',
    '''Tambien te voy a pasar una colección de recetas para el almuerzo y para los snacks🥗🥙. Así el plan funcionará al 100%\n
    Igualmente disponemos de una comunidad que te va aportar: Motivación, recetas de nuevos platos casi a diario, retos semanales, plan de entrenamiento (si lo necesitas), resolver dudas las 24 hrs del día y cursos online sobre consejos para alimentarnos bien.\n
    y obvio el Desafio 21 dias!! con acceso TOTAL a la plataforma de actividades y las charlas con los medicos a tu disposicion!!\n
    El seguimiento es continuo con revisión semanal y por supuesto podrás preguntarme las veces que necesites.
    ''']
    },
    "PRODUCTOS" : {
        "messages" : ['IMG:IMAGEN1.jpg',
    '''Te cuento que Herbalife salio premiado por la afamada revista Health and Fitness como el mejor desayuno del 2019!!''',
    'IMG:IMAGEN2.png','''Estos son los 3 productos basicos!  

Batido Nutricional:
Es una comida completa, que te aporta todos los nutrientes que necestias, y tiene las mismas calorias que una manzana🍎!, al igual que todos los productos Herbalife, son naturales, y por eso es que no tienen contraindicaciones y todo el mundo los puede tomar!
Te va a dar saciedad, energia a full🔋!!!!, Como puede reemplazar una comida, te ayuda a reducir los excesos de manera natural! Y como tiene proteina de soja, te vas a ver tonificada enseguida🏃🏼‍♀️!!

Te de Hierbas:
Es una bebida a base de Te verde concentrado, y Te negro!!, Si sentis cansancio o desgano durante el dia, este es tu nuevo mejor amigo🤝!, Ademas, tiene una propiedad que acelera el metabolismo, o sea que vas a ir ""quemando grasita extra"" mientras haces tus actividades del dia. Le decimos el GYM de bolsillo🏃🏼‍♀️!

Aloe Vera:
Amo este producto!, Ayuda a desintoxicar el aparato digestivo!! Te da una sensacion de alivio inmediato, y al pasar los dias, vas a sentir como te regularizas intestinalmente♻️! Al limpiar el aparato digestivo, permitis que absorba mayor cantidad de nutrientes, de las comidas, y obvio del Batido!!, Los cambios son muy notorios en poco tiempo✅!''',
'IMG:IMAGEN3.jpg','''La *proteína* es un producto que se le agrega al batido para darle más valor proteico. Te da mayor saciedad y ayuda a ganar masa muscular🏋‍♂..no tiene gusto entonces también yo la uso para cocinar dulce🥞 o salado🍲
Te ayuda mucho a tonificar y que al bajar todo quede en su lugar 😜
'''
    ]
    },
    "OBJECIONES" : {
        'messages' : [
    '''ES CARO''',
    '''Sinceramente a mi en un principio me parecia caro!, pero en verdad, te sale menos que un cafe en un bar, y por los resultados que da,  ahora hasta lo pagaria el doble! , y eso hablando solo del producto, sin contar todas las actividades que incluye, el coach 24hs, y la comunidad a disposicion con los medicos y todo el servicio de apoyo y acompañamiento.''',
    '''EFECTO REBOTE''',
    '''Yo tambien le tenia miedo al efecto rebote, escuche varias cosas, pero me explicaron que las personas a veces llegan al resultado que buscaban con Herbalife, y despues dejan los productos, pero tambien dejan de aplicar los habitos aprendidos, y vuelven a los viejos habitos, y obviamente, vuelven al mismo resultado que tenian. Pero esta claro que es mas facil echarle la culpa a un producto que hacerse cargo de lo que uno pone en el plato. Por eso es clave aprovechar todo el servicio, para poder forjar nuevos habitos saludables, que te permitan mantener el resultado toda la vida, independientemente de un producto!''',
    '''SON NATURALES, SON SEGUROS, TIENEN CONTRAINDICACIONES?''',
    '''Genial, yo pregunte lo mismo! , son super seguros y naturales, ademas te podes tomar toda la cantidad de producto que quieras y nada malo te va a pasar!, cumplen con la ley de "megadosis" que dice justamente eso!, si podes comer un pollito con ensalada, entonces tambien podes tomar cualquier producto, porque son comida.\n
    Pensa que esta en 95 paises Herbalife, o sea que esos 95 ministerios de salud los avalan para su venta libre, por personas comunes que no hace falta que sean medicos o nutricionistas, son geniales.'''
        ]
    },

    'COMO COMPRAR': {
        "messages" : ['ARGENTINA','URUGUAY','CHILE'], 
        "keyboard" : [['COMPRAR ARGENTINA'],['COMPRAR URUGUAY'],['COMPRAR CHILE']]
    },
    'COMPRAR ARGENTINA': {
        "messages": ["""*HERBALIFE TIENDA. Descárgala en tu celular.*
Versión para iOS: 
https://apps.apple.com/ar/app/herbalife-nutrition-tienda/id1154285940""",
"""Version para Android:
https://play.google.com/store/apps/details?id=com.hrbl.mobile.android.ordering""",
"Te envió las indicaciones de como comprar. Lo podes hacer por la aplicación o entrando a la página web.",
"https://drive.google.com/file/d/1DRTvYbTPo9jHLv6C9zuOa-ncF0ldESXy/view?usp=drivesdk "]
    },
    'COMPRAR URUGUAY': {
        'messages': ['VID:compraruruguay.mp4']
    },
    'COMPRAR CHILE': {
        'messages': ['https://youtu.be/f12y37NfvRg']
    },

    'COMO REGISTRARSE': {
        "messages" : ['ARGENTINA','URUGUAY','CHILE'], 
        "keyboard" : [['REGISTRO ARGENTINA'],['REGISTRO URUGUAY'],['REGISTRO CHILE']]
    },
    'REGISTRO ARGENTINA': {
        "messages": ["""https://www.myherbalife.com/?ReturnUrl=%2fHome%2fDefault

1. Ingresar al link 
2. Seleccionar tu pais
3. Hace click en: Registrate como distribuidor independiente (aplica en linea)
4. Generar tu usuario con tu mail y una clave
5. Aceptar las reglas del standard de oro (marca en cada casillero)
6. Poner  los datos de tu patrocinador, ( ID Y  PRIMERAS 3 LETRAS DEL APELLIDO ❤️) 
7. Por último comprar el Pack de bienvenida SI ES QUE AUN NO LO TENES  (Opción Kit Caja RECOMENDADO $1.550 con gastos de envío e IVA incluídos, Kit Bolso $3737)""",
'IMG:registroarg.jpg','VID:registroarg.mp4']
    },
    'REGISTRO URUGUAY': {
        "messages": ["""https://www.myherbalife.com/?ReturnUrl=%2fHome%2fDefault

1. Ingresa al link 
2. Creas una cuenta con tu email y contraseña 
3. Pones los datos del sponsor, que en este caso eres tu (TU ID Y APELLIDO ❤️) 
4. Rellenas tus datos   
5. Aceptas las garantías de oro (son 6) 
6. Por último compras el Pack de bienvenida ( Opción Kit Caja RECOMENDADO$1.050 con gastos de envío e IVA incluídos, Kit Bolso $1.725)""",
'IMG:registrouru1.jpg','IMG:registrouru2.jpg', """Te dejo el video de como registrarte correctamente 
https://youtu.be/Xcu9dOSmCmg"""]
    },
    'REGISTRO CHILE': {
        "messages": ["""https://accounts.myherbalife.com/Account/Create?appId=1&locale=es-CL&redirect=https://www.myherbalife.com/es-CL/ 🇨🇱 

1. Entra al link 
2. Creas una cuenta con tu email y contraseña 
3. Metes los datos del sponsor, que en este caso eres tu (TU ID Y APELLIDO ❤️) 
4. Rellenas tus datos   5.Aceptas las garantías de oro (son 6) 
6. Por último compras el Pack de bienvenida ($32.130 con gastos de envío e IVA incluídos)""",
'IMG:registrochi.jpg',"""Te dejo el video de como registrarte correctamente 
https://youtu.be/Xcu9dOSmCmg"""]
    },
    'SEGUIMIENTO': {
        'messages': ['PRE PRODUCTO - DÍA  que pago','DIA 0 (recibe los productos)','DIA 1','DIA 2','DIA 3','DIA 7','DIA 14','DIA 21','MENSUAL','Programar Mensajes en Telegram','IDEAS PARA POST','RECETAS','RESULTADO'],
        'keyboard': [
            ['PRE PRODUCTO', 'DIA 0'],
            ['DIA 1','DIA 2','DIA 3'],
            ['DIA 7','DIA 14','DIA 21'],
            ['MENSUAL','PROGRAMAR MENSAJES'],
            ['IDEAS POST','RECETAS','RESULTADO']
            ]
    },
    'PRE PRODUCTO': {
        'messages':['FIL:comienzo.pptx',
            'IMG:bienvenida.jpg',
            """🔈Y un pequeño audio con la explicación para que se descargue Telegram y se registre en HLOK""",
            """Bueno listo! Bájate la app Telegram y avísame así empezamos 😉 Es gratis y no ocupa casi espacio! Decime cuando estés lista con eso!
Para instalar Telegram en tu móvil, selecciona uno de los siguientes links según sea tu dispositivo:
👉Si tienes *Android*: https://telegram.org/dl/android
👉Si tienes *iPhone/iPad*: https://telegram.org/dl/ios""",
            """Como participar de las actividades ❓
1ro: te registras gratis en ente Link en la comunidad virtual y participar de las clases 
(AGREGAR TU LINK DE INVITADOS EN TU HLOK)""",
            """2do:
T𝗲𝗻é𝘀 𝗾𝘂𝗲 𝗯𝗮𝗷𝗮𝗿𝘁𝗲 𝗹𝗮 𝗮𝗽𝗹𝗶𝗰𝗮𝗰𝗶ó𝗻 𝗭𝗢𝗢𝗠 𝗱𝗲𝗹 𝗽𝗹𝗮𝘆 𝘀𝘁𝗼𝗿𝗲 ó 𝗰𝗼𝗻 𝗲𝘀𝘁𝗲 𝗹𝗶𝗻𝗸 
👇👇👇👇👇👇
https://play.google.com/store/apps/details?id=us.zoom.videomeetings""",
            """COMO USAR HLOK: en el link que te envíe registrate.
1) una vez registrada podes ingresa con tu usuario y contraseña desde cualquier dispositivo a la pagina 
www.hlok.es
2) Vas a las líneas que hay a la  izquierda y seleccionas opción calendario 🗓 
3) selecciona día, horario y la actividad .. (las clases son en vivo)
4) automáticamente te redirige a la sala Zoom ! (Recorda activar tu audio en zoom: Abajo a la izquierda te aparece estos signos 🔈🎧 si no escuchas apreta en el signo y marca “llamar a través del audio del dispositivo” ó “marcar utilizando de internet”) 
5) listo ✅ disfruta la clase o taller 🌪⚡️❤️

Te envio un video que explica como acceder fácilmente a las actividades y puedas aprovechar nuestra Comunidad Saludable!
Espero que la Disfrutes!""",
            'https://youtu.be/krivfCJrJhU',
            """Súmate al canal de DESAFIO 21D, asi vas viendo los tips y comenzas a poner en práctica en estos dias de adaptación, con este Link  👇 
(ENVIAR Link Del Canal)""",
            'FIL:guia_para_armar_platos.pdf','FIL:recetas_saladas.pdf','FIL:recetas_dulces.pdf',
            """*Colaciones inteligentes*
📌2 huevos duros
📌2 rodajas de pan lactal de salvado con 100 gramos de jamón cocido natural
📌1 lata de atún
📌1 yogurt firme ligth + 10 almendras
📌3 tostadas riera con queso ligth
📌*1 batido Herbalife*
📌1 fruta + 15 almendras""",'colaciones inteligentes']
    },
    'DIA 0':{
        'messages': ["""Estoy muy contenta de que hayas arrancado con tu plan y estoy para ayudarte! 🎉
Te mando las indicaciones de cómo preparar los productos y te pido que no te olvides de pasarme tu foto inicial y tus medidas cuanto antes, así vamos registrando cada cambio 😃🔝""",
            """✅Desayuno :
1️⃣ 200 cc de agua en una licuadora 🍶 + 3 hielos 🧊 + 3 🥄🥄cucharadas de batido nutricional al ras + 1🥄 de proteína al ras
**Licuar unos minuto y beber**🥤
2️⃣En 200 cc de agua 🍶 poner una cucharada (tamaño té) de TE HERBAL (se puede hacer frío, tibio o caliente) 🍵
3️⃣: tomar un vaso de agua al terminar
**De esta incorporamos todos los nutrientes y activamos el metabolismo aumentando la energia**

DURANTE EL DIA
Comer algo (colaciones) cada 3 horas

🍽Almuerzo como venis haciendo!! ideal algo de proteína (carne, pollo, pescado o legumbres) con ensalada (o plato del desafío)
Tomar durante el dia agua!! 1 litro cada 25kg de tu cuerpo. 💦
🍽CENA como en el almuerzo.""",'IMG:GUIA_DE_BIENESTAR.jpg']
    },
    'DIA 1': {
        'messages': ["""Hola....... Como estas? DÍA 1 🥳 que emoción, Ya probaste tu batido, aloe y te ?
Contame como te preparaste el batido como si tuvieras que enseñarme. 

Del 1 al 10, cuánto te gustó el batido? 

Contame, si el batido te llenó, si quedaste saciada"""]
    },
    'DIA 2': {
        'messages': ["""Hola....Como estas? Buen dia!🤗
Ya desayunaste?  Del 1 al 10, cuánto te gustó el batido hoy?
Tienes alguna duda?
Tenés agendado conectarte a alguna de las actividades?

Lo otro que te quería recordar, es que mandes a la comunidad fotos de tus platos, así veo de ir haciendo alguna corrección si es necesario."""]
    },
    'DIA 3': {
        'messages': ["""Cómo estás ? 
Felicitaciones, ya estamos en el día 3 de nutrición completa e inteligente. 

Cómo te sentís ? 
Tu energía? 
Te sentís más deshinchada? 

Los primeros días podemos notar más una sensación de ansiedad, esto es por el cambio de alimentación, porque estamos tomando menos azúcar de la que normalmente ingerimos en nuestro día a día ! 
Quizás sientas que el cuerpo te pide más, pero no es hambre, es falta de azúcar. Estamos privando a nuestro organismo de algo que está acostumbrado a tomar y puede que lo notes más estos días !  Contame  qué tal !"""]
    },
    'DIA 7': {
        'messages': ["""Buen día!!!
Wooowww felicitaciones llegamos a la primer semana de todos estos cambios.🥳

Te sentis más deshinchada ? Más adaptada !? Seguro que si ! 😉 En la energía también notarás mucho más ! 
Eso es gracias al batido🥤 ya que esta balanceando nuestra alimentación, proporcionándole a nuestras células todos los nutrientes que necesitan para funcionar correctamente!! 

Si estas yendo a orinar más frecuentemente, es normal. Esto es porque aumentaste el consumo de agua 💦 y por el efecto del Té Herbal, ayuda a eliminar radicales libres de nuestro cuerpo. 

Te recuerdo llenar la ficha de seguimiento para ir viendo tus avances ! 📝
Vamos con todo !💪💪

Alguien de tu entorno ha notado algún cambio de los que me contás?"""]
    },
    'DIA 14': {
        'messages': ["""Hola buen día...
2 semanitas ya junas en este proceso. ✨✨
Como te sentiste esta semana?
Avísame cómo vas ! 

Cómo te te sentís con el grupo de comunidad, lo miras? Te esta sirviendo? 

Recorda llenar tu ficha del día 14 !📝


Ya para cuando se te terminen los productos podes evaluar la posibilidad de comprar con descuento generando un usuario y contraseña (yo te ayudo a hacerlo, es muy fácil) y pedis directo en la página de Herbalife con el 25% de descuento! 👍 te dejo un video de 7’ que te explica cómo es! 

https://youtu.be/L6ZwR5l2w90 """]
    },
    'DIA 21': {
        'messages': ["""Buen día!!! 🤗

FELICITACIONES!!!🎉🎉🎉
Hemos logrado el primer reto, ya 21 dias. 
Son 21 días para crear un nuevo hábito ! Y cómo siempre digo ... es un día a la vez pero es increíble lo que puedes cambiar en días, lo que te habías acostumbrado en meses !

Vamos a llenar la ficha para ver tus avances y sobre todo la FOTO !!!📝📸 Seguramente vamos a notar grandes cambios.

Contame tu experiencia ! Como te has sentido en este proceso.

Quiero que sigamos en contacto para seguir evaluando y corrigiendo si es necesario. Recuerda que tu participación en el grupo de comunidad y tu experiencia es super importante para ayudar a los que recién están comenzando."""]
    },
    'MENSUAL': {
        'messages': ['Se personaliza en base  al cliente ! Lo importante es al menos al menos 1 vez al mes hacer seguimiento.']
    },
    'PROGRAMAR MENSAJES': {
        'messages': ['https://youtu.be/gqHmIQj18Tk']
    },
    'IDEAS POST': {
        'messages': ["""Reto de Transformacion Personal Región SAM/CAM
https://www.estoesherbalife.com/sc/reto-transformacion""",
'https://yosoyherbalifenutrition.com/salud-y-bienestar/ ']
    },
    'RECETAS': {
        'messages': ['FIL:MI_NUTRICION FAVORITA-LIBRO_DE_RECETAS_HERBALIFE.pdf',
            'FIL:Mi-Nutricion-Favorita_Tomo-II.pdf',
            """Recetas de batidos 👇
https://t.me/joinchat/AAAAAEetGY990CnScYq_uA""",
            """Aprende a comer 👇
https://t.me/joinchat/AAAAAEaZ4iGdpyh7JTsXUw""",
            """DRIVE RECETAS
https://drive.google.com/drive/folders/1XFosFLxuxG91HjKyQG7VyCNgWdvZaqWP?usp=sharing""",
            """Canal de Recetas TALLER DE COCINA
https://t.me/joinchat/AAAAAFj9DgDbdMo3AlWPjQ"""]
    },
    'RESULTADO': {
        'messages': ["""Resultados 👇

https://t.me/joinchat/AAAAAEYwJl1RXZfgnkEw9A"""]
    },
    'MARATON 10 DIAS': {
        'messages': ["""La *MARATÓN DE 10 DIAS* es un reto de transformación orientado a generar disciplinas positivas para lograr un bienestar en tan sólo 10 días.
Ser parte de una comunidad activa y entusiasta con objetivos en común te ayudará a lograr resultados increíbles. 

Podrás disfrutar de:
🔥 Plan de alimentación
🔥Plan de entrenamiento
🔥Comunidades entusiastas 
🔥 Clases de alimentación Online
🔥Suplementacion para potenciar tu resultado 
🔥Coach personalizado 24/7
🔥Atractivos premios

Anímate y pierde de *3 a 5 kilos* en tan sólo 10 Días 💪🏻""",'IMG:maraton1.jpg','IMG:maraton2.jpg','IMG:maraton3.jpg','IMG:maraton4.jpg','IMG:maraton5.jpg','IMG:maraton6.jpg']
    },
    "HLOK" : {
        "messages" : ['INVITADO','FLYERS','Tutoriales asociados'], 
        "keyboard" : [['INVITADO'],['FLYERS'],['TUTORIALES']]
    },
    "INVITADO" : {
        "messages" : ['''COMO USAR HLOK: 

1) una vez registrada (con el link que te envie) podes ingresar con tu usuario y contraseña desde cualquier dispositivo a la pagina 

www.hlok.es
2) Vas a las líneas que hay a la  izquierda y seleccionas opción calendario 
3) selecciona día, horario y la actividad .. (las clases son en vivo)
4) automáticamente te redirige a la sala Zoom ! (Recorda activar tu audio en zoom: Abajo a la izquierda te aparece estos signos 🔈🎧 si no escuchas apreta en el signo y marca “llamar a través del audio del dispositivo” ó “marcar utilizando internet”) 
5) listo ✅ disfruta la clase o taller 🌪⚡️❤️

Avísame cuando te registres asi te envío un video que explica como usar bien la página para que aproveches mejor las actividades que vos quieras 😉''',
'''Te envio un video que explica como acceder fácilmente a las actividades y puedas aprovechar nuestra Comunidad Saludable!

Espero que la Disfrutes!

https://youtu.be/krivfCJrJhU ''']
    },
    'FLYERS' : {
        "messages" : ['''CANAL FLYERS 
https://t.me/joinchat/AAAAAFQGYsKMPgqMHrXJZA''']
    },
    'TUTORIALES' : {
        "messages" : ['''Canal TUTORIAL ASOCIADOS
https://t.me/joinchat/AAAAAFFfGGHpY08TNJPcFQ''']
    },
    "CAPACITACION" : {
        "messages" : ['FORMACIONES BÁSICAS','PLANILLAS DE HÁBITOS','AUDIOS', 'MANUAL 4'],
        "keyboard" : [['FORMACIONES BASICAS'],['PLANILLAS DE HABITOS'],['AUDIOS','MANUAL 4']]
    },
    "FORMACIONES BASICAS" : {
        "messages" : ['''Formaciones básicas 👇

https://t.me/joinchat/AAAAAFjhbwSHcIocvXaMMw''','''Usar Llevar y Atraer

https://www.youtube.com/watch?v=O_H6zWWIOKI''']
    },
    "PLANILLAS DE HABITOS" : {
        "messages" : ['''FIL:13-Pasos_para_el_Exito.pdf''','''Modelo de presupuesto finanzas personales 

https://drive.google.com/file/d/1Nj_w8Z5T9qw7pJkcy8sntbdaiGuxYNiV/view?usp=drivesdk''']
    },
    "AUDIOS" : {
        "messages" : ['''JIM ROHN - LA PARABOLA DEL SEMBRADOR

https://www.youtube.com/watch?v=f6i455QJhec''','''CONSTRUYENDO SU RED DE MERCADEO - JIM ROHN

https://www.youtube.com/watch?v=5v9QtjAI-zI''','''Jim Rohn El mejor audio de entrenamiento de Jim Rohn

https://www.youtube.com/watch?v=syheoEE_-ds''','''Cambia tu mentalidad - Eduardo Salazar

https://www.youtube.com/watch?v=NXHB8bXDNmg''']
    },
    "MANUAL 4" : {
        "messages" : ['FIL:AR-LIBRO4.pdf']
    },
     "DESAFIO 5D" : {
        "messages" : ['INVITACIONES','DESAFIO 5D AMIGAS','INFO PARA GRUPOS 5D'],
        "keyboard" : [['INVITACIONES'],['DESAFIO 5D AMIGAS'],['INFO PARA GRUPOS 5D']]
    },
    "INVITACIONES" : {
        "messages" : ['''Hola 😁, cómo estás? 
Te cuento que vamos a comenzar un DESAFÍO 5 DÍAS TOTALMENTE GRATIS ✨ para todos los interesados en:

✔️Bajar de peso
✔️Mejorar su alimentación
✔️Controlar la ansiedad
✔️Aumentar su masa muscular
✔️Crear hábitos saludables

Se realiza por  un grupo de WhatsApp restringido que no tiene interacción, sólo INFORMACIÓN📝

 Recibirás :
1️⃣ Tips saludables para lograr TU OBJETIVO ‼️🥗 
2️⃣ Acceso a Talleres virtuales EN VIVO: cocina saludable,🥘 alimentación correcta👌🏻, yoga🧘🏻‍♀️ y gimnasia funcional🤸🏻‍♀️ con profesores certificados._
3️⃣ RECETAS SALUDABLES, SIMPLES Y RICAS
4️⃣ Durante 5 dias recibiras asesoramiento premium, de parte de tu coach!, con quien en ese periodo podras hacer todo tipo de consultas,como si ya estuvieras participando del 🏵DESAFIO 21 PRO🏵
                                        
⭐️Al finalizar recibirás un regalo para poder continuar avanzando hacia tu MEJOR VERSIÓN.

Si querés participar escribí QUIERO haciendo click en este link👇

wa.me/(coloca tu número celular con el codigo de pais sin 0 y sin 15) 

⚠️Los cupos son limitados💫, por lo que te sugiero te anotes cuanto antes. ''','''RESPUESTA AL GUION DE INVITACION (por WA)''','''Hola! Bienvenid@! 
Como estas? 😃

Mi nombre es ---------! 🙋🏻‍♀️ 
 
Qué bueno que te interese participar en nuestro *DESAFÍO de 5 días totalmente GRATUITO y VIRTUAL!* Te felicito por *_ocuparte de tu bienestar!_*🥰  Recibirás información muy valiosa para _forjar hábitos saludables._ Empezamos un nuevo desafío el próximo *LUNES* .

*Contame* 

✳️ Tu nombre? 
✳️ Tu edad? 
✳️ Que resulatdo estás buscando tener?''','''Excelente!!!! Vamos a pasar una semana muy linda aprendiendo un montón de cosas para dar inicio a los cambios que vos queres conseguir!! 💛 |

Te pido que me agendes así te puedo ir mandando desde el sistema (lista de difusión) información complementaria para optimizar el seguimiento y asegurarnos tu resultado! 🤝💚 No voy a ser para nada invasivo, y si queres dejar de recibir los mensajes me avisas y te saco de la lista ✅ 

*La intención del desafío de 5 dias! Es que puedas recibir valor y herramientas que te ayuden a empezar el cambio!, y además mostrarte un poco la forma de trabajo que tenemos en los *DESAFIOS 21 DÍAS PRO*, en donde el cambio y la transformación es total y permanente! 💚🙌*''','''Te va a encantar 
Podes invitar a 5 personas más si querés. Y me pasas sus nros que los agrego🙌🏻💫''','''LUEGO SE LOS AGREGA AL GRUPO Y A LA LISTA DE DIFUSIÓN!



Felicitaciones por tomar la responsabilidad de tu salud! 💛 Ahora vamos JUNTOS! ''','''IMG:desafio5d.jpg''']
    },
    "DESAFIO 5D AMIGAS" : {
        "messages": ['''Este es un Desafio de whatsapp, donde solo participan amigas de clientas y clientas. 
La idea es que por privado le sugieras a tu cliente la posiblidad de sumar amigos al desafio 5d gratuito y de esta forma si ellos luego se suman al desafio 21d van  avanzar en la escala de descuentos
EJEMPLO (puede ser por audio):
Hola XXX como estas?
Te cuento que estamos armando un desafio 5 dias gratuito para compartir con amigas y amigos!!
Voy a estar acompañadolas en esos días y pasando tips y recetas 
Si tus amigas se suman ...te van ayudar a que puedas tener mas descuento en tus productos..te gusta la idea????''',
'''cuando la clienta dice que si!  se le explica que ella tambien va a estar en el grupo de whatsapp, para darle confianza a sus amigas y se le pide porfavor, que comparta su desayuno, su actividad, y todo lo que ella misma vio de otras que la inspiraron!  tenemos que inspirar a tus amigas !!
De esta manera ya empiezan a hacer la actividad de Coaches sin saberlo.''','''Si necesitan de apoyo para poder invitar a sus amigas.. se les comparte esta foto para que inviten ya q muchas quieren publicarlo en sus redes''',
'''IMG:desafio5damigas.jpg''','''Otra opcion para que compartan''',''' Hola cómo estaaaassssss 🌷💟🌼  ! te cuento que este lunes se hace un desafío de 5 días  #fullDetox, que es totalmente GRATUITO, para mejorar hábitos de alimentación y sumar algo de ejercicio a tu semana ! 💪🏽 solamente se realiza  con amigas de participantes..y como yo estoy, te puedo invitar!!! es genial! 

Avisame y Si queres te sumo para guardarte el lugar y le paso tu numero a mi Coach ✨🍋🌼  🥰!!! 🥳🥳🥳 🕺🙌🏻🌸''']
    },
    "INFO PARA GRUPOS 5D": {
        "messages": ['Sumate a estos canales y usalos como modelo para tu desafio de 5D',
        'https://t.me/joinchat/AAAAAFdkDiup5HFlzmXJMg',
        'https://t.me/joinchat/VRqy4nbwxrexAY48',
        'https://t.me/joinchat/AAAAAFSIgtterMIWVRB8Gg']
    }
}
