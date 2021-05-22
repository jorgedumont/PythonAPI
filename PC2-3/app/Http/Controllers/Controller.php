<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function getconection(){
        $hostname = "2.139.176.212";
        $username = "pr_grupoa";
        $password = "pr_grupoa";
        $db = "prgrupoa";
        $dbconnect=mysqli_connect($hostname,$username,$password,$db);

        if ($dbconnect->connect_error) {
            print("Fallo al conectarse a la base de datos: ". $dbconnect->connect_error);
        }else{
            return $dbconnect;
        }
    }

    public function scraperTiempo(){
        $vArg = "tres cantos";
        $command = "C:\Users\isabe\Anaconda3\python.exe C:\\xampp\\htdocs\\PC3\\PythonAPI\\Scrapers\\tiempo.py " . escapeshellarg($vArg);
        $result = exec($command);
        $dbconnect=$this->getconection();
        //echo gettype($result);
        $result = utf8_encode($result);
        echo $result;
        echo "-------------";
        $result = json_decode($result,true);
        //echo gettype($result);
        $idMunicipio=$result[0]["idMunicipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$idMunicipio'");
        $row = mysqli_fetch_assoc($query);
        $id = $row['id'];
        //$id=24930;
        foreach($result as $value){
            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Fecha FROM climas WHERE (idMunicipio = '$id') AND (Fecha = '$Fecha')");
            $row_select_fecha = mysqli_fetch_assoc($query_comprobacion);
            $fecha_select = $row_select_fecha['Fecha'];
            if($fecha_select == $Fecha ){
                $query_update =mysqli_query($dbconnect,"UPDATE climas SET tMaxima = '$tMaxima' , tMinima = '$tMinima', tMedia = '$tMedia', 
                    Humedad = '$Humedad', Presion = '$Presion', Viento = '$Viento' WHERE (idMunicipio = '$id') AND (Fecha = '$Fecha')");
                //echo "Datos actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
                    VALUES ('$id', '$Fecha','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
                //echo "Nuevos datos - ";
            }
            
            
            //echo $query . "\n";
            /*if (!mysqli_query($dbconnect, $query2)) {
                echo('Error insertando en la tabla de climas'. "\n");
            }*/
        }
        //return $result;
    }/*
        
        }*/
    public function scraperTiempo2(Request $request){
        $arg = $request->input('name');
        $command = "C:\Users\isabe\Anaconda3\python.exe C:\\xampp\\htdocs\\PC3\\PythonAPI\\Scrapers\\tiempo.py " . escapeshellarg($arg);
        $result = exec($command);
        $dbconnect=$this->getconection();
        //echo gettype($result);
        //echo $result;
        $result = utf8_encode($result);
        $result = json_decode($result,true);
        //echo gettype($result);
        $idMunicipio=$result[0]["idMunicipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$idMunicipio'");
        $row = mysqli_fetch_assoc($query);
        $id = $row['id'];
        //echo $id;
        //$id=24930;
        foreach($result as $value){
            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];
            $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
            VALUES ('$id', '$Fecha','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
        //return $result;
            //echo $query . "\n";
            /*if (!mysqli_query($dbconnect, $query2)) {
                echo('Error insertando en la tabla de climas'. "\n");
            }*/
        }
        return response()->json($result);
    }

    public function scraperTripAdyComms(){
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\isabe\Anaconda3\python.exe C:\\xampp\\htdocs\\PC3\\PythonAPI\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        //echo $result;
        return $result;
    }

    
    
}
