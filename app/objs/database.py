from pathlib import Path
import subprocess
import re


class Database:
    def __init__(self):
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.database = None
        self.db_type = None
        self.server_instance = None

    # ============================== PUBLIC METHODS ============================== #

    def add_new_config(self, username, password, host, port, database, db_type, server_instance=None):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.db_type = db_type
        self.server_instance = server_instance

        save_path = Path(f'existing/{self.database}') if not self.db_type.startswith('Oracle') else Path(f'existing/{self.username}')

        if not save_path.exists():
            save_path.mkdir()

        self._save_dotenv(save_path)
        self._get_sql_metadata(save_path)
        if not self.db_type.startswith('Mongo'):
            self._filter_metadata(save_path)

    
    def get_added_databases(self):
        if not Path('existing').exists():
            Path('existing').mkdir()
        databases = [db.name for db in Path('existing').iterdir() if db.is_dir()]
        return databases
    

    def get_dbms(self, database):
        try:
            with open(f'existing/{database}/.env', 'r') as f:
                lines = f.readlines()
                config = {line.split('=')[0]: line.split('=')[1].strip().replace('"', '') for line in lines}
            return config['DB_TYPE']
        except FileNotFoundError:
            return None



    # ============================== PRIVATE METHODS ============================== #
        
    def _save_dotenv(self, save_path):

        """Save the database configuration to a .env file"""

        with open(save_path / '.env', 'w') as f:
            f.write(f'PGUSERNAME="{self.username}"\n')
            f.write(f'PGPASSWORD="{self.password}"\n')
            f.write(f'NAME="{self.database}"\n')
            f.write(f'DB_TYPE="{self.db_type}"\n')
            if self.db_type == 'Microsoft SQL Server':
                f.write(f'SERVER="{self.server_instance}"\n')
            else:   
                f.write(f'HOST="{self.host}"\n')
                f.write(f'PORT="{self.port}"\n')

    
    def _get_sql_metadata(self, dotenv_path):

        """Getting the SQL schema"""

        script_path = f'../scripts/{self.db_type}.ps1'
        if self.db_type.startswith('Mongo'):
            file_name = 'metadata.txt'
        else:
            save_path = 'metadata.sql'
        pipeline = ['powershell.exe', 
                    '-ExecutionPolicy', 'Unrestricted', 
                    '-File', script_path,
                    '-savePath', dotenv_path / file_name,
                    '-username', self.username,
                    '-password', self.password,
                    '-name', self.database]
        
        if self.db_type.startswith('Oracle') or self.db_type.startswith('Mongo'):
            params = {'host': self.host, 'port': self.port}
            for k, v in params.items():
                pipeline.append(f'-{k}')
                pipeline.append(v)
        
        elif self.db_type == 'Microsoft SQL Server':
            pipeline.append('-serverInstance')
            pipeline.append(self.server_instance)

        result = subprocess.run(pipeline)
        if result.returncode != 0:
            raise Exception(f'Error: {result.stderr}')

    def _filter_metadata(self, metadata_path):

        """Filter the SQL metadata"""

        try:
            with open(metadata_path / 'metadata.sql', "r", encoding='utf-8') as f:
                metadata = f.read()
        except UnicodeDecodeError:
            with open(metadata_path / 'metadata.sql', "r", encoding='utf-16') as f:
                metadata = f.read()
        finally:
            metadata = metadata.replace('`', ' ').replace('਍ഀ', '').replace('"', '').replace('\n\n\n', '')
            pattern = re.compile(r"CREATE TABLE[\s\S]*?;", re.MULTILINE)
            matches = pattern.findall(metadata)

        with open(metadata_path / 'metadata.sql', 'w') as f:
            for match in matches:
                f.write(match)
                f.write('\n\n')






        

        