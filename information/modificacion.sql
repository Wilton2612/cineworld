ALTER SCHEMA `cine`  DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;

commit;

SELECT default_character_set_name FROM information_schema.SCHEMATA S WHERE schema_name = "cine";

UPDATE cine.pelicula SET imagen='https://es.web.img2.acsta.net/pictures/22/02/28/16/18/2106533.jpg' WHERE cine.pelicula.idpelicula = 3;
