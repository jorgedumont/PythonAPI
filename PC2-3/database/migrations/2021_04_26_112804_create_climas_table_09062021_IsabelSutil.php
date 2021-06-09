<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateClimasTable_Isabel extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('climas_09062021_Isabel', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idMunicipio');
            $table->string('Nombre');
            $table->date('Fecha');
            $table->integer('UV');
            $table->string('Todos_los_campos');
            $table->timestamps();
        });

        Schema::table('climas_09062021_Isabel', function (Blueprint $table) {
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
        Schema::dropIfExists('climas_09062021_Isabel');
    }
}
