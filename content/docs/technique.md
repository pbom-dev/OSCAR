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

**The Syntax**
```YAML

id: # REQUIRED - <key:value> prefix with T,M,D - example T1123
type: # REQUIRED - <key:value> choose one of the following: Technique,Mitigation,Detection
tactic: # REQUIRED - <list> - choose at least one technique
realm: # REQUIRED - <list> - multiple choice
summary: # REQUIRED - <key:value>
description: # REQUIRED - <key:value> - supports markdown
mitigations: # REQUIRED - <list> -reference to mitigation references
detections: # REQUIRED - <list> - reference to detection defintitions
subtechinques: # OPTIONAL <list> - reference to TechIDs
references: # OPTIONAL <list> - reference to attacks, articals, blogs etc...
metadata:
  state: # REQUIRED <key:value> choose  draft or release
  version: # OPTIONAL <key:value> note a version number of this document

```

**Example:**

```YAML
id: T0120
type: Technique
tactic: Initial Access
realm:
    - Container Security
    - Open Source Security
    - Artifact Security
summary: Dependency Confusion
description: |
    Dependency confusion is a type of supply chain attack that occurs when an attacker exploits the way some package managers, such as npm and PyPI, resolve dependencies when installing software libraries.
    In a typical software development project, developers rely on a variety of external libraries, often referred to as dependencies, to build their applications. These libraries are typically stored in a remote repository, and developers use a package manager to install and manage them. An attacker will utilize prior knowledge of usage of dependencies (*Discover used open-source dependencies*) to upload a malicious package with the same name to a public repository. This might "confuse" package managers to use to public resource instead of the local one - thus executing or infecting the CI/CD. This can happen on the developer's machine or the build system and has the potential to further steps of an attack - for example, if the malicious code exfiltrate an access token to production environment

mitigations:
# reference to mitigation references
    - M1200

detections: 
# reference to detection defintitions
    - Detect rogue outgoing traffic from CI/CD system
    
subtechinques:
# reference to TechIDs
    - 

refrences:
    - https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610
    - https://pytorch.org/blog/compromised-nightly-dependency/
metadata:
    version: 0.1
    state: draft
 
```

# The Structure of the template

## id

**Type:** String\
**Description:** A unique identifier for the technique, always prefixed by the letter "T" and working upwards sequentially from 1000\
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Sample Response:**

```YAML
id: 'T6823'
```

## type
**Type:** String\
**Description:** The type of data entity - options are `Technique`,`Mitigation`,`Detection`\
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Sample Response:**

```YAML
type: Technique
```

## tactic

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
tactic: Initial Access
```


## realm

**Type:** options\
**Description:** reference to one or more CI/CD realms \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Options:**

  - `Container Security`
  - `Open Source Security`
  - `SCM Posture`
  - `Secrets Hygiene`
  - `Code Security`
  - `Cloud Security`
  - `CI/CD Posture`
  - `Artifact Security`
  - `Infrastructure as code`

**Sample Response:**
```YAML
realm:
    - Container Security
    - Open Source Security
    - Artifact Security
```

## summary

**Type:** String\
**Description:** High level summary of the technique \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

**Sample Response:**

```YAML
summary: Dependency Confusion
```

## description

**Type:** String (long text)\
**Description:** detailed description of the technique, including reference to the way an adversary shall use the technique. Markdown is supported \
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>


**Sample Response:**

```YAML
decription: |
      Dependency confusion is a type of supply chain attack that occurs when an attacker exploits the way some package managers, such as npm and PyPI, resolve dependencies when installing software libraries.
```

## mitigiations

**Type:** String (long text)\
**Description:** a list of mitigation methods - please reference a mitigation id. \
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

```YAML
mitigations:
  - M1200
```

## detections


**Type:** String (long text)\
**Description:** a list of detection methods - please reference a detection id.\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

```YAML
detections:
  - D1200
```

## subtechinques

**Type:** array\
**Description:** A list of all sub-techniques associated with the technique itself.\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

**Sample Response:**

```YAML
subtechnique: 
  - T1001
  - T1002
```

## references

**Type:** array\
**Description:** A list of all references - links to articles, blogs etc..\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

**Sample Response:**

```YAML
references:
  - https://pytorch.org/blog/compromised-nightly-dependency/
```

## metadata

**Type:** array\
**Description:** metadata\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

### metadata.state
**Type:** options\
**Description:** state of document. The options are `draft` or `release`\
**Field requirement:** <span style="color:#FF3A39;background-color:#FFF2F1">Mandatory</span>

### metadata.versionte
**Type:** String\
**Description:** Version number\
**Field requirement:** <span style="color:#39B55B; background-color:#EBF7EE;">Optional</span>

**Sample Response:**

```YAML
metadata:
  - state: draft
  - version: 0.1
```
