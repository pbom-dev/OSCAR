---
title: "Technique"
description: "Techniques represent “how” an adversary achieves a tactical objective by performing an action. For example, an adversary create a backdoor in third party software used within the organization's supply chain. Techniques may also represent “what” an adversary gains by
performing an action. This is a useful distinction for the Discovery tactic as the techniques highlight what type of information an adversary is after with a particular action. 

Sub-techniques further break down behaviors described by techniques into more specific descriptions of how behavior is used to achieve an objective. For example, with backdoor added to third party code, the adversary would need to become a maintainer of the third party library or masquerade the backdoor within a potentially legitimate pull request.

There may be many ways, or techniques, to achieve tactical objectives, so there are multiple
techniques in each tactic category. Likewise, there may be multiple ways to perform a technique
so there can be multiple distinct sub-techniques under a technique."
---

## The structure of a technique

**The Syntax:**

```YAML
id: id
technique:
  summary: summary
  description: description
tactic: tactic
product.lifecycle: [product.lifecycle]
realms: [realms]
sub.realms: [sub.realms]
metadata:
  version: version
  state: state
  created.date: created.date
  last.updated: last.updated
  created.by: created.by
detections: [detections] 
mitigations: [mitigations]
sub.techniques: [sub.techniques]
```

**Example:**

```YAML
id: T1001
technique:
  summary: 'Discover naming conventions from public repositories'
  description: 'adversaries may learn of internal conventions of code structure, functions and package names through an observation of the organization's external footprint and contribution via public repositories'
tactic: 'Reconnaissance'
product.lifecycle: [deployment, maintainance-runtime,development,disposition]
realms: [product-lifecycle-instrastructure]
sub.realms: [git-security]
metadata:
  version: 1.0.0
  state: released
  created.date: 2023-02-11
  last.updated: 2023-02-11
  created.by: naorpenso
detections: [D1001,D1003] 
mitigations: [M1005,M1010]
sub.techniques: [T1001.001, T1001.002]
```

## The Structure of the template

### id

**Type:** String\
**Description:** A unique identifier for the technique, always prefixed by the letter "T" and working upwards sequentially from 1000\
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Sample Response:**

```YAML
id: 'T6823'
```

### technique

**Type:** Container\
**Description:** A container for the information regarding the technique
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>


#### technique.summary

**Type:** String\
**Description:** High level summary of the technique \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

#### technique.Description

**Type:** String (long text)\
**Description:** detailed description of the technique, including reference to the way an adversary shall use the technique \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

### tactic

**Type:** options\
**Description:** reference to the tactic the technique is associated with \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Options:**

- `Reconnaissance` - The adversary is trying to gather information they can use to plan future operations.
- `Resource Development` - The adversary is trying to establish resources they can use to support operations.
- `Initial Access` - The adversary is trying to gain access.
- `Execution` - The adversary is trying to execute an attack.
- `persistance` - The adversary is trying to maintain their foothold.
- `Privilege Escalation` - The adversary is trying to gain higher-level permissions.
- `Defense Evasion` - The adversary is trying to avoid being detected.
- `Credential Access` - The adversary is trying to steal accounts, passwords, and tokens.
- `Discovery` - The adversary is trying to figure out the supply chain ecosystem / environment.
- `Lateral Movement` - The adversary is trying to move through the environment, projects.
- `Collection` - The adversary is trying to gather data of interest to their goal.
- `Command and Control` - The adversary is trying to communicate with compromised systems to control them.
- `Exfiltration` - The adversary is trying to steal data.
- `Impact` - The adversary is trying to manipulate, interrupt, or destroy your systems and data. 

**Sample Response:**

```YAML
tactic: 'Reconnaissance'
```

### product.lifecycle

**Type:** options array\
**Description:** reference to the tactic the technique is associated with \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Sample Response:**

```YAML
tactic: 'reconnaissance'
```



### sub.technique

**Type:** array\
**Description:** A list of all sub-techniques associated with the technique itself.\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

**Sample Response:**

```YAML
sub.technique: [T1001.001,T1001.002]
```





