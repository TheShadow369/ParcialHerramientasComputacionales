# Restaurante Uni-Jave:

Este Sistema funciona en base a un menú de *tres opciones* en específico, tituladas y diferenciadas por sus respectivos números, para elegir la opción solo debe ingresar el numero de la acción que desee realizar o efectuar: La entrada “*Seleccione Opción Requerida* :” solicita únicamente un numero entre "*0*" y "*1*", sin espacios, referentes a las opciones del sistema, exclusivamente funcionaran una de estas *tres opciones*, en caso de que se digite algo diferente enviara el siguiente aviso, "*Invalido*", indicando en un principio lo que se ingresó. lo que desprenderá el menú de nuevo y solicitará el ingreso de la opción, de nuevo.

_**0**. Cerrar_

_**1**. Venta_

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/2o3GiorEl3-gYCLd2zRUaG5eUErI-tLf8CcTgO9O0K2GWAtgxgcEJDIcIu97VDVjfYSRTrK83uAMngo-JZxKZSdtxSocjHTObARenLgbnQEelSXr-s73NqRU0G48_f6nzVkcfD3HWkvF-uP2JAXB30ZjXccAWJyAI4IAS7QwBMtlBOW_cFmVmFYQuDr-8O0FeTChkhjISTrAnQvE32jBSZ20CwAM-1PuIMNmbq-4o7bra8HMuMGxyqghG8Dsz7zXxOvYIS7U7d5GWj7j4cBVdWZ5ttV1e7cG4wTwHrtmo_ibrDLerdwSS48toGXpQtAFq7VejzgiNwINpvbk3mt6dLHCoiWam00dJlIs2bYx4XhC5kXiI0fbC4lulotF9S1nhOaOEjDDlKi3LtBPK8B4b7EX6tdEQN1ilISIBT69YZVrsh6NmxDdZqWmwmF_eZs8TnxeY2P2gqr_mpjysokM9YOMEAhPY8IAt7mZyegxM4_QIRU2ACKOSPmsVj51ILxU3UmfiJ6YeQpqf18R1w4ynzHoOM3026T4j72LxIFh3rn-sQjFHT1YElhZHNdv9mnkrnVj3Sq7HJPNAuAaz9gBKA7wLEaEnKDq-eqEGhqNbr-t6NvcQI6pWAqvwZNlYxSGx2tNOo19IsyaDcr6iGOsxH2bRkSPzDh4vT27-q_NTdNvE-V3WKBXtVZWCGuA6fUqvHFlsFafCGxdsexgnlbG3MSb11aC3kKEXblvmTK4L_YDWZBLkdmFn4b6I68=w776-h162-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>


El programa en su esencia se basa en una pequeña base de datos que relaciona un código estrictamente _cuatro_ caracteres numéricos, con una descripción del producto, sumado al costo de dicho producto.

Identificado con el número _“0”_, la opción _“Cerrar”_ lo que hace es acabar todos los procesos y simplemente cerrar el programa, de la cafetería, el cual imprime un mensaje de _“Cerrando”_.

