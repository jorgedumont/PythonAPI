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
        $arg = $request->input('name');
        $command = "C:\Users\isabe\Anaconda3\python.exe C:\\xampp\\htdocs\\PC3\\PythonAPI\\Scrapers\\tiempo.py " . escapeshellarg($arg);
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
            $caracteristicas_hoteles = $value["Caracteristicas"];
            $caracteristicas_hoteles_formateadas = str_replace("'","",$caracteristicas_hoteles);
            $referencia_hoteles = $value["Referencia"];
            
            $query_comprobacion =mysqli_query($dbconnect,"SELECT Nombre FROM hotels WHERE (idMunicipio = '$idMunicipio') AND 
                (Nombre = '$nombre_hoteles')");
            $row_nombre = mysqli_fetch_assoc($query_comprobacion);
            $nombre_select = $row_nombre['Nombre'];
            
            if($nombre_select == $nombre_hoteles){
                $query_update =mysqli_query($dbconnect,"UPDATE hotels SET Descripcion = '$descripcion_hoteles' ,Caracteristicas = '$caracteristicas_hoteles_formateadas', Referencia = '$referencia_hoteles' 
                    WHERE (idMunicipio = '$idMunicipio') AND (Nombre = '$nombre_hoteles')");

                //echo "- Datos hoteles actualizados - ";
                
            }
            else{
                $query2 = mysqli_query($dbconnect,"INSERT INTO hotels (idMunicipio,Nombre,Descripcion,Caracteristicas,Referencia)
                    VALUES ('$idMunicipio', '$nombre_hoteles','$descripcion_hoteles','$caracteristicas_hoteles_formateadas','$referencia_hoteles')");

                //echo "- Nuevos datos hoteles - ";
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

    public function scraperTripAdyCommsParam($vArg){
        set_time_limit (5000);
        $command = "C:\Users\isabe\Anaconda3\python.exe C:\\xampp\\htdocs\\PC3\\PythonAPI\\Scrapers\\TripAdFinal.py " . escapeshellarg($vArg);
        $result = exec($command);
        $result = utf8_encode($result);
        $result = json_decode($result,true);

        $dbconnect=$this->conexionBD();
        
        $Municipio = $result["lugares"]["ocio"][0]["Municipio"];
        $query = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$Municipio'");
        $row = mysqli_fetch_assoc($query);
        $idMunicipio = $row['id'];

        
        //insert de los sitios
        $this->insert_localizaciones_TripAd($result, $vArg, $idMunicipio, $dbconnect);

        return $result;
    }

    public function scraperTripAd(Request $request){
        $vArg = $request->input('name');
        $dbconnect=$this->conexionBD();
        $queryid = mysqli_query($dbconnect,"SELECT id FROM municipios WHERE Nombre = '$vArg'");
        $filaid = mysqli_fetch_assoc($queryid);
        $id = $filaid['id'];
        $querysentimiento = mysqli_query($dbconnect,"SELECT AnalisisSentimiento FROM busquedas WHERE created_at between DATE_ADD(now(),INTERVAL -7 DAY) and now() and idMunicipio = '$id' and Scraper =1");
        if ($querysentimiento -> num_rows==0){
           $resultado = $this->scraperTripAdyCommsParam($vArg); 
           $sentimiento = $resultado["analisis sentimiento"];
           $queryinsertsentimiento = mysqli_query($dbconnect,"INSERT INTO busquedas (idMunicipio,AnalisisSentimiento,created_at,updated_at,Scraper)
                    VALUES ('$id', '$sentimiento',now(),now(),'1')");    
        }else{
            $filasentimiento = mysqli_fetch_assoc($querysentimiento);
            $queryocio = mysqli_query($dbconnect,"SELECT Nombre FROM ocios o WHERE o.idMunicipio = '$id'");
            while($filasocio =mysqli_fetch_assoc($queryocio)){
                $ocio[]=$filasocio;
            }
            $queryrestaurantes = mysqli_query($dbconnect,"SELECT Nombre, Detalles FROM restaurantes r WHERE r.idMunicipio = '$id'");
            while($filasrestaurantes =mysqli_fetch_assoc($queryrestaurantes)){
                $restaurantes[]=$filasrestaurantes;
            }
            $queryhoteles = mysqli_query($dbconnect,"SELECT Nombre, Descripcion, Caracteristicas FROM hotels h WHERE h.idMunicipio = '$id'");
            while($filashoteles =mysqli_fetch_assoc($queryhoteles)){
                $hoteles[]=$filashoteles;
            }
            $querysentimientonuevo = mysqli_query($dbconnect,"SELECT AnalisisSentimiento FROM busquedas b WHERE b.idMunicipio = '$id' LIMIT 1");
            while($filassentimiento =mysqli_fetch_assoc($querysentimientonuevo)){
                $sentimiento[]=$filassentimiento;
                $analisissentimiento=$filassentimiento['AnalisisSentimiento'];
                $queryinsertarsentimiento = mysqli_query($dbconnect,"INSERT INTO busquedas (idMunicipio,AnalisisSentimiento,created_at,updated_at,Scraper)
                VALUES ('$id', '$analisissentimiento',now(),now(),'0')");
            }
            
            $resultado=array_merge($ocio,$restaurantes,$hoteles,$sentimiento);
        }
        return $resultado;
    }

    public function busquedasRecientes(){
        $dbconnect=$this->conexionBD();
        $querybusquedareciente = mysqli_query($dbconnect,"SELECT idMunicipio FROM busquedas ORDER BY id DESC LIMIT 5");
        while($filabusqueda = mysqli_fetch_assoc($querybusquedareciente)){
            $resultadobusqueda[]=$filabusqueda;
        }
        foreach($resultadobusqueda as $busqueda){
            $busquedanombre = $busqueda['idMunicipio'];
            $querynombrepueblo = mysqli_query($dbconnect,"SELECT Nombre FROM municipios WHERE id = '$busquedanombre'");
                $resultadonombres[]=$filanombre;
            }
        }
        return $resultadonombres;
    }

    public function busquedasPopulares(){
        $dbconnect=$this->conexionBD();
        $querybusquedareciente = mysqli_query($dbconnect,"SELECT idMunicipio, COUNT(idMunicipio) FROM busquedas GROUP BY idMunicipio ORDER BY COUNT(*) DESC LIMIT 5");
        while($filabusqueda = mysqli_fetch_assoc($querybusquedareciente)){
            $resultadobusqueda[]=$filabusqueda;
        }
        foreach($resultadobusqueda as $busqueda){
            $busquedanombre = $busqueda['idMunicipio'];
            $querynombrepueblo = mysqli_query($dbconnect,"SELECT Nombre FROM municipios WHERE id = '$busquedanombre'");
            while($filanombre = mysqli_fetch_assoc($querynombrepueblo)){
                $resultadonombres[]=$filanombre;
            }
        }
        return $resultadonombres;
    }
}
