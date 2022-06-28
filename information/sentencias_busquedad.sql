
/*PELICULAS DE UN TEATRO QUE ESTÁN EN SALA*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
where  cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=1 AND cine.teatro_pelicula.idteatro=1;

/*PELICULAS DE UN TEATRO QUE ESTÁN PROXIMAS A ESTRENARSE*/
SELECT cine.pelicula.*
FROM cine.teatro_pelicula, cine.pelicula 
where  cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=0 AND cine.teatro_pelicula.idteatro=1;


/*ALIMENTOS QUE SE VENDEN, INCLUYE BEBIDAS*/
SELECT cine.alimento.idalimento, cine.alimento.nombre, cine.alimento.precio, cine.bebida.*
FROM cine.alimento, cine.bebida, cine.teatro_alimento
WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND cine.teatro_alimento.idteatro = 5 AND
cine.alimento.bebida_fk = cine.bebida.idbebida;

/*BEBIDAS QUE SE VENDEN, SOLO BEBIDAS*/
SELECT cine.bebida.*
FROM cine.alimento, cine.bebida, cine.teatro_alimento
WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND cine.teatro_alimento.idteatro = 4 AND
cine.alimento.bebida_fk = cine.bebida.idbebida;