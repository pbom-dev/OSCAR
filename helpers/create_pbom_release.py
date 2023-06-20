import yaml
import json
import glob
import os
import logging
import argparse

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(funcName)s:%(lineno)d - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
logger.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

TACTICS_ENUM = {
    "Reconnaissance": "TA01",
    "Resource Development": "TA02",
    "Initial Access": "TA03",
    "Execution": "TA04",
    "Persistence": "TA05",
    "Privilege Escalation": "TA06",
    "Defense Evasion": "TA07",
    "Credential Access": "TA08",
    "Lateral Movement": "TA09",
    "Collection": "TA10",
    "Exfiltration": "TA11",
    "Impact": "TA12"
 }

class PageGenerator(object):
    '''
    This class will generate the full page for a technique with all the mitigations and detections
    '''
    def __init__(self, mitigation_path, detection_path):
        self.mitigation_path = mitigation_path
        self.detection_path = detection_path
        self.detections = self.read_detection()
        self.mitigations = self.read_mitigation()

    def read_mitigation(self):
        d = {}
        files_glob = glob.glob(os.path.join(self.mitigation_path, '*.yaml'))
        for fname in files_glob:
            j = self.yaml_to_json(fname)
            d[j['id']] = j
        return d
    
    def read_detection(self):
        d = {}
        files_glob = glob.glob(os.path.join(self.detection_path, '*.yaml'))
        for fname in files_glob:
            j = self.yaml_to_json(fname)
            d[j['id']] = j

        return d
    
    def yaml_to_json(self,yaml_file):
        with open(yaml_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data


    def generate(self, tech_fname):
        # save_to_file will save the mitigation and detection files to the mitigation_path and detection_path

        tech = {}
        j = self.yaml_to_json(tech_fname)
        tech = j.copy()
        tech['mitigations'] = []
        tech['detections'] = []

        for m in j['mitigations']:
            try:
                tech['mitigations'].append(self.mitigations[m])
            except KeyError:
                #logger.error(f"No mitigations in {tech_fname}")
                pass
            
        for d in j['detections']:
            try:
                tech['detections'].append(self.detections[d])
            except KeyError:
                #logger.error(f"No detections in {tech_fname}")
                pass


        return tech



def parse_args():
    parser = argparse.ArgumentParser(description='Create PBOM release')
    parser.add_argument('-s', '--source', help='OSCAR source path', required=True)
    parser.add_argument('-d', '--dest', help='PBOM data destination path', required=True)
    return parser.parse_args()

def setup_directory(pbom_data_path):
    logger.info("Creating directories")
    try:
        os.mkdir(os.path.join(pbom_data_path, 'pbom_data'))
        os.mkdir(os.path.join(pbom_data_path, 'pbom_data', 'techniques'))
        os.mkdir(os.path.join(pbom_data_path, 'pbom_data', 'mitigations'))
        os.mkdir(os.path.join(pbom_data_path, 'pbom_data', 'detections'))
        os.mkdir(os.path.join(pbom_data_path, 'pbom_data', 'campaigns'))
    except:
        logger.error("Can't create directory")

def yaml_to_json(yaml_file):
    with open(yaml_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def create_release(oscar_source_path, pbom_data_path):
    '''
    This function will create the release for PBOM
      - it will create the json files for the techniques, mitigations and detections
      - it will create the full page for each technique
      - it will copy the files to the pbom_data directory
    '''
    # setup directories
    setup_directory(pbom_data_path)

    logger.info("Generating matrix.json")
    generate_matrix(oscar_source_path, pbom_data_path)
    # transform mitigations and detections to json and save to the pbom_data directory
    logger.info("Copying mitigations and detections to pbom_data directory")

    for fname in glob.glob(os.path.join(oscar_source_path, "mitigations","*.yaml")):
        with open(os.path.join(pbom_data_path, 'pbom_data', 'mitigations', fname.split('/')[-1].replace('.yaml', '.json')), 'w') as f:
            json.dump(yaml_to_json(fname), f, indent=4)

    for fname in glob.glob(os.path.join(oscar_source_path, "detections","*.yaml")):
        with open(os.path.join(pbom_data_path, 'pbom_data', 'detections', fname.split('/')[-1].replace('.yaml', '.json')), 'w') as f:
            json.dump(yaml_to_json(fname), f, indent=4)
    
    p = PageGenerator(os.path.join(oscar_source_path, 'mitigations'), os.path.join(oscar_source_path, 'detections'))
    
    for tech_fname in glob.glob(os.path.join(oscar_source_path, "techniques","*.yaml")):
        full_page = p.generate(tech_fname)
        # save to file
        with open(os.path.join(pbom_data_path, 'pbom_data', 'techniques', tech_fname.split('/')[-1].replace('.yaml', '.json')), 'w') as f:
            json.dump(full_page, f, indent=4)
    
    # generate attack story
    logger.info("Generating attack story")
    generate_attack_story(oscar_source_path, pbom_data_path)


def generate_attack_story(oscar_source_path, pbom_data_path):
    '''
    This function will generate the attack story for PBOM
    '''
    colors = {
        "supply-chain": "#FF0000",
        "pre-supply-chain": "#00FF00",
        "post-supply-chain": "#0000FF"
    }
    j = {}
    story_path = os.path.join(oscar_source_path, 'stories')
    # read all yamls from path  
    story_list = []
    for filename in glob.glob(story_path + '/*.yaml'):
        logger.info('Reading file: %s', filename)
        with open(filename, 'r') as f:
            # read yaml file
            y = yaml.load(f, Loader=yaml.SafeLoader)
            # convert to json
            #print(y)
            j = {
                "name": y['summary'],
                "description": y['description'],
                "techniques": [],
                "legendItems": [],
                "metadata": [],
                "links": y['links'],
                "id": y['id']
            }

            for attack in y['attacks']:
                for technique in attack['techniques']:
                    temp_tech = {
                        "techniqueID": technique['techniqueID'],
                        "tactic": technique['tactic'],
                        "techName": technique['techName'],

                        "color": attack['stage'],
                        "attack_index": attack['index'],
                        "entity_name": attack['attack']
                    }
                    if 'comment' in technique:
                        temp_tech['comment'] = technique['comment']
                    else:
                        temp_tech['comment'] = ""
                    j['techniques'].append(temp_tech)

                # add legend items
                j['legendItems'].append({
                    "color": colors[attack['stage']],
                    "label": attack['stage'],
                    "name": attack['attack'],
                    "index": attack['index'],
                    "customer": attack['customer'],
                    "supplier": attack['supplier']
                })

        # sort techniques by attack_index and tactic
        j['techniques'] = sorted(j['techniques'], key=lambda k: (k['attack_index'], TACTICS_ENUM[k['tactic']]))
                        
        # save to json
        with open(os.path.join(pbom_data_path, 'pbom_data', 'campaigns', filename.split('/')[-1].replace('.yaml', '.json')), 'w') as f:
            f.write(json.dumps(j, indent=4))
        story_list.append({
            "name": j['name'],
            "filename": filename.split('/')[-1].replace('.yaml', '.json')
        })

    # sort story list techniques by index and TACTICS_ENUM
    #story_list = sorted(story_list['techniques'], key=lambda k: (k['index'], TACTICS_ENUM[k['tactic']]))

    # save story list
    with open(os.path.join(pbom_data_path, 'pbom_data', 'campaigns', 'story_list.json'), 'w') as f:
        f.write(json.dumps(story_list, indent=4))



def generate_matrix(oscar_source_path, pbom_data_path):
    j = {}
    tech_path = os.path.join(oscar_source_path, 'techniques')
    # read all yamls from path  
    for filename in glob.glob(tech_path + '/*.yaml'):
        logger.debug('Reading file: %s', filename)
        with open(filename, 'r') as f:
            # read yaml file
            y = yaml.load(f, Loader=yaml.SafeLoader)
            # convert to json
            #print(y)
            if y['tactic'] not in j:
                j[y['tactic']] = {"items": [],
                                  "amount": 0,
                                  "tooltip": y['tactic'],
                                  "tacticid": TACTICS_ENUM[y['tactic']]}

            # default subtechniques
            
            y.setdefault('subtechinques', [])

            item = {"tags": y['realm'],
                "id": y['id'],
                "name": y['summary'],
                "tooltip": y['summary'],
                "url": f"https://pbom.dev/techniques/&t_id={y['id']}",
                "description": y['description'],
                #"subTechniques": [] if y['subtechinques']==[None] else y['subtechinques'],
                #"subTechniuqesAmount": len([] if y['subtechinques']==[None] else y['subtechinques']),
                "version": "1.0",
                "created": "1970-01-01T00:00:00",
                "updated": "1970-01-01T00:00:00",
                "contributors": ["OscarTheGrouch"]
                }
            j[y['tactic']]['items'].append(item)
            j[y['tactic']]['amount'] += 1

    # sort matrix by tacticid

    # sort items by id
    for tactic in j:
        j[tactic]['items'] = sorted(j[tactic]['items'], key=lambda k: k['id'])
        j[tactic]['amount'] = len(j[tactic]['items'])

    with open(os.path.join(pbom_data_path, 'pbom_data', 'matrix.json'), 'w') as f:
        logger.info("Saving matrix.json to %s", os.path.join(pbom_data_path, 'matrix.json'))
        f.write(json.dumps(j, indent=4))

if __name__ == '__main__':

    args = parse_args()
    pbom_data_path = args.dest
    oscar_source_path = args.source
    logger.info("Creating PBOM release")
    create_release(oscar_source_path, pbom_data_path)
    #generate_attack_story(oscar_source_path, pbom_data_path)
    logger.info("Done")
