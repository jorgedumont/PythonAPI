<?php
namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Http\Request;


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
        $command = "C:\Users\manu1\Anaconda3\python.exe C:\\Users\\manu1\\GitHub\\PythonAPI\\Scrapers\\tiempo.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }


    public function scraperTripAdyComms()
    {
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\manu1\Anaconda3\python.exe C:\\Users\\manu1\\GitHub\\PythonAPI\\Scrapers\\test.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }
    
}
