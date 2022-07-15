use cine;



/*INSERTS FOR TABLE BEBIDA*/
INSERT INTO bebida VALUES(1,'Manzana 500 ml', 6000);
INSERT INTO bebida VALUES(2,'Manzana 1.5 L', 12000);

INSERT INTO bebida VALUES(3,'Uva 500 ml', 6000);
INSERT INTO bebida VALUES(4,'Uva 1.5 L', 12500);

INSERT INTO bebida VALUES(5,'Colombiana 500 ml', 5800);
INSERT INTO bebida VALUES(6,'Colombiana 1.5 L', 11000);

INSERT INTO bebida VALUES(7,'Pepsi 500 ml', 6000);
INSERT INTO bebida VALUES(8,'Pepsi 1.5 L', 11500);

INSERT INTO bebida VALUES(9,'Naranja 500 ml', 5500);
INSERT INTO bebida VALUES(10,'Naranja 1.5 L', 11000);

INSERT INTO bebida VALUES(11,'Natu Malta 500 ml', 5000);
INSERT INTO bebida VALUES(12,'Agua 500 ml', 3000);


/*INSERTS FOR TABLE ALIMENTOS*/
INSERT INTO alimento VALUES(1, 'Perro caliente', 10000, 1, 'https://cdn.pixabay.com/photo/2012/02/29/16/12/hot-19456_960_720.jpg');
INSERT INTO alimento VALUES(2, '2 Perro caliente', 20000, 2, 'https://images.pexels.com/photos/4113463/pexels-photo-4113463.jpeg?auto=compress&cs=tinysrgb&w=600');

INSERT INTO alimento VALUES(3, 'Hamburguesa', 12000, 3, '');
INSERT INTO alimento VALUES(4, '2 Hamburguesa', 22000, 4, '');

INSERT INTO alimento VALUES(5, 'Sándwich', 9000, 5, '');
INSERT INTO alimento VALUES(6, '2 Sándwich', 19000, 6, '');

INSERT INTO alimento VALUES(7, 'Papas fritas', 8000, 7, '');
INSERT INTO alimento VALUES(8, 'Combo Papas fritas', 20000, 8,'');

INSERT INTO alimento VALUES(9, 'Hamburguesa con queso', 13000, 9, '');
INSERT INTO alimento VALUES(10, '2 Hamburguesa con queso doble', 21000, 10, '');


/*INSERTS FOR TABLE TEATROS*/
INSERT INTO teatro VALUE(1,'El Eden','Bogotá', 'https://cdn.pixabay.com/photo/2018/03/09/01/20/city-3210384_960_720.jpg');
INSERT INTO teatro VALUE(2,'Americano','Barranquilla', 'https://cdn.pixabay.com/photo/2019/03/26/17/52/barranquilla-4083262_960_720.jpg');
INSERT INTO teatro VALUE(3,'Santa Lucia','Neiva', 'https://www.hotelneivaplaza.com/assets/cache/uploads/1400x933/portada.jpg');
INSERT INTO teatro VALUE(4,'El Caraño','Quibdó', 'https://www.portafolio.co/files/article_multimedia/uploads/2019/05/17/5cded0c63393d.jpeg');
INSERT INTO teatro VALUE(5,'Ocean Mall','Santa Marta', 'https://cdn.pixabay.com/photo/2020/03/13/18/00/colombia-4928729_960_720.jpg');