La opción identificada con el numero _“1”_, su función es replicar el funcionamiento de una venta, donde solicita una entrada de la siguiente manera _“Ingrese Producto :”_, la cual solicita el nombre del producto a llevar, en caso de que la entrada este vacía, lo regresara al menú, si se ingresa por lo menos un carácter, hay que hacer referencia de que se espera que se ingrese un producto verdadero, ya después se solicita una entrada referente, al código del producto, cuando ya pase esto empezará a un contador de errores con un limiste de errores, en caso de que se cumpla este límite, el programa volverá al menú, se vera de la siguiente manera _“Ingrese código del producto:”_ en donde se debe ingresar exclusivamente caracteres numéricos y en este caso debe contener al menos _"cuatro"_ caracteres, en caso de que no pase esto indicara el siguiente mensaje _“Invalido”_, y volverá a solicitar el código y sumara un error, esto mismo pasara con las siguientes entradas, involucradas con números si no son dígitos o números, imprimirá el mensaje _“Invalido”_, y contara como error, después de haber ingresado todos los productos, debe ingresar el producto vacío.

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/TtUjqKksVxnfrZBAQ1HO8TeOG0rI12YRR9SxKz-a5Nq2PoJYKtAiafuMWtApwB_r62kjGJ3c8yGmd3uQNyKnvdkD6cMikc5dca0uBSY0w_IOl5QxrxaDf7-d5KUA20S-4oj8k_XGMbm9M-1KuPcrSjYtHM1wNktxT1CDZHUtMEuNmgqExidTbWTmA5hsSdJLBVeolpOOQMoBDK2rCtJZKGindiDWArQrZcX3bR0s4E5Y2A14KBIG_uCorC2MRWdb_3YtWpeuAG4c2GJdwFqekOobltV2zLHECasTpM8HJBsm0k6wY3f0PLAnLQab9mU-HRuHyaOjuJv_mDzSohuJus1RDBScI2xUafiHE9CO3dHRJRdb_-wDPP1bbqqkmZpaLmiW2cwo2bit8-nOmG6h7lPYvdfqBGRcJyQfF3jJDqwog0vx3EwDWY6cXZW-OQ9pGbFWfqEBABGgDDUzeRYGIoK319SghMWYalEIEuIMunL2C4RsOWafzA-ZiMby7U41Htmz7L-3sHScT4hmmLQVjtPbuEprXUX043FHMxr26oQvfaLiFiMFJzflTZF8j0lcy4UILO2i3vl1kgycacWaSxvplwlTgFkcCdDhYXFe6o36BAVYyW-Eaptutw53tBhvL_94PivvFSHO5Mn-tcALvwNUyvbwNqpFdtFbxV_rwCWrK05GDIw_mBdy6VeDX0aXwLUuDmiP1ncjrpUX9e6Nrv81_geuGv7iV6XZnB8xQC0l3SWcVkALyZS4-f4=w665-h615-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>

Posteriormente solicitara tanto el tipo de _cliente_ y su _documento de identidad_, solo cuando la palabra que se ingrese sea de “***Profesor***"o “***Estudiante***” ellos obtendrán descuento en su compra, en caso del profesor 20%, si es un _estudiante_ sin beca será de 30 % y si tiene beca será de 50 %, en cualquier otro caso no habrá descuento.

En caso de que sea _estudiante_ preguntara si tiene beca o no, para ello deberá escribir, la palabra _“yes”_ en caso de la decisión sea positiva o _“no"_, en caso contrario, para así identificar el porcentaje de descuento que se debe aplicar.

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/EaYmWGx5AMquV8KF4sYex5UJh4HQZNuND9EWJeSlMLReSXmfqt8p_f9GSYbpnWs3goQ2-6S6ZsddJSJv2iuh1_Qa9yclzpkXhZo-L0jEaJvn_6s07LM9Kowkieow-9SQhiLVaol-aMgU_mxLLWHtjMaS-la4Nx1n0ZZazWv4kgtJeJ9ME4Ourp7Ov61Tho9cQF_mVWAFb0rVCgNO7OQI-bVCQsh8Atav3vLgI8vg1W_VUBMYKEo1sCdNAp7Gl8Aj4Z_W1ekKCjgiFtJUnX9pHSPitnoUn7swAMxso0qHbIZG2rwo5UHuWGBaa4O7lrRukmUcn0eExYYrVxKNquqZ0MR58XDiTqUWgkmAjSSPbLTf3SAoSowC_bHtbAeKdVA6pDTHDlqQ_sUQUeO0wGPr6fdGVDQwpaxPV6GSmortJ3ki9pKwYDN4gX9csOprzKUzhglI4t5CFBTiN091M-yBdACzBVl27xX6snMwQ0OffphVsOkvoBq2KfjaEjJCq6DdA_45nqtWCLTjujOp8u27h9kEjGaAvv_LaRhXs-Dxk75oTGfBwavgaF1AeBbeCK_6CUHggwdlqolaz43zvWBFF1krP-4wNV3CMVgtTaauT9HhC70SmpQCl03zqXHk0DRcnHZNjhknbA-sSC6HpNI_6dl4Es8OdWLPA3hdAStvtTw4AambH826qblnl88IMbYf9xnivPFeFq0Yb2MCTzfrKPbQjyvMKTLclEXRWZyzS9klDKVTlUebTOxCSiM=w821-h300-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>

