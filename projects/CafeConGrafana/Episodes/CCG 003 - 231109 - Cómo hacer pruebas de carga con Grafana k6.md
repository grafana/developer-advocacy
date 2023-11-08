---
url: https://youtube.com/live/NF2R-Zk9iek
date: 2023-11-09
---
# CCG 003 - Todo sobre k6 con Daniel Gonzalez Lopes

<iframe width="560" height="315" src="https://www.youtube.com/embed/NF2R-Zk9iek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Invitado(s): [Daniel Gonzalez Lopes](https://www.linkedin.com/in/danielgonzalezlopes/)

## Checklist

- [x] Contactar al invitado(s) y mencionarles de Cafe con Grafana.
	> En Grafana Labs, hacemos un show semanal en vivo llamado [Cafe con Grafana](https://www.youtube.com/watch?v=fodMyzisa6s), donde invitamos a genta a hablar sobre grafana y sus subproductos, observabilidad, o visualización. Te vi en [blog post/video/post] en un blogpost de k6 y creemos que seria genial tenerte en el show para traer tu experiencia y platicar de k6.
	Café Con Grafana es una conversacion de una hora transmitida en vivo al [Canal de Grafana en YouTube](https://youtube.com/@grafana). Es muy casual, se puede solo charlar, compartir pantalla, hacer demos, o lo que tu gustes. Si quisieras venir nos daria mucho gusto! 
- [x] Si el invitado acepta, mandar invitacion para la fecha del show. Se debe confirmar el momento, 13:00 UTC (15:00 CEST) en Jueves. Se debe solicitar una foto que se pueda usar para promocionar o de menos permiso para usar su foto de perfil en redes sociales.
- [x] Mandar una invitacion de calendario a la par del bloque de Cafe Con Grafana. Nombrar a la invitacion con el numero de episodio y su nombre. Ejemplo: `Café con Grafana #010 con Pepe Pancho`. Esto para apartar la fecha en calendarios. La invitacion debe ser agendada 15 minutos antes del stream (para checar microfonos y demas) asi como 15 minutos despues (para permitir sacar cualquier información restante). Tiempo total de la invitacion 1.5 horas.
- [x] Crear imagen thumbnail en [Canva](https://canva.com) usando el formato de Café con Grafana. Usar [thumbsup.tv](https://thumbsup.tv) para revisar que el thumbnail se vea bien en diferentes dispositivos. LA IMAGEN YA ESTÁ EN LA CARPETA DE CANVA https://www.canva.com/folder/FAFuWGuLXes
- [x] Agendar transmisión en [Streamyard](https://streamyard.com), y seleccionar el canal de Grafana en YouTube como destino.
	- [x] Incluir en el titulo el numero de episodio, Ejemplo: `(In Spanish) Todo sobre k6 (Café con Grafana #003)`.
	- [x] Agregar la descripcion de estandar de episodio. Agregar los contactos de los invitados.
- [x] Obtener el link de invitacion a Streamyard y con él actualizar la ubicación en la invitación de calendario enviada al invitado.
- [x] Obtener el link de Youtube del show. Agregarlo a esta pagina en la URL del inicio.
- [x] Crear el evento y anunciarlo [en la pagina de Meetup de Grafana en español](https://www.meetup.com/grafana-friends-virtual-en-espanol/).
- [ ] Agendar un tweet para el momento del inicio del show diciendo "(In Spanish) Cafe con Grafana empieza transmisión!"
- [x] Agendar un mensaje similar en el Slack interno de Grafana  (en `#community`).
- [x] Agendar un mensaje similar en el Slack interno de Grafana  (en `#social-grafañol`).
- [x] Agendar un mensaje similar en el Slack público de Grafana  (en `#grafañol`)
- [x] Agendar un mensaje similar en el Slack público de Grafana  (en `#announcements`)


## Puntos a hablar

> Listar los puntos que se hablarán en el episodio. Mantenerse solo en puntos breves para que el episodio sea una conversacion y fluya con naturaleza. Que no se sienta scripteado.

- Intro
	- *Bienvenidos a la hora de echar un Cafe con Grafana. Somos Antonio y Nicole, Dev Advocates en Grafana y hoy hablaremos de k6: qué es, cómo usarlo, y todo. Después de este episodio, ustedes podrán lanzar pruebas de carga usando k6.*
- Anuncios
	- Leandro no está aquí, pero tiene una razón muy buena...
- Introducir invitado: Daniel
	- Quien eres?
	- A que te dedicas?
	- Cuanto llevas usando Grafana (o algun otro)?
	- Cuanto llevas usando k6?
- Qué es k6?
	- open source
	- Go + JavaScript
	- Es solo para performance testing?
	- Instalación + Scripting
		- (Demo - Daniel) QuickPizza y cómo instalar y comenzar con k6
			- Usare ejemplos en de el folder fundamentals the k6 en quickpizza
	- Modos de ejecución
		- `k6 run test.js`
- Analisis de resultados
	- k6 dashboard
	- Prometheus Remote Write // Prometheus + Grafana
- Qué es GCk6?
	- Cuál es la diferencia entre k6 Cloud y Grafana Cloud?
	- Como se integran?
		- `k6 run test.js -o cloud`
		- `k6 cloud test.js`
- Extensiones de k6
	- Maneras de extender k6, con ejemplos de los más populares/nuestros favoritos
		- JavaScript (jslib)
		- Go (xk6)
			- [xk6-dashboard](https://github.com/grafana/xk6-dashboard)
			- [xk6-disruptor](https://github.com/grafana/xk6-disruptor)
			- [xk6-kubernetes](https://github.com/grafana/xk6-kubernetes)
			- [k6-operator](https://github.com/grafana/k6-operator)
			- [k6x](https://github.com/szkiba/k6x)
		- módulos experimentales
			- [k6 redis](https://k6.io/docs/javascript-api/k6-experimental/redis/)
			- [k6 websockets](https://k6.io/docs/javascript-api/k6-experimental/websockets/)
			- [k6 timers](https://k6.io/docs/javascript-api/k6-experimental/timers/)
			- [k6 tracing](https://k6.io/docs/javascript-api/k6-experimental/tracing/)
			- [k6 browser](https://k6.io/docs/javascript-api/k6-browser/)
- Integraciones entre k6 y el ecosistema Grafana
	- Grafana
	- Prometheus
	- Loki
	- Tempo
	- Faro
	- Cuál es la relación entre pruebas y observabilidad?
- Cierre
	- Dónde puede la gente aprender más de k6?
	- Dónde te puede seguir/contactar la gente?
	- Este viernes en Grafana Office Hours tenemos a Daniel y nuestra otra colega, Olha Yevtushenko. Vamos a hablar de k6, pero en particular el uso de k6-operator y private load zones para hacer pruebas distribuidas con k6 en Kubernetes.

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
