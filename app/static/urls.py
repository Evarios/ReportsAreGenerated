URL = {
    'PostgreSQL': f'postgresql://{{USERNAME}}:{{PASSWORD}}@{{HOST}}:{{PORT}}/{{DATABASE}}',
    'MySQL': f'mysql://{{USERNAME}}:{{PASSWORD}}@{{HOST}}:{{PORT}}/{{DATABASE}}',
    'Oracle_SID': f'oracle+oracledb://{{USERNAME}}:{{PASSWORD}}@{{HOST}}:{{PORT}}/{{DATABASE}}',
    'Oracle_SERVICE_NAME': f'oracle+oracledb://{{USERNAME}}:{{PASSWORD}}@{{HOST}}:{{PORT}}/?service_name={{DATABASE}}'
}