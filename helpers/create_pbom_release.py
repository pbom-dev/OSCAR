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
                                  "tooltip": y['tactic']}

            # default subtechniques
            
            y.setdefault('subtechinques', [])

            item = {"tags": y['realm'],
                "id": y['id'],
                "name": y['summary'],
                "tooltip": y['summary'],
                "url": "https://pbom.dev/",
                "subTechniques": [] if y['subtechinques']==[None] else y['subtechinques'],
                "subTechniuqesAmount": len([] if y['subtechinques']==[None] else y['subtechinques']),
                "version": "1.0",
                "created": "1970-01-01T00:00:00",
                "updated": "1970-01-01T00:00:00",
                "contributors": ["OscarTheGrouch"]
                }
            j[y['tactic']]['items'].append(item)
            j[y['tactic']]['amount'] += 1
    
    with open(os.path.join(pbom_data_path, 'pbom_data', 'matrix.json'), 'w') as f:
        logger.info("Saving matrix.json to %s", os.path.join(pbom_data_path, 'matrix.json'))
        f.write(json.dumps(j, indent=4))

if __name__ == '__main__':

    args = parse_args()
    pbom_data_path = args.dest
    oscar_source_path = args.source
    logger.info("Creating PBOM release")
    create_release(oscar_source_path, pbom_data_path)
    logger.info("Done")