/*INSERTS FOR TABLE SERVICES*/
INSERT INTO servicio VALUES(1,'Espacios Publicitarios', 
'Coloque su marca en un alto tráfico con que cuentan nuestras salas de cine, 
promocione su producto con mayor eficacia con los servicios de stand, rompe-tráfico, dummies, adhesivos, muestreos, pendones. 
El BTL es más directo al requerir una segmentación más minuciosa, permitiendo así una relación más directa con el consumidor. 
Espacios de alto tráfico: salas y lobbies. Paute tambén en cajas y vasos de nuestra cafetería.', 
'Cineworld no se hace responsable por el material entregado por parte del cliente. 
El material debe ser entregado disco extraíble (USB) o transferencia vía web. 
La entrega debe hacerse minimo con 6 días de anticipación. 
La producción del material es a cargo del cliente.', 'https://cdn.pixabay.com/photo/2019/07/27/17/56/london-underground-4367265_960_720.jpg');

INSERT INTO servicio VALUES(2,'Festejo de Cumpleaños', 
'Festeje los cumpleaños de sus hijos, amigos, familiares y compañeros de oficina o empresa en las instalaciones de Cineland, 
podrá elegir el paquete que ofrecemos y disfrutar con las personas que más quieres. Incluye refrigerio, 
tarjeta de invitación y material visual gráfico relacionada a la película (según disponibilidad).', 
'Se realiza el evento a un mínimo de 15 cupos. No incluye el valor de acompañantes (padres, hermanos, familiares o encargados). 
Para las funciones 3d se venderán las gafas 3d para observar la película, 
aquellos que posean del articulo pueden llevarla sin ninguna restricción. 
No incluye torta y está prohibida la entrada de bebidas y alimentos.', 'https://cdn.pixabay.com/photo/2016/11/18/15/47/birthday-1835449_960_720.jpg');

INSERT INTO servicio VALUES(3,'Salon de Eventos', 
'Festeje sus eventos como festejo de cumpleños a sus hijos, amigos, familiares, 
compañeros de oficina o empresa en las instalaciones de Cineworld. 
Podrá elegir el paquete que ofrecemos y disfrutar con las personas que más quieres. 
Capacida maxíma para 25 personas. Disponible: Mayales, Suchiimma, Santa Lucía, De Moda', 
'El alquiler se hace mínimo para 1 hora. No incluye decoraciones.', 'https://cdn.pixabay.com/photo/2014/08/31/10/03/theater-432045_960_720.jpg');

INSERT INTO servicio VALUES(4,'Funciones Privadas', 
'En Cineworld disfruta con tu empresa, colegios, instituciones, empresas o amigos el 
privilegio de adquirir una función especial en forma económica y exclusiva para todos sus asistentes de los estrenos semanales. 
Seleccione la película de su preferencia , disfrute el momento con nuestros productos de comida en combos con precios especiales. 
Contamos con más de 46 salas a nivel nacional.', 
'Condiciones Válido unicamente en horas de la mañana. Sólo es prestado a un mínimo de 100 cupos. 
Aplica para cualquier sala de cine Cineland. Para las funciones 3d se venderán las gafas 3d para observar la película, 
aquellos que posean del articulo pueden llevarla sin ninguna restricción.', 'https://cdn.pixabay.com/photo/2017/08/09/15/33/private-function-2614908_960_720.jpg');

INSERT INTO servicio VALUES(5,'Alquiler de Salas', 
'Realice sus conferencias, reuniones y capacitaciones a nivel empresarial e institucional donde puede desarrollar 
todo su potencial Contamos con cómodas sillas, proyección y sonido digital de alta calidad y 
una buena atención que merecen sus asistentes Utilice nuestras salas para conferencias, lanzamientos, capacitaciones, seminarios, 
congresos o diferentes reuniones de carácter empresarial o académico Cautive por completo a sus espectadores.', 
'Se realizan alquileres únicamente en horarios no comerciales solamente en las mañanas. 
Proyección de sus contenidos en las salas digitales. Servicio de alimentación. Aplican condiciones y restricciones.',
'https://cdn.pixabay.com/photo/2017/05/18/11/04/key-2323278_960_720.jpg');

/*INSERTS FOR TABLE QUEJAS*/
INSERT INTO queja VALUES(1, 'juan1@gmail.com', 'Juan Gonzalez', 3125675634, 'Solicitud de información', 'Hola, necesito información acerca de las salas de cine.', 1);
INSERT INTO queja VALUES(2, 'felipe2@gmail.com', 'Felipe Vargas', 3137892990, 'Sugerencias', 'Hola, para el alquiler de salas sugiero que sean más organizados.', 1);
INSERT INTO queja VALUES(3, 'ramirez@gmail.com', 'Mateo Ramirez', 3201235463, 'Quejas y reclamos', 'Hola, por favor necesito que me duelvan el dinero de la entrada.', 1);

INSERT INTO queja VALUES(4, 'alejandro4@gmail.com', 'Alejandro Mera', 3237680232, 'Empleo', 'Hola, necesito información para aplicar al empleo.', 2);
INSERT INTO queja VALUES(5, 'maria@gmail.com', 'Maria lopez', 3242349870, 'Sugerencias', 'Hola, sugiero que mejoren las comida.', 2);
INSERT INTO queja VALUES(6, 'gabriela@gmail.com', 'Gabriela Martinez', 3218279291, 'Quejas y reclamos', 'Hola, me voy a quejar por publicidad engañosa.', 2);

INSERT INTO queja VALUES(7, 'carlos3@gmail.com', 'Carlos Hernandez', 3125612634, 'Otros', 'Hola, muchas felicitaciones, buen servicio.', 3);
INSERT INTO queja VALUES(8, 'hugo98@gmail.com', 'Hugo Bocanegra', 3137892886, 'Sugerencias', 'Hola, sugiero que sean estrictos con los empleados.', 3);
INSERT INTO queja VALUES(9, 'martin90@gmail.com', 'Martin Ariza', 3196769890, 'Solicitud de información', 'Hola, necesito saber cuando se estrena Avatar 2.', 3);

INSERT INTO queja VALUES(10, 'lucas67@gmail.com', 'Lucas Acevedo', 3115575634, 'Empleo', 'Hola, que habilidades necesito para ser recepcionista.', 4);
INSERT INTO queja VALUES(11, 'leonel@gmail.com', 'Leonel Valderrama', 3207250912, 'Otros', 'Hola, muchas felicitaciones por el servicio.', 4);
INSERT INTO queja VALUES(12, 'daniel30@gmail.com', 'Daniel Zabala', 3237638279, 'Sugerencias', 'Hola, sugiero que limpien las salas.', 4);

INSERT INTO queja VALUES(13, 'pablo48@gmail.com', 'Pablo Rodriguez', 3189802312, 'Otros', 'Hola, muchas felicitaciones.', 5);
INSERT INTO queja VALUES(14, 'alvaro89@gmail.com', 'Alvaro Valencia', 3129839282, 'Sugerencias', 'Hola, reparen las pantallas.', 5);
INSERT INTO queja VALUES(15, 'diego34@gmail.com', 'Diego Diaz', 3218379282, 'Empleo', 'Hola, a cuál es el proceso para aplicar al empleo.', 5);


/*INSERTS FOR TABLE SOLICITUDES*/
INSERT INTO solicitud VALUES(1, 'juan1@gmail.com', 'Juan Gonzalez', 3125675634, 'Hola, estoy interesado en poner publicidad en sus salas.', 1, 5);
INSERT INTO solicitud VALUES(2, 'felipe2@gmail.com', 'Felipe Vargas', 3137892990,'Hola, necesito un salón para un evento.', 3,5);
INSERT INTO solicitud VALUES(3, 'ramirez@gmail.com', 'Mateo Ramirez', 3201235463, 'Hola, quiero alquilar una sala para ver un pelicula.', 5,5);

INSERT INTO solicitud VALUES(4, 'alejandro4@gmail.com', 'Alejandro Mera', 3237680232,'Hola, cómo es el proceso para festejar un cumpleaños.',2, 4);
INSERT INTO solicitud VALUES(5, 'maria@gmail.com', 'Maria lopez', 3242349870, 'Hola, deseo poner publicidad en su instalaciones.',1, 4);
INSERT INTO solicitud VALUES(6, 'gabriela@gmail.com', 'Gabriela Martinez', 3218279291, 'Hola, quiero adquirir un salón de eventos.',3, 4);

INSERT INTO solicitud VALUES(7, 'carlos3@gmail.com', 'Carlos Hernandez', 3125612634, 'Hola, deseo alquilar una sala.',5, 3);
INSERT INTO solicitud VALUES(8, 'hugo98@gmail.com', 'Hugo Bocanegra', 3137892886,  'Hola, quiero hacer una función privada.', 4,3);
INSERT INTO solicitud VALUES(9, 'martin90@gmail.com', 'Martin Ariza', 3196769890,  'Hola, necesito un salón de eventos', 3,3);

INSERT INTO solicitud VALUES(10, 'lucas67@gmail.com', 'Lucas Acevedo', 3115575634,'Hola, quiero celebrar un cumpleaños.',2, 2);
INSERT INTO solicitud VALUES(11, 'leonel@gmail.com', 'Leonel Valderrama', 3207250912,'Hola, por favor me dan información para alquilar una sala.',5, 2);
INSERT INTO solicitud VALUES(12, 'daniel30@gmail.com', 'Daniel Zabala', 3237638279, 'Hola, quiero poner publicidad, más información.',1, 2);

INSERT INTO solicitud VALUES(13, 'pablo48@gmail.com', 'Pablo Rodriguez', 3189802312,'Hola, información para adquirir un salón de eventos.',3, 1);
INSERT INTO solicitud VALUES(14, 'alvaro89@gmail.com', 'Alvaro Valencia', 3129839282, 'Hola, que requiero para poner un aviso.', 1,1);
INSERT INTO solicitud VALUES(15, 'diego34@gmail.com', 'Diego Diaz', 3218379282, 'Hola, cuánto cuesta una función privada.',4, 1);

/*INSERTS FOR TABLE PELICULAS*/
INSERT INTO pelicula VALUES(1, 'Doctor Strange en el multiverso de la locura', 126, 'superhéroes', 'El Dr. Stephen Strange abre un portal al multiverso al utilizar un hechizo prohibido. Ahora, su equipo debe enfrentarse a una amenaza que podría destruirlo todo.',
'https://www.youtube.com/watch?v=KREBGtEeW9U', 'Sam Raimi', 'Benedict Cumberbatch, Elizabeth Olsen, Chiwetel Ejiofor, Benedict Wong', 1, 
'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/OO6WGPSOYFCXVHBYNYZWKNTEDI.jpg');

INSERT INTO pelicula VALUES(2, 'Garra', 117, 'Comedia dramática, Deportes', 'Un cazatalentos de baloncesto sin suerte descubre a un jugador extraordinario en Madrid y lo lleva a los Estados Unidos sin haber recibido una autorización previa del equipo para el que trabaja.',
'https://www.youtube.com/watch?v=lvRWUIUoaqU', 'Jeremiah Zagar', 'Adam Sandler, Queen Latifah, Ben Foster, Juancho Hernangómez', 1, 
'https://www.aceprensa.com/wp-content/uploads/2022/06/garra.jpg');

INSERT INTO pelicula VALUES(3, 'La ciudad perdida', 112, 'Aventuras, acción y comedia', 'La escritora solitaria Loretta Sage escribe sobre lugares exóticos en sus populares novelas de aventuras con un atractivo modelo de portada, Alan. Mientras está de gira promocionando su nuevo libro, es secuestrada por un excéntrico multimillonario.',
'https://www.youtube.com/watch?v=2kzxPG4cz2g', 'Aaron Nee', 'Sandra Bullock, Channing Tatum, Daniel Radcliffe', 1, 
'https://pics.filmaffinity.com/La_ciudad_perdida-223738504-large.jpg');

INSERT INTO pelicula VALUES(4, 'Morbius', 104, 'Acción, Fantasía oscura, Ciencia ficción', 'Ambientada en el universo de Spider Man, se centra en uno de sus villanos más icónicos, Morbius, un doctor que tras sufrir una enfermedad en la sangre y fallar al intentar curarse, se convirtió en un vampiro.', 
'https://www.youtube.com/watch?v=EA4v3wl7faA', 'Daniel Espinosa', 
'Jared Leto, Matt Smith, Adria Arjona, Jared Harris', 1, 
'https://es.web.img3.acsta.net/pictures/22/02/10/13/16/1386612.jpg');

INSERT INTO pelicula VALUES(5, 'Sonic 2', 122, 'Comedia, acción y aventuras', 'Después de establecerse en Green Hills, Sonic quiere demostrar que tiene madera de héroe. La prueba de fuego llega con el retorno del malvado Robotnik, y su nuevo compinche, Knuckles, en busca de una esmeralda que destruye civilizaciones.',
'https://www.youtube.com/watch?v=YlkN8K2oOMo', 'Jeff Fowler', 'Jim Carrey, James Marsden, Tika Sumpter, Adam Pally', 1, 
'https://es.web.img3.acsta.net/pictures/22/02/18/10/20/5195258.jpg');


INSERT INTO pelicula VALUES(6, 'Moonfall', 120, 'Acción, Catástrofes, Ciencia ficción', 'Una fuerza misteriosa golpea a la Luna fuera de su órbita y la envía en choque directo contra la Tierra a toda velocidad. Unas semanas antes del impacto con el mundo al borde de la aniquilación, la ejecutiva de la NASA y ex astronauta Jo Fowler está convencida de tener la clave para salvar nuestro planeta.',
'https://www.youtube.com/watch?v=CLRxtNfjqlM', 'Roland Emmerich', 'Halle Berry, Patrick Wilson, John Bradley-West, Michael Peña', 0, 
'https://pics.filmaffinity.com/Moonfall-196397735-large.jpg');


INSERT INTO pelicula VALUES(7, 'Red', 100, 'Aventura, Comedia, Animación', 'Mei Lee, una niña de 13 años un poco rara pero segura de sí misma, que se debate entre seguir siendo la hija obediente que su madre quiere que sea y el caos de la adolescencia.',
'https://www.youtube.com/watch?v=5IdjR-8MNSE', 'Domee Shi', 'Rosalie Chiang, Sandra Oh, Maitreyi Ramakrishnan', 0, 
'https://es.web.img3.acsta.net/pictures/21/11/17/16/03/3925548.jpg');

INSERT INTO pelicula VALUES(8, 'Umma', 83, 'Sobrenatural, Suspenso', 'Umma, que es la palabra coreana para madre, relata la historia de Amanda (Sandra Oh) y su hija (Fivel Stewart) que viven una vida tranquila en una granja estadounidense, pero cuando los restos de su madre llegan de Corea, Amanda se ve atormentada.',
'https://www.youtube.com/watch?v=QQdXvvtu-iI', 'Iris Shim', 'Sandra Oh, Fivel Stewart, Dermot Mulroney, Odeya Rush', 0, 
'https://pics.filmaffinity.com/Umma-553762298-large.jpg');

INSERT INTO pelicula VALUES(9, 'The Contractor', 103, 'Acción, Suspenso', 'Cuando su nueva misión sale mal, un soldado de élite se encuentra atrapado en una peligrosa conspiración y luchando para mantenerse con vida el tiempo suficiente para llegar a casa y descubrir los verdaderos motivos de quienes lo traicionaron.',
'https://www.youtube.com/watch?v=e7glvM8Xh0w', 'Tarik Saleh', 'Chris Pine, Ben Foster, Gillian Jacobs', 0, 
'https://pics.filmaffinity.com/The_Contractor-413096848-large.jpg');

INSERT INTO pelicula VALUES(10, 'The Batman', 176, 'Suspenso, Crimen, Drama, Superhéroes', 'En su segundo año luchando contra el crimen, Batman explora la corrupción existente en la ciudad de Gotham y el vínculo de esta con su propia familia. Además, entrará en conflicto con un asesino en serie conocido como "el Acertijo".',
'https://www.youtube.com/watch?v=fWQrd6cwJ0A', 'Matt Reeves', 'Robert Pattinson, Zoë Kravitz, Paul Dano, Jeffrey Wright', 0, 
'https://es.web.img3.acsta.net/pictures/22/01/27/16/40/2914301.jpg');



/*INSERTS FOR TABLE TEATROS-ALIMENTOS*/
/*teatro Bogotá*/
INSERT INTO teatro_alimento VALUES(1,1);
INSERT INTO teatro_alimento VALUES(1,2);
INSERT INTO teatro_alimento VALUES(1,3);
INSERT INTO teatro_alimento VALUES(1,4);
INSERT INTO teatro_alimento VALUES(1,5);
INSERT INTO teatro_alimento VALUES(1,6);
INSERT INTO teatro_alimento VALUES(1,7);
INSERT INTO teatro_alimento VALUES(1,8);
INSERT INTO teatro_alimento VALUES(1,9);
INSERT INTO teatro_alimento VALUES(1,10);

/*teatro Barranquilla*/
INSERT INTO teatro_alimento VALUES(2,1);
INSERT INTO teatro_alimento VALUES(2,2);
INSERT INTO teatro_alimento VALUES(2,3);
INSERT INTO teatro_alimento VALUES(2,4);
INSERT INTO teatro_alimento VALUES(2,5);

/*teatro Neiva*/
INSERT INTO teatro_alimento VALUES(3,6);
INSERT INTO teatro_alimento VALUES(3,7);
INSERT INTO teatro_alimento VALUES(3,8);
INSERT INTO teatro_alimento VALUES(3,9);
INSERT INTO teatro_alimento VALUES(3,10);

/*teatro Quibdó*/
INSERT INTO teatro_alimento VALUES(4,1);
INSERT INTO teatro_alimento VALUES(4,3);
INSERT INTO teatro_alimento VALUES(4,5);
INSERT INTO teatro_alimento VALUES(4,7);
INSERT INTO teatro_alimento VALUES(4,9);

/*teatro Santa Marta*/
INSERT INTO teatro_alimento VALUES(5,2);
INSERT INTO teatro_alimento VALUES(5,4);
INSERT INTO teatro_alimento VALUES(5,6);
INSERT INTO teatro_alimento VALUES(5,8);
INSERT INTO teatro_alimento VALUES(5,10);


/*INSERTS FOR TABLE TEATROS-PELICULAS*/
/*teatro Bogotá*/
/*peliculas en cine*/
INSERT INTO teatro_pelicula VALUES(1,1);
INSERT INTO teatro_pelicula VALUES(1,2);
INSERT INTO teatro_pelicula VALUES(1,3);
/*peliculas próxima a estrenar*/
INSERT INTO teatro_pelicula VALUES(1,9);
INSERT INTO teatro_pelicula VALUES(1,10);

/*teatro Barranquilla*/
/*peliculas en cine*/
INSERT INTO teatro_pelicula VALUES(2,3);
INSERT INTO teatro_pelicula VALUES(2,4);
INSERT INTO teatro_pelicula VALUES(2,5);
/*peliculas próxima a estrenar*/
INSERT INTO teatro_pelicula VALUES(2,7);
INSERT INTO teatro_pelicula VALUES(2,8);

/*teatro Neiva*/
/*peliculas en cine*/
INSERT INTO teatro_pelicula VALUES(3,1);
INSERT INTO teatro_pelicula VALUES(3,2);
INSERT INTO teatro_pelicula VALUES(3,5);
/*peliculas próxima a estrenar*/
INSERT INTO teatro_pelicula VALUES(3,6);
INSERT INTO teatro_pelicula VALUES(3,9);

/*teatro Quibdó*/
/*peliculas en cine*/
INSERT INTO teatro_pelicula VALUES(4,2);
INSERT INTO teatro_pelicula VALUES(4,4);
INSERT INTO teatro_pelicula VALUES(4,5);
/*peliculas próxima a estrenar*/
INSERT INTO teatro_pelicula VALUES(4,7);
INSERT INTO teatro_pelicula VALUES(4,10);

/*teatro Santa Marta*/
/*peliculas en cine*/
INSERT INTO teatro_pelicula VALUES(5,1);
INSERT INTO teatro_pelicula VALUES(5,4);
INSERT INTO teatro_pelicula VALUES(5,5);
/*peliculas próxima a estrenar*/
INSERT INTO teatro_pelicula VALUES(5,8);
INSERT INTO teatro_pelicula VALUES(5,9);


/*INSERTS FOR TABLE TEATROS-SERVICIOS*/
/*teatro Bogotá*/
INSERT INTO teatro_servicio VALUES(1,1);
INSERT INTO teatro_servicio VALUES(1,3);
INSERT INTO teatro_servicio VALUES(1,4);

/*teatro Barranquilla*/
INSERT INTO teatro_servicio VALUES(2,1);
INSERT INTO teatro_servicio VALUES(2,2);
INSERT INTO teatro_servicio VALUES(2,5);

/*teatro Neiva*/
INSERT INTO teatro_servicio VALUES(3,3);
INSERT INTO teatro_servicio VALUES(3,4);
INSERT INTO teatro_servicio VALUES(3,5);

/*teatro Quibdó*/
INSERT INTO teatro_servicio VALUES(4,1);
INSERT INTO teatro_servicio VALUES(4,2);
INSERT INTO teatro_servicio VALUES(4,3);

/*teatro Santa Marta*/
INSERT INTO teatro_servicio VALUES(5,1);
INSERT INTO teatro_servicio VALUES(5,3);
INSERT INTO teatro_servicio VALUES(5,5);


/*INSERTS FOR TABLE HORARIOS*/
INSERT INTO horario VALUES(1,'1:10');
INSERT INTO horario VALUES(2,'1:40');
INSERT INTO horario VALUES(3,'3:50');
INSERT INTO horario VALUES(4,'4:20');
INSERT INTO horario VALUES(5,'6:30');
INSERT INTO horario VALUES(6,'7:00');
INSERT INTO horario VALUES(7,'9:10');
INSERT INTO horario VALUES(8,'9:40');


/*INSERTS FOR TABLE PELICULAS-HORARIOS*/
INSERT INTO pelicula_horario VALUES(1,3);
INSERT INTO pelicula_horario VALUES(1,5);
INSERT INTO pelicula_horario VALUES(1,7);

INSERT INTO pelicula_horario VALUES(2,1);
INSERT INTO pelicula_horario VALUES(2,6);
INSERT INTO pelicula_horario VALUES(2,8);

INSERT INTO pelicula_horario VALUES(3,2);
INSERT INTO pelicula_horario VALUES(3,4);
INSERT INTO pelicula_horario VALUES(3,6);

INSERT INTO pelicula_horario VALUES(4,1);
INSERT INTO pelicula_horario VALUES(4,5);
INSERT INTO pelicula_horario VALUES(4,8);

INSERT INTO pelicula_horario VALUES(5,4);
INSERT INTO pelicula_horario VALUES(5,6);
INSERT INTO pelicula_horario VALUES(5,7);
commit;