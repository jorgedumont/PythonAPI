<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateComentariosOciosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('comentarios_ocios', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idLugar');
            $table->string('Nombre');
            $table->string('Descripcion');
            $table->string('Referencia');
            $table->timestamps();
        });

        Schema::table('comentarios_ocios', function (Blueprint $table){
            $table->foreign('idLugar')->references('id')->on('ocios');
            
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('comentarios_ocios');
    }
}
