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
    'IMG:IMAGEN2.png', 
    '''Estos son los 3 productos basicos!\n
    Batido Nutricional:\n
    Es una comida completa, que te aporta todos los nutrientes que necestias, y tiene las mismas calorias que una manzana🍎!, al igual que todos los productos Herbalife, son naturales, y por eso es que no tienen contraindicaciones y todo el mundo los puede tomar, incluso embarazadas, lactantes y niños!!\n
    Te va a dar saciedad, energia a full🔋!!!!, Como reemplaza comidas, hace que bajes el exceso de grasa de manera natural! Y como tiene proteina de soja,  te vas a ver tonificada enseguida🏃🏼‍♀️!!\n\n
    Te de Hierbas:\n
    Es una bebida a base de Te verde concentrado, y Te negro!!, Si sentis cansancio o desgano durante el dia, este es tu nuevo mejor amigo🤝!, Ademas, tiene una propiedad que acelera el metabolismo, o sea que vas a ir "quemando grasita extra" mientras haces tus actividades del dia. Le decimos el GYM de bolsillo🏃🏼‍♀️!\n\n
    Aloe Vera:\n
    Amo este producto!, Ayuda a desintoxicar el aparato digestivo!! Te da una sensacion de alivio inmediato, y al pasar los dias, vas a sentir como te regularizas intestinalmente♻️! Al limpiar el aparato digestivo, permitis que absorba mayor cantidad de nutrientes, de las comidas, y obvio del Batido!!, Los cambios son muy notorios en poco tiempo✅!''',
    'IMG:IMAGEN3.jpg',
    '''Proteina:\n
    Este producto te va a dar super saciedad, pero lo mas importante es que contribuye con practicamente todas las funciones vitales y los sistemas del cuerpo🙋🏼‍♀️!, Ayuda a construir masa muscular de manera natural. Te cuento que el musculo "se alimenta de la grasa" para ganar energia, y por eso es que cuanto mas musculo creas, mas grasa eliminas😉!!, para descenso de peso, si podes añadir este producto en tu plan, vas a ver cambios enseguida!!'''
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
        'keyboard': [['PRE PRODUCTO', 'DIA 0'],['DIA 1','DIA 2','DIA 3'],['DIA 7','DIA 14','DIA 21'],['MENSUAL','PROGRAMAR MENSAJES']['IDEAS POST','RECETAS','RESULTADO']]
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
            'GUIA PARA ARMAR PLATOS','recetas saladas','recetas dulces',
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
🍽CENA como en el almuerzo.""",'GUIA DE BIENESTAR']
    }
}


