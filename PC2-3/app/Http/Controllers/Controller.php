<?php
namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;


class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

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
        $aFinal = array_count_values($aFechas);
        return(array_slice($aFinal, -5));
    }
}
