# solidwall-repo
curl - это добавление 100 рандомных приложух
curl_for_del - это удаление всех распаршенных uuid
parse_json - это парсинг полученных с помощью GET запроса всей инфы uuid для obj_id
Последовательная цепочка работы такая:
1) Делаем REST APi запрос получаем токен
2) Делаем curl.py
3) Делаем REST APi запрос получаем список приложух
4) parse_json.py парсим полученные uuid
5) curl_for_del - это удаление всех распаршенных uuid
