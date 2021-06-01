<?php
namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Carbon\Carbon;


class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;


    public function conexionBD(){
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


    public function scraperTiempo(Request $request)
    {
        $vArg = $request->input('name');
        $vPython = env('PYTHON_PATH');
        $vScript = env('TIEMPO_SCRIPT_PATH');
        $command = $vPython." ".$vScript." " . escapeshellarg($vArg);
        $result = exec($command);
        $dbconnect=$this->conexionBD();
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
        }
        return response()->json($result);
    }
    /*
    public function scraperTiempo()
    {
        $vArg = "tres cantos";
        $vPython = env('PYTHON_PATH');
        $vScript = env('TIEMPO_SCRIPT_PATH');
        $command = $vPython." ".$vScript." " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }

    public function scraperTiempo2(Request $request)
    {
        $vArg = $request->input('name');
        $vPython = env('PYTHON_PATH');
        $vScript = env('TIEMPO_SCRIPT_PATH');
        $command = $vPython." ".$vScript." " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }
    */

    public function scraperTripAdyComms()
    {
        //Falta cambiarlo a un input
        $vArg = "tres cantos";
        set_time_limit (5000);
        $vPython = env('PYTHON_PATH');
        $vScript = env('TRIPADVISOR_SCRIPT_PATH');
        $command = $vPython." ".$vScript." " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        //sentimentAnalysis($result);
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
    
    public function admin()
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
        $aFinal = array_count_values($aFechas);
        return(array_slice($aFinal, -5));
    }
}
