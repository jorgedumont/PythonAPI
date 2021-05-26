<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Support\Facades\DB;
use Carbon\Carbon;

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
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\tiempo.py " . escapeshellarg($vArg);
        $result = exec($command);
        $dbconnect=$this->getconection();
        //echo gettype($result);
        $result = utf8_encode($result);
        echo $result;
        //echo "-------------";
        //$fecha_carbon = Carbon::now();
        $fecha_carbon = new Carbon("yesterday");
          
        //echo "-------------";
        $result = json_decode($result,true);
        //echo gettype($result);
        $idMunicipio=$result[0]["idMunicipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$idMunicipio'");
        $row = mysqli_fetch_assoc($query);
        $id = $row['id'];
        //$id=24930;
        foreach($result as $value){
            $fecha_carbon = $fecha_carbon->addDays(1);
            $fecha_carbon_formateada = $fecha_carbon->format('Y-m-d');

            //echo "-------------";
            //echo $fecha_carbon;
            //echo "-------------";
            //echo $fecha_carbon_formateada;
            //echo "-------------";

            
            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];

            $query_comprobacion =mysqli_query($dbconnect,"SELECT Fecha FROM climas WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon_formateada')");
            $row_select_fecha = mysqli_fetch_assoc($query_comprobacion);
            $fecha_select = $row_select_fecha['Fecha'];
            
            if($fecha_select == $fecha_carbon_formateada){
                $query_update =mysqli_query($dbconnect,"UPDATE climas SET tMaxima = '$tMaxima' , tMinima = '$tMinima', tMedia = '$tMedia', 
                    Humedad = '$Humedad', Presion = '$Presion', Viento = '$Viento' WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon_formateada')");
                echo "Datos actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
                    VALUES ('$id', '$fecha_carbon','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
                echo "Nuevos datos - ";
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
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\tiempo.py " . escapeshellarg($arg);
        $result = exec($command);
        $dbconnect=$this->getconection();
        //echo gettype($result);
        //echo $result;
        $result = utf8_encode($result);
        $result = json_decode($result,true);
        $fecha_carbon = new Carbon("yesterday"); 
        //echo gettype($result);
        $idMunicipio=$result[0]["idMunicipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$idMunicipio'");
        $row = mysqli_fetch_assoc($query);
        $id = $row['id'];
        //echo $id;
        //$id=24930;
        foreach($result as $value){
            $fecha_carbon = $fecha_carbon->addDays(1);
            $fecha_carbon_formateada = $fecha_carbon->format('Y-m-d');

            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];
            
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Fecha FROM climas WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon_formateada')");
            $row_select_fecha = mysqli_fetch_assoc($query_comprobacion);
            $fecha_select = $row_select_fecha['Fecha'];
            if($fecha_select == $fecha_carbon_formateada ){
                $query_update =mysqli_query($dbconnect,"UPDATE climas SET tMaxima = '$tMaxima' , tMinima = '$tMinima', tMedia = '$tMedia', 
                    Humedad = '$Humedad', Presion = '$Presion', Viento = '$Viento' WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon_formateada')");
                //echo "Datos actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
                    VALUES ('$id', '$fecha_carbon','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
                //echo "Nuevos datos - ";
            }
            
        //return $result;
            //echo  $query . "\n";
            /*if (!mysqli_query($dbconnect, $query2)) {
                echo('Error insertando en la tabla de climas'. "\n");
            }*/
        }
        return response()->json($result);
    }


    public function insert_localizaciones_TripAd($result, $vArg, $idMunicipio, $dbconnect){
       
        $json_ocio = $result["lugares"]["ocio"];
        $json_hoteles = $result["lugares"]["hoteles"];
        $json_restaurantes = $result["lugares"]["restaurantes"];       

        //insert lugares ocio
        foreach($json_ocio as $value){
            $nombre_ocio = $value["Nombre"];
            $referencia_ocio = $value["Referencia"];

            $query_comprobacion_ocio =mysqli_query($dbconnect,"SELECT Nombre FROM ocios WHERE (idMunicipio = '$idMunicipio') AND 
                (Nombre = '$nombre_ocio')");
            $row_nombre_ocio = mysqli_fetch_assoc($query_comprobacion_ocio);
            $nombre_select = $row_nombre_ocio['Nombre'];
            
            if($nombre_select == $nombre_ocio){
                $query_update =mysqli_query($dbconnect,"UPDATE ocios SET Referencia = '$referencia_ocio' WHERE (idMunicipio = '$idMunicipio') AND 
                    (Nombre = '$nombre_ocio')");
                //echo "Datos ocio actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO ocios (idMunicipio,Nombre,Referencia)
                    VALUES ('$idMunicipio', '$nombre_ocio','$referencia_ocio')");
                //echo "Nuevos datos ocio - ";
            }
        }

        //insert lugares hoteles
        foreach($json_hoteles as $value){
            $nombre_hoteles = $value["Nombre"];
            $descripcion_hoteles = $value["Descripcion"];
            $referencia_hoteles = $value["Referencia"];
            
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Nombre FROM hoteles WHERE (idMunicipio = '$idMunicipio') AND 
                (Nombre = '$nombre_hoteles')");
            $row_nombre = mysqli_fetch_assoc($query_comprobacion);
            $nombre_select = $row_nombre['Nombre'];
            
            if($nombre_select == $nombre_hoteles){
                $query_update =mysqli_query($dbconnect,"UPDATE hoteles SET Descripcion = '$descripcion_hoteles' , Referencia = '$referencia_hoteles' 
                    WHERE (idMunicipio = '$idMunicipio') AND (Nombre = '$nombre_hoteles')");
                //echo "Datos hoteles actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO hoteles (idMunicipio,Nombre,Descripcion,Referencia)
                    VALUES ('$idMunicipio', '$nombre_hoteles','$descripcion_hoteles','$referencia_hoteles')");
                //echo "Nuevos datos hoteles - ";
            }
        }

        //insert lugares restaurantes
        foreach($json_restaurantes as $value){
            $nombre_restaurantes = $value["Nombre"];
            $descripcion_restaurantes = $value["Detalles"];
            $referencia_restaurantes = $value["Referencia"];
            
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Nombre FROM restaurantes WHERE (idMunicipio = '$idMunicipio') AND 
                (Nombre = '$nombre_restaurantes')");
            $row_nombre = mysqli_fetch_assoc($query_comprobacion);
            $nombre_select = $row_nombre['Nombre'];
            
            if($nombre_select == $nombre_restaurantes){
                $query_update =mysqli_query($dbconnect,"UPDATE restaurantes SET Detalles = '$descripcion_restaurantes' , Referencia = '$referencia_restaurantes' 
                    WHERE (idMunicipio = '$idMunicipio') AND (Nombre = '$nombre_restaurantes')");
                //echo "Datos restaurantes actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO restaurantes (idMunicipio,Nombre,Detalles,Referencia)
                    VALUES ('$idMunicipio', '$nombre_restaurantes','$descripcion_restaurantes','$referencia_restaurantes')");
                //echo "Nuevos datos restaurantes - ";
            }
        }
    }
    public function scraperTripAdyComms2()
    {
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }


    public function scraperTripAdyComms(){
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        $result = json_decode($result,true);

        $dbconnect=$this->getconection();
        
        $Municipio = $result["lugares"]["ocio"][0]["Municipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$Municipio'");
        $row = mysqli_fetch_assoc($query);
        $idMunicipio = $row['id'];

        
        //insert de los sitios
        $this->insert_localizaciones_TripAd($result, $vArg, $idMunicipio, $dbconnect);

        return $result;
    }

    public function estadisticasUsuarios()
    {
        $usuarios = DB::table('users')->count();
        return $usuarios;
    }

    public function estadisticasSesiones()
    {
        $sesiones = DB::table('sessions')->count();
        return $sesiones;
    }

    public function estadisticasFallos()
    {
        $fallos = DB::table('failed_jobs')->count();
        return $fallos;
    }
    
    public function graficaFechas()
    {
        $aFechas = [];
        $data = DB::table('users')->get();
        $data = json_encode($data);
        $data = json_decode($data, true);
        foreach ($data as $value){
            $fecha = $value['created_at'];
            $fecha = explode(" ", $fecha);
            $fecha = $fecha[0];
            //print($fecha . " / ");
            array_push($aFechas, $fecha);
        }

        return(array_count_values($aFechas));
    }
    
    
    
}
