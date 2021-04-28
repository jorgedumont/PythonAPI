<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateClimasTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('climas', function (Blueprint $table) {
            $table->id();
            $table->string('idMunicipio');

            //$table->foreign('idMunicipio')->references('id')->on('municipios');

            $table->string('Nombre');
            $table->date('Fecha');
            $table->integer('tMaxima');
            $table->integer('tMainima');
            $table->double('tMedia');
            $table->integer('Humedad');
            $table->integer('Presion');
            $table->integer('Viento');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('climas');
    }
}
