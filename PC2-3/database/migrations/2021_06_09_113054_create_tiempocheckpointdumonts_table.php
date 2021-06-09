<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTiempocheckpointdumontsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('tiempocheckpointdumonts', function (Blueprint $table) {
            $table->id();
            $table->date('Fecha');
            $table->unsignedBigInteger('idMunicipio');
            $table->string('HumedadyPresion');
            $table->integer('UV');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('tiempocheckpointdumonts');
    }
}
