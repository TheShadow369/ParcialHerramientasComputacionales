# Restaurante Uni-Jave:

Este Sistema funciona en base a un menú de *tres opciones* en específico, tituladas y diferenciadas por sus respectivos números, para elegir la opción solo debe ingresar el numero de la acción que desee realizar o efectuar: La entrada “*Seleccione Opción Requerida* :” solicita únicamente un numero entre "*0*" y "*1*", sin espacios, referentes a las opciones del sistema, exclusivamente funcionaran una de estas *tres opciones*, en caso de que se digite algo diferente enviara el siguiente aviso, "*Invalido*", indicando en un principio lo que se ingresó. lo que desprenderá el menú de nuevo y solicitará el ingreso de la opción, de nuevo.

_**0**. Cerrar_

_**1**. Venta_

<div>
<p style = 'text-align:center;'>
<img src="https://drive.google.com/file/d/1pqHowTfjxxpKCnRD8xcxS8TE4u6RXOeC/view?usp=sharing" alt="JuveYell" width="500px">
</p>
</div>


El programa en su esencia se basa en una pequeña base de datos que relaciona un código estrictamente _cuatro_ caracteres numéricos, con una descripción del producto, sumado al costo de dicho producto.

Identificado con el número _“0”_, la opción _“Cerrar”_ lo que hace es acabar todos los procesos y simplemente cerrar el programa, de la cafetería, el cual imprime un mensaje de _“Cerrando”_.

La opción identificada con el numero _“1”_, su función es replicar el funcionamiento de una venta, donde solicita una entrada de la siguiente manera _“Ingrese Producto :”_, la cual solicita el nombre del producto a llevar, en caso de que la entrada este vacía, lo regresara al menú, si se ingresa por lo menos un carácter, hay que hacer referencia de que se espera que se ingrese un producto verdadero, ya después se solicita una entrada referente, al código del producto, cuando ya pase esto empezará a un contador de errores con un limiste de errores, en caso de que se cumpla este límite, el programa volverá al menú, se vera de la siguiente manera _“Ingrese código del producto:”_ en donde se debe ingresar exclusivamente caracteres numéricos y en este caso debe contener al menos _"cuatro"_ caracteres, en caso de que no pase esto indicara el siguiente mensaje _“Invalido”_, y volverá a solicitar el código y sumara un error, esto mismo pasara con las siguientes entradas, involucradas con números si no son dígitos o números, imprimirá el mensaje _“Invalido”_, y contara como error, después de haber ingresado todos los productos, debe ingresar el producto vacío.

<div>
<p style = 'text-align:center;'>
<img src="https://photos.app.goo.gl/d8B6KzkGJW3m6vaf6" alt="JuveYell" width="500px">
</p>
</div>

Posteriormente solicitara tanto el tipo de _cliente_ y su _documento de identidad_, solo cuando la palabra que se ingrese sea de “***Profesor***"o “***Estudiante***” ellos obtendrán descuento en su compra, en caso del profesor 20%, si es un _estudiante_ sin beca será de 30 % y si tiene beca será de 50 %, en cualquier otro caso no habrá descuento.

En caso de que sea _estudiante_ preguntara si tiene beca o no, para ello deberá escribir, la palabra _“yes”_ en caso de la decisión sea positiva o _“no"_, en caso contrario, para así identificar el porcentaje de descuento que se debe aplicar.

<div>
<p style = 'text-align:center;'>
<img src="https://photos.app.goo.gl/4hPS1GwmD54s2bvx7" alt="JuveYell" width="500px">
</p>
</div>

Ya al final imprimirá una _factura_, indicando el tipo de cliente y su documento.
Por cada producto imprimirá su _código, descripción, cantidad, precio por unidad y precio total dependiendo de la cantidad_, en ese mismo orden.

En la siguiente línea imprimirá el _valor total_, de toda la compra, en la siguiente línea mostrara el porcentaje de _descuento aplicado_ al total de la compra y en la siguiente línea imprimirá el total con descuento, posteriormente volverá al Menú y solicitara de nuevo a elegir una de las opciones presentes.

<div>
<p style = 'text-align:center;'>
<img src="https://photos.app.goo.gl/bY4Kx34hpKioArCP8" alt="JuveYell" width="500px">
</p>
</div>

Para resolver el problema de _identificar los valores y de pago total, pago con descuento aplicado y el valor de descuento, según el tipo de usuario_, Utilizamos una función titulada _totales_, que revise como entrada una lista con varias sablistas donde hay con la información de cada producto, ordenada de la siguiente manera el _producto, código cantidad y precio_, dependiendo de la cantidad de productos que se ingresen será el tamaño de la lista, cabe recalcar que al final de la lista principal se encontrara el tipo de _cliente_.

<div>
<p style = 'text-align:center;'>
<img src="https://photos.app.goo.gl/y59T8NFd4sNTzsiY9" alt="JuveYell" width="500px">
</p>
</div>

Retorna una _tupla_ con los valores del _total a pagar, el descuento aplicado y el total con el descuento ya aplicado_, en caso de que se ingrese valores o respuesta erróneas a la hora de preguntar si el estudiante tiene beca, tendrá tres oportunidades para responder o dar una respuesta en caso contrario, se retornara un boleano _False_, que como resultado imprimirá el mensaje “_Invalido_”y volverá al menú principal.
La otra es un procedimiento llamado _factura_, que pide como datos de entrada, la lista de los antes mencionada, la _tupla_ de la definición anterior y el documento de identidad, y lo que hace como tal es imprimir la _factura_ según el formato indicado anteriormente.

<div>
<p style = 'text-align:center;'>
<img src="https://photos.app.goo.gl/bRuL2KfxNLPNUQcF8" alt="JuveYell" width="500px">
</p>
</div>
