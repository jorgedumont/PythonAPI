<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUvsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('uvs', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('idMunicipio');
            $table->string('UV');
            $table->string('Descripcion');
            $table->string('Minutos_Piel_Clara');
            $table->string('Minutos_Piel_Oscura');
            $table->integer('Factor_Proteccion_Piel_Clara');
            $table->integer('Factor_Proteccion _Piel_Oscura');
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
        Schema::dropIfExists('uvs');
    }
}
