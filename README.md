# Riello-RSTool

Come funziona?
--Utilizza una connessione TCP per collegarsi ad un inverter Riello RS <br />
--Invia delle richieste modbus per riceve informazioni <br />
--Decodifica le risposte modbus <br />
<br />
Come utilizzare lo script? <br />
--Example: python main.py [id] [ip address] [port] <br />
--ID: variabile per il debug dell'applicazione, per ricevere i dati di produzione giornaliera, produzione istantanea, temperatura dell'inverter, utilizzare ID: 0 <br />
--IP: indirizzo ip utilizzato dall'inverter per collegarsi in wi-fi <br />
--PORT: porta utilizzata dall'inverter per comunicare, di default è 502 <br />
