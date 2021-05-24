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
            
            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];

            $query_comprobacion =mysqli_query($dbconnect,"SELECT Fecha FROM climas WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon')");
            $row_select_fecha = mysqli_fetch_assoc($query_comprobacion);
            $fecha_select = $row_select_fecha['Fecha'];
            if($fecha_select == $fecha_carbon ){
                $query_update =mysqli_query($dbconnect,"UPDATE climas SET tMaxima = '$tMaxima' , tMinima = '$tMinima', tMedia = '$tMedia', 
                    Humedad = '$Humedad', Presion = '$Presion', Viento = '$Viento' WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon')");
                //echo "Datos actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
                    VALUES ('$id', '$fecha_carbon','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
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

            $idMunicipio=$value["idMunicipio"];
            $Nombre=$value["Nombre"];
            $Fecha=$value["Fecha"];
            $tMaxima=$value["tMaxima"];
            $tMinima=$value["tMinima"];
            $tMedia=$value["tMedia"];
            $Humedad=$value["Humedad"];
            $Presion=$value["Presion"];
            $Viento=$value["Viento"];
            
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Fecha FROM climas WHERE (idMunicipio = '$id') AND (Fecha = '$fecha_carbon')");
            $row_select_fecha = mysqli_fetch_assoc($query_comprobacion);
            $fecha_select = $row_select_fecha['Fecha'];
            if($fecha_select == $Fecha_carbon ){
                $query_update =mysqli_query($dbconnect,"UPDATE climas SET tMaxima = '$tMaxima' , tMinima = '$tMinima', tMedia = '$tMedia', 
                    Humedad = '$Humedad', Presion = '$Presion', Viento = '$Viento' WHERE (idMunicipio = '$id') AND (Fecha = '$Fecha_carbon')");
                //echo "Datos actualizados - ";
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO climas (idMunicipio,Fecha,tMaxima,tMinima,tMedia,Humedad,Presion,Viento)
                    VALUES ('$id', '$Fecha_carbon','$tMaxima','$tMinima','$tMedia','$Humedad','$Presion','$Viento')");
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

    public function scraperTripAdyComms()
    {
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
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
