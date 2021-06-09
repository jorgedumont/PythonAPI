<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTiemposTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('tiempos', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idMunicipio');
            $table->string('Nombre');
            $table->date('Fecha');
            $table->integer('tMaxima');
            $table->integer('tMinima');
            $table->double('tMedia');
            $table->integer('Humedad');
            $table->integer('Presion');
            $table->integer('Viento');
            $table->integer('IndiceUV');
            $table->timestamps();
        });

        Schema::table('tiempos', function (Blueprint $table) {
            $table->foreign('idMunicipio')->references('id')->on('municipios');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('tiempos');
    }
}
