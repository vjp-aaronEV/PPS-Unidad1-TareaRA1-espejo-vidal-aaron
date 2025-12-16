# Ejecución de las pruebs unitarias

### 1. Cuando se crea un lavadero, éste no tiene ingresos, no está ocupado, está en fase 0 y todas las opciones de lavado (prelavado a mano, secado a mano y encerado) están puestas a false.

Como se puede ver en la imagen, este test pasa correctamente por lo que no hay que corregir nada en el código. El test hace estos pasos:
- Comprueba que la fase del lavadero es inactiva
- Comprueba que los ingresos son de 0
- Comprueba que **no** está ocupado
- Y comprueba que **ninguna** de las fases esté inicializada
![Ejecuión test 1](img/Ejecucion_Pruebas/1/1.png)

---

### 2. Cuando se intenta comprar un lavado con encerado pero sin secado a mano, se produce una ValueError.
Al igual que el test anterior pasa sin ningún error, lo que siginifica que la ejecución del código con las opciones asginadas da el error esperado, de nuevo estás son las fases del test:
- Ejecuta un lavado con las siguientes opciones: 
    - Prelavado: False (Sin prelavado)
    - Secado a mano: False (Sin secado a mano)
    - Encerado: True (Con encerado)
- Comprueba que la ejecución de estas opciones da como resultado el error ```ValueError```
![Ejecuión test 2](img/Ejecucion_Pruebas/2/2.png)

---

### 3. Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una ValueError.
Fases del test: 
- Inicia un lavado con cualquier configuración
- Intenta empezar otro lavado cuando se está ejecutando uno y comprueba si el error lanzado es el ```ValueError```.

En este caso el test falla, ya que nosotros estamos buscando que la ejecución produzca un error de tipo ```ValueError``` pero nos está devolviendo un error de tipo ```RuntimeError```.
![Ejecuión test 2 fallida](img/Ejecucion_Pruebas/3/3_0_runtime.png)
Si miramos el código, podemos ver que es porque en el código está especifcado que lance este error, para poder solcionarlo simplemente cambiamos el error ```RuntimeError``` por ```ValueError```.
![Codigo antes de solucion](img/Ejecucion_Pruebas/3/3_1_antes_correccion.png)
![Codigo despues de solucion](img/Ejecucion_Pruebas/3/3_2_despues_correccion.png)
Una vez cambiado si volvemos a ejecutar la purbe ya podemos ver que ahora si lo pasa correctamente.
![Test 3 ejecutado satisfactoriamente](img/Ejecucion_Pruebas/3/3_4_test_corregido.png)

---

### 4. Si seleccionamos un lavado con prelavado a mano, los ingresos de lavadero son 6,50€.
Fases del test: 
- Inicia un lavado con las opciones:
    - Prelavado a mano: True (Con prelavado a mano)
    - Secado a mano: False (Sin secado a mano)
    - Encerado: False (Sin encerado)
- Ejecuta la función de cobrar
- Comprueba que los ingresos del lavadeo son 6.50€

En este caso podemos ver que pasa el test correctamente por lo que no tendríamos que corregir nada en el código.
![Test 4 ejecutado](img/Ejecucion_Pruebas/4/4.png)

---

### 5. Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€.
Fases del test: 
- Inicia un lavado con las opciones:
    - Prelavado a mano: False (Sin prelavado a mano)
    - Secado a mano: True (Con secado a mano)
    - Encerado: False (Sin encerado)
- Ejecuta la función de cobrar
- Comprueba que los ingresos del lavadero son 6.00€

En este caso el test falla por lo que tenemos que ir al código para ver porque está fallando.
![Test 5 ejecutado fallido](img/Ejecucion_Pruebas/5/5_0_test_fallido.png)
En el código podemos ver cuál es el problema, el test falla porque el coste de **secado a mano** está configurado como 1.20€ en vez de 1.00€ que sería el valor correcto.
![Código test 5 antes correcion](img/Ejecucion_Pruebas/5/5_1_antes_correccion.png)
![Código test 5 después correcion](img/Ejecucion_Pruebas/5/5_2_despues_correccion.png)
Una vez cambiado el código podemos ver que ya pasa el test correctamente.
![Test 5 ejecutado correctamente](img/Ejecucion_Pruebas/5/5_3_test_correcto.png)

---

### 6. Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€.
Fases del test: 
- Inicia un lavado con las opciones:
    - Prelavado a mano: False (Sin prelavado a mano)
    - Secado a mano: True (Con secado a mano)
    - Encerado: True (Con encerado)
- Ejecuta la función de cobrar
- Comprueba que los ingresos del lavadero son 7.20€

Al igual que anterior test este también falla por lo que que tenemos que ir al código para cuál es el fallo.

![Test 6 fallido](img/Ejecucion_Pruebas/6/6_0_test_fallido.png)
En el código podemos ver que falla porque el **coste de encerado** está asignado como 1.00€, cambiamos el valor a 1.20€ para corregir el fallo.
![Código test 6 antes correcciion](img/Ejecucion_Pruebas/6/6_1_antes_correccion.png)
![Código test 6 después correcciion](img/Ejecucion_Pruebas/6/6_2_despues_correccion.png)
Una vez corregido el código ya podemos ver que el test pasa correctamente
![Test 6 correcto](img/Ejecucion_Pruebas/6/6_3_test_correcto.png)

---