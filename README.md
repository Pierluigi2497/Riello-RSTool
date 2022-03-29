# Riello-RSTool

Come funziona?
--Utilizza una connessione TCP per collegarsi ad un inverter Riello RS
--Invia delle richieste modbus per riceve informazioni
--Decodifica le risposte modbus

Come utilizzare lo script?
--Example: python main.py [id] [ip address] [port]
--ID: variabile per il debug dell'applicazione, per ricevere i dati di produzione giornaliera, produzione istantanea, temperatura dell'inverter, utilizzare ID: 15
--IP: indirizzo ip utilizzato dall'inverter per collegarsi in wi-fi
--PORT: porta utilizzata dall'inverter per comunicare, di default è 502
