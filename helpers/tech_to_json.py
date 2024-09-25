import glob
import json
import logging
import sys
import yaml

### setup logging to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(path):
    j = {}

    # read all yaml files from path
    for filename in glob.glob(path + '/*.yaml'):
        logger.info('Reading file: %s', filename)
        with open(filename, 'r') as f:
            # read yaml file
            y = yaml.load(f, Loader=yaml.SafeLoader)
            # convert to json
            # print(y)
            if y['tactic'] not in j:
                j[y['tactic']] = {"items": [],
                                  "amount": 0,
                                  "tooltip": y['tactic']}

            # default subTechniques

            y.setdefault('subTechniques', [])

            item = {"tags": y['realm'],
                    "name": y['summary'],
                    "tooltip": y['summary'],
                    "url": "https://pbom.dev/",
                    "subTechniques": [] if y['subTechniques'] == [None] else y['subTechniques'],
                    "subTechniquesAmount": len([] if y['subTechniques'] == [None] else y['subTechniques'])}
            j[y['tactic']]['items'].append(item)

    with open('matrix.json', 'w') as f:
        f.write(json.dumps(j, indent=4))


if __name__ == '__main__':
    main(sys.argv[1])