Ya al final imprimirá una _factura_, indicando el tipo de cliente y su documento.
Por cada producto imprimirá su _código, descripción, cantidad, precio por unidad y precio total dependiendo de la cantidad_, en ese mismo orden.

En la siguiente línea imprimirá el _valor total_, de toda la compra, en la siguiente línea mostrara el porcentaje de _descuento aplicado_ al total de la compra y en la siguiente línea imprimirá el total con descuento, posteriormente volverá al Menú y solicitara de nuevo a elegir una de las opciones presentes.

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/ClF9THye8wH75GNxL359Xxz9mCpdCyGKKorJJnAykIpT287zAhs6E1hWV0xdmXFodEhEJuds-7JaJCrID9XrGynyeLm_ZhFpcvV9t9Lu3Fosi1mo4VyO7SpJvdK5s7JXegJ7CpZMddfeKPD9fW8tqAFU-eO83CPjfP06xTxd1EJUMpKkUnG3Ft-5oJQNpPd-yuAgjjo4bFMsbR8J8orUjoFiXIZvvGNJOh1A8w8JhKE21dhxZdO_CCf6dYxHl-ppmVqRTCpBfXgSdhAu8KCt9YELZ5bcazwkSbAGh-8Xlv_iWvFccxLEgzPeJYDGvQrZVjhFDmF-NwKIBCILIdit9olJaCHOQcJHNyylYmcxwDFVVb1PxREbuxoOz3g4y1QGuuWvk0ieq0U3DXyv_55npBUcyytYZpzV0YRXJFYjHpKpN4tKMB5eumuZzi82v1_g6cAVzEaxpPaD1BvJtJd3tmYjlUyo3TspIkGEuR_wyMGJkv2bHwVASqWz1M4ITvcHYs3LDR0qwhCgxq8WBMVl5Wjom8kArV8IPGrHgjWwQnlI_LU6QjdQpS8_4UepKUR5v5YwRs3HrkaerzCSq_OqRjFHeqC7u-HDjLHlySnKILKUD0If2TBREZiW0caDD37LzMlMvgh2ksdlJZnaXlStGUGSLyYyuXTaUOhlNhMwp3PtS1THXEUXZ_icLKmw5vGfdlaABI38ZxDocB79RFoaJyiCeqMbm-HOFzl_VXorF9dagw5NLpYprWvbO0c=w611-h633-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>

