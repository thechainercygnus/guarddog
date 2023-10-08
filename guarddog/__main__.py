from fabric import Connection
import yaml

def load_targets() -> dict:
    with open('targets.yaml', 'r') as reader:
        target_file_contents = reader.read()
    dict_from_yaml = yaml.safe_load(target_file_contents)
    return dict_from_yaml['targets']

if __name__ == "__main__":
    targets = load_targets()
    for target in targets:
        print(f'Building connection for {target["name"]}')
        c = Connection(
            host=target['properties']['address'],
            user=target['properties']['sshUser'],
            connect_kwargs={'password': target['properties']['sshPass']}
        )
        try:
            c.run("ip a | grep br0")
        except Exception as e:
            print(e)
    