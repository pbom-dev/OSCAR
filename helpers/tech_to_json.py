import sys
import logging
import glob
import yaml
import json

### setup logging to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(path): 
    j = {}

    # read all yamls from path
    for filename in glob.glob(path + '/*.yaml'):
        logger.info('Reading file: %s', filename)
        with open(filename, 'r') as f:
            # read yaml file
            y = yaml.load(f, Loader=yaml.SafeLoader)
            # convert to json
            #print(y)
            if y['tactic'] not in j:
                j[y['tactic']] = {"items": [],
                                  "amount": 0,
                                  "tootlip": y['tactic']}

            # default subtechniques
            
            y.setdefault('subtechinques', [])

            item = {"tags": y['realm'],
                "name": y['summary'],
                "tooltip": y['summary'],
                "url": "https://pbom.dev/",
                "subTechniques": [] if y['subtechinques']==[None] else y['subtechinques'],
                "subTechniuqesAmount": len([] if y['subtechinques']==[None] else y['subtechinques'])}
            j[y['tactic']]['items'].append(item)
    
    with open('matrix.json', 'w') as f:
        f.write(json.dumps(j, indent=4))
        
if __name__=='__main__':
    main(sys.argv[1])
