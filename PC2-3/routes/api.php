<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Controller;
use App\Http\Controllers\ImportsController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

///Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
///    return $request->user();
///});

Route::post('register', 'App\Http\Controllers\UserController@register');
Route::post('login', 'App\Http\Controllers\UserController@authenticate');

Route::group(['middleware' => ['jwt.verify']], function() {

    Route::post('user','App\Http\Controllers\UserController@getAuthenticatedUser');

});


Route::post('buscar.tiempo', 'App\Http\Controllers\Controller@scraperTiempo');
#Route::post('buscar.tiempo', ImportsController::class);
Route::post('buscar.tripadvisor', 'App\Http\Controllers\Controller@scraperTripAd');
Route::post('buscar.tripadvisor.lugares', 'App\Http\Controllers\Controller@scraperTripAdyCommsParam');


Route::get('estadisticas.usuarios', 'App\Http\Controllers\Controller@estadisticasUsuarios');
Route::get('estadisticas.sesiones', 'App\Http\Controllers\Controller@estadisticasSesiones');
Route::get('estadisticas.fallos', 'App\Http\Controllers\Controller@estadisticasFallos');

Route::get('grafica.fechas', 'App\Http\Controllers\Controller@graficaFechas');
