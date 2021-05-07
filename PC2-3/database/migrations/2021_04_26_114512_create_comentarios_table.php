<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateComentariosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('comentarios', function (Blueprint $table) {
            $table->id();
            $table->integer('idLugar');
            $table->string('Nombre');
            $table->string('Descripcion');
            $table->string('Referencia');
            $table->timestamps();
        });

        Schema::table('comentarios', function (Blueprint $table){
            //$table->foreign('idLugar')->references('id')->on('hotels','restaurantes','ocios');
            #$table->foreign('idLugar')->references('id')->on('restaurantes');
            #$table->foreign('idLugar')->references('id')->on('ocios');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('comentarios');
    }
}
