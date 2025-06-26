# wifi-master

Un programa para atacar a un dispositivo en una red, haciendolo perder la conexion.

## Acerca de este proyecto

Este es mi primer 'script', no busque muchas cosas sobre como hacerlo, en la mayoria fue logica e ingenio, cualquier aporte es bien recibido.


## ¿Que tiene de "especial"?

El script guarda los ultimos datos ingresados (BSSID,nombre de las tarjetas de red,etc) que permite que sea mas rapido si queremos realizar multiples ataques o no estamos seguro si al dispositivo que estamos atacando es el correcto.

## ¿Que precisamos?

Solo tenemos que tener Python y ta 👍.

## Como usarlo

### 1.Clona el repositorio

```bash
git clone https://github.com/devMathiux/wifi-master.git
```
### 2.Nos paramos en el directorio
```bash
cd wifi-master
```

### 3.Iniciamos el script 
```bash
python main.py
```

## Manual

Cuando se ejecute nos va a pedir el nombre de la tarjeta de red, que ya incluí el comando para que se ejecute y lo muestre ahi, generalmente va a ser wlan0 o alguno similar. Luego de hacer esto el internet se "desactivara" para realizar la "busqueda de redes".

Luego pide el nombre de la tarjeta de red en modo monitor, que tambien lo incluí, tambien suele ser wlan0mon o similares.

Luego se van a mostrar las redes disponibles, juntos con los datos necesarios para acceder en ella, el BSSID y el CH.

Tocamos Ctrl+C una vez que encontremos la red buscada y luego nos pedira ambos datos podemos copiarlos(Ctrl+Shift+C) para no equivocarnos (Pegamos con Ctrl+Shift+V).

Luego nos mostrara los dispositivos de esa red, cuando encontremos al que atacar tocamos Ctrl+c para detener la busqueda e ingresamos su STATION.

Despues de eso el ataque iniciara, lo detendremos con Ctrl+C, una vez esto suceda ya volvera el internet a la computadora.

## License

This project is licensed under the [MIT License](LICENSE)
