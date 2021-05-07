<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ImportsController extends Controller
{
    /**
     * Handle the incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function __invoke(Response $response)
    {
        $response = 'http://127.0.0.1:8000/api/buscar.tiempo';
        /*
        $json = file_get_contents($response);
        $jsonF = json_encode( $json,JSON_UNESCAPED_UNICODE);//Para tratar tildes con JSON (creo que ya vienen tratados desde scripts por lo que no hace falta)
        $data = json_decode($json, true);
        echo $response;
        */
        tiempoToBBDD($response);

    }
    /*
    public function tiempoToBBDD(Response $response)
    {
        $conn = mysqli_connect($DB_HOST,$DB_USERNAME,$DB_PASSWORD,$DB_DATABASE);
        if(!$con){
            die("Conection failed: " . mysqli_connect_error());
        }else {
            echo "Connection OK!";
        }
        foreach($data as $row)
        {
            $sql = "INSERT INTO climas(Nombre,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento) VALUES('".$row[0]."', '".$row[2]."', '".$row[3]."', '".$row[4]."', '".$row[5]."', '".$row[6]."', '".$row[7]."', '".$row[8]."')"
            mysqli_query($conn, $sql);
        }
        echo "Datos Clima en BBDD!";
    }*/
    
}
