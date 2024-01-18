---
url: https://www.youtube.com/watch?v=GCQHZR_cgHo
date: 2024-01-18
---
# CCG 009 - Kuberneteando k6 con Jorge Turrado

<iframe width="560" height="315" src="[https://www.youtube.com/watch?v=GCQHZR_cgHo](https://www.youtube.com/watch?v=GCQHZR_cgHo)" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Invitado(s): [Jorge Turrado](https://www.linkedin.com/in/jorge-turrado-ferrero/)

## Checklist

- [x] Contactar al invitado(s) y mencionarles de Cafe con Grafana.
	> En Grafana Labs, hacemos un show semanal en vivo llamado [Cafe con Grafana](https://www.youtube.com/watch?v=fodMyzisa6s), donde invitamos a genta a hablar sobre grafana y sus subproductos, observabilidad, o visualización. Te vi en [blog post/video/post] en un blogpost de k6 y creemos que seria genial tenerte en el show para traer tu experiencia y platicar de k6.
	Café Con Grafana es una conversacion de una hora transmitida en vivo al [Canal de Grafana en YouTube](https://youtube.com/@grafana). Es muy casual, se puede solo charlar, compartir pantalla, hacer demos, o lo que tu gustes. Si quisieras venir nos daria mucho gusto! 
- [x] Si el invitado acepta, mandar invitacion para la fecha del show. Se debe confirmar el momento, 13:00 UTC (15:00 CEST) en Jueves. Se debe solicitar una foto que se pueda usar para promocionar o de menos permiso para usar su foto de perfil en redes sociales.
- [x] Mandar una invitacion de calendario a la par del bloque de Cafe Con Grafana. Nombrar a la invitacion con el numero de episodio y su nombre. Ejemplo: `Café con Grafana #010 con Pepe Pancho`. Esto para apartar la fecha en calendarios. La invitacion debe ser agendada 15 minutos antes del stream (para checar microfonos y demas) asi como 15 minutos despues (para permitir sacar cualquier información restante). Tiempo total de la invitacion 1.5 horas.
- [x] Crear imagen thumbnail en [Canva](https://canva.com) usando el formato de Café con Grafana. Usar [thumbsup.tv](https://thumbsup.tv) para revisar que el thumbnail se vea bien en diferentes dispositivos. LA IMAGEN YA ESTÁ EN LA CARPETA DE CANVA https://www.canva.com/folder/FAFuWGuLXes
- [x] Agendar transmisión en [Streamyard](https://streamyard.com), y seleccionar el canal de Grafana en YouTube como destino.
	- [x] Incluir en el titulo el numero de episodio, Ejemplo: `(Spanish) Kuberneteando con k6 (Café con Grafana #009)`.
	- [x] Agregar la descripcion de estandar de episodio. Agregar los contactos de los invitados.

'''
	Hoy vamos a echar un café con Jorge Turrado, un SRE en Lidl International Hub, MVP de Microsoft por 5 años, y Embajador de CNCF entre otras cosas.
	El nos viene a platicar como exprime los recursos y provee una plataforma para que los developers puedan hacer sus test de carga de manera sencilla. Para esto se apoya mucho en k6 operator pero también componentes propios de Kubernetes para los que hacen operadores.
	Ademas nos contará de las mezclas que usan imitando KEDA usando abstracciones de helm, configMaps, Persistent Volumes y mucho mas!
	Una mezcla loca de experiencias y detalles que no se pueden perder!

	Contacto Jorge:
	LinkedIn: https://www.linkedin.com/in/jorge-turrado-ferrero/
	GitHub: https://github.com/JorTurFer
	X: https://twitter.com/JorgeTurrado

	Contacto Imma:
	LinkedIn: https://www.linkedin.com/in/imma-valls/
	GitHub: https://github.com/immavalls
	X: https://twitter.com/eyeveebee

	Contacto Nicole:
	Mastodon: https://pkm.social/@nicole
	GitHub: https://github.com/nicolevanderhoeven
	Site: https://nicolevanderhoeven.com

	Contacto Antonio:
	LinkedIn: https://www.linkedin.com/in/antonio-cm/
	GitHub: https://github.com/tonypowa

	Contacto Leandro:
	Linkedin: https://www.linkedin.com/in/leandromelendez/
	GitHub: https://github.com/SrPerf
	X: https://twitter.com/SrPerf

	Mas acerca de Grafana Labs:
	Website: https://grafana.com
	Repo: https://github.com/grafana/grafana
'''
- [x] Obtener el link de invitacion a Streamyard y con él actualizar la ubicación en la invitación de calendario enviada al invitado.
- [x] Obtener el link de Youtube del show. Agregarlo a esta pagina en la URL del inicio.
- [x] Crear el evento y anunciarlo [en la pagina de Meetup de Grafana](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [x] Agendar mensajes para el momento del inicio del show diciendo "(In Spanish) Cafe con Grafana empieza transmisión!"
	- [x] Agendar un mensaje similar en el Slack interno de Grafana  (en `#community`).
	- [x] Agendar un mensaje similar en el Slack interno de Grafana  (en `#social-grafañol`).
	- [x] Agendar un mensaje similar en el Slack público de Grafana  (en `#grafañol`)
	- [x] Agendar un mensaje similar en el Slack público de Grafana  (en `#announcements`)
- [x] Hacer posts en redes sociales para promocionar el episodio
- [x] Agregar episodio e información a los calendarios "Grafana Community" y "Grafana Labs Events"


## Puntos a hablar

> Listar los puntos que se hablarán en el episodio. Mantenerse solo en puntos breves para que el episodio sea una conversacion y fluya con naturaleza. Que no se sienta scripteado.

- Intro
	- *Bienvenidos a la hora de echar un Cafe con Grafana. Somos Antonio, Imma y Leandro, Dev Advocates en Grafana y hoy hablaremos de k6 y kubernetes y para ello traemos a Jorge Turrado.*
- Introducir invitado
	- Quien eres?
	- A que te dedicas?
	- Cuanto llevas usando productios de Grafana?
- Temas a hablar
	- Platicanos un poco de lo que haces en tu dia a dia?
	- Que es Kubernetes?
	- Que es KEDA?
	- Que es lo que han implementado? 
	- ~Muestranos que se logra?~ (Tarda >1 hora, así que no vamos a ver demo, solo como lo organizamos)
 	- Y en el mundo real (nuesto caso en KEDA es bastante especialito), como usais esto en SCRM?
	- Demo time! (es casi lo mismo que KEDA, así que no vamos a tener problema y HTTP es más rápido para ver la idea)
	- <<Algun otro tema? @nicolevanderhoeven @antonio @JorTurFer>>
   	- {antonio] Cuentanos sobre algun caso en el que hayas utilizado k6 para pruebas de rendimiento.¿Qué dificultades tuviste y cómo las resolviste?
   	- {antonio]¿Qué estrategias empleas para garantizar que las pruebas de rendimiento sigan siendo eficaces a medida que evoluciona vuestra aplicación?
   	- {antonio] ¿Cómo te mantienes al día de los avances en metodologías y herramientas de pruebas de rendimiento, incluidas las actualizaciones de k6?
	- Que otras cosas has hecho?
- Anuncios
	- ObservabilityCon de Grafana manden CFPs e inscribanse!
 	- Tenemos Meetup.com en español! Estén al dia con este show y mas https://www.meetup.com/grafana-friends-virtual-en-espanol/
	- Nuev video y serie de Lisa Jung: https://youtu.be/TQur9GJHIIQ
- Cierre
	- Donde puede la gente aprender mas de el tema?
	- Donde te puede seguir/contactar la gente?
	- Algun anuncio para tu abuelita o mamá o hijos?
	- Mas anuncios de cierre

### 15 minutos antes

> Que hablar y arreglar con el invitado los 15 minutos antes de la transmision.

- [ ] Que pronombres usas?
- [ ] Avisar de los puntos a tratar y que son guia pero nada mas. Es una conversación libre.
- [ ] Si alguien va a compartir pantalla, hay que hacerlo ahi. Para ver que funciona y arreglar cualquier detalle.
- [ ] Avisar que va a poder ver comentarios de YouTube, pero si necesita compartir algo o links, hay que pasarlos de una vez en el chat privado o durante el show.
- [ ] Usa el chat privado si nos quieres decir algo, o dilo en el show en alto si lo deseas.
- [ ] Si te sientes incomodo con algun tema, dilo abiertamente o en privado en el chat.
- [ ] Al final vamos a despedirnos, pero quedate despues para platicar como estuvo el show.
- [ ] Si algo pasa y pierdo conexion... mantente ahi por un momento y estaremos de regreso.

## Despues de la transmision

- [ ] Agregar timestamps al video (minimo 4).
- [ ] Agregar los links compartidos en la descripcion del video.
- [ ] Agregar el video a los playlists de contenido en español.
