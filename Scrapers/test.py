
import json
import pickle


vData = [{"0":"tres cantos","1":"Hoy","2":"12 may","3":19,"4":9,"5":14.0,"6":"57%","7":"1018hPa","8":"28 km\/h"},{"0":"tres cantos","1":"Ma\u00f1ana","2":"13 may","3":17,"4":7,"5":12.0,"6":"64%","7":"1016hPa","8":"22 km\/h"},{"0":"tres cantos","1":"Viernes","2":"14 may","3":21,"4":8,"5":14.5,"6":"56%","7":"1016hPa","8":"20 km\/h"},{"0":"tres cantos","1":"S\u00e1bado","2":"15 may","3":24,"4":10,"5":17.0,"6":"57%","7":"1017hPa","8":"20 km\/h"},{"0":"tres cantos","1":"Domingo","2":"16 may","3":28,"4":14,"5":21.0,"6":"51%","7":"1016hPa","8":"23 km\/h"},{"0":"tres cantos","1":"Lunes","2":"17 may","3":24,"4":12,"5":18.0,"6":"50%","7":"1017hPa","8":"12 km\/h"},{"0":"tres cantos","1":"Martes","2":"18 may","3":26,"4":13,"5":19.5,"6":"38%","7":"1019hPa","8":"16 km\/h"}]

vData1 = json.dumps(vData)

vData2 = json.loads(vData1)

print(vData2)



