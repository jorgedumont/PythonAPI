<?php

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
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\tiempo.py " . escapeshellarg($vArg);
        $result = exec($command);
        //echo $result;
        return $result;
    }

    public function scraperTripAdyComms(){
        $vArg = "tres cantos";
        set_time_limit (5000);
        $command = "C:\Users\jdumo\Anaconda3\python.exe C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Scrapers\\TripAd.py " . escapeshellarg($vArg);
        $result = exec($command);
        //echo $result;
        return $result;
    }
    
}