Para resolver el problema de _identificar los valores y de pago total, pago con descuento aplicado y el valor de descuento, según el tipo de usuario_, Utilizamos una función titulada _totales_, que revise como entrada una lista con varias sablistas donde hay con la información de cada producto, ordenada de la siguiente manera el _producto, código cantidad y precio_, dependiendo de la cantidad de productos que se ingresen será el tamaño de la lista, cabe recalcar que al final de la lista principal se encontrara el tipo de _cliente_.

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/73cNZ2vNq95jKU8n00krBx5_jGVtNPuxxN2_PfpDgPt3R2iPYZgsPpq7d2DyZ4rA5EBCytmyf_KlUzl86zNB2HMNDN7_5PpKVfa_MBFxx-8EYWs6aw-5_449vei3GR-TXTFIJteR_Rz41kzgZWyvXtC3IZJd0pzT3Kp6m0gDg4HdCcosPmQBmVko2PvLXp_u3gA67AXSLwpYIwnIJtu0DCpi8tZxDl2o4GE2eF_Yu6hbJ7V3mN1jYqV9AZSmHcGaAa7fde1rA0McKtWVfWKr2Sx5reFSVVdG2gVkpL0uVQ1zREAuli-FPs2ZT4fIaFgGbaTerWUokiM6HNMB0zO0qiHdu332aXMa5hvwCTqumKt8v-oIJsZdlis_fP3QMHUzNQmVGySiAXPjb3qfvNmjpk4qIiLj7SSXLOW3o_r5eyNA0EvjG19jVHoL1kzEOtbpz7xH2x3U28J0aSFRMlUyLyGTHwl6NL3IO7yRxZ8eNKTgl7SNO6m8_9RqUVrvG2NzaYrbX1D7pVgaLCl-HGL6uQPp33Qf-XJb1es-3W5cTPfHcndunsOsByPZPyV6RNjLwGnx1AL9LjuiVJREe98_PFEowaDqz2ZW_lILDsVtFRiWz_ZYwTj4h1vXNyl6A8-WbsGK5yqK3WyrH9Dd9AZufcufgC5GhS_LBQLZvps5mX36pD2UxECRiz2XnixxpJkBi4NWmIupAlBe6F8Gr3Dv8_AkdASXfLicdgoDV7WY_0MJGLWQB_F74PGKoiM=w637-h633-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>

Retorna una _tupla_ con los valores del _total a pagar, el descuento aplicado y el total con el descuento ya aplicado_, en caso de que se ingrese valores o respuesta erróneas a la hora de preguntar si el estudiante tiene beca, tendrá tres oportunidades para responder o dar una respuesta en caso contrario, se retornara un boleano _False_, que como resultado imprimirá el mensaje “_Invalido_”y volverá al menú principal.
La otra es un procedimiento llamado _factura_, que pide como datos de entrada, la lista de los antes mencionada, la _tupla_ de la definición anterior y el documento de identidad, y lo que hace como tal es imprimir la _factura_ según el formato indicado anteriormente.

<div>
<p style = 'text-align:center;'>
<img src="https://lh3.googleusercontent.com/KRh4hSAIJfcBXn_UOypA-lFnHr-mO_QvvYz-DKsWS_OPyENjx805ngOsk8bvJzqehAd-QKeVlafWiwSDJWyHUMm6v9fflzC9AJ1W9p2MqV4jprsrVkgR_kx9f1Licp2NUy6JWXYmrC6AfaZnUZvOztU6Lta9k7Y1usTFTHtA_J49Rzjlf4Wd5wFQXOjEiIa7R-BsGyCWHWb5loPi-TxA5hlXCeg9XNR3aMyu66aCV4erMKAImf1QvhGSb0bJeTS9EwB6VSvrEj1ihNn1NLt746G2XTCos3q81dAFEraVuMHsM7EKgC1TcvpHj1dD0nMN82blAjmSRDwvTCyZdRRzrE69MW36Jzig9XXJAyEGUVo13AruoS42HDmElip3uQqy5inmOCEtwGWpq9myoOUShBdAO2xA63oExew4_23VhStCroI1bKQnQBF5jyZLpkBGzI3bfVHhH7VuPscqjOTmFhP2vCmOrokG836LrUfCNMW8sKYXAZKIqdk8HMDYW-Q1QhWgabeun0_Zclg_9EyAiTeGXxR92wzpz_Tg1psk_EOhaC6WVrVebfLAJOre8eyn7eihpf2vCI6iztCFm3JJ43RlVbruQ4RlLQgQrNOds5uXFi8glPhIBRnWSWLuC1TkcsVGOZjHuAoJZ-hh9CuDCZuohBiDxxnf7F8fdnyiwxRC57bBJamRlr0CSicE8gU3LXWluSU9qAgCJievzXHj9w9kAUZPDR1LgzPTfkK0RCOa3RsUIZrzDhQYUmI=w791-h291-no?authuser=0" alt="JuveYell" width="500px">
</p>
</div>
