ALTER SCHEMA `cine`  DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;


SELECT default_character_set_name FROM information_schema.SCHEMATA S WHERE schema_name = "cine";

UPDATE cine.pelicula SET imagen='https://mx.web.img3.acsta.net/pictures/22/03/02/09/31/2544961.jpg' WHERE cine.pelicula.idpelicula = 8;

UPDATE cine.pelicula SET genero='Superhéroes' WHERE cine.pelicula.idpelicula = 1;

UPDATE cine.alimento SET imagen ='https://cdn.pixabay.com/photo/2022/05/25/21/33/burgers-7221445_960_720.jpg' WHERE cine.alimento.idalimento = 10;
commit; 

UPDATE cine.alimento SET nombre ='Combo pollo con papas fritas' WHERE cine.alimento.idalimento = 8;
