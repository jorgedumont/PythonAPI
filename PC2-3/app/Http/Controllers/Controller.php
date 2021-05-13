<?php
//header('Content-Type: application/json; charset=utf-8');
//json_encode($data, JSON_UNESCAPED_UNICODE)
namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function scraperTiempo(){
        $vArg = "tres cantos";
        $command = "C:\Users\manu1\Anaconda3\python.exe C:\\Users\\manu1\\GitHub\\PythonAPI\\Scrapers\\tiempo.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        //echo $result;
        return $result;
    }

    public function scraperTripAdyComms(){
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\manu1\Anaconda3\python.exe C:\\Users\\manu1\\GitHub\\PythonAPI\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        //echo $result;
        return $result;
    }
    
}
