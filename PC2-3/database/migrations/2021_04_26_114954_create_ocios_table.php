<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateOciosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ocios', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idMunicipio');
            $table->string('Nombre');
            $table->string('Comentario');
            $table->string('Referencia');
            $table->timestamps();
        });

        Schema::table('ocios', function (Blueprint $table) {
            //$table->foreign('idMunicipio')->references('identificador')->on('municipios');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ocios');
    }
}
