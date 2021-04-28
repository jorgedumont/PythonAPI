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
            $table->integer('idMunicipio');

            //$table->foreign('idMunicipio')->references('id')->on('municipios');

            $table->string('Nombre');
            $table->string('Comentario');
            $table->string('Referencia');
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
        Schema::dropIfExists('ocios');
    }
}
