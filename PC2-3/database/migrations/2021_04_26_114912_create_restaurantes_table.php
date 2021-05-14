<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateRestaurantesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('restaurantes', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idMunicipio');
            $table->string('Nombre');
            $table->string('Detalles');
            $table->string('Comentario');
            $table->string('Referencia');
            $table->timestamps();
        });

        Schema::table('restaurantes', function (Blueprint $table) {
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
        Schema::dropIfExists('restaurantes');
    }
}
