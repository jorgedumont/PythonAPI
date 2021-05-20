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
        $vArg = "tres cantos";
        set_time_limit (5000);
        $vPython = env('PYTHON_PATH');
        $vScript = env('TRIPADVISOR_SCRIPT_PATH');
        $command = $vPython." ".$vScript." " . escapeshellarg($vArg);
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
    
}
