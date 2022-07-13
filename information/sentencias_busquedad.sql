
/*PELICULAS DE UN TEATRO QUE ESTÁN EN SALA*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
WHERE  cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=1 AND cine.teatro_pelicula.idteatro=1;

/*PELICULAS DE UN TEATRO QUE ESTÁN PROXIMAS A ESTRENARSE*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
WHERE  cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=0 AND cine.teatro_pelicula.idteatro=1;

/*ALIMENTOS QUE SE VENDEN, INCLUYE BEBIDAS*/
SELECT cine.alimento.idalimento, cine.alimento.nombre, cine.alimento.precio, cine.alimento.imagen, cine.bebida.*
                FROM cine.alimento, cine.bebida, cine.teatro_alimento
                WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND 
                cine.alimento.bebida_fk = cine.bebida.idbebida AND 
                cine.teatro_alimento.idteatro = 1;

/*BEBIDAS QUE SE VENDEN, SOLO BEBIDAS*/
SELECT cine.bebida.*
FROM cine.alimento, cine.bebida, cine.teatro_alimento
WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND 
cine.alimento.bebida_fk = cine.bebida.idbebida AND 
cine.teatro_alimento.idteatro = 5;

/*BUSCAR TEATRO EN PARTICULAR*/
SELECT * 
FROM cine.teatro
WHERE cine.teatro.idteatro = 1;


/*SERVICIOS QUE OFRECE CINEWORLD*/
SELECT cine.servicio.* 
FROM cine.teatro_servicio, cine.servicio
WHERE cine.teatro_servicio.idservicio = cine.servicio.idservicio AND cine.teatro_servicio.idteatro=3;


/*PELICULA EN PARTICULAR EN SALA*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
WHERE cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=1 AND cine.teatro_pelicula.idteatro=1 AND cine.pelicula.idpelicula=1;


/*PELICULA EN PARTICULAR QUE ESTÁN PROXIMAS A ESTRENARSE*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
WHERE  cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=0 AND cine.teatro_pelicula.idteatro=1 AND cine.pelicula.idpelicula=10;

