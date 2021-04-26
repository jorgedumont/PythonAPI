<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Tymon\JWTAuth\Exceptions\TokenBlacklistedException;
use Tymon\JWTAuth\Exceptions\TokenExpiredException;
use Tymon\JWTAuth\Facades\JWTAuth;
use Validator;

class TonkensController extends Controller
{
    //Metodo login
    public function login(Request $request){
        $credentials = $request->only('email', 'password');

        $validator = Validator::make($credentials,[
            'email' => 'required|email',
            'password' => 'required'
        ]);

        if($validator->fails()){
            return response()->json([
                'success' => false,
                'message' => 'Wrong validation',
                'errors' => $validator->errors()
            ], 422);
        }

        $token = JWTAuth::attempt($credentials);

        if($token){
            return response()->json([
                'success' => true,
                'token' => $token,
                'user' => User::where('email', $credentials['email'])->get()->first()
            ], 200);
        }else{
            return response()->json([
                'success' => false,
                'message' => 'Wrong credentials',
                'errors' => $validator->errors()
            ], 401);            
        }

        return null;

    }

    //Metodo expiracion token
    public function refreshToken(){
        $token = JWTAuth::getToken();
        try{
            $token = JWTAuth::refresh($token);
            return response()->json([
                'success' => true,
                'token' => $token
            ], 200);
        }catch(TokenExpiredException $ex){
            return response()->json([
                'success' => false,
                'message' => 'Need to login again please (Expired)'
            ], 422); 
        }catch(TokenBlacklistedException $ex){
            return response()->json([
                'success' => false,
                'message' => 'Need to login again please (Blacklisted)'
            ], 422); 
        }

    }

    //Metodo logout (te quita el token)
    public function logout(){
        $token = JWTAuth::getToken();
        try{
            JWTAuth::invalidate($token);
            return response()->json([
                'success' => true,
                'message' => 'Logout successful'
            ], 200);

        }catch(JWTException $ex){
            return response()->json([
                'success' => false,
                'message' => 'Failed logout, please try again'
            ], 422);
        }


    }


}
